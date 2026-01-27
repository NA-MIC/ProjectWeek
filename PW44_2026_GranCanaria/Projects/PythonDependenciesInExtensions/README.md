---
layout: pw44-project

permalink: /:path/

project_title: Python dependencies in extensions
category: Infrastructure
presenter_location: 

key_investigators:

- name: Ebrahim Ebrahim
  affiliation: Kitware
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: Andras Lasso
  affiliation: Queen's
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Many Slicer extension developers have to deal with the problem of external python dependencies: how to specify them, how and when to install them, and how to validate that the required things are installed. Everyone addresses the problem in a different way, often re-inventing the wheel and also often generating new great ideas. I'd like to collect all the best practices and turn them into a framework that is built into core slicer for extension developers to more easily grab and use. Something like "stick your dependencies in here and the use `slicer.util.check_python_dependences` and `slicer.util.install_python_dependencies`. If that turns out to be a bad idea for whatever reason, at least I can collect all the best practices and put them into the extension development documentation.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


* Encode into Slicer some way to make it more convenient for extension developers to handle external python dependencies.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


* Gather best practices on external python dependency handling in Slicer extensions, and then distill them into an optimized approach.
* Encode that approach in Slicer somehow, either as utility functions, updates to extension templates, or simply documentation.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


### Table of existing practices

2026-01-26

I've broken down the problem of external Python dependency into three components:

- **Checking:** How do we check whether the dependency requirements are already met by the environment?
- **Triggering:** What causes the requirement installation process to start?
- **Installing:** How do we carry out requirement installation?

