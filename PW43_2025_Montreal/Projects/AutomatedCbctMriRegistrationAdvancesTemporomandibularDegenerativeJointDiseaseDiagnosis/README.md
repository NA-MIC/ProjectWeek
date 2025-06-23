---
layout: pw43-project

permalink: /:path/

project_title: Automated CBCT-MRI Registration Advances Temporomandibular Degenerative Joint Disease
  Diagnosis
category: Quantification and Computation

key_investigators:

- name: Alban Gaydamour
  affiliation: University of Michigan
  country: USA

- name: Lucia Cevidanes
  affiliation: University of Michigan
  country: USA

- name: Gaelle Leroux
  affiliation: CPE Lyon
  country: France

- name: Juan Prieto
  affiliation: University of North Carolina
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Enzo Tulissi
  affiliation: University of Michigan
  country: USA

---

### Project Description

Accurate registration between CBCT and MRI scans offers complementary visualization of osseous and soft tissue structures around the temporomandibular joint (TMJ). This project aims to automate the registration process to support more effective diagnosis of temporomandibular degenerative joint disease.

### Objective

1. Develop a robust multi-step registration pipeline to align MRI and CBCT images in the TMJ region.
2. Enhance diagnostic accuracy by integrating soft tissue and osseous imaging modalities.
3. Move toward a fully automated workflow that eliminates manual intervention.

### Approach and Plan

1. Perform initial coarse alignment using TorchReg to approximate global positioning of the volumes.
2. Automatically crop both CBCT and MRI volumes to isolate the TMJ region of interest.
3. Apply Elastix-based deformable registration to the cropped images for fine alignment.
4. Evaluate registration quality through both visual assessment and quantitative metrics.
5. Plan to implement automated TMJ region localization to eliminate manual cropping.

### Progress and Next Steps

1. Implemented automated global registration using TorchReg.
2. Established an automated cropping protocol focused on the TMJ region to reduce failure modes in deformable registration.
3. Completed fine registration using Elastix on cropped image pairs.
4. Next steps include developing automated tools to segment MRIs and adding an articular disc label to improve interpretability

### Illustrations

### **Figure 1:** Input MRI (grey) and CBCT (beige)
![Left half of the head](https://github.com/user-attachments/assets/4f7dd2ff-5461-41a3-b03e-b2f2d6949aa7)

### **Figure 2:** Patient after first registration
![Superposition of MRI and CBCT after first registration](https://github.com/user-attachments/assets/9fe4e5b5-386c-4a44-9d2a-3137fe9907e9)

### **Figure 3:** Cropping of the left TMJ
![Region of Interest used for cropping of the TMJ](https://github.com/user-attachments/assets/b2be7af9-9237-4204-9641-8fc8dc8af751)

### **Figure 4:** Patient after second registration
![Superposition of MRI and CBCT after second registration](https://github.com/user-attachments/assets/98eddeb9-ce15-4e02-a079-7faa236ee6d4)

### Background and References

- [TorchReg](https://github.com/codingfisch/torchreg)
- [Elastix](https://github.com/SuperElastix/elastix)
- [Github](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools)
