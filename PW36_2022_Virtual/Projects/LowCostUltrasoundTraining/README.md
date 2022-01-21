Back to [Projects List](../../README.md#ProjectsList)

# Low-Cost Ultrasound Training

## Key Investigators

- David García Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- Csaba Pinter (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- Rebecca Hisey (Queen's University, Kingston, ON, Canada)
- Leah Groves (Queen's University, Kingston, ON, Canada)
- Ahmed Mahran (Toronto General Hospital, ON, Canada)
- Matt McCormick (Kitware, Inc., United States)
- Steve Pieper (Isomics, Inc., United States)
- Fryderyk Kögl (BWH, TUM)

# Project Description

[**Ebatinca S.L.**](https://ebatinca.com/) is currently developing a **low-cost training platform for ultrasound imaging and ultrasound-guided procedures** in low- and middle-income countries. We are developing a 3D Slicer based application to perform training exercises and evaluate participants. The app is called **TrainUS** and it will be available soon with open-source license.

Currently, we have already integrated some basic features:

- Participant/recording management: create, edit, delete, filter

- Hardware selection and configuration: connection with PLUS toolkit, US imaging parameters...

![Configuration](https://user-images.githubusercontent.com/10816661/149749292-03676c38-4aef-4590-a3cb-48cd1533694b.PNG)

- Selection of training exercises

![TrainingSession](https://user-images.githubusercontent.com/10816661/149749209-3063512a-4b55-4372-a2cd-79d4e131cf07.PNG)

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Identify features to improve US training applications in 3D Slicer
2. Identify best approach to calibrate the ultrasound probe for US-guided procedures.
3. Discuss best exercises to train ultrasound imaging and US-guided procedures.
4. Identify specific clinical procedures of interest for low- and middle- income countries.
5. Discuss how to improve low-cost US training in 3D Slicer: virtual reality, artificial intelligence...

## Ideas
1. Discuss best approach (and required additional developments, if any) to record an ultrasound (US) image volume and US probe position, and then enable trainees to simulate US imaging in that recorded volume by freely moving an US probe with respect to a phantom (instead of patient). This would enable the recording of US images of real anatomy and pathologies by expert radiologists. This would be really useful to create custom training exercises for medical students regarding detection of pathologies in US images, and others.
    - Can we use US volume reconstruction + Registration + Volume reslice driver to achieve this?
    - Does reslicing of a reconstructed US volume generates realistic US images?

2. A useful feature for ultrasound training will be to ask multiple-choice questions to users during the session. These questions could be used to ensure that, apart from hand-eye coordination, users understand the whole workflow for US-guided procedures. Customized questions could be included for each procedure to be trained.
    - How could we show this questions in Slicer? Could we generate custom Qt widgets for this? Pop-up windows?

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Bring together researchers interested in low-cost ultrasound training
1. Establish multi-institutional collaborations towards improving ultrasound training in 3D Slicer
1. Define useful features for ultrasound training that can be added to 3D Slicer as extensions.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. We have identified that for training applications in 3D Slicer, it would be very useful to be able to ask questions to the users and ensure that the concepts are clear.Therefore, we have decided to develop a new extension to enable the creation and visualization of multiple choice questions in 3D Slicer. The idea would be to create questions banks which are saved in CSV files and then enable the visualization of the selected questions by custom Qt widgets. This extension will be called [**SlicerEducation**](https://github.com/EBATINCA/SlicerEducation).
2. We have started the development of a 3D Slicer module to facilitate the calibration of tracked ultrasound probes. This modules allows users to use two different methods for calibration: (1) a [stylus-based method](https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!3712&ithint=file%2cpptx&authkey=!ACNGX3PqH0BLg74), where the stylus tip position is recorded in the US image and a point-based registration is then performed, or (2) a [line-based method](https://link.springer.com/article/10.1007/s11548-016-1390-7), where a tracked needle (or stylus) can be moved across the US plane recording point along the needle and a line-to-point registration is performed.
3. We have discussed the possibility of developing a module to train echocardiography in 3D Slicer using US simulation and a [**heart atlas from Toronto General Hospital**](https://sketchfab.com/apil_tgh/collections/toronto-heart-atlas). Example of web app developed by APIL research group: [https://apil-slice.web.app/#](https://apil-slice.web.app/#)
4. 

3. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
- Pop-up window with quiz:

    <img src="https://user-images.githubusercontent.com/10816661/150458655-92474a92-75e2-422c-a9ff-b11aae5b3431.PNG" alt="drawing" width="650"/>

    <img src="https://user-images.githubusercontent.com/10816661/150457041-96964903-cfaf-44aa-be0e-6a16b056818b.gif" alt="drawing" width="650"/>

- Module for tracked US probe calibration:

    <img src="https://user-images.githubusercontent.com/10816661/150459051-981f03c9-075c-44a4-b43f-5eebd2f94b8b.PNG" alt="drawing" width="650"/>
    
    <img src="https://user-images.githubusercontent.com/10816661/150455592-2d1ed13a-774b-471d-97eb-100462ef81fa.png" alt="drawing" width="650"/>
    
- Echocardiography simulator ([https://apil-slice.web.app/#](https://apil-slice.web.app/#)):

    https://user-images.githubusercontent.com/10816661/150458053-8047c409-ba45-45d1-8688-e19b92b13e48.mp4

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

- **TrainUS** GitHub repository: [TrainUs app](https://github.com/EBATINCA/TrainUS)

- **SlicerEducation** GitHub repository: [SlicerEducation](https://github.com/EBATINCA/SlicerEducation)

- Google doc: [here](https://docs.google.com/document/d/1ettQu9WYvy-Dlz7vt42-5Hm7xJOltJJQ69PJZ_WBffg/edit?usp=sharing)

- Tracked US probe calibration methods: [stylus-based method](https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!3712&ithint=file%2cpptx&authkey=!ACNGX3PqH0BLg74) & [line-based method](https://link.springer.com/article/10.1007/s11548-016-1390-7)

- Echocardiography simulator: [https://apil-slice.web.app/#](https://apil-slice.web.app/#)

- Heart atlas from Toronto General Hospital: [here](https://sketchfab.com/apil_tgh/collections/toronto-heart-atlas)
