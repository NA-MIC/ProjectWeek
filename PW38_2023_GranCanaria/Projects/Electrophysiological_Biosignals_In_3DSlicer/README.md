Back to [Projects List](../../README.md#ProjectsList)

# Electrophysiological biosignals in 3D Slicer: a case of EMG to control 3D models

## Key Investigators

- Jordan Ortega Rodríguez (Medical Technology Group - Instituto de Astrofísica de Canarias. IACTEC)
- Gara Ramos (Medical Technology Group - Instituto de Astrofísica de Canarias. IACTEC)
- Natalia Arteaga (Medical Technology Group - Instituto de Astrofísica de Canarias. IACTEC)

# Project Description

The aim of this project is to acquire and visualize electrophysiological biosignals on 3D Slicer via Arduino, 
as these biosignals can provide information about the subject's physiological data that can complement other 
applications based on image analysis. In particular, the module "EMGArduino" makes it possible to use the subject's
electromyogram (EMG) to control the movement of a 3D model.

## Objective

Objective 1. Establish an interface between Slicer and Arduino to acquire electrophysiological signals.
Objective 2. The streaming and visualization of the electrophysiological biosignals in Slicer in the time domain in terms of voltage amplitude. 
Objective 3. Send commands from EMG signals to Slicer to control movements of 3D models loaded into the 3D scene (e.g. antropomorphic hand).

## Approach and Plan

1. First of all, it is necessary to have an electronic board for the acquisition and conditioning of electrophysiological 
   signals whose output can be connected to an Arduino board. In this project, the MySignals SW eHealth and Medical IoT Development Platform
   (Libelium) [2] has been used. However, any electonic signal acquisition pcb that is suitably designed for electrofisiological
   biosignal preprocessing can be used.  

2. Development of the Arduino IDE code for the acquisition of EMG signals.
 
3. There is a Slicer extension called ArduinoController and develovep by Paolo Zafinno et al. (Department of Clinical 
   and Experimental Medicine, University “Magna Graecia” of Catanzaro) [1] that allows to connect and receive/send 
   data from/to Arduino boards. Based on this extension, it is possible to create a module that uses the Arduino to receive
   data from a subject's electrophysiological signals (e.g. EMG) and transfer them to 3D Slicer.

4. Adaptation of the module created to load 3D models into the 3D scenes of the Slicer.

5. Interaction with the uploaded 3D models and the Arduino output data as a function of the acquired subject EMG biosignal
   voltage amplitude variations. 

## Progress and Next Steps

1. Once we had an electronic PCB for the acquisition (Fig.1) and processing of the electrophysiological signal, the corresponding IDE
   code was developed and loaded onto the Arduino board. This code also allows the visualisation of the EMG signal on a TFT screen 
   integrated in the acquisition PCB (Video 1) and the transmission of data to a Slicer module (Fig.2).

2. The visualisation of the EMG signal in the slicer scene was done through the ArduinoController module [1] (Video 2).

3. The next step will focus on creating a module that allows loading 3D models into the Slicer scene and controlling/setting
   some of its parameters (such as position or colour) directly depending on the voltage variation of the EMG signal of the subject. 


# Illustrations

### Data Acquisition Board for the EMG signals
<img src="https://github.com/JordanOrt/EMG_Slicer/blob/1546b5817a2116dead5ebac659b9e32520a62fc6/MySiganIoT.jpg" width="500"/>

### EMG data plot in 3D Slicer
<img src="https://github.com/JordanOrt/EMG_Slicer/blob/1546b5817a2116dead5ebac659b9e32520a62fc6/EMG-Arduino%20Plot.png" width="500"/>


# Videos

### Biosignals Data Acquisition Board with Arduino system
![](https://github.com/NA-MIC/ProjectWeek/blob/master/PW38_2023_GranCanaria/Projects/Electrophysiological_Biosignals_In_3DSlicer/DAQ-board-and-Arduino.gif)

### Streamming the EMG signal in 3d Slicer
![](https://github.com/NA-MIC/ProjectWeek/blob/master/PW38_2023_GranCanaria/Projects/Electrophysiological_Biosignals_In_3DSlicer/EMG_Slicer.gif)

### Controlling a 3D Hand with EMG signals in 3D Slicer
![](https://github.com/NA-MIC/ProjectWeek/blob/master/PW38_2023_GranCanaria/Projects/Electrophysiological_Biosignals_In_3DSlicer/EMG-3DHand.gif)

# Background and References

[1] Zaffino P, Merola A, Leuzzi D, Sabatino V, Cosentino C, Spadea MF. SlicerArduino: A Bridge between Medical 
    Imaging Platform and Microcontroller. Bioengineering. 2020 Sep;7(3):109.)

[2] MySignals - eHealth and Medical IoT Development Platform. Libelium. Video: https://www.youtube.com/watch?v=MiMDOT-Wt4w

