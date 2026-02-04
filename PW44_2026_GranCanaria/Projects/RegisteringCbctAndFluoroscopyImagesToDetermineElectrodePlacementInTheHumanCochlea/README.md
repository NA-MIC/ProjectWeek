---
layout: pw44-project

permalink: /:path/

project_title: Registering CBCT and fluoroscopy images to determine electrode placement in the human
  cochlea
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Attila Nagy
  affiliation: University of Szeged
  country: Hungary

- name: Paolo Zaffino
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Attila Tanács
  affiliation: University of Szeged
  country: Hungary
  
- name: András Lasso
  affiliation: Queen's University
  country: Canada, ON
  
- name: Roland Nagy (remote)
  affiliation: University of Szeged
  country: Hungary

- name: Ádám Perényi (remote)
  affiliation: University of Szeged
  country: Hungary
---

# Project Description

<!-- Add a short paragraph describing the project. -->


Cochlear implant electrode placeemnt is exteremely important during cochlear surgery, as inserting it as close as possible to the modiolus produces the best results (lower energy consumption of the device, better hearing outcomes, speec recognition ans so on).
But it is an imaging nightmare: imeging the inner ear isn't that easy, and doing so with metal inserted is even more challenging. One of the best option is to use fluroscopy images, but then we lose the 3rd dimension.
If we could register the two modalities, we could have the desired accuracy and extend the measurements into 3D.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Brainstorm about ideas, and maybe create a prototype using example data.

- Collect ideas
- Collect even more ideas
- Hopefully create a prototype



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->



- Examine the CBCT and fluoroscopy images and identify the points. One for sure is that the CBCT images have bad distances, as usual...
- Try to overlay/register fluoroscopy images using anatomical landmarks



## Progress and Next Steps
With some sample data we tried the new Virtual CathLab module. It seems that it has most of the functionality we need to bring our work further.
Also, created a small anonymization Slicer extension that will fit our later workflow.


1. Describe specific steps you **have actually done**.
- Checked the Virtual CathLab module.
- Successfully loaded our own imaing CBCT data into it, and we had similar results as our fluoroscopy images
- Createn a batch anoymization extension




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![](https://github.com/user-attachments/assets/db4355c7-71b9-418e-ab0d-07d18bd3c004)
![](https://github.com/user-attachments/assets/104baf5d-bcde-4378-b411-b7f450d4f9db)

Progress:
Anonymization moudle UI:
<!-- <iframe width="960" height="540" src="https://www.youtube.com/embed/L2dJuvdan_0"> </iframe> -->
<iframe width="960" height="540" src="https://www.youtube.com/embed/L2dJuvdan_0?si=oUD2uVGXpINsztF-"> </iframe>

In case the embedded video doesn't work, here is the link to YouTube:
https://www.youtube.com/watch?v=L2dJuvdan_0

Anonymization moudle UI:
 ![](https://github.com/user-attachments/assets/f8629ab0-713c-4ffa-a4b4-0ca0cd36ca65)


Example module usage with our own cochlear implant CBCT data:
![](https://github.com/user-attachments/assets/680dd100-0976-4829-94b0-7755068e8605)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_
