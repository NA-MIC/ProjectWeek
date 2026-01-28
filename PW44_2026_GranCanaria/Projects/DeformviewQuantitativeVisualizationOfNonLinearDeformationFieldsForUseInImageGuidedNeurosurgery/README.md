---
layout: pw44-project

permalink: /:path/

project_title: 'DeformView: Quantitative Visualization of Non-Linear Deformation Fields for Use in
  Image-Guided Neurosurgery'
category: Quantification and Computation
presenter_location: 

key_investigators:

- name: Isabel Frolick
  affiliation: McGill University
  country: Canada

- name: Elise Donszelmann-Lund
  affiliation: McGill University
  country: Canada

- name: Étienne Léger
  affiliation: McGill University
  country: Montreal Neurological Institute, Canada

- name: Raphäel Christin
  affiliation: McGill University
  country: Canada

- name: Kaleem Siddiqi
  affiliation: McGill University
  country: Centre of Intelligent Machines, Canada

- name: D. Louis Collins
  affiliation: McGill University
  country: Montreal Neurological Institute, Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We have been developing DeformView, a visualization module for 3D Slicer that improves the interpretation of non-linear brain deformation (“brain shift”) during image-guided neurosurgery and as a training tool for inexperienced surgeons and researchers. 
DeformView provides two dense, intuitive visualization maps: (1) a dense displacement magnitude map (mm), and (2)
a Jacobian determinant magnitude map representing local tissue expansion and compression (%).

The proposed module combines scientifically derived, intuitive colour maps and voxel-wise
cursor pointer that directly displays displacement values on hover, a function not available in existing
Slicer tools, to improve user understanding and confidence.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. **_Objective A._ Improve user experience** and stability by identifying and fixing bugs, refining interactions, and ensuring reliable performance across datasets.
2. **_Objective B._ Gather user feedback** from researchers and clinicians to guide the design of additional features, including potentially adding features to visualize registration error and uncertainty within the module).
3. **_Objective C._ Integrate transform grid/ glyph** visualizations directly into DeformView to provide complementary spatial context alongside dense deformation maps.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We will systematically test DeformView across representative datasets (focusing on IGNS-focused data - ReMIND, RESECT, BITE, etc.) and use cases to identify and resolve software bugs. We will ask attendees to use the module to identify common workflows, areas of improvement. We will also perform stress and destructive testing.
2. User-centered design and feedback: We will conduct structured feedback sessions with expert users, non-expert users, and clinicians, using our targeted questionnaires and short tasks to identify desired features and usability gaps. We will lead discussions with attendees to identify areas of improvement and feature prioritization.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


### Progress
We have implemented the core functionality of the DeformView module, including dense deformation visualization, Jacobian-based expansion/compression maps, and voxel-wise readout on cursor hover. Initial testing confirms that primary visualization goals have been achieved, with only minor usability and stability issues remaining.

We conducted a user study with 10 non-expert participants (average 2.9 years of imaging research experience) to evaluate module functionality. Participants compared DeformView to the existing 3D Slicer Transform Visualizer across four attributes: helpfulness in comprehension, interpretability, intuitiveness, and user confidence, using Likert ratings and the System Usability Scale. On average, DeformView was rated higher across all categories (mean: 4.1/5.0 vs 3.2/5.0), with statistically significant improvements in helpfulness (p=0.008) and intuitiveness (p=0.027). Overall, 80% of participants preferred DeformView over the existing module, confirming the value of our visualization approach.

#### Native Apple Silicon Mac Build
<img width="454" height="371" alt="image" src="https://github.com/user-attachments/assets/d06771dd-edc0-4d53-8b58-ef250698447d" />



### Next Steps

TODO: 
1. Colour Map and Legend Modifications

- Reduce legend text size 
- Investigate and fix legend scale reload bug
- Resolve remaining default colour map behaviour, consistent default colour levels when loading new maps
- Interaction between legend and colour level/window controls
- Clarity of colour map loading and switching- add descriptive text under the “Color Map” selector

2. Jacobian-Specific Visualization Controls

