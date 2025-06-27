---
layout: pw43-project

permalink: /:path/

project_title: 'Segmenting and quantifying fat herniation and muscle conformational change in fractured
  orbits '
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Chi Zhang
  affiliation: Texas A&M College of Dentistry
- name: Caelan Ducommun
  affiliation: Texas A&M College of Dentistry
- name: Gwen Tran
  affiliation: Texas A&M College of Dentistry
- name: Andrew Read-Fuller
  affiliation: Texas A&M College of Dentistry
---

# Project Description

Segmentation of orbital soft tissue and bones are difficult because the structures are small and thin and boundaries are not well defined in medical CT scans. Fractured orbits introduced additional challenges, including cracked and isolated bones, muscle conformational changes (e.g., shape and size), fat herniation into adjacent sinuses, and hematoma. Detecting and delineating these conditions are crucial for surgical decision making and planning.

Manual segmentation of orbit is laborious and technical. The available deep learning tools are scarce. TotalSegmentator recently included a model for segmenting extraocular muscles but it might only be based on about twenty manual segmentations with no peer-reviewed publications. Boundaries between some muscles (e.g., superiour rectus & levator palpebrae) cannot be validated due to CT image qualities. A company from Finland has a model for segmenting orbital tissue but they did not incorporate fractured conditions. Consequently, fat is indistinguishable from blood in herniation cases.

-Segmentation of orbital fat (herniation into maxillary sinus) vs. blood. A Finnish commercial software include blood as fat segmentation, thus failed to compute herniation. <br>
<img src="https://github.com/user-attachments/assets/444d7704-1965-41cb-a42d-621dc1fa88d6" width="400"/>
<img src="https://github.com/user-attachments/assets/e72d0d66-a01c-40da-a5cd-dd4b4ad58212" width="350"/><br>
<img src="https://github.com/user-attachments/assets/e65d9afd-587a-427c-a414-bc0a0243a6b2" width="400"/>
<img src="https://github.com/user-attachments/assets/c54ffdc2-004d-46c0-a94a-6c6e8dcd37b5" width="350"/><br>

<br>
-Conformational change in inferior rectus (segmented by TotalSegmentator):<br>
<img src="https://github.com/user-attachments/assets/0d8e2ae1-f45c-4a45-82bf-9b4a9a9505aa" width="450"/>
<img src="https://github.com/user-attachments/assets/658c39f1-91cc-486f-a466-0c8eebb81339" width="450"/>


## Objective
1. Create repeatable semi-automatic approaches for accurately segmenting orbital tissue, including thin bone & soft tissue, especially in fractured conditions
2. Creating repeatable metrics based on segmentation results to detect and quantify tissue changes to aid decision making
3. Stretching goal: validate TotalSegmentaor results and initiate deep learning segmentation development. Detecting and segmentting fractures.



## Approach and Plan

1. Use TotalSegmentator as a start point to correct its results, then add fat tissue with a focus of differentiating herniated fat vs. blood (Grow-from-Seeds appear to perform well). How to consistently delineate anterior boundary of orbital fat.
2. Focus on detecting and quantifying fat herniation and inferior rectus muscle (also medial rectus) conformational changes because they are most frequently used in decision making.
3. Fat herniation: register the contralateral side to the fractured side to quantify herniation using Hausdorf distance, distance map, etc.
4. Inferior rectus m.: perhaps connecting centroids of each slice to draw its basic shape and use cross section area to quantify sizes.
5. Consulting people at PW to prepare for deep learning segmentation model training for detection and segmentation, including how to efficiently creating training dataset.




## Progress and Next Steps

1. Testing nnInitiatve to prepare manual segmentation and potential traning dataset. Continue develop a repeatable workflow for orbital fracture cases. <br>
![Screenshot from 2025-06-26 23-41-36](https://github.com/user-attachments/assets/26bc4612-22cf-4400-a99e-816356722af6)
![Screenshot from 2025-06-26 23-42-56](https://github.com/user-attachments/assets/cf9dc043-0c9a-4323-87ee-6b5db2fd5a0f)


3. Using the centroid of each slice of inferior rectus to create a curve (subsampled to 20 points). The shape of the curve, such as maximum curvature, might be able to detect muscle conformational change related to surgical decision, such as simple logistic regression.<br>
Unfractured side <br>
![Screenshot from 2025-06-27 01-00-41](https://github.com/user-attachments/assets/d4046e22-d9de-4090-a159-0e37105db479)
![Screenshot from 2025-06-27 01-02-50](https://github.com/user-attachments/assets/9400ace4-b85c-469d-a0ec-fb72d93778c4)

4. Still difficult to quantify fat herniation, though nnInteractive and Grow from Seeds can capture it well. The reason is because the anterior boundary of the fat tissue is arbitrarily delineated and asymmetry of orbits.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

