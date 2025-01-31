Back to [Projects List](../../README.md#ProjectsList)

# Stereotactic tools for DBS and intraEEG exploration procedures

## Key Investigators

- Sara Fdez Vidal (ICM)
- Jordan Cornillault (ICM)
- Eric Bardinet (ICM)

# Project Description

To improve and update the Slicer plug-ins we have developed for pyDBS and EpiLOC toolboxes.

## Objective

1. PyDBS PostOperative Report Plug-in. pyDBS is use mostly to localize the electrodes implanted in some regions of the Basal Ganglia, to tune the stimulation with regard to the surrounded anatomy. We process a big amount of data coming from multicentric research projects and for clinicians. We provide to our users a quantitative and qualitative report but also a visual report for each subject processed, with some almost-standar views.
2. EpiPlan slicer Plug-in. We have developed a prototype to help the neurologists and anatomists of our center to plan the surgical procedure to perform intracranial EEG exploration of certain epileptic patients. We want to enhance the plug-in by adding new features and making the graphical interface and user interface interactions more robust
3. MrTrix Tracking on PyDBS.

## Approach and Plan
1. Get feedback from slicer team
2. Get help for new features implementation
2. Design of news GUIs and plug-ins architectures, adding a logic for the oldest ones

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
Development of our plug-ins :
  - Jordan : updating and improving post-operative Slicer plug-in in pyDBS
  - Sara : planning of surgical iEEG exploration procedure for epilepsy

Discussions about developments :
- Csaba and Andras :  how to use  SegmetEditorLogicalEffect in python to intersect segments
- Steve : markups and reformat problems

Discussions about dissemination of our modules:
- Jean-Christophe Fillon-Robin, about Girder, that could be used to develop a web server
- Csaba Pinter, about the development of a Slicer solution dedicated to Stereotaxy (build and custom options)
- Steve Pieper, about dissemination of our stereotaxy modules, as an extension or a Slicer solution, about QMenta
Discussions about our projects:
- Lauren O'Donnell, about Slicer DMRI and how to use her atlas to map fiber tracts inside the basal ganglia in parkinsonian patients, and use this for anatomo-functional studies


# Illustrations

PyDBS Intra Operative plug-in.

<img src="pydbs-Ima2.png"  height="360">

Epiloc PostOperative Visualization plug-in.

<img src="Epiloc-ima-1.png" height="360">

Epiloc  last implant planning schema exported to ROSA planning workstation .

<img src="dh.png" height="460">
# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data
