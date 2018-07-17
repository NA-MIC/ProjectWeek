
## Brain Tumour Segmentation 
# Key Investigators
- Daiana Pur (Biomedical Engineering, Western University) 

# Project Description
Adding a Brain Tumour Segmentation feature to an existing Neurosurgical Planning tool

## Objective
1. Visualize Tumour   
2. Learn the features of SegmentEditor
3. Learn features of module_segment_statistics 
4. Introduce SegmentEditor features into existing scripted extension
5. Troubleshoot
 

## Approach and Plan

1. Visualize different types of Tumours (high grade glioma vs low grade glioma etc) by obtaining sample data
2. Different types of tumours require different approaches depending on size, visiblility of contrast 


## Progress and Next Steps
1.Obtained Sample Data, tried different settings for creating mask over tumors 
- module_segment_statistics module computes volume, surface, mean intensity, and various other metrics for each segment.
- SlicerDMRI to obtain tracts around tumour 

2. Troubleshooting existing extension

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

https://sites.duke.edu/pcqiba/2018/05/13/new-protocol-for-tumor-segmentation-using-3d-slicer/
http://www2.imm.dtu.dk/projects/BRATS2012/Jakab_TumorSegmentation_Manual.pdf
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991434/
http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html

- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data
