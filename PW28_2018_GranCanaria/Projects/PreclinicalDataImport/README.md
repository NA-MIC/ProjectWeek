Back to [Projects List](../../README.md#ProjectsList)

# Improve multivolume preclinical MRI data import (DCE, DTI). 

## Key Investigators

-	Sharon Peled (Brigham and Women’s, USA)
-	Andras Lasso (Queen’s University, Canada)
-	Lauren O’Donnell (Brigham and Women’s, USA)

# Project Description

Correct Slicer dynamic MRI DICOM frame data and DTI gradient data loading for Bruker preclinical MRI systems (Paravision version 6).


## Objective

1. Modify the multivolume importer to correctly display and represent preclinical DCE MRI DICOM data.
1. Modify the DTI loader.

## Approach and Plan

1. DCE: The first correction is to make sure the frame time in DCE MRI is not merely copied from the 'RepetitionTime' field in the DICOM files. Instead, this should be multiplied by the number of phase encoding steps. Test. 
1. DTI: modify gradient data loading.

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References
Link to MRI data:
https://www.dropbox.com/sh/0ijt66kej9y7uo5/AADUwatia0cI60SftswEq0O6a?dl=0
<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->
