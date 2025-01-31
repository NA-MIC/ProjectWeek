/*=========================================================================

  Program:   OpenIGTLink -- Example for Tracker Server Program
  Language:  C++

  Copyright (c) Insight Software Consortium. All rights reserved.

  This software is distributed WITHOUT ANY WARRANTY; without even
  the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
  PURPOSE.  See the above copyright notices for more information.

  Modified by:
            Francisco J. Marcano Serrano (fmarcano@ull.edu.es)
            David Diaz Martin (ddiazmar@ull.edu.es)
        NA-MIC 2020, January 20-24th - Las Palmas de Gra Canaria - Spain

     1. GetRandomMatrix was modified to receive position parameters phi & theta
     2. OUR_INPUT_FIFO_NAME was defined with the name of the FIFO device used for collecting data from the microcontroller
     3. makeFIFO, openFIFO, closeFIFO and readFIFO functions, added.
     4. Machine state implemented in readFIFO to handle read data properly
     5. Two more parameters for program invocation.
=========================================================================*/

#include <iostream>
#include <math.h>
#include <cstdlib>

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

#include "igtlOSUtil.h"
#include "igtlTransformMessage.h"
#include "igtlServerSocket.h"

void GetRandomTestMatrix(igtl::Matrix4x4& matrix,float *phi, float *theta);


#define OUR_INPUT_FIFO_NAME "/dev/acqchardev"
int our_input_fifo_filestream = -1;
#define WAIT_FOR_HEADER_HIGH 0x1B
#define WAIT_FOR_HEADER_MIDDLE1 0x1C
#define WAIT_FOR_HEADER_MIDDLE2 0x1D
#define WAIT_FOR_HEADER_LOW  0x1E
#define WAIT_FOR_PHI 0x1F
#define WAIT_FOR_THETA 0x20

int STATE_READ = 0;
int SEND_TO_CLIENT = 0;

//--------------------------------------
//----- CREATE A FIFO / NAMED PIPE -----
//--------------------------------------
void makeFIFO(){
	int result;
	printf("Making FIFO...\n");
	result = mkfifo(OUR_INPUT_FIFO_NAME, 0777);		//(This will fail if the fifo already exists in the system from the app previously running, this is fine)
	if (result == 0)
	{
		//FIFO CREATED
		printf("New FIFO created: %s\n", OUR_INPUT_FIFO_NAME);
	}
}


void openFIFO(){
	printf("Process %d opening FIFO %s\n", getpid(), OUR_INPUT_FIFO_NAME);
	our_input_fifo_filestream = open(OUR_INPUT_FIFO_NAME, (O_RDONLY | O_NONBLOCK));
	//Possible flags:
	//	O_RDONLY - Open for reading only.
	//	O_WRONLY - Open for writing only.
	//	O_NDELAY / O_NONBLOCK (same function) - Enables nonblocking mode. When set read requests on the file can return immediately with a failure status
	//	if there is no input immediately available (instead of blocking). Likewise, write requests can also return
	//	immediately with a failure status if the output can't be written immediately.
	if (our_input_fifo_filestream != -1)
		printf("Opened FIFO: %i\n", our_input_fifo_filestream);
}

#define NOVALUE -9999999.0
float readFIFO(float *phi, float*theta){
    // Read up to 255 characters from the port if they are there
    if (our_input_fifo_filestream != -1)
    {
        unsigned char rx_buffer[256];
        int rx_length = read(our_input_fifo_filestream, (void*)rx_buffer,1);		//Filestream, buffer to store in, number of bytes to read (max)
        if (rx_length < 0)
        {
            //An error occured (this can happen)
            printf("FIFO Read error\n");
		return(NOVALUE);
        }
        else if (rx_length == 0)
        {
		return(NOVALUE);
            //No data waiting
        }
        else
        {
            unsigned char c;
            //Bytes received
            rx_buffer[rx_length] = '\0';
            c = rx_buffer[0];
	    // sscanf((const char *)rx_buffer,"%f,%f",phi,theta);
            // printf("FIFO read : %f , %f\n", *phi, *theta);

	    switch(STATE_READ){
	    case WAIT_FOR_HEADER_HIGH :
		if(c == 0xFF){
			STATE_READ = WAIT_FOR_HEADER_MIDDLE1;
		}
		break;
	    case WAIT_FOR_HEADER_MIDDLE1:
		if(c == 0xFF){
			STATE_READ = WAIT_FOR_HEADER_MIDDLE2;
		} else {
			STATE_READ = WAIT_FOR_HEADER_HIGH;
		}
		break;
	    case WAIT_FOR_HEADER_MIDDLE2:
		if(c == 0xFF){
			STATE_READ = WAIT_FOR_HEADER_LOW;
		} else {
			STATE_READ = WAIT_FOR_HEADER_HIGH;
		}
		break;
	    case WAIT_FOR_HEADER_LOW:
		if(c == 0xFF){
			STATE_READ = WAIT_FOR_PHI;
		} else {
			STATE_READ = WAIT_FOR_HEADER_HIGH;
		}
		break;
	    case WAIT_FOR_PHI:
		*phi = (3.0/255.0) * (float)c;
		STATE_READ = WAIT_FOR_THETA;
		break;
	    case WAIT_FOR_THETA:
		*theta = (3.0/255.0) * (float)c;
		SEND_TO_CLIENT = 1;
		STATE_READ = WAIT_FOR_HEADER_HIGH;
            	printf("%f , %f;  ",*phi,*theta);
		break;
	    default:
		break;
            }

	    return(0);
        }
	return(NOVALUE);
    }
}

