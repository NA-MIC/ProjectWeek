---
layout: pw45-project

permalink: /:path/

project_title: Recon-all correction script based on manual subcortical segmentation files
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Jarrett Rushmore
  affiliation: Center for Morphometric Analysis
  country: Massachusetts General Hospital, USA

- name: Benoît Verreman
  affiliation: ETS
  country: Canada

- name: Sylvain Bouix
  affiliation: ETS
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


White and pial surfaces and parcellation (aparc+aseg) from recon-all pipeline (FreeSurfer 7.4.1) need quite a few manual corrections.
At the same time, 100 cases from HCP-YA dataset were manually segmented using HOA2 atlas.
The goal of the project is to leverage the latter to get better results with recon-all.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Make the pipeline more straightforward, by using only one edited input image (subcortical HOA segmentation)
2. Visually check the different scenario results of the script, and solve following region issues: hippocampus/amygdala, temporal lobe
3. Train an nnUNet model on segmenting white and gray matter based on manually edited ribbon



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Create a new script to merge HOA and FS aseg.presurf.mgz file (merge_hoa_into_aseg.py)
2. Modify previous script (ribbon_edit_script.sh) to adapt to new input
3. Use edited ribbon of HOA to train an nnUNet model



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. merge_hoa_into_aseg.py works properly
2. Final result is good: surfaces and parcellation are HOA compatible (minimal corrections needed)
3. nnUNet trained model didn't segment properly WM/GM
  - add HOA subcortical labels to help segmentation
  - compare with other models (like Unest)



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
<img width="2228" height="2926" alt="HOABV_Project Week(1)" src="https://github.com/user-attachments/assets/4a51c349-5b44-49f5-895e-b5648b22506d" />


