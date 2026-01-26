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



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Update Slicer ExtensionsIndex to include DICOM related metadata, update schema ([See branch here](https://github.com/Sunderlandkyl/Slicer/tree/dicom_plugin_extension_check))
2. Update [Slicer Package Manager](https://github.com/girder/slicer_package_manager) to handle additional DICOM support metadata
    - This can be done by specifying a [rule-engine](https://pypi.org/project/rule-engine/) string that can be used to define extension compatibility with Modality and SOPClassUID.
    - Ex:
    ```"(Modality == 'SEG') or (SOPClassUID == '1.2.840.10008.5.1.4.1.1.30') or (Modality == 'SR' and (SOPClassUID == '1.2.840.10008.5.1.4.1.1.88.22' or SOPClassUID == '1.2.840.10008.5.1.4.1.1.88.33'))"```
3. Update 3D Slicer core to query the list of available extensions to find an extension that can handle the current modality. (Kyle has the branch already)
4. Integrate this PR with other efforts to update the extension manager (extensions tiers, multiple categories, etc. - see [https://github.com/girder/slicer_package_manager/pull/124](https://github.com/girder/slicer_package_manager/pull/124))
5. Update SlicerIDCBrowser?
6. Need to revisit QuantitativeReporting DICOM plugin - it won't be able to load segmentation of a SM image!


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [https://github.com/girder/slicer_package_manager](https://github.com/girder/slicer_package_manager)
- [https://pypi.org/project/rule-engine/](https://pypi.org/project/rule-engine/)

