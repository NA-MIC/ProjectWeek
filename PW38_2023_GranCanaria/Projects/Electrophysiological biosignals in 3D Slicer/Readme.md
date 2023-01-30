Back to [Projects List](../../README.md#ProjectsList)

# Electrophysiological biosignals in 3D Slicer: a case of EMG to control 3D models

## Key Investigators

- Jordan Ortega Rodríguez (Astrophysic Institute of Canary Islands - IACTEC)
- Gara Ramos (Astrophysic Institute of Canary Islands - IACTEC)

# Project Description

The aim of this project is to acquire and visualize electrophysiological biosignals in 3D Slicer through Arduino, 
as these bio-signals can provide information on physiological data of the subject that can complement other applications 
based on image analysis. In particular, the module "EMGArduino" allows to use the subjets electromyiogram (EMG) 
to control the movement of an antropomorfic hand 3D model.

## Objective

Objective 1. Establish an interface between Slicer and Arduino to acquire electrophysiological signals.
Objective 2. Visualizate electrophysiological biosignals in Slicer in the time domain in terms of voltage amplitude. 
Objective 3. Send commands from EMG signals to Slicer to control movements of 3D models loaded into the 3D scene.


## Approach and Plan

1. First of all, it is necessary to have an electronic pcb for the acquisition and conditioning of electrophysiological 
   signals whose output can be connected to an Arduino board. In this project, we used the MySignals SW eHealth 
   and Medical IoT Development Platform (Libelium) [2]. However, any electonic signal acquisition pcb that is 
   propertly designed for the treatment of electrofisiological biosignals can be used.  

2. Develop the EMG signals acquisition IDE code for the Arduino board.
 
3. There is an Slicer extension called ArduinoController and develovep by Paolo Zafinno et al. (Department of Clinical 
   and Experimental Medicine, University “Magna Graecia” of Catanzaro) [1] that allows connecting and receiving/sending 
   data from/to Arduino boards. Based on this extension, it is possible to create a module that uses the Arduino to receive
   data from a subject's electrophysiological signals (for example: EMG) and transfer them to 3D Slicer.

4. Adapting the created module to load 3D models into the Slicer's 3D scenes.

5. Interacting with the loaded 3D models and the Arduino output data in function of the voltage amplitude variations 
   of the acquired subject's EMG biosignals. 


## Progress and Next Steps

1. Once we have an electronic PCB for acquisition (Fig.1) and electrophysiological signal processing, 
   the corresponding IDE code was developed and loaded onto the Arduino board. This code also allows the visualisation 
   of the EMG signal on a TFT screen integrated in the acquisition PCB (Video 1) and 
   the data transmission to a Slicer module (Fig.2).

2. The visualization of the EMG signal in the slicer's plot scene was made through the ArduinoController module [1] (Video 2).

3. The next step will be focused in to create a module that allows to load 3D models to a Slicer's scene and control/set some of their parameter
   (such as position or colour) directly in function of the subject´s EMG signal voltage variation. As an ilustrative example purpose, 
   we previously developed this application in LabVIEW (Video 3), where the subject wear a surface EMG PCB that allows 
   him to control a 3D hand model. The aim is to replicate this application in 3D Slicer.


# Illustrations

![Fig.1](https://github.com/JordanOrt/EMG_Slicer/blob/1546b5817a2116dead5ebac659b9e32520a62fc6/MySiganIoT.jpg)
![Video 1 (EMG DAQ-Arduino)](https://github.com/JordanOrt/EMG_Slicer/blob/1546b5817a2116dead5ebac659b9e32520a62fc6/EMG_MySignals-Arduino.mp4)
![Fig.2](https://github.com/JordanOrt/EMG_Slicer/blob/1546b5817a2116dead5ebac659b9e32520a62fc6/EMG-Arduino%20Plot.png)
![Video 2 (Real time streamming of EMG data from Arduino to 3D Slicer)](https://github.com/JordanOrt/EMG_Slicer/blob/1546b5817a2116dead5ebac659b9e32520a62fc6/EMG_Slicer.mp4)
![Video 3 (Example of controlling a 3D hand model by EMG signals developed in LabVIEW interface)](https://github.com/JordanOrt/EMG_Slicer/blob/1546b5817a2116dead5ebac659b9e32520a62fc6/EMG_Hand_Labview.mp4)


# Background and References

[1] Zaffino P, Merola A, Leuzzi D, Sabatino V, Cosentino C, Spadea MF. SlicerArduino: A Bridge between Medical 
    Imaging Platform and Microcontroller. Bioengineering. 2020 Sep;7(3):109.)

[2] MySignals - eHealth and Medical IoT Development Platform. Libelium. Video: https://www.youtube.com/watch?v=MiMDOT-Wt4w
