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
Not much progress, got pulled into other things all week.
- Had a good meeting about MONAI Label and discussion with Andres and Khaled.
- Plan to meet with MONAI Deploy SDK team in the near future to discuss how users are expected to build custom applications
- Khaled and Andres pointed out the MONAI Bundle format which is used in the MONAI Model Zoo (https://github.com/Project-MONAI/model-zoo)

The end goal is a directory structure something like this, but it's still a bit unclear to us how it will work.

```
/src
	/shared python code
		- custom operators or pre/postprocessing steps
		- custom models
	/monai-label-apps
        (These should be able to use MONAI Bundles. Each Application may have custom input from the user which may be different than e.g. deep edit or deep grow. The MONAI Label applications are expected to be applicable to already-curated (e.g. cropped) datasets.)
		- /app1 (e.g. https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py, which runs in MONAI Label Server)
		- /app2
		- /app3
	/monai-deploy-apps
        (These set up the pre/postprocessing pipelines prior to running the model which are required for integration at the application level (e.g. cropping to lungs). Each App should be able to be packaged into Docker containers individually.
		- /app1 (e.g. https://github.com/Project-MONAI/monai-deploy-app-sdk/blob/main/examples/apps/ai_unetr_seg_app/app.py)
		- /app2
	/monai-bundles
        (These include the actual model, the network definition, the training and inference pre/postprocessing steps (e.g. NormalizeIntensityd). Unclear how this would pull in private pre/postprocessing steps or models.
		- model bundle 1 (e.g. https://github.com/Project-MONAI/model-zoo/tree/dev/models/brats_mri_segmentation/configs)
		- model bundle 2
```
