Back to [Projects List](../../README.md#ProjectsList)

# Kaapana related experiments/discussions/collaboratons

## Key Investigators

- Andrey Fedorov (Brigham and Women’s Hospital, USA)
- Marco Nolden (German Cancer Research Center, Germany)
- Hans Meine (Fraunhofer MEVIS, Germany)
- Klaus Kades (German Cancer Research Center, Germany)

# Project Description

[Kaapana](https://kaapana.readthedocs.io/en/stable/intro_kaapana.html#what-is-kaapana) is a Kubernetes-based open source toolkit for platform provisioning in the field of medical data analysis. Kapana is leveraging a number of open source tools that are relevant for the NA-MIC community (specifically, OHIF Viewer, MITK, nnU-Net segmentation tools) and relies on DICOM for managing images, image-derived data and metadata.

In this project current, perspective and aspiring users of Kaapana will have the opportunity to work with the developers of the platform to get help with deploying and using the platform, and to discuss potential problems or directions for future development and collaboration.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Deploy latest version of the platform locally and on GCP.
1. Discuss specific topics of interest.
1. Document results of discussion, share any code developed in the process.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Deploy Kaapana on Andrey's linux laptop.
1. Deploy Kaapana on a GCP VM.
1. Establish shared GCP project for collaboration.
1. Discuss specific topics of interest as summarized below, document the main points of the discussion (in the below, "I" refers to Andrey Fedorov).


**Improved Slicer integration** : we already have Slicer app added to Kaapana following the example of MITK (see https://github.com/fedorov/kaapana/tree/0.1.2-november-slicer). However, communication to / out of the app is quite clunky. Specifically, we have not figured out how to be able to select cases from the dashboard and open those directly in Slicer. Also, we would like to have a workflow that writes DICOM segmentations etc back into the DICOM server. Related to [Integration of Desktop Apps](../KaapanaIntegrationOfDesktopApps/README.md).

**Integration with GCP Healthcare DICOM stores** : right now we use dcm4chee as the DICOM server. This is problematic while deploying kaapana on the cloud, since 1) it is huge waste of resources: we already have our data in storage buckets, we need to replicate those files on attached disk (and attached storage is very expensive), then import into dcm4chee (which is very very very slow, and does not work for all types of DICOM objects - SRs are rejected); 2) I am not sure it is scalable to use dcm4chee. We can very easily set up a DICOM store under GCP Healthcare, which is cheaper, faster, is highly scalable, and can be accessed using standard DICOMweb interface with authentication. It would be extremely helpful to be able to use that GCP DICOM Store in place of dcm4chee. Related to [Connecting/Using Kaapana to Google Cloud/Google Health/Google FHIR](../KaapanaConnectingKaapanaToGoogleCloudAndHealthAndFHIR/README.md).

**Integration with IDC** : All of IDC data is available from public GCP buckets, egress is free. All you need is to have Google Cloud SDK https://cloud.google.com/sdk installed, and to do searching, one needs to have a GCP project and credentials. Maybe we can discuss this. Related to [Data and model exchange across different sources](../KaapanaDataAndModelExchangeAcrossDifferentSources/README.md).

**Integration of new analysis tools into Kaapana** : we have been developing use cases that utilize publicly available AI tools, starting from DICOM images and producing DICOM output, see some here: https://app.modelhub.ai/. It would be good to go over the process of adding one of those to kaapana as an experiment, so I can understand the process. We could also use prostate cancer segmentation model from MONAI zoo that we are going to investigate in this project: https://github.com/NA-MIC/ProjectWeek/pull/486/files#diff-1b4e320dd5db1df87192959dee521ff75d94129c1b97ede523d6b740271191b7R3. Related to [Data and model exchange across different sources](../KaapanaDataAndModelExchangeAcrossDifferentSources/README.md). Relatred questions:
 * how to debug failures? e.g., see [this as an example](https://kaapana.slack.com/archives/C018MPL9404/p1674230282696369?thread_ts=1674181916.424089&cid=C018MPL9404)

**Running Kaapana on Google Kubernetes Engine** : while using GCP, we've been following an extremely naive and inefficient approach for deploying Kaapana. We allocate a fixed linux VM, and install it as if we are on a on-prem server. As I understand it, to fully leverage the power of k8s, it would make a lot more sense to use Google Kubernetes engine. My knowledge of k8s and microk8s is very close to 0, so maybe this is something that is highly trivial. Maybe we could experiment with this together. We can even set up a shared GCP projects where I can add you, so you can experiment directly. Related to [Connecting/Using Kaapana to Google Cloud/Google Health/Google FHIR](../KaapanaConnectingKaapanaToGoogleCloudAndHealthAndFHIR/README.md).

**DICOM Dashboard Setup** : having a dashboard summarizing a data collection in a meaningful way is a recurring theme also outside of kaapana. We would like to investigate to which degree the requirements coming with common use cases (such as AI annotation, cohort definition, AI model training, automatic quality assurance) are already met and if they're not, how extensible the existing dashboard is. Furthermore, it would be interesting to assess whether such a dashboard can be shared with other projects (IDC, Grand-Challenge), and whether that really makes sense in practice. Related to [Fast viewing and tagging of DICOM Images](../KaapanaFastViewingAndTaggingOfDICOMImages/README.md).

**Maintenance of Kaapana instance** : discuss the process of checking for security vulnerabilities, updating the developers of identified vulnerabilities, communicating the need to update to the users, look if scanning features available in GCP could be helpful.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Andrey is working on setting up Kaapana on the linux laptop he plans to bring along.
1. Andrey is setting up a GCP project to share with the Kaapana developers for experimentation.
2. Hans has access to some(?) kaapana installation at MEVIS (from the RACOON project).

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References


* [Kaapana docs](https://kaapana.readthedocs.io/en/stable/intro_kaapana.html#what-is-kaapana)
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
