---
layout: pw44-project

permalink: /:path/

project_title: Adding DICOM Support Information To Extension Manager
category: DICOM
presenter_location: 

key_investigators:

- name: Kyle Sunderland
  affiliation: Queen's University
  country: Canada

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Currently DICOM support in extensions is written to a json file in the slicer repo ([DICOMExtensions.json](https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOM/DICOMExtensions.json)), however this information is not frequently updated as new extensions are added, unmaintained extensions removed, and additional modality support added to extensions.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Add additional metadata to the extension index to describe DICOM support implemented in each extension.
2. During DICOM import if no DICOM plugins are able to load the modality, then query the list of available extensions to find an extension that can import the data.
3. Also add additional metadata information (multiple categories, soft dependencies, etc).



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Update Slicer ExtensionsIndex to include DICOM related metadata, update schema ([See branch here](https://github.com/Sunderlandkyl/ExtensionsIndex/tree/dicom_support_rule))
2. Update [Slicer Package Manager](https://github.com/girder/slicer_package_manager) to handle additional DICOM support metadata
    - This can be done by specifying a [rule-engine](https://pypi.org/project/rule-engine/) string that can be used to define extension compatibility with Modality and SOPClassUID.
    - Ex:
    ```"(Modality == 'SEG') or (SOPClassUID == '1.2.840.10008.5.1.4.1.1.30') or (Modality == 'SR' and (SOPClassUID == '1.2.840.10008.5.1.4.1.1.88.22' or SOPClassUID == '1.2.840.10008.5.1.4.1.1.88.33'))"```
3. Update 3D Slicer core to query the list of available extensions to find an extension that can handle the current modality. ([See branch here](https://github.com/Sunderlandkyl/Slicer/tree/dicom_plugin_extension_check))
4. Integrate this PR with other efforts to update the extension manager (extensions tiers, multiple categories, etc. - see [https://github.com/girder/slicer_package_manager/pull/124](https://github.com/girder/slicer_package_manager/pull/124))
5. Update SlicerIDCBrowser?
6. Need to revisit QuantitativeReporting DICOM plugin - it won't be able to load segmentation of a SM image!


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Support for additional metadata types in json/s4ext and Girder:
    - dicom_support_rule: Logical expression that can be evaluated to suggest extensions that are able to handle a specific DICOM file.
    - keywords: Additional terms that can be searched when filtering extensions
    - tier: Rebased version of Jc's branch that adds extension support "tier"
    - reccomendations: List of reccomended extensions that should be installed by the user. Not including build dependencies
      
2. Evaluation of dicom_support_rule to suggest extensions from within Slicer
    -  Added logic to the DICOM module so that when the loading of an extension fails, we suggest that the user install an extension that can load their data.
      
# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

### Extension suggestion
<img width="2222" height="1580" alt="image" src="https://github.com/user-attachments/assets/23334375-e646-4e1b-9437-091c561410c0" />

### Girder contents
<img width="2405" height="1590" alt="image" src="https://github.com/user-attachments/assets/6dace467-46a2-4ee6-bd02-3029f130c8d0" />

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [https://github.com/girder/slicer_package_manager](https://github.com/girder/slicer_package_manager)
- [https://pypi.org/project/rule-engine/](https://pypi.org/project/rule-engine/)

