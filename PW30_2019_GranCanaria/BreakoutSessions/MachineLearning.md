Back to [Breakout Sessions List](../README.md#breakout-sessions)

# Machine learning best practices

Goal of the meeting: share with each other how machine learning is implemented by various groups, see if we can find common patterns and way of leveraging similar efforts.

## Participants
- Andras Lasso (PerkLab, Queen's University)
- Steve Pieper (Isomics)
- Marco Nolden (DKFZ), Jonas Scherer (DKFZ)
- Hans Meine (Mevis)
- Jean-Christophe Fillion-Robin (Kitware)
- Deepak Roy Chittajallu (Kitware) - remotely
- Matt Jolley (CHOP) - remotely
- Christian Herz (CHOP) - remotely

## Meeting minutes

Interventional applications (Andras Lasso):

- Use cases: continuous ultrasound segmentation, object detection in video or ultrasound stream
- Low latency is important, processing must happen locally
- Platform: Windows, anaconda, TensorFlow, Keras
- Classify images and separate into training, validation and testing datasets using Jupyter Notebook
- First approach saved images local machine. Image was detected and the prediction was written to a file to be read by Slicer. Significant delay due to file reading/writing/change detection (turnaround time is about a second).
- Second approach streams image data to Keras using OpenIGTLink and return classification along the same connection.
- OpenIGTLink implementation for Python: https://github.com/SlicerIGT/pyIGTLink
- Tools for training data generation for deep learning in Slicer: https://github.com/SlicerIGT/UsAnnotationExport

Cardiac segmentation applications (Matt Jolley, Christian Herz):

- Echo-cardiographic research
- Use Slicer to generate training data for segmentation
- Leaflet segmentation: vnet on local gpu, and also niftinet; tensorflow
- Question: how do you augment data in an intelligent fashion? It would be nice to have standardized, ITK-based tools for data augmentation.

Mevis (Hans Meine):

- Dashboard, docker, kubernetes-like job scheduling (Nomad from hashicorp, together with Consul & Vault)
- Web frontend for segmentation/annotation (MeVisLab-based server-side rendering & interaction). The desktop application viewport are sent over to the web page using custom efficient protocol. Developed own inference service using RPC (based on ZeroMQ).
- Integrated [tensorflow C++ API](https://www.tensorflow.org/guide/extend/cc) in mevislab. It allows efficient in-process inference. Previously lasagne and theano (which even needed a compiler at runtime), now it is nice to use tensorflow C++ .. no dependency on Python.
- Server for model serving: Several official 3rd party products considered as improvement over own classification server:
  - [TensorFlow Serving](https://www.tensorflow.org/serving/)
  - [NVIDIA TensortRT Inference Server](https://devblogs.nvidia.com/nvidia-serves-deep-learning-inference/)
  - [Clipper.ai](http://clipper.ai/)
- These offer features such as
  - serving multiple models in one service
  - automatic loading (/ unloading) of modules on demand (/ after timeout)
  - hot-plugging models / new versions of models
- Data augmentation: using MeVisLab
- After solving the DL infrastructure problem per-site, the next step is the inter-site communication – we need a data channel acknowledged / accepted by hospitals to transfer models. (The only real-world deployed system for federated learning known to me so far uses small text files to transfer models, but that does not scale to DL models.)

DKFZ (Marco Nolden):

- Deploying platform in a network for 10 hospitals
- Provide software platform, can send data from pacs
- Everything is docker, leverage kubernetes
- DICOM4CHE with 10TB stores cohorts locally
- Number of patients: approx 1800, 3800 studies, 65k series
- Web-based interface for cohort selection: Dicom tags extracted and send to kibana
- Metadata analysis, generate graph
- Possible to filter data by selecting filter, then can run algorithm
- Nvidia-docker as a base for doing model inference
- Would like to use ohif for viz
- Input as DICOM, use dicomseg2nrrd, and also have a “preservemetadata” module

Steve:

- DeepInfer: Alireza Mehrtash, Tina (BWH)
  - Model registry for docker containers
  - Requirements: docker installed on local machine, download model (may be GBs)
- TOMAAT (side project by Fausto Milletari, now NVIDIA):
  - Data is sent to remote server
  - May or may not be actively developed
- BioimageSuiteWeb:
  - Web application running on your client:
  - https://bioimagesuiteweb.github.io/unstableapp/tfjsexample.html
  - Press red “Run 2D” button in the corner, model is run in the browser
  - TF model exported & made available to both desktop & web (using [tensorflow.js](https://js.tensorflow.org/))

Deepak:

- Cohort selection, send it for annotation, train, deploy, analytics
- No single solution but many components
- Girder for data management:
  - plugins generate thumbnails and visualization, tag with metadata
  - Asset store allows using different storage solutions
  - REST API for file operations
  - Virtual folder for each cohort
  - Data access control
- Annotation
  - HistomicsTK: Web-based tools for visualization, annotation
  - ParaView Glance: considering adding Slicer-like annotation tools
- Containerize and run CLIs on the web (based on CTK CLI) [slicer_cli_web_plugin](https://github.com/cdeepakroy/slicer_cli_web_plugin)
  - Multiple CLIs per docker possible, list & inspect via entrypoint
  - CLIs are regular ones, so all Girder / docker integration is taken care of by this
  - Input / output files are selected from Girder collections, handled by the plugin
  - Even progress output is displayed in the web
- Paraview Glance
- Data augmentation: many 2D tools (such as [imgaug](https://imgaug.readthedocs.io/en/latest/)), but not really for 3D
  - ITK-based tools could be added for translation, rotation, bspline deformation etc.
  - Others provide some data augmentation:
    - Niftynet
    - NVidia DALI: https://github.com/NVIDIA/DALI
    - DKFZ BatchGenerator. See https://github.com/MIC-DKFZ/batchgenerators#readme

![](./MachineLearning_BreakoutSession.jpg)

## Background and References

Machine learning solutions used in Slicer:
- [DeepInfer](http://www.deepinfer.org/): store models on cloud and run locally in docker container
- [TOMAAT](https://github.com/faustomilletari/TOMAAT-Slicer): store and run models on cloud
- [SlicerIGT](https://github.com/SlicerIGT/UsAnnotationExport): real-time segmentation of 2D ultrasound image streams, train and run models locally

- [Chest imaging platform](https://projectweek.na-mic.org/PW27_2018_Boston/Projects/CIPDeepLearningLungSegmentation/): work in progress? does not seem to be integrated in the public repository yet

Related efforts:
- [NiftyNet](https://github.com/NifTK/NiftyNet)
- [MITK-Diffusion](http://mitk.org/wiki/MitkDiffusion#Requirements): contains deep learning based tractography module (requires manual python installation and only works on Linux)
- [DLTK](https://github.com/DLTK/DLTK): directly implemented on top of TensorFlow (not on top of Keras or pytorch)
- [netharn](https://github.com/Erotemic/netharn): Parameterized fit and prediction harnesses for pytorch.
  * This project focuses on deploying pytorch models.
  * It was initially developed at Kitware.
  * Instead of simply introspecting a single file to extract code for your model, it is able to recursively pull code from external modules in order to ensure that the exported model topology is truly standalone and not dependent on whatever tool was used to train it.
  * Note that the current internal version (0.1.5: pending public release) contains a more powerful version of the existing public (0.1.1) export and deploy code.
  * For questions, jon.crall@kitware.com, jcfr@kitware.com
- [Girder](http://girder.readthedocs.io/)
  * Girder is both a standalone application and a platform for building new web services and could be leveraged to support sharing of both data and deployed models.
  * For questions, michael.grauer@kitware.com, jcfr@kitware.com
- [DIVA Platform](https://github.com/Kitware/DIVA) for Annotating Activities and Objects in Video
  * For questions, michael.grauer@kitware.com, jcfr@kitware.com
  * Poster available [here](https://data.kitware.com/api/v1/file/5c4ef2628d777f072b1a5324/download).
  * This is along the lines of annotation creation, display, inter annotator agreement, spatiotemporal clustering, audits, workflows, crowdsourcing, cloud hosting with scalability and availability.