The table below includes all 94 extensions that are currently in the [Slicer extension index](https://github.com/Slicer/ExtensionsIndex) and that have some external python dependencies to deal with, and my best quick guess as to how they approach each of the problems above.
Here is a legend to interpret the terms I've put in the table:

- **Checking:**
  - _simple_: Checkng is done by trying to import and and catching if it fails. It could also be done with importlib. No version checking.
  - _version_: Does some kind of version checking as well.
- **Triggering:**
  - _user_: Nothing triggers an automatic install. The user will have to install by following some steps.
  - _top level_: The install is triggered at some top level like the module enter function, such that it would happen the first time the module is even switched to for example. It could also be at the truly top-level-- in this case it would be triggered during module discovery, which is undesirable.
  - _processing_: When the user goes to run some kind of processing in the extension, that's when it actually checks if it has the dependencies it needs and kicks off install if not.
  - _button_: User has to press a button to install.
- **Installing:**
  - _user_: User has to do it by following some steps.
  - _simple_: Just `slicer.util.pip_install`.
  - _isolated_: There is a separate environment (such as a virtual env) into which the dependencies are installed (and so it is not going to be slicer's `pip_install` but some script or shell process that carries out installation).
  - _blocking-prevention_: Attempts to stop the installation from fully blocking the application. This could be by using threading of some sort or spawning a background process, or by otherwise trying to give slicer a chance to process events while the install is happening.
  - _display_: Has some more sophisticated display of what's going on while pip installing


---

<table>
     <thead>
          <tr>
               <th>Extension</th>
               <th>Checking</th>
               <th>Triggering</th>
               <th>Installing</th>
          </tr>
     </thead>
     <tbody>
          <tr>
               <td>ShapeVariationAnalyzer</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">user</td>
               <td style="background-color: #ccffcc; color: #006600">isolated</td>
          </tr>
          <tr>
               <td>SlicerVolBrain</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">user</td>
               <td style="background-color: #eeeeee">user</td>
          </tr>
          <tr>
               <td>PerkTutor</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>Q3DCExtension</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>QuantitativeReporting</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SegmentationReview</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>Slicer-ABLTemporalBoneSegmentation</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>Slicer-ASLtoolkit</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>Slicer-MusculoskeletalAnalysis</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>Slicer-PET-MUST-segmenter</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>Slicer-TITAN</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerANTsPy</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerAnatomyCarve</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerArduinoController</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerAuto3dgm</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerAutomatedDentalTools</td>
               <td style="background-color: #ccffcc; color: #006600">version</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerAutoscoperM</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerBigImage</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerBiomech</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerBreastUltrasoundAnalysis</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerBreast_DCEMRI_FTV</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerCADSWholeBodyCTSeg</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerCBCTToothSegmentation</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerCineTrack</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerColoc-Z-Stats</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerConnectToSupervisely</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerDBSCoalignment</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerDICOMwebBrowser</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerDMRI</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerDebuggingTools</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerDensityLungSegmentation</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerDentalModelSeg</td>
               <td style="background-color: #ccffcc; color: #006600">version</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #ccffcc; color: #006600">isolated, blocking-prevention</td>
          </tr>
          <tr>
               <td>SlicerFreeSurfer</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerHDBrainExtraction</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerHeadCTDeid</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerHeart</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerIDCBrowser</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #ccffcc; color: #006600">display</td>
          </tr>
          <tr>
               <td>SlicerIVIMFit</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerImageAugmenter</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">button</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerJupyter</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerKonfAI</td>
               <td style="background-color: #ccffcc; color: #006600">version</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #ccffcc; color: #006600">blocking-prevention</td>
          </tr>
          <tr>
               <td>SlicerLungCTAnalyzer</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerMEMOS</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerMHubRunner</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerMONAIAuto3DSeg</td>
               <td style="background-color: #ccffcc; color: #006600">version</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #ccffcc; color: #006600">blocking-prevention</td>
          </tr>
          <tr>
               <td>SlicerMONAIViz</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerMOOSE</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">button</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerMassVision</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerModalityConverter</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">button</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerMorph</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerMorphoDepot</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerMultiverSeg</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerMuscleMap</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerNNInteractive</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #ccffcc; color: #006600">display, blocking-prevention, isolated</td>
          </tr>
          <tr>
               <td>SlicerNNUnet</td>
               <td style="background-color: #ccffcc; color: #006600">version</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerNetstim</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerNeuro</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #ccffcc; color: #006600">display</td>
          </tr>
          <tr>
               <td>SlicerNeuroStrip</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerNeuropacs</td>
               <td style="background-color: #ccffcc; color: #006600">version</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerOpenLIFU</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #ccffcc; color: #006600">display</td>
          </tr>
          <tr>
               <td>SlicerOrbitSurgerySim</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #ccffcc; color: #006600">display</td>
          </tr>
          <tr>
               <td>SlicerPhotogrammetry</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerPipelines</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerPolycysticKidneySeg</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">button</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerPyTorch</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">button</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerPythonTestRunner</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerRVXLiverSegmentation</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerRadiomics</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerSPECTRecon</td>
               <td style="background-color: #ccffcc; color: #006600">version</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #ccffcc; color: #006600">display</td>
          </tr>
          <tr>
               <td>SlicerSandbox</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerSegmentHumanBody</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerSegmentWithSAM</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerSkeletalRepresentation</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerSoundControl</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerStereotaxia</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerSurfaceLearner</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerThemes</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">button</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerTissueSegmentation</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerTomoSAM</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerTorchIO</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerTotalSegmentator</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">processing</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerTractParcellation</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #dddddd">button</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerTrame</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerUltrasound</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>SlicerUniGradICON</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>Slicerflywheelcaseiterator</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>TCIABrowser</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>TOMAAT-Slicer</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>aigt</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
          <tr>
               <td>opendose3d</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #ccffcc; color: #006600">display</td>
          </tr>
          <tr>
               <td>slicer_flywheel_connect</td>
               <td style="background-color: #dddddd">simple</td>
               <td style="background-color: #eeeeee">top level</td>
               <td style="background-color: #dddddd">simple</td>
          </tr>
     </tbody>
</table>

### Next steps

2026-01-26

In the table above, the green cells are the items I think are worth revisiting and learning from for this project.

Other things I found while looking through these that I'd like to consider:

- Using `slicer.util.restart` to restart after install
- Showing a status message: `slicer.util.showStatusMessage`
- Showing the python console: `slicer.util.displayPythonShell`
- Using `slicer.util.tryWithErrorDisplay`
- Using a `BusyCursor` context manager

Further points that I'd like to follow up on:

- I found some [thoughts from JC](https://github.com/Slicer/Slicer/issues/7171) that I'd like to look over carefully.
- On that note, besides _checking_, _triggering_, and _installing_, I think there is also the problem of how to _specify_ dependencies.
- I had forgotten about [this work by David](https://github.com/Slicer/Slicer/issues/7707). This could help with the _triggering_ question in particular. One consideration is to not make things too opaque so as to make debugging difficult (e.g. say a module import fails; will the error be incomprehensible?)
- What about the problem of conflicts between requirements of different extensions? For an example see the mess that was caused by the conflict between the total segmentator and NNUnet extensions.
- When extension unit tests are running, they have the ability to influence each other's slicer python environment. It would be nice if there were some way to revert the slicer python environment before each extension test begins. This is out of the scope of the present project but we can consider how it might be done.

### Refined next steps

A plan of attack:

- Come up with a dependency specification format. Use [JC's commentary](https://github.com/Slicer/Slicer/issues/7171) and AI help to find the best solution. Consider the strange dependency conflict handling that takes place in [NNUnet](https://github.com/KitwareMedical/SlicerNNUnet/blob/e44b00883e8f373c72bf79c50455bd2c776ed8cf/SlicerNNUnet/SlicerNNUNetLib/InstallLogic.py#L32) and [Total Segmentator](https://github.com/lassoan/SlicerTotalSegmentator/blob/2e5f9c3aa38365cc63eba2f3c8ea1c2e2b79acd8/TotalSegmentator/TotalSegmentator.py#L745), or whether we can handle bringing the [currently isolated docker environment and requirements in NNInteractive](https://github.com/coendevente/SlicerNNInteractive/tree/76545192e1a925f911a31dea72802ad04d089072/server) into slicer's python. 
- Come up with a solution to the *checking* problem, referencing the extensions with the *version* tag in the table above and with some AI help.
- Come up with a solution to the *triggering* problem, referencing [David's work](https://github.com/Slicer/Slicer/issues/7707) and some AI help.
- Come up with a solution to the *installation* problem by addressing the following:
  - Display: Progress reporting, the option to prompt the user about what is happening and whether they want to proceed, showStatusMessage, busy cursor if not running in background. Reference the extensions with the *display* tag above.
  - Blocking prevention approach. Reference the extensions with the *blocking-prevention* tag above.
- Consider whether there is room to appraoch the problem of "environment reversion" for the sake of extension testing.
- Implementation

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_Coming soon..._



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- The [SlicerOpenLIFU](https://github.com/OpenwaterHealth/SlicerOpenLIFU) extension is where I have most recently applied what I know about handling python dependencies. But it could be so much better.

