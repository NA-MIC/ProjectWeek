Back to [Projects List](../../README.md#ProjectsList)

# Data and model exchange across different sources

Kaapana tutorial for the 38th NA-MIC project week:

https://drive.google.com/file/d/1A7-8Ru0uTJHFFa17rZtkBpvNhJao_F7x/view?usp=share_link

## Key Investigators

- Benjamin Hamm (German Cancer Research Center, Germany)
- Ünal Akünal (German Cancer Research Center, Germany)
- Markus Bujotzek (German Cancer Research Center, Germany)
- Klaus Kades (German Cancer Research Center, Germany)
- Andrey Fedorov (Brigham and Women's Hospital, USA)

# Project Description

Implementations and discussion about a standardized data and model exchange between different platforms such as Kaapana and MONAI. Working on integrating Kaapana with other toolkits.
- Motivation: Running Kaapana platforms in multiple (inter-)national projects: RACOON, DART, ...
- Goal: Standarized and Federated Data Analysis / Federated Learning require standardized model exchange formats

![image](https://user-images.githubusercontent.com/103252889/215480450-23dfe16c-fd20-473a-a185-9e0262a275c0.png)


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Support standardized data and AI model I/O interfaces in Kaapana.

1. Support of various AI model sources
- Integration of MONAI Model Zoo into Kaapana
     - inference pipeline as a Kaapana workflow / as a Kaapana extension
     - training pipeline
     - generic support of MONAI Bundles (MONAI Label / MONAI Deploy / MONAI FL)
- Standardized remote model execution, execution of models from modelhub.ai within Kaapana
2. Integration/support of data sources:
- TCIA download/(upload) into Kaapana 
- Integration with IDC: download of data via Google Cloud SDK
3. Integration of new analysis tools into Kaapana
4. Javascript/Python library client to communicate with Kaapana

Relate to:
- [Kaapana overall](https://github.com/NA-MIC/ProjectWeek/tree/master/PW38_2023_GranCanaria/Projects/Kaapana_overall)

## Approach and Plan

1. Support of various AI model sources
- Integration of MONAI Model Zoo into Kaapana
     - inference pipeline as a Kaapana workflow / as a Kaapana extension
     - training pipeline
     - generic support of MONAI Bundles (MONAI Label / MONAI Deploy / MONAI FL)
- Standardized remote model execution, execution of models from modelhub.ai within Kaapana
- Current progress:
![image](https://user-images.githubusercontent.com/103252889/215465416-394f3a57-176b-469b-a6ce-505bd359908b.png)

2. Integration/support of data sources:
- TCIA download/(upload) into Kaapana
     - Kaapana workflow to download specific TCIA datasets
     - select to-be-downloaded dataset via UI
     - send downloaded dataset to Kaapana's PACS

## Progress and Next Steps

1. Support of various AI model sources
- Integration of MONAI Model Zoo into Kaapana
     - Proof of concept: Intgration of MONAI Model Zoos spleen CT segmentation works
     - tbd: Finalize integration in Kaapana
     - tbd: Add more monai bundles
- Support of MHub
     - Completed the implementation of a workflow in Kaapana for modelhub.ai
     - Supports each model already available in mhub
     - A wrapper around the dockerfile of models in mhub
     - Ability to visualize the segmentations in Slicer, MITK or OHIF

2. Integration/support of data sources:
- TCIA download/(upload) into Kaapana
     - Implemented `service-tcia-download`. Now it is possible to drag and drop a .tcia manifest file into Kaapana (in minio). This will start a workflow which                downloads the data from TCIA via their REST-API. Number of workers can be set in the operator.


# Illustrations

<img width="1436" alt="Screen Shot 2023-02-03 at 13 39 36" src="https://user-images.githubusercontent.com/16197349/216624581-fe7610cd-2186-4cc8-9002-9f28769cd055.png">
<img width="1424" alt="Screen Shot 2023-02-03 at 13 41 09" src="https://user-images.githubusercontent.com/16197349/216624614-01aecb5d-8d47-4274-acba-5f2ecc582e2d.png">!


![mitk_p](https://user-images.githubusercontent.com/16197349/216622165-10c09abc-63fa-4703-9f67-63345a810c56.PNG)
![mitk_ts](https://user-images.githubusercontent.com/16197349/216622179-15b9d365-8e58-4b48-9966-db93dde5294b.PNG)

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

tbd

# Background and References

- https://www.kaapana.ai/
- http://app.modelhub.ai/
- https://www.cancerimagingarchive.net/
- https://monai.io/

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
