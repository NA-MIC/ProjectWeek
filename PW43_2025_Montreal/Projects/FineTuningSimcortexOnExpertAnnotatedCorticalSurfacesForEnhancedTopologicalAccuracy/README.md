---
layout: pw43-project

permalink: /:path/

project_title: Fine-Tuning SimCortex on Expert-Annotated Cortical Surfaces for Enhanced Topological
  Accuracy
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Kaveh Moradkhani
  affiliation: École de Technologie Supérieure
  country: Canada

- name: Sylvain Bouix
  affiliation: École de Technologie Supérieure
  country: Canada

- name: Jarrett Rushmore
  affiliation: 'Boston University Medical '
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


SimCortex is a deep-learning framework that simultaneously reconstructs all four cortical surfaces (left/right white-matter and pial) from T1-weighted MRI, with a focus on minimizing inter-surface collisions and self-intersections while maintaining high geometric fidelity. To further improve robustness and generalization, we will fine-tune SimCortex—initially trained using FreeSurfer-generated segmentations—on an expert-annotated set of 50 manually segmented MRI volumes.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. **Fine‐tune SimCortex with high‐quality, manually labeled data **
A. We will fine-tune the pre‐trained SimCortex model to 50 expert‐annotated MRI segmentations, aiming to improve its ability to generate anatomically accurate, collision‐free cortical surfaces.

2. Objective B. **Compare outputs from multiple fine‐tuned configurations against the FreeSurfer‐trained baseline using geometric metrics**
A. We will run several fine‐tuning variants and quantitatively evaluate collision rate, self‐intersection fraction, Chamfer distance, ASSD, and HD, directly comparing each to the original FreeSurfer‐trained model.

3. Objective C. **Visually evaluate reconstructed surfaces in 3D‐Slicer to confirm anatomical plausibility**
A. We will load and inspect the cortical meshes from each configuration using 3D Slicer.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


	•	**Preprocessing:** Convert 50 manually segmented MRI datasets into a format compatible with the SimCortex framework through a preprocessing pipeline.
	•	**Model Fine-Tuning:** Fine-tune the SimCortex model using the preprocessed manual datasets to improve anatomical accuracy and generalization.
	•	**Evaluation Metrics:**  Evaluate Model performance across configurations using quantitative metrics.
	•	**Baseline Comparison:** Compare results with the baseline SimCortex model originally trained on FreeSurfer-generated segmentations.
	•	**Expert Review:** Collaborate with Professor Jarrett Rushmore (neuroanatomy expert) to visually inspect the cortical reconstructions for anatomical plausibility.
	•	**Configuration Selection:** Identify optimal configurations based on combined quantitative performance and expert-guided visual assessment.



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


_No response_

