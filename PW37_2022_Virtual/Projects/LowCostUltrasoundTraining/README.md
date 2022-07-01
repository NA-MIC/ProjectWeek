Back to [Projects List](../../README.md#ProjectsList)

# Low-Cost Ultrasound Training

## Key Investigators

- David García Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- Csaba Pinter (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- Rebecca Hisey (Queen’s University, Kingston, ON, Canada)
- Matthew Holden (Carleton University, Ottawa, ON, Canada)

# Project Description
[**Ebatinca S.L.**](https://ebatinca.com/) is currently developing a **low-cost training platform for ultrasound imaging and ultrasound-guided procedures** in low- and middle-income countries. We are developing a 3D Slicer based application to perform training exercises and evaluate participants. The app is called [**TrainUS**](https://github.com/EBATINCA/TrainUS) and it is available with open-source license.

Some basic features have already been developed: participant/recording management, hardware connection, selection of training exercises,... Currently, we are working on the development of basic exercises to train basic ultrasound skills. The app should be able to evaluate recordings made by users and to provide feedback about their performance. 

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
Develop specific module to train in-plane needle insertions. The module should display instructions on how to perform the exercise correctly and should enable the recording of ultrasound-guided needle insertions. Then, recordings must be evaluated using the [PerkTutor extension](http://perktutor.github.io/), getting overall performance metrics (elapsed time, needle path length, rotations, translations,...). Performance metrics must be displayed in plots and tables to the users, providng specific feedback to users about their performance.

Once integrated, this module could serve as a reference/example for the development of future exercises in TrainUS.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Determine best way to manage recordings of ultrasound images and tracking data. Currently, we are saving the entire sequence browser node as .sqbr files which can then be easily imported into Slicer using the PerkTutor extension.
2. Define best methodology to display exercise instructions to users: images vs video
3. Discuss the usefulness of assessing performance metric values in "real-time" during sequence playback. Example: distance from needle tip to US plane. Real-time vs overall metrics.
4. Integrate exercise into TrainUS app. 
5. Discuss best strategy to provide specific feedback to users based on recorded data from experts. Deep learning?

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Saving recordings into a single .sqbr file seems the best option for easy import/export. Current infrastructure enables saving the entire vtkMRMLSequenceBrowserNode into a .sqbr file. Custom app should include updated versions of Slicer and PerkTutor to include the fixes related to the following issues which prevented a correct management of .sqbr files: [#6429](https://github.com/Slicer/Slicer/issues/6429) and [#6435](https://github.com/Slicer/Slicer/issues/6435)
2. It has been proposed that it may be a good idea to show the instructions (images or videos) while the exercise is being performed. This could be integrated as a possible configuration for the exercises. Currently, instructions can be shown as images or videos using slice views integrated into the Slicer layout.
3. The new feature to measure and evaluate performance metrics in real-time is considered really useful by the community. This is specially useful to identify specific parts of the recordings where performance drops significantly.
4. Feedback for basic skills exercises can be computed with current methodologies integrated into PerkTutor extension. No deep learning is needed unless complexity of the exercise/procedure increases.
5. Automatic segmentation (deep learning) could be integrated into specific exercise to compute useful data/metrics from the US image. Example: position of a vessel/mass on the image, position of the needle,...
6. Exercise integrated into TrainUS custom app.

# Illustrations

Instructions slides displayed to the user before starting the exercise:

<img src="https://user-images.githubusercontent.com/10816661/176864328-fce55960-6ac9-4298-8133-1865579b2fb0.PNG" alt="drawing" width="800"/>

Video with instructions displayed to the user before starting the exercise:

<img src="https://user-images.githubusercontent.com/10816661/176864506-5fd9951c-4510-40b2-a811-b353e5126088.gif" alt="drawing" width="800"/>

Plot showing real-time metric values during recording playback:

<img src="https://user-images.githubusercontent.com/10816661/176864573-041abd73-0c4b-4907-9c58-12798853655c.gif" alt="drawing" width="800"/>

Table showing overall performance metrics computed using PerkTutor extension:

<img src="https://user-images.githubusercontent.com/10816661/176864902-8d15ebb6-b90b-4009-909e-69c11b37a6c8.PNG" alt="drawing" width="800"/>


<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References
- Previous [Low-Cost Ultrasound Training](https://github.com/NA-MIC/ProjectWeek/blob/master/PW36_2022_Virtual/Projects/LowCostUltrasoundTraining/README.md) during 36th Project Week held virtually on January 17-21, 2022.
- **TrainUS** GitHub repository: [TrainUS app](https://github.com/EBATINCA/TrainUS)
- **PerkTutor** GitHub repository: [PerkTutor extension](https://github.com/PerkTutor/PerkTutor)

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
