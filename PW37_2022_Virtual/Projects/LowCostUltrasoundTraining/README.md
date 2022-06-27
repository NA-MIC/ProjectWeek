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
4. Integrate exercise into TrainUS app. Custom app should include updated versions of Slicer and PerkTutor to include the fixes related to the following issues: [#6429](https://github.com/Slicer/Slicer/issues/6429) and [#6435](https://github.com/Slicer/Slicer/issues/6435)
5. Discuss best strategy to provide specific feedback to users based on recorded data from experts. Deep learning?
6. Determine best way to integrate video-based metrics into PerkTutor.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

Instructions displayed to the user before starting the exercise: 

<img src="https://user-images.githubusercontent.com/10816661/175936290-b9afd877-eeb1-488a-a71b-1670ec172846.JPG" alt="drawing" width="800"/>

Plot showing real-time metric values during recording playback:

<img src="https://user-images.githubusercontent.com/10816661/175937246-11d0edb7-cf30-408c-beda-e38bb79f19b1.JPG" alt="drawing" width="800"/>

Table showing overall performance metrics computed using PerkTutor extension:

<img src="https://user-images.githubusercontent.com/10816661/175937477-0e872bf7-efdb-4215-9781-704dfb2a156b.JPG" alt="drawing" width="800"/>


<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References
- Previous [Low-Cost Ultrasound Tracking](https://github.com/NA-MIC/ProjectWeek/blob/master/PW36_2022_Virtual/Projects/LowCostUltrasoundTraining/README.md) during 36th Project Week held virtually on January 17-21, 2022.
- **TrainUS** GitHub repository: [TrainUS app](https://github.com/EBATINCA/TrainUS)
- **PerkTutor** GitHub repository: [PerkTutor extension](https://github.com/PerkTutor/PerkTutor)

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
