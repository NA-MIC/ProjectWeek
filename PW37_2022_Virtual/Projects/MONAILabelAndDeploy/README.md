back to [Projects List](../../README.md#ProjectsList)

# MONAI Label + Deploy SDK Repository Setup Example

## Key Investigators
- Erik Ziegler (Novometrics LLC, Lexington, MA)
- Roya Khajavi (Department of Radiology, Brigham and Women’s Hospital, Boston, MA)
- Steve Pieper (Isomics Inc, Cambridge, MA)
- Ron Kikinis (Department of Radiology, Brigham and Women’s Hospital, Boston, MA)
- Andres Diaz-Pinto (Nvidia)
  
## Project Description
We have designed, developed, and validated deep learning methods for mediastinal lymph node segmentation. We want to use active learning and MONAI Label to transfer this to additional areas of the body (e.g. abdominal or retroperitoneal lymph nodes). We want to use MONAI Deploy SDK as the framework for pre/post-processing in our production inference pipeline. It's currently unclear how a MONAI Label App relates to a MONAI Deploy SDK Application. They feel largely disconnected at the moment, despite sharing the same project name. It's not possible to build a repository of custom Operators in MONAI Deploy that are shared across Applications without publishing a public Python package first.

## Objective

To work with the MONAI Deploy SDK and MONAI Label teams to identify how to structure a repository for use with both toolkits. 

## Approach and Plan

We will use the mediastinal subset of TCIA CT Lymph Node as data for development and performing experiments. Below is our plan during the course of project week:
1. Setup MONAI Label approach for lymph node segmentation workflow (see [LNQ Project](../LNQ/README.md) for more details)
2. Determine how to wrap / reorganize this application to share code with a MONAI Deploy SDK Application
3. Publish an example repository for this setup
4. Work with MONAI Deploy SDK team to identify how custom Operators can be shared across Applications
   
## Progress and Next Steps