- Jacobian colour legend labels
- Set Jacobian window and level to constant values to ensure consistent interpretation -  fixed scaling (check that we want this)


3. User Interface and Readability Improvements
- Adjust cursor text size for improved readability
- Implement a full reset of default settings, not limited to window/level
- Should colour be 'color' in the UI? Americanize.


4. Stability and Bug Fixes

- Fix crash when two images are overlaid (temp mitigation -> set one image to 0% opacity on module entry)





# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


**Displacement Magnitude Map**  
Voxel-wise magnitude of non-linear deformation between preoperative T2-FLAIR MRI and intraoperative tumour resection T2-FLAIR, from Case 50 of the ReMIND dataset. Warmer colours indicate larger tissue displacement.

<img src="https://github.com/user-attachments/assets/72cd8330-0b6c-4e1b-bed4-29fcaef86351" width="800" alt="Displacement magnitude map" />

---

**Overlay of Displacement Magnitude (Colour Map) & Current 3D Slicer Transform Visualizer Module (Glyphs)

The current Transform Visualizer module (core 3D Slicer module) visualizes deformation as glyphs (arrows), grid, and contour. When integrated together, it is more intuitive where deformation has occurred (DeformView) and the direction of deformation (Transform Visualizer).

<img width="800" alt="NAMIC-Overlay" src="https://github.com/user-attachments/assets/7f059022-35c2-41d7-ae36-b223d832a4a6" />


---
**Jacobian determinant magnitude map**  
Visual of the Jacobian map, where red indicates tissue expansion and blue is tissue compression, as a percentage. This is the same data as the above displacement magnitude example.

<img width="700" alt="Jacobian_mag" src="https://github.com/user-attachments/assets/4b01baf2-ddc9-44da-b8c2-9a5b81b702b8" />


---

**User Study Results**  
Comparison of **DeformView** with the existing Transform Visualizer module (n=10) across four attributes: helpfulness, interpretability, intuitiveness, and user confidence (1–5 scale; higher scores indicate better performance). DeformView is rated higher across all categories, with significant improvements in helpfulness and intuitiveness.

<img src="https://github.com/user-attachments/assets/22094efd-4df5-4a33-b21e-ed3e88a6c897" width="800" alt="User study results" />





# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Miner, R. C. (2017). Image-guided neurosurgery. Journal of Medical Imaging and Radiation Sciences, 48(4), 328–335.

Abhari, K., Baxter, J. S., Chen, E. C., Khan, A. R., Peters, T. M., De Ribaupierre, S., & Eagleson, R. (2014). Training for planning tumour resection: augmented reality and human factors. IEEE Transactions on Biomedical Engineering, 62(6), 1466–1477.

King, F., Lasso, A., & Pinter, C. (2015, August 4). TransformVisualizer (Documentation/Nightly/Modules). 3D Slicer Wiki. [Link](https://www.slicer.org/wiki/Documentation/Nightly/Modules/TransformVisualizer)

Vlachogianni, P., & Tselios, N. (2022). Perceived usability evaluation of educational technology using the System Usability Scale (SUS): A systematic review. Journal of Research on Technology in Education, 54(3), 392–409.

Drouin, S., Kochanowska, A., Kersten-Oertel, M., Gerard, I. J., Zelmann, R., De Nigris, D., … & Collins, D. L. (2017). IBIS: an OR ready open-source platform for image-guided neurosurgery. International Journal of Computer Assisted Radiology and Surgery, 12(3), 363–378.

Chung, M. K., Worsley, K. J., Paus, T., Cherif, C., Collins, D. L., Giedd, J. N., … & Evans, A. C. (2001). A unified statistical approach to deformation-based morphometry. NeuroImage, 14(3), 595–606.

Juvekar, P., Dorent, R., Kögl, F., Torio, E., Barr, C., Rigolo, L., … & Kapur, T. (2024). REMiND: The brain resection multimodal imaging database. Scientific Data, 11(1), 494.

Crameri, F., & Hason, S. (2024). Navigating color integrity in data visualization. Patterns, 5(5), 100972. doi:10.1016/j.patter.2024.100972

