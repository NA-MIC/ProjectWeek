---
layout: pw40-project

permalink: /:path/

project_title: MHub Tutorials and Structured Report Support
category: DICOM
presenter_location: Onsite

key_investigators:
- name: Leonard Nürnberg
  affiliation: Maastricht University
---

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Implement a new MHub core module to export non-segmentation data as DICOM Structured Report.
1. Objective B. Offer support for interested developers explaining how to contribute models to MHub and how to use and configure MHub models for easy and reproducible research.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

Objective A
1. Examine the requirements and limitations of DICOM Structured Reports.
1. Examine existing libraries and frameworks that can help in the creation of DICOM Structured Reports.
1. Check to what extent the internal data representation of MHub complies with the requirements of DICOM Structured Reports and, if necessary, plan an extension of the internal data representation.

Objective B
1. Organize a break-out session for all interested developers. We can provide tutorials and answer specific questions on request. It would be great to know who is interested in submitting a model to MHub or using MHub models and gather questions in advance to provide customized tutorials.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Developers of MHub models must wrap all non-file outputs (e.g. prediction results or classification labels) in mhub-io objects and describe their semantics.
1. MHub currently offers a JSONExporter module that can be used to query MHub's internal data representation and generate a customizable json (or csv).

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

![MHub Submission Process](https://raw.githubusercontent.com/MHubAI/documentation/main/documentation/figures/submission_sequence_diagram.png)

![Slicer MHub Visualization](https://raw.githubusercontent.com/MHubAI/documentation/main/tutorials/run_totalsegmentator_on_idc_collection/figures/slicer_inspect_data.png)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Documentation
- [MHub documentation](https://github.com/MHubAI/documentation)
- [MHub Handling Logical Output](https://github.com/MHubAI/documentation/blob/main/documentation/mhubio/how_to_write_an_mhubio_module.md#handling-logical-output-data)
- [MHub Report Exporter Documentation](https://github.com/MHubAI/mhubio/blob/main/mhubio/core/RunnerOutput.py)

Code
- [MHub-IO Logical Output](https://github.com/MHubAI/mhubio/blob/main/mhubio/core/RunnerOutput.py)

