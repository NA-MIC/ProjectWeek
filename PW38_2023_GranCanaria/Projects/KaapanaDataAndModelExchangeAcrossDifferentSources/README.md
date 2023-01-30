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

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

tbd

# Illustrations

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
