---
layout: pw44-project

permalink: /:path/

project_title: wsidicomizer-based conversion into DICOM WSI format for Imaging Data Commons
category: DICOM
presenter_location: 

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: David Clunie
  affiliation: PixelMed Publishing
  country: USA

- name: Daniela Schacherer
  affiliation: Fraunhofer MEVIS
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project is motivated by the operational needs of the [Imaging Data Commons](https://learn.canceridc.dev/) to have a sustainable mechanisms supported by open-source software for harmonizing various slide microscopy images in vendor-specific representations into DICOM Whole Slide Imaging format. Our current procedures is not sustainable, since they rely on the PixelMed tools by David Clunie, which are based on a coding style and build process that has not changed since initiated over 20 years ago, unfortunately have "bus factor" of 1, and are not open for community contributions. We started using [`wsidicomizer`](https://github.com/imi-bigpicture/wsidicomizer) as a replacement, but there are gaps in the functionality to be remedied, and additional testing that needs to be done before we can consider operational switch.

This project is the continuation of the [earlier project at PW42 2025](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/EvaluationOfImiBigpictureWsidicomizerAsAToolForConversionIntoDicomWholeSlideImagingFormat/). 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Implement routing of the DICOM metadata.
2. Evaluate extensibility of the conversion approach to various input types.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Improve the conversion script developed for the HMS SARDANA sample to handle metadata.
2. Evaluate conversion of the .czi samples.
3. Evaluate metadata routing in the Mirax conversion script



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

```
CSV Files → CCDIMetadataLoader → DomainMetadata → MetadataBuilder → WsiDicomizerMetadata + Dataset
                  ↓                                       ↓
            UIDRegistry                           Code Tables (CSV)
             (SQLite)
```

1. Set up [exploration repository](https://github.com/fedorov/pw44-wsi-conversion) that included code base from various related conversion tools and conversion scripts I worked on earlier
2. Identified relevant sample earlier converted in IDC from the [CCDI-MCI collection](https://portal.imaging.datacommons.cancer.gov/explore/filters/?collection_id=CCDI&collection_id=ccdi_mci), which was selected as the initial target for development
3. Used Claude Code and Copilot to independently develop plan and initial implementation for migrating from pixelmed (see `copilot_solution` and `claude_solution`) in the repo
4. Used Claude Code and Copilot to independently scritinize both solution and summarize pros and cos (see reports in the top level of the repo)
5. Examined the analysis, implementations, selected Copilot solution as the preferred (supported by the analysis)
6. Iterated to make [the converter](https://github.com/fedorov/pw44-wsi-conversion/blob/main/copilot-solution/convert_ccdi.py) work on the selected CCDI-MCI sample
7. Iterated to add features and refine organization
8. Confirmed functionality on an independent sample not supplied to the agent during development
9. Confirmed `dciodvfy` DICOM validator does not report issues related to the specimen metadata.
10. Confirmed converted images load with the QuPath BioFormats DICOM loader
11. Next steps:
  * validate specimen metadata against the pixelmed-conversion results
  * look into ICC profile handling, pixel data total size difference, potentially missing label/overview images
  * extend/test for collections other than CCDI

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_
## Curious examples of failures of Claude

* remind to check documentation in the prompt?
<img width="600" height="430" alt="image" src="https://github.com/user-attachments/assets/a8e4d117-a619-4ac2-9cbb-460b2120835c" />

* need to understand the code ...
<img width="602" height="607" alt="image" src="https://github.com/user-attachments/assets/72c38fe5-8144-43a1-81a9-b7996e6a66a3" />


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

