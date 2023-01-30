Back to [Projects List](../../README.md#ProjectsList)

# DICOM Meta-Dashboard

## Key Investigators

- Hans Meine (Fraunhofer MEVIS, Germany)
- Stefan Denner (German Cancer Research Center, Germany)
- Klaus Kades (German Cancer Research Center, Germany)
- Andrey Fedorov (BWH)

**Project channel on Discord: #dicom-meta-dashboard** (TBD: add link)

# Project Description

In practice, importing DICOM files into workspaces (e.g., for reader studies, analyses, ...) requires some manual filtering, sorting, and selection.
* sorting out "scout" images (localizers)
* sorting out images with artifacts, the acquisition of which was repeated anyhow
* identifying studies that need to be merged, e.g. when an imaging study is cancelled / incomplete and has to be repeated / completed within a few days, leading to two DICOM studies that together make up a single logical timepoint
* classifying the remaining images as "native", "contrast-enhanced" (incl. phase), "showing the complete liver", "T1-weighted", "DCE-MRI sequence", ...
* counting the number of complete "cases", e.g. "I need a prior and a matching follow-up image", "I need a native and a contrast-enhanced image", "I need n different dynamic contrast enhanced images"
Basically, one could describe the above as "putting images into the correct buckets", and a related task would be to check how many cases are "complete", in the sense that a specified number of buckets is "filled".

There are probably countless attempts at supporting this, but this project is
about checking what the Meta dashboard that comes with
[Kaapana](https://kaapana.readthedocs.io/en/stable/intro_kaapana.html#what-is-kaapana)
already supports and could (/should) support in the future.

Having a dashboard summarizing a data collection in a meaningful way is a recurring theme also outside of kaapana. We would like to investigate to which degree the requirements coming with common use cases (such as AI annotation, cohort definition, AI model training, automatic quality assurance) are already met and if they're not, how extensible the existing dashboard is. Furthermore, it would be interesting to assess whether such a dashboard can be shared with other projects (IDC, Grand-Challenge), and whether that really makes sense in practice.
Related to [Fast viewing and tagging of DICOM Images](../KaapanaFastViewingAndTaggingOfDICOMImages/README.md) (as well as to previous PW endeavors around Chronicle and DICOMweb by Steve Pieper).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Use the Meta Dashboard without kaapana, on data that is not in a PACS.
2. Understand the limits of the current OpenSearch/Kibana stack, and whether it supports all intended use cases.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Find out about the schema / information used by the Meta dashboard.
1. Try to set up the Meta dashboard outside of kaapana.
1. Feed OpenSearch with data from a dataset that is not in a PACS.
1. Document results (code / schema / design / use cases).

## Progress and Next Steps

1. Hans has access to some(?) kaapana installation at MEVIS (from the RACOON project).
2. Hans has learned from Stefan about the current process / integration of the Meta dashboard in kaapana, and about its code location(s).

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

* [Kaapana docs](https://kaapana.readthedocs.io/en/stable/intro_kaapana.html#what-is-kaapana)
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
