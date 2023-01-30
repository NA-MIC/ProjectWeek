Back to [Projects List](../../README.md#ProjectsList)

# MHub Integration

## Key Investigators

- Leonard Nürnberg (Department of Radiology, Brigham and Women’s Hospital, Boston, MA)
- Dennis Bontempi (Department of Radiology, Brigham and Women’s Hospital, Boston, MA)
- Andrey Fedorov (Department of Radiology, Brigham and Women’s Hospital, Boston, MA)

# Project Description

We are working on a repository to standardize Deep Learning models in medical imaging and make them easily accessible to everyone.
A central point of our efforts is to develop a standardized I/O framework for all models to unify the data stream into and out of these models, making them interchangeable. Seamless integration of our repository with Slicer would allow immediate application and exploration of models without the need to set up model environments locally.

Therefore, we are planning a Slicer extension that will allow to search our repository from within Slicer to deploy and run these models locally, using the Slicer interface for data input and output.

Link to the [Plugin](https://github.com/AIM-Harvard/SlicerMHubRunner/tree/docs).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Discover how to run models in Slicer securely, conflict-free, and platform-independent. 
2. Objective B. Validate and customise our definitions of a generic I/O framework.
3. Objective C. Document pros and cons of docker vs native python integration of the model, support with experimental results. Concerns re Docker communicated earlier:
  * Docker may be challenging to install and setup (org constraints, permissions, expertise)
  * Docker images are large and slow to download
  * Support of GPU with Docker is not straightforward/limited
  * <add you concern re using Docker for interfacing AI models in Slicer here>

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. We have two approaches in mind: packaging models in Docker containers and running models in separate Python environments. For both options, we need to weigh the pros and cons to find the most appropriate solution that maximizes the user base while avoiding or minimizing manual per-model customization.
2. We want to create a clear understanding of the challenges and drawbacks of using Docker. We will provide a step-by-step guide to setting up Docker and are looking for volunteers to try out the setup under our guidance and report back their valuable feedback.
2. We would like to discuss and find the best standard for model outputs (e.g., segmentation label names).
4. We plan to develop a slicer plugin that connects data loaded into Slicer to a model via our i/o framework and transfers the model outputs back into Slicer, using selected DL models as proofs of concept.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. We have developed an experimental modular conversion framework to bridge between a standardized I/O and specific model requirements.
2. We dockerized two models (Totalsegmentator, Platipy) using our I/O FW.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
 
<img src="https://github.com/AIM-Harvard/SlicerMHubRunner/blob/main/MRunner/Resources/Icons/PluginOverview.png?raw=true" alt="Plugin Module Overview" width="670"/>
