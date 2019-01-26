Back to [Breakout Sessions List](../README.md#breakout-sessions)

# Machine learning best practices

We will share with each other how machine learning is implemented by various groups, see if we can find common patterns and way of leveraging similar efforts.

Anybody who is interested in using machine learning for medical image computing is welcome.

## Agenda

Lookup day and time on the [calendar](../README.md#program-calendar).

* Presenting current approaches for
  * training data generation
  * deployment of trained models for end-users
* Discuss possibilities for creating common software infrastructure (in CTK or similar toolkits)

## Participants
- Andras Lasso (PerkLab, Queen's University) - with presentation
- Steve Pieper (Isomics) - with presentation?
- Marco Nolden (DKFZ) - with presentation?
- Deepak Roy Chittajallu (Kitware) - with presentation
- Bence Horvath (Unirversity of Szeged) - with presentation?

Please add your name above if you plan to attend.

Those who already have machine learning projects are encouraged to prepare with a short presentation (maximum 5 minutes; slides are optional) about how they do it now. Please add "with presentation" next to your name.

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
- [DLTK](https://github.com/DLTK/DLTK): directly implemented on top of TensorFlow (not on top of Keras or pytorch)
