Back to [Breakout Sessions List](../README.md#BreakoutSessions)

# Machine learning best practices

## Agenda
* Presenting current approaches for
  * training data generation
  * deployment of trained models for end-users
* Discuss possibilities for creating common software infrastructure (in CTK or similar toolkits)

## Presenters
- Andras Lasso (PerkLab, Queen's University)
- Steve Pieper (Isomics)
- Marco Nolden (DKFZ)
- (add your name here if you participate at the session and you already use machine learning)

## Meeting minutes

Meeting minutes will be added here.

## Background and References

Machine learning solutions used in Slicer:
- [DeepInfer](http://www.deepinfer.org/): store models on cloud and run locally in docker container
- [TOMAAT](https://github.com/faustomilletari/TOMAAT-Slicer): store and run models on cloud
- [SlicerIGT](https://github.com/SlicerIGT/UsAnnotationExport): real-time segmentation of 2D ultrasound image streams, train and run models locally
- [Chest imaging platform](https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/CIPDeepLearningLungSegmentation/): work in progress? does not seem to be integrated in the public repository yet

Related efforts:
- [NiftyNet](https://github.com/NifTK/NiftyNet)
- [MITK-Diffusion](http://mitk.org/wiki/MitkDiffusion#Requirements): contains deep learning based tractography module (requires manual python installation and only works on Linux)
