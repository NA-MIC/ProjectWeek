---
layout: pw41-project

permalink: /:path/

project_title: BAMF nnUNet MRI Breast Model
category: Segmentation / Classification / Landmarking
presenter_location: Online

key_investigators:

- name: Rahul Soni
  affiliation: BAMF Health
  country: Singapore

- name: Jithendra Kumar
  affiliation: BAMF Health
  country: Singapore

- name: Jeff Van Oss
  affiliation: BAMF Health
  country: US

- name: Gowtham Murugesan
  affiliation: BAMF Health
  country: US

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We trained an nnUNet model to segment Breast, Fibroglandular Tissue, and Structural Tumor from MRI scans. We prepared the training set from multiple source such as [Breast-MRI-NACT-Pilot](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=22513764), [Duke-Breast-Cancer-MRI](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=70226903), and [ISPY1-Tumor-SEG-Radiomics](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=101942541) 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. `Model Container`: We would like to bring our model resources into a deployable container that can be used by research community to use our models for Breast segmention of MRI Scans
2. `Ease of Use`: Anyone should be able to pull the container (without access issues), mount the input scans and get segmentations
3. `Flexibility`: Target users should be able to get outputs in different formats like `dicom`, `nifti`, `nrrd` etc
4. `Scalability`: Support for single point inference as well as batched inference



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


We already have trained model weights and a python module that provides an interface for segmentation using the aforesaid model. Next steps for us would be to:
- Publish models weights in Zenodo
- Wrap around segmentation module using Mhub core APIs
- Build and test the container
- Create documentation



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Trained the Breast and tumor segmentation model
2. Wrote a segmentation / inference module using trained model weights
3. Added support for `nifti` and `nrrd` outputs



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


Coming soon



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Coming soon

