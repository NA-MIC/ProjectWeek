Back to [Projects List](../../README.md#ProjectsList)

# Setting up University Courses on Computer Assisted Medical Imaging, Manufacturing and Interventions using Open Source Technologies and 3D Slicer

## Key Investigators

- Juan Ruiz (ULPGC)
- Idafen Santana (ULPGC)
- Mario Monzón (ULPGC)
- María Rosa Rodríguez (ULPGC)
- Marie Ndiaye  y Sidi el Wafi
- Mamadou Samba Camara
- Adama Faye
- Idy Diop
- Mouahmed Diop
- Papa Alioune Cisse
- Youssou Faye
- Mame Diarra Sy
- Ahmed Dhahara Kane
- Attila Tanács (University of Szeged)
- Attila Nagy (University of Szeged)

# Project Description

In order to meet the demand for professionals in the field of computer assisted medical imaging, manufacturing and interventions, universities need to set up courses that provide students with the necessary knowledge and skills. Designing a university course on this topic requires careful consideration of the syllabus and design materials that will be used. This project will explore how universities can create a syllabus and design material for a course on computer assisted medical imaging, manufacturing and interventions using open source technology.

## Objective

1. Define the topics that should be covered in the syllabus
1. Select learning resources and bibliography to support the course contents
1. Design materials to be used in the lessons based on open source technologies
1. Develop common contents to facilitate exchange of personnel and students from different countries

## Approach and Plan

1. Explore the competences that are required in the professional market to define the course content
1. Discuss with the 3D Slicer community how to create materials based on open source technology and integrate them on a syllabus
1. Propose a biomedical engineering course program

## Progress and Next Steps

We have designed the following syllabus proposal:

**Computer Assisted Medical Imaging and Interventions (60 hours – 6 ECTS)**

An introductory course that uses 3D Slicer to demonstrate all the necessary concepts.

- 40 hours (4 ECTS) to introduce all the main concepts along with practical demos using the well-known medical image computing open software ecosystem 3D Slicer split into 10 subjects, each one to be taught in two classes of two hours.
  - Subject 1 provides a general introduction to medical images
  - Subjects 2 trough 9 use Slicer Notebooks on Jupyter Lab
  - Subject 10 develops an introductory application using Slicer

- 20 hours (2 ECTS) to develop a practical use-case on 3D Slicer as a self-contained application. Projects offered:
  - Creating a Virtual Reality application in Slicer
  - Integration of a deep learning model to segment medical images
  - Developing a module for image guided therapy (IGT)

**Concepts (40 hours)**

1.	Introduction to medical imaging modalities
    <ol type="a">
      <li>Digital images (general intro, not specific to medical imaging)</li>
      <li>Ultrasound</li>
      <li>X-Ray, mammography, fluoroscopy </li>
      <li>Digital volumetric images (general intro, not specific to medical imaging)</li>
      <li>Computed Tomography (CT)</li>
      <li>Magnetic Resonance Imaging (MRI)</li>
    </ol>

2.	Loading, storing & visualizing medical images
    <ol type="a">
      <li>File formats commonly used with images (general intro, not specific to medical imaging)</li>
      <li>File formats for medical imaging research</li>
      <li>An introduction to DICOM</li>
      <li>The visualization model. Rendering scenes composed of multimodal data (general intro, not specific to medical imaging)</li>
      <li>Digital volumetric images (general intro, not specific to medical imaging)</li>
      <li>Surface vs volume rendering (general intro, not specific to medical imaging)</li>
      <li>Putting it all together with 3D Slicer</li>
    </ol>

 3. Segmentation of medical images (2D and 3D)
    <ol type="a">
      <li>Computer-assisted manual segmentation</li>
      <li>A first introduction to automated segmentation using simple methods</li>
      <li>Contour and surface extraction from image segments</li>
      <li>Putting it all together with 3D Slicer</li>
    </ol>

 4. Working with physical models in medical applications
    <ol type="a">
      <li>An introduction to 3D printing for medical applications</li>
      <li>Building your own “phantoms” (homemade physical models)</li>
      <li>Commercial manikins for clinical training </li>
      <li>Virtualizing phantoms and manikins</li>
    </ol>

 5. Building and rendering scenes with VR/AR in medical applications
    <ol type="a">
      <li>Importing virtual models of medical devices and clinical environments</li>
      <li>Extracting anatomy surface models from 3D image data</li>
      <li>Visualizing the scene on conventional, VR/AR and holographic displays </li>
      <li>An introduction to collaborative VR </li>
      <li>Putting it all together with 3D Slicer </li>
    </ol>

 6. Registration of medical image data
    <ol type="a">
      <li>2D and 3D image registration</li>
      <li>Model (point cloud / surface) registration </li>
      <li>Image-model registration </li>
      <li>Putting it all together with 3D Slicer </li>
    </ol>

 7. Quantitative analysis from medical image data
    <ol type="a">
      <li>Feature extraction workflow</li>
      <li>Following-up variations through time (single individual)</li>
      <li>Comparing individuals</li>
      <li>Putting it all together with 3D Slicer </li>
    </ol>

**ADVANCED TOPICS**

 8. Advanced segmentation of medical images using neural networks
    <ol type="a">
      <li>An introduction to neural networks for image segmentation using Pytorch</li>
      <li>An introduction to Monailabel for NN training with medical images</li>
      <li>An introduction to inference with Pytorch and Monailabel</li>
      <li>Putting it all together with 3D Slicer </li>
    </ol>

 9. An introduction to image guided therapy (IGT)
    <ol type="a">
      <li>Geometrical transforms</li>
      <li>Tracking systems</li>
      <li>Intraoperative imaging</li>
      <li>Putting it all together with 3D Slicer and the Plus Toolkit: building navigation systems</li>
    </ol>

10. Building simple medical applications with 3D Slicer (IGT)
    <ol type="a">
      <li>An introduction to the SW architecture of 3D Slicer</li>
      <li>The MRML scene description</li>
      <li>An introduction to Qt and Qt designer</li>
      <li>Using widgets in 3D Slicer</li>
      <li>Taking advantage of the available logic in 3D Slicer</li>
      <li>Putting it all together in a simple 3D Slicer application</li>
    </ol>

**Use cases (20 hours)**

The projects offered are based on the concepts studied in subjects 5, 8 and 9:

1.	Creating a Virtual Reality application in Slicer (Subject 5):
    <ol type="a">
      <li>Learn the basic actions needed to interact with objects and move around the Slicer scene using the VR controllers.</li>
      <li>Develop a virtual reality system for medical applications which allows the user to share and interact in real time with data from medical images.</li>
    </ol>


2.	Segmentation of medical images using neural networks (Subject 8):
    <ol type="a">
      <li>Develop a module in 3D Slicer to run the inference of a PyTorch model for the segmentation of medical images.</li>
    </ol>

3.	Developing a Python module for image guided therapy (IGT) (Subject 9):
    <ol type="a">
        <li>The objective is to create a module in 3D Slicer to load navigation data and perform fiducial-based registration.</li>
     </ol>


# Background and References

Examples of material which could be used to supplement the course content:
* _Biomedical Signal and Image Processing_ by K. Najarian and R. Splinter
* _Principles of Medical Imaging for Engineers_ by M. Chappell
* [3D printing medical devices](https://formlabs.com/blog/3d-printing-medical-devices/)
* [Slicer Virtual Reality](https://github.com/KitwareMedical/SlicerVirtualReality): Extension for 3D slicer that enables user to interact with the 3D scene using virtual reality
* [Slicer3: Image Guided Therapy (IGT)](https://www.slicer.org/wiki/Slicer3:_Image_Guided_Therapy_(IGT)): Tools to enable research in image guided therapy
