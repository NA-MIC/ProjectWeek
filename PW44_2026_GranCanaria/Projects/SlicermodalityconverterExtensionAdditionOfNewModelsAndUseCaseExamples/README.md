---
layout: pw44-project

permalink: /:path/

project_title: SlicerModalityConverter Extension - addition of new models and use case examples
category: Quantification and Computation
presenter_location: 

key_investigators:

- name: Ciro Benito Raggio
  affiliation: Karlsruhe Institute of Technology
  country: Germany

- name: Paolo Zaffino
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Maria Francesca Spadea
  affiliation: Karlsruhe Institute of Technology
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


SlicerModalityConverter is a 3D Slicer extension designed for medical image-to-image (I2I) translation.

The ModalityConverter module provides a user-friendly interface for integrating multiple AI models trained for I2I translation (currently MRI-to-CT). It also supports GPU acceleration for faster inference, and is designed to allow users to easily integrate custom models.

More about the module [here](https://github.com/ciroraggio/SlicerModalityConverter).



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Integration of new translation models for T1w-to-T2w MRI translation.
2. Creating use case examples with video tutorials. 



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Integrate two new pre-trained models for T1w-to-T2w translation (presented in this [study](https://arxiv.org/abs/2507.14575) and released in this [repository](https://github.com/AndreaMoschetto/medical-I2I-benchmark)), following the guidelines reported in the module documentation for integrating custom models.

2. Create video tutorials demonstrating the common uses of existing models. For example, show how to use MRI-to-synthetic CT translation models to extract the skull's representation from a T1w brain MRI.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

### Preogress
1. The integration of the two pre-trained T1w-to-T2w translation models was completed but not accepted. Although preliminary tests were performed, the achieved performance was not satisfactory for practical use. In addition, the training strategy adopted for these models makes their general usability and scalability difficult in a broader clinical/research context. For these reasons, the models were not officially integrated into the module.

2. A CBCT-to-CT translation model for the head and neck district was successfully integrated into the module.

3. A short tutorial was added to demonstrate how to extract the skull directly from a T1-w MRI using the MRHead example, exploiting the models available in the Modality Converter module.

### Next steps

1. Evaluate the possibility of integrating alternative, more robust T1w–T2w translation models with better generalization performance.

2. Extend the tutorial section with additional use cases based on the currently integrated models.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
* New model:
  ![](https://github.com/user-attachments/assets/537263e2-9a5a-4ec6-988d-3db61fd9dade)


* Tutorial: [Skull Extraction from T1w MRI via Deep Learning-based Image-to-Image Translation in 3D Slicer](https://github.com/ciroraggio/SlicerModalityConverter/blob/develop/ModalityConverter/assets/tutorials/MRItoCT-skull.mp4)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_
