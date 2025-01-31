Back to [Projects List](../../README.md#ProjectsList)

# NorMIT-Plan: Segmentation, 3D Modeling and Planning of Liver Resections

## Key Investigators

- Rafael Palomar (The Intervention Centre, Oslo University Hospital; NTNU)
- Rahul P. Kumar (The Intervention Centre, Oslo University Hospital)
- Louise Oram (The Intervention Centre, Oslo University Hospital; Oslo and Akershus University College)

# Project Description

NorMIT-Plan is part of the **Nor**wegian centre for **M**inimally **I**nvasive Guided **T**hrerapy (NorMIT). The centre offers resources for medical technology research in minimally invasive therapies. NorMIT-Plan is a software package developed as a 3D Slicer extension which will provide tools for segmentation, 3D modeling and surgical plannif for liver resection procedures.

## Objective

1. Publish NorMIT-Plan in the extension manager.
2. Change models management to organs management.
3. Complete testing.
4. Fix known issues (aka rendering with depth-peeling).

## Approach and Plan

1. Get the NorMIT-Plan extension published in the extension manager.
2. Design an architecture for organ management. Then, working on the implementation of the new nodes, DMs, etc.
3. Testing, testing, testing.

## Progress and Next Steps

Currently, NorMIT-Plan consists of two modules (vessels segmentation and resection planning). The two modules are now functional and ready to be packed into an extension (Slicer project week). Despite the fact these modules are functional, some improvements (e.g., organ management) would be needed (Slicer project week) to provide users with a better experience. To a great degree, testing has been implemented. Along with the improvements to the vessels segmentation and the surgery planning modules, new segmentation modules for liver parenchyma and tumors will come during 2018.

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [Source code](https://github.com/TheInterventionCentre/NorMIT-Plan)

 1. Palomar, Rafael, et al. "A novel method for planning liver resections using deformable Bézier surfaces and distance maps." Computer Methods and Programs in Biomedicine 144 (2017): 135-45.
 2. Palomar, Rafael, et al. "Surface reconstruction for planning and navigation of liver resections." Computerized Medical Imaging and Graphics 53 (2016): 30-42.
 3. Kumar, Rahul P., et al. "Three-Dimensional Blood Vessel Segmentation and Centerline Extraction based on Two-Dimensional Cross-Section Analysis." Annals of Biomedical Engineering 43 (2015): 1223-34.
