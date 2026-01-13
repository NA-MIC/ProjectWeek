---
layout: pw44-project

permalink: /:path/

project_title: Exploration of foundation models and their embeddings for other tasks using the cloud
category: Cloud / Web
presenter_location: 

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The popularity and use of foundation models (FMs) have exploded in recent years. Within the medical imaging field alone, numerous models have been developed to support various downstream tasks, including classification and segmentation. 

However, as a user, it's hard to understand the embeddings that the models produce. Also, it's hard to figure out: 
1) which model to use, and 
2) what tasks the model supports. 

In this project, we plan to explore how the cloud can help us understand these embeddings from various FMs. Recently, we have extracted embeddings from lung cancer tumors in the National Lung Screening Trial (NLST) CT dataset from 9 different models. We will use the latest features in the Google Cloud Platform to help us explore and understand these embeddings. 

We are most interested in: 
1) how these embeddings can be visualized, and if clusters are visible, 
2) if these embeddings can be used to find similar patients, and 
3) if they can actually be used for other tasks 

Possible extensions to this work: 
1) We could explore the embeddings that Google has provided from their pathology foundation model [here](https://research.google/blog/health-specific-embedding-tools-for-dermatology-and-pathology/) and [here](https://github.com/Google-Health/imaging-research/tree/master/path-foundation).
2) We could extend this exploration to lung ultrasound images, where visualizing the embedding space could help us choose representative and diverse images for expert annotation 

How could it relate to Slicer and Imaging Data Commons (IDC)? Given a sample patient image, we could retrieve the k-closest patients in IDC. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. We will figure out how to store these embeddings in the cloud to enable a quick search and comparison. 
2. Next, we will explore and visualize these embeddings. 
3. Then, we will use these embeddings to perform image retrieval -- finding similar patients in the NLST collection. 
4. Lastly, we will show how to use these embeddings for a downstream task. 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We will see if Google Cloud Platform BigQuery (BQ) can be used to store the embeddings: https://docs.cloud.google.com/bigquery/docs/vector-search-intro and https://docs.cloud.google.com/bigquery/docs/vector-index
2. Next, we will create an interactive plot to explore embeddings and any clustering in a low-dimensional space. We will let the user click on points to open up an OHIF link with the original image data. 
3. We will investigate whether vector search or a similarity search can be performed to find similar patients. 



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->







# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


Initial analysis (no cloud) of using embeddings for lung cancer histology classification: 
<img width="412" height="326" alt="Image" src="https://github.com/user-attachments/assets/bd9434d2-80bb-4309-9f74-5d5d18b319c8" />

Initial analysis (no cloud) of using embeddings for lung cancer staging classification: 
<img width="412" height="326" alt="Image" src="https://github.com/user-attachments/assets/4ddbf08d-e352-4c26-9c70-51d6bbbed3b9" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

