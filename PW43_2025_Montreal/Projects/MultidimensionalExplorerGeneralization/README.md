---
layout: pw43-project

permalink: /:path/

project_title: Multidimensional explorer generalization
category: Cloud / Web

key_investigators:

- name: Steve Pieper
  affiliation: Isomics
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Several projects involve looking at clinical and imaging data for large collections, resulting in a multidimensional data space that can be difficult to quickly comprehend.

This project explores the use of eCharts with Slicer to make interactive visualizations of this kind of data.

Although we have some hand-coded examples for specific projects, it could be of interest to create a more generic tool using the Slicer dicomDatabase, tables, markups, and other data sources to generate visualizations.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

During Project Week I would like to brainstorm with the community about various use cases and requirements.  From this I would like to determine what kind of core features would support these and how they could be bundled and exposed in a Slicer extension.

Since the current "UI" for creating these visualizations is a text editor the ability to explore the data in this way is limited to people with both Python and JavaScript expertise.  I would like to see if there are ways to build infrastructure to make it easier to apply these techniques with less programming required.  It's possible that LLM tools like Gemini or DeepSeek can already perform this task.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Identify use cases and discuss:
    * [TMJ Dashboard]([url](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/ExtractionOfOrofacialPainComorbiditiesFromClinicalNotesUsingLargeLanguageModels/))
    * [Data from IDC]([url](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/UsingIdcAndAiForHypothesesExplorationInTheNlstCohort/))
    * Others TBD at project week
2. See how easy it would be to adapt the code for these use case and also see how hard it would be for people to create their own interactive charts for their data.
3. Try auto-generating these charts using LLM technology


## Progress and Next Steps

1. Tried DeepSeek and Gemini to create charts and it was not helpful, so I just did it myself by looking at examples from IDC documentation and previous experiments.
2. Made a [sample script](https://gist.github.com/pieper/04b72eb1a60192a33c207fb73d9f7170) for echart parallel coordinates to demo IDC data exploration in a qSlicerWebWidget.
    * The demo uses the idc_index package to summarize a high level view of IDC data
    * Gist is posted as a reference
    * Determined a limit to the size of data that can be displayed in a qSlicerWebWidget (around 1000) but 60K can be displayed when loaded in chrome.  Workaround TBD.
    * Chrome demo with full dataset hosted here: [https://pieper.github.io/sites/idc-chart/](https://pieper.github.io/sites/idc-chart/)
3. Talked with TMJ and IDC teams as planned and got more ideas for applications of this technique
4. Talked with MassVision team (Amoon) and shared mutual enthusiasm for prettier and more interactive plots and plan to continue collaboration
5. Learned that there's a [pyecharts](https://pyecharts.org/#/) package that may be easier to use than current javascript wrapping (but may also make debugging harder)


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


An example parallel coordinates visualization: [https://storage.googleapis.com/sdp-lnq-site/site/index.html](https://storage.googleapis.com/sdp-lnq-site/site/index.html).
In this example, Slicer is used to pre-render thumbnails for interactive exploration, and clicking on the link takes you to an IDC-hosted viewer to see the full dataset.  This allow the full interactive chart to be hosted in a google storage bucket.

Previous experiments with parallel coordinates charts leveraged the qSlicerWebWidget to support bidirectional communication between the JavaScript-based parallel coordinates chart and the Python-based Slicer visualization.

* In this example, measures of tissue microstructure for dozens of whitematter tracts for hundreds of patients can be interactively compared.  Screenshots of each structure are shown as you mouse over the chart and clicking on a particular one loads the corresponding 3D file into Slicer.

<iframe width="420" height="315" src="https://www.youtube.com/embed/I4bytomQrao">
 </iframe>

* In this example a multiparametric MRI scan of a patient with a brain tumor is shown in Slicer and statistics from different volumes are shown in the parallel coordinates chart.  The video shows the two-way interaction of the chart with the volume visualization.  For example, when regions are selected in Slicer using the Segment Editor, the signal intensities are plotted on the chart in colors corresponding to the segment color.  Alternatively, the user can select combinations like high fractional anisotropy and low mean diffusivity and Slicer displays all voxels meeting that criterion as an overlay on all the images.  The goal is for clinical researchers to be able to explore the 3D anatomical distribution of tissues with different signal properties in and around the tumor.

<iframe width="420" height="315" src="https://www.youtube.com/embed/Y4MyThyeIPs">
 </iframe>



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

