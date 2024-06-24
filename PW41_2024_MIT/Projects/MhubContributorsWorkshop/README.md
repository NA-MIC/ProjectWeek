---
layout: pw41-project

permalink: /:path/

project_title: MHub Contributors
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Leonard Nürnberg
  affiliation: Brigham and Women's Hospital
  country: Boston

- name: Andriy Fedorov
  affiliation: Brigham and Women's Hospital
  country: Boston

- name: Hugo Aerts
  affiliation: Brigham and Women's Hospital
  country: Boston

---

# Project Description

<!-- Add a short paragraph describing the project. -->


MHub.ai is a platform for deep-learning models in medical imaging. We aim to make AI in medical imaging as simple as possible. Therefore, all MHub models need zero set-ups, can be run with a single command, have a standardized IO interface, run directly on DICOM data, are fully customizable to run on other data types and file structures, are tested and reproducible, and run entirely offline. MHub also provides a toolbox to support developers with data conversion, organization, and standardization tasks.

We want to demonstrate **WHY** bundling models in the MHub standard, make them as simple as possible to use, and provide a valuable resource to the community. 

Furthermore, we're thrilled to show **HOW** any model or algorithm can be wrapped into an MHub container. We plan to show the process, explain the tools we use, answer questions, and provide assistance and guidance to those who want to use or contribute to an MHub model.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Present the MHub.ai platform and model repository with more than 20 models (and counting).
2. Demonstrate the benefits of containerized and standardized models and how you can build on them for reproducible research.
3. Show how to implement any model in MHub in three steps and provide them to the community.
4. Support participants in implementing (their) models into MHub.
5. Gather feedback, improve our documentation, and explore what topics, formats, details, and intensity are best for the educational materials.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


We plan to hold a workshop or break-out session where we demonstrate every step of the contribution process for MHub models in a walk-through style tutorial. We will give detailed examples, discuss best practices, and provide hands-on guidance to all who are planning to implement models into MHub.







## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. **MHub.ai Documentation**
We have [detailed documentation](https://github.com/MHubAI/documentation/tree/main) on [how to run a model](https://github.com/MHubAI/documentation/blob/main/documentation/mhub/run_mhub.md) in MHub and documentation on the individual [tools provided within the MHub-IO framework](https://github.com/MHubAI/documentation/blob/main/documentation/mhubio/mhubio_modules.md).

2. **MHub.ai Model Deployment**
We created a tutorial that guides through the implementation of a model into the universal MHub format.
   - [T3 - Create the Thresholder Model for MHub]([https://github.com/MHubAI/documentation/blob/main/tutorials/run_totalsegmentator_on_idc_collection/mhub_tutorial_001.md](https://github.com/MHubAI/documentation/blob/main/tutorials/create_thresholder_model_for_mhub/mhub_tutorial_003.md))

4. **MHub.ai Contribution Process**
MHub has a clearly defined contribution process. 
The requirements and the process are explained in our [documentation](https://github.com/MHubAI/documentation/blob/main/documentation/mhub_contribution/contributing_a_model.md).

5. **MHub.ai Tutorials**
We wrote two more tutorials demonstrating how to run and customize MHub models based on public data from IDC and how to visualize and compare results in 3D Slicer.
   - [T1 - Run TotalSegmentator on IDC Collection](https://github.com/MHubAI/documentation/blob/main/tutorials/run_totalsegmentator_on_idc_collection/mhub_tutorial_001.md)
   - [T2 - Run Custom MHub Lung Segmentation Workflow on Chest CT in Nifti Format
](https://github.com/MHubAI/documentation/blob/main/tutorials/run_lungmask_on_chestct_in_nifti_format/mhub_tutorial_002.md)



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Mhub Contribution Flowchart](https://raw.githubusercontent.com/MHubAI/documentation/main/documentation/figures/submission_sequence_diagram.png)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->



You can learn more about the MHub platform, repository, and framework at the following links.
- [MHub.ai website](https://mhub.ai)
- [Model-Repository](https://mhub.ai/models)
- [Github Organization](https://github.com/MHubAI/)

---

To dive deeper, you can find the developer documentation, tutorials, and the implementation of all models currently in our repository under these links.
- [Models repository](https://github.com/MHubAI/mdoels)
- [Documentation](https://github.com/MHubAI/documentation)
- [Tutorials](https://github.com/MHubAI/documentation/tree/main/tutorials)

