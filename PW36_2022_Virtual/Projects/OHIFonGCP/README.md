Back to [Projects List](../../README.md#ProjectsList)

# OHIF deployment using Google Cloud Platform and Firebase

## Key Investigators

- Andrey Fedorov (BWH)
- Igor Octaviano (Radical)
- Deepa Krishnaswamy (BWH)
- Bill Longabaugh (Institute for Systems Biology)
- Steve Pieper (Isomics)


# Project Description

This project aims to document the instructions of deploying [OHIF Viewer](https://github.com/OHIF/Viewers) v2 on [Google Cloud](https://cloud.google.com/sdk/docs/install) as a [FireBase](https://firebase.google.com/) hosted application. Such hosted OHIF Viewer can be used to connect the viewer to Google Healthcare DICOM stores. The main motivation for this is to support users analyzing the data available in [NCI Imaging Data Commons (IDC)](https://imaging.datacommons.cancer.gov) in visualizing results of IDC data analysis.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. As simple as possible instructions of deploying OHIF Viewer
2. Collect user feedback


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Go over the prerequisites (GCP OAuth, Firebase)
2. Clean up the [Colab notebook](https://colab.research.google.com/drive/1PbYm6HVgsXaUYrcujBr_bPWS5hrBMSUW?usp=sharing) draft prepared earlier
3. Prepare examples of populating a GCP Healthcare DICOM store with analysis results and visualizing those
4. Update [IDC documentation](https://learn.canceridc.dev/)
5. Collect feedback from anyone interested

## Progress and Next Steps

Tutorial for the most part is completed, and (almost!) ready for testing - see [here](https://docs.google.com/document/d/1v4Syu_yOV6yH--QBLGzsL9fJ7-XyD1CnQu4iTIoPVD8/edit?usp=sharing) the google doc, which links to 2 colab notebooks that are intended to allow you to deploy the viewer without having to install any of the dev tools on your computer, and populate a cloud-based DICOM store.

Unfortunately, there are outstanding issues:
* Deepa encountered an error described in [this thread](https://discourse.canceridc.dev/t/google-cloud-deployment-of-the-ohif-viewer/246/2) - Andrey cannot explain this
* Andrey ran into a permissions issues while populating a DICOM store in [this notebook](https://colab.research.google.com/drive/1KwvAuBmTRKyt8PrYKUE5nDTZcwkWEEdc?usp=sharing) - amazingly, this also has not been explained yet, even with all the experience Bill L put into this
* on the second attempt to complete, Deepa ran into "Error 500: Internal error" deploying with Firebase


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

* [NCI Imaging Data Commons (IDC)](https://imaging.datacommons.cancer.gov)
* [OHIF Viewer](https://github.com/OHIF/Viewers)
* [IDC tutorial Google Colab notebooks](https://learn.canceridc.dev/cookbook/notebooks)

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
