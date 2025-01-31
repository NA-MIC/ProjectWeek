Back to [Projects List](../../README.md#ProjectsList)

# Segmentation overlay for prostatecancer.ai

## Key Investigators

- [Omar Toutounji][omar] ([Medical Informatics Lab][med-i-lab])
- [James Petts][james] ([Institute for Cancer Research, London][icr-london])
- [Steve Pieper][steve] ([Isomics, Inc.][Isomics])
- [Erik Ziegler][erik] ([Radical Imaging][radical])
- [Danny Brown][danny] ([Radical Imaging][radical])
- [Anneke Meyer][anneke]
- [Alireza Sedghi][alireza] ([Medical Informatics Lab][med-i-lab])
- [Parvin Mousavi][parvin] ([Medical Informatics Lab][med-i-lab])

# Project Description

Advances in machine learning and deep learning have made it possible to embed the knowledge of experienced physician/radiologist into computational models and have shown state-of-the art performance in various image analysis tasks including computer-assisted detection, diagnosis, and prognosis of several forms of cancers including prostate cancer. However, models are not fully integrated with the current standard of care in clinic. We have developed prostatecancer.ai, an [OHIF-based][ohif] medical image viewer which enables deployment of AI models in a web-browser while simultaneously providing standard image viewing and reporting schemes.

## Objective

1. Integrate James A Petts’s segmentation tools and cornerstone’s overlay tool
2. Explore a feature that would allow "local" end users to upload their own DICOM images

# Progress and Next Steps

## Before project week
![Screenshot of ProstateCancer.ai](https://github.com/NA-MIC/ProjectWeek/blob/master/PW31_2019_Boston/Projects/SegOverlay_ProstateCancerAI/Screenshot_ProstateCancerAI.PNG)
Illustrates the use of the AI Probe feature on prostatecancer.ai before project week

## After project week
![Screenshot of ProstateCancer.ai](https://github.com/NA-MIC/ProjectWeek/blob/master/PW31_2019_Boston/Projects/SegOverlay_ProstateCancerAI/Screenshot_AfterProjectWeek.png)
Illustrates the use of the AI Probe feature on the completely re-written prostatecancer.ai v2 with seg support after project week

## Next steps

ProstateCancer.ai v2 is in its very early steps and will need a lot of refinement and improvement.


# Background and References

1. [prostatecancer.ai's github page][prostatecancer.ai-github]


[radical]: http://radicalimaging.com/
[icr-london]: https://www.icr.ac.uk/
[omar]: https://github.com/omartoutounji
[james]: https://github.com/jamesapetts
[erik]: https://github.com/swederik
[danny]: https://github.com/dannyrb
[med-i-lab]: http://medi.cs.queensu.ca/
[alireza]: https://github.com/sedghi
[steve]: https://github.com/pieper
[Isomics]: http://isomics.com
[anneke]: https://github.com/AnnekeMeyer
[prostatecancer.ai-github]: https://github.com/Tesseract-MI/prostatecancer.ai
[parvin]: http://medi.cs.queensu.ca/users/parvin-mousavi
[ohif]: http://ohif.org/
