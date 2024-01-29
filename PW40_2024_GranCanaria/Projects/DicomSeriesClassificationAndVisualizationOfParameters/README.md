---
layout: pw40-project

permalink: /:path/

project_title: DICOM series classification and visualization of parameters
category: DICOM
presenter_location: In-person

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

- name: Bálint Kovács
  affiliation: DKFZ
  country: Germany

- name: Stefan Denner
  affiliation: DKFZ
  country: Germany 

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

- name: David Clunie
  affiliation: PixelMed (IDC)
  country: USA
  
---

# Project Description

<!-- Add a short paragraph describing the project. -->

To use and develop AI methods, significant data curation is required. In some cases like prostate cancer segmentation, clinicians often use multiple MRI sequences for diagnosis such as T2, diffusion-weighted series, and derived maps.

Unfortunately, the information describing the sequences is often missing or incorrect, as it's prone to errors from technicians. The proper sequence could be analyzed visually, but this is cumbersome if thousands of scans need to be analyzed. Therefore, automatic methods for determining the right series are of interest.

We propose methods to aid in the curation of DICOM data, as well as aids to help in vizualization of DICOM parameters.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

We would like to develop approaches for aiding in the curation of data. The first will be the development of visualization tools to understand DICOM parameters used in scanning. Secondly, we will develop AI methods for classifying MRI scans, with a focus on prostate cancer.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Use packages such as [hiplot ](https://ai.meta.com/blog/hiplot-high-dimensional-interactive-plots-made-easy/) to visualize DICOM scanning parameters across different collections and modalities in IDC.
3.  Develop approaches for data curation using AI - e.g. determine the scan sequence, or if endorectal coil is present, etc.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Started [repo here](https://github.com/deepakri201/DICOMTagViz/) for initial [hiplot](https://github.com/facebookresearch/hiplot) exploration of DICOM tags of T2 weighted axial series of prostate imaging collections from IDC 

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Hiplot visualization of T2 weighted axial parameters from 5 different prostate cancer imaging collections in IDC

![](https://github.com/NA-MIC/ProjectWeek/assets/59979551/420c4733-c27e-4ef8-87a9-ebc35bb8e224)

Same hiplot but with rendering in the browser!

![](https://github.com/NA-MIC/ProjectWeek/assets/59979551/043542a8-99fb-42ad-8724-dc94588027c3)




# Background and References

[GitHub repo](https://github.com/deepakri201/DICOMTagViz/)

Some earlier work with parallel coordinates plots in Slicer:
* https://github.com/pieper/SlicerMultiMapper
* https://www.youtube.com/watch?v=Y4MyThyeIPs

Some earlier work on sequence classification:
1.  Ranjbar S, Singleton KW, Jackson PR, Rickertsen CR, Whitmire SA, Clark-Swanson KR, et al. A Deep Convolutional Neural Network for Annotation of Magnetic Resonance Imaging Sequence Type. J Digit Imaging. 2020 Apr;33(2):439–46. [doi:10.1007/s10278-019-00282-4](https://dx.doi.org/10.1007/s10278-019-00282-4)
2.  Noguchi T, Higa D, Asada T, Kawata Y, Machitori A, Shida Y, et al. Artificial intelligence using neural network architecture for radiology (AINNAR): classification of MR imaging sequences. Jpn J Radiol. 2018 Dec;36(12):691–7. [doi:10.1007/s11604-018-0779-3](https://dx.doi.org/10.1007/s11604-018-0779-3)
3.  Cluceru J, Interian Y, Lupo JM, Bove R, Butte A, Crane J. Automatic Classification of MR Image Contrast. In: ISMRM. 2020. Available from: https://archive.ismrm.org/2020/1804.html
4.  Remedios S, Roy S, Pham DL, Butman JA. Classifying magnetic resonance image modalities with convolutional neural networks. In: Mori K, Petrick N, editors. Medical Imaging 2018: Computer-Aided Diagnosis. Houston, United States: SPIE; 2018. p. 89. Available from: https://www.spiedigitallibrary.org/conference-proceedings-of-spie/10575/2293943/Classifying-magnetic-resonance-image-modalities-with-convolutional-neural-networks/10.1117/12.2293943.full [doi:10.1117/12.2293943](https://dx.doi.org/10.1117/12.2293943)
5.  Braeker N, Schmitz C, Wagner N, Stanicki BJ, Schröder C, Ehret F, et al. Classifying the Acquisition Sequence for Brain MRIs Using Neural Networks on Single Slices. Cureus. 2022 Feb;14(2):e22435. [doi:10.7759/cureus.22435](https://dx.doi.org/10.7759/cureus.22435)
6.  Vieira de Mello JP, Paixão TM, Berriel R, Reyes M, Badue C, De Souza AF, et al. Deep Learning-based Type Identification of Volumetric MRI Sequences. In: 2020 25th International Conference on Pattern Recognition (ICPR). Milan, Italy: IEEE; 2021. p. 1–8. Available from: https://ieeexplore.ieee.org/document/9413120 [doi:10.1109/ICPR48806.2021.9413120](https://dx.doi.org/10.1109/ICPR48806.2021.9413120)
7.  Mahmutoglu MA, Preetha CJ, Meredig H, Tonn J-C, Weller M, Wick W, et al. Deep Learning–based Identification of Brain MRI Sequences Using a Model Trained on Large Multicentric Study Cohorts. Radiology: Artificial Intelligence. 2024 Jan;6(1):e230095. [doi:10.1148/ryai.230095](https://dx.doi.org/10.1148/ryai.230095)
8.  Kasmanoff N, Lee MD, Razavian N, Lui YW. Deep multi-task learning and random forest for series classification by pulse sequence type and orientation. Neuroradiology. 2023 Jan 1;65(1):77–87. [doi:10.1007/s00234-022-03023-7](https://dx.doi.org/10.1007/s00234-022-03023-7)
9.  Svdvoort. DeepDicomSort. 2022. Available from: https://github.com/Svdvoort/DeepDicomSort
10.  van der Voort SR, Smits M, Klein S, for the Alzheimer’s Disease Neuroimaging Initiative. DeepDicomSort: An Automatic Sorting Algorithm for Brain Magnetic Resonance Imaging Data. Neuroinform. 2021 Jan 1;19(1):159–84. [doi:10.1007/s12021-020-09475-7](https://dx.doi.org/10.1007/s12021-020-09475-7)
11.  HD-SEQ-ID. www.neuroAI-HD.org; 2023. Available from: https://github.com/NeuroAI-HD/HD-SEQ-ID
12.  HeuDiConv. NIPY developers; 2022. Available from: https://github.com/nipy/heudiconv
13.  Gai ND. Highly Efficient and Accurate Deep Learning–Based Classification of MRI Contrast on a CPU and GPU. J Digit Imaging. 2022 Jun 1;35(3):482–95. [doi:10.1007/s10278-022-00583-1](https://dx.doi.org/10.1007/s10278-022-00583-1)
14.  Cluceru J, Lupo JM, Interian Y, Bove R, Crane JC. Improving the Automatic Classification of Brain MRI Acquisition Contrast with Machine Learning. J Digit Imaging. 2023 Feb;36(1):289–305. [doi:10.1007/s10278-022-00690-z](https://dx.doi.org/10.1007/s10278-022-00690-z)
15.  Mello JPV de. Jpvmello/type-identification-mri-sequences. 2023. Available from: https://github.com/Jpvmello/type-identification-mri-sequences
16.  Kasmanoff N. MRI Content Detection. 2022. Available from: https://github.com/nkasmanoff/mri-content-detection
17.  MRI Sequence Classification - No overlapping. Available from: https://docs.google.com/document/d/1UmE7jFfWaAxsS6wXodPRkdKeyDAcVdEWXfMKGzGiiKk/edit?usp=sharing&usp=embed_facebook
18.  T1 vs T2 MRI | T1and T2 MRI image comparison. mrimaster. Available from: https://mrimaster.com/t1-vs-t2-mri/
19.  Pizarro R, Assemlal H-E, De Nigris D, Elliott C, Antel S, Arnold D, et al. Using Deep Learning Algorithms to Automatically Identify the Brain MRI Contrast: Implications for Managing Large Databases. Neuroinform. 2019;17(1):115–30. [doi:10.1007/s12021-018-9387-8](https://dx.doi.org/10.1007/s12021-018-9387-8)
20.  Gauriau R, Bridge C, Chen L, Kitamura F, Tenenholtz NA, Kirsch JE, et al. Using DICOM Metadata for Radiological Image Series Categorization: a Feasibility Study on Large Clinical Brain MRI Datasets. J Digit Imaging. 2020 Jun;33(3):747–62. [doi:10.1007/s10278-019-00308-x](https://dx.doi.org/10.1007/s10278-019-00308-x)