void closeFIFO(){
	//----- CLOSE THE FIFO -----
	(void)close(our_input_fifo_filestream);
}


int main(int argc, char* argv[])
{
  //------------------------------------------------------------
  // Parse Arguments

  if (argc != 5) // check number of arguments
    {
    // If not correct, print usage
    std::cerr << "Usage: " << argv[0] << " <port> <fps>"    << std::endl;
    std::cerr << "    <port>     : Port # (18944 in Slicer default)"   << std::endl;
    std::cerr << "    <fps>      : Frequency (fps) to send coordinate" << std::endl;
    std::cerr << "    <slotSize> : Bytes / slot " << std::endl;
    std::cerr << "    <rps>      : Frequency (rps) reading by client request" << std::endl;
    exit(0);
    }

  int    port     = atoi(argv[1]);
  double fps      = atof(argv[2]);
  int    slotSize = atoi(argv[3]);
  int    rps      = atoi(argv[4]);
  int    interval = (int) (1000.0 / fps);

  static float phi = 0.0;
  static float theta = 0.0;

  igtl::TransformMessage::Pointer transMsg;
  transMsg = igtl::TransformMessage::New();
  transMsg->SetDeviceName("Tracker");

  igtl::ServerSocket::Pointer serverSocket;
  serverSocket = igtl::ServerSocket::New();
  int r = serverSocket->CreateServer(port);

  if (r < 0)
    {
    std::cerr << "Cannot create a server socket." << std::endl;
    exit(0);
    }

  igtl::Socket::Pointer socket;
  makeFIFO();
  openFIFO();
  STATE_READ = WAIT_FOR_HEADER_HIGH;
  while (1)
    {
	float aux;
    //------------------------------------------------------------
    // Waiting for Connection
    socket = serverSocket->WaitForConnection(1000);

    if (socket.IsNotNull()) // if client connected
    {
	for (int i = 0; i<slotSize*rps ; i++){
		aux = readFIFO(&phi,&theta);
      //------------------------------------------------------------
		if(SEND_TO_CLIENT != 0){
       		 	igtl::Matrix4x4 matrix;
       		 	GetRandomTestMatrix(matrix,&phi,&theta);
       		 	transMsg->SetDeviceName("Tracker");
        		transMsg->SetMatrix(matrix);
        		transMsg->Pack();
        		socket->Send(transMsg->GetPackPointer(), transMsg->GetPackSize());
        		igtl::Sleep(interval); // wait
        		// igtl::Sleep(1); // wait
			SEND_TO_CLIENT = 0;
		}

	}
    }
   }
  //------------------------------------------------------------
  // Close connection (The example code never reachs to this section ...)

  socket->CloseSocket();

}


void GetRandomTestMatrix(igtl::Matrix4x4& matrix,float *phi, float *theta)
{
  float position[3];
  float orientation[4];

  // random position
  position[0] = 50.0 * cos((*phi));
  position[1] = 50.0 * sin((*phi));
  position[2] = 50.0 * cos((*phi));

  // random orientation
  orientation[0]=0.0;
  orientation[1]=0.6666666666*cos((*theta));
  orientation[2]=0.577350269189626;
  orientation[3]=0.6666666666*sin((*theta));

  //igtl::Matrix4x4 matrix;
  igtl::QuaternionToMatrix(orientation, matrix);

  matrix[0][3] = position[0];
  matrix[1][3] = position[1];
  matrix[2][3] = position[2];

  igtl::PrintMatrix(matrix);
}
