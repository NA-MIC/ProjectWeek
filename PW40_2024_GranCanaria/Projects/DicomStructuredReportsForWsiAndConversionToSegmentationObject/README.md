---
layout: pw40-project

permalink: /:path/

project_title: DICOM Structured Reports for WSI and conversion to segmentation object
category: Cloud / Web
presenter_location: In-person

key_investigators:

- name: Maximilian Fischer
  affiliation: DKFZ
  country: Germany

- name: Philipp Schader
  affiliation: DKFZ
  country: Germany

- name: Marco Nolden
  affiliation: DKFZ
  country: Germany

- name: Daniela Schacherer
  affiliation: Fraunhofer MEVIS
  country: Germany

- name: David Clunie
  affiliation: PixelMed
  country: USA

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Chris Bridge
  affiliation: MGH
  country: USA

- name: Klaus Maier-Hein
  affiliation: DKFZ
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

In this project, we want to investigate and compare several approaches to convert DICOM Structured reports into DICOM segmentation objects. We use the integrated SLIM Viewer in Kaapana to create Structured Reports on DICOM WSI files and also want to compare the QuPath viewer as additional DICOM WSI viewer in Kaapana.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A: Examine existing libraries to render the coordinates from the SR file as segmentation.
2.  Objective B: Examine conversion methods to create DICOM annotation objects from the SR files
3.  Objective C: Evaluate file formats of QuPath DICOM WSI annotations.
4.  Objective D: Explore integration capabilities of QuPath as Viewer in Kaapana

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Familiarize with the highdicom librariy
2.  Compare result with custom visulaizations
3.  Evaluate conversion tools for SR files
4.  Test PACS connectivity of QuPath

## Progress and Next Steps

1. Familiarized with the highdicom library for accessing the SR coordinates
2. Switching to a more generic way for rendering the coordinates
3. ```ruby
for i in range(AnnotatetObjects3):
    Type=FileFull.ContentSequence[13].ContentSequence[i].ContentSequence[2].ConceptCodeSequence[0].CodeMeaning
    Coords3=FileFull.ContentSequence[13].ContentSequence[i].ContentSequence[3].GraphicData
    x_coords3 = [int((Coords3[i]-Origin_X)/spacing_x) for i in range(0, len(Coords3), 3)]
    y_coords3 = [int((Coords3[i]-Origin_Y)/spacing_y) for i in range(1, len(Coords3), 3)]
    if Type=='Tissue':
        tissue_list.append([x_coords3,y_coords3])
        color=(255,0,0)
    else:
        tumor_list.append([x_coords3,y_coords3])
        color=(0,0,255)
    contours = np.array([[[abs(x), abs(y)] for x, y in zip(x_coords3, y_coords3)]], dtype=np.int32)
```
4. ```ruby
sr = hd.sr.srread("/Users/maximilianfischer/ProjectsMountDir/CMU-1/Consistent/SR/DICOM/1E447C90/E88940CE/4E17833F.dcm")
groups = sr.content.get_planar_roi_measurement_groups()
groups[0].roi
groups[0].roi.value
coords=[]
for x in range(groups[0].roi.value.shape[0]):
    coords.append([groups[0].roi.value[x][0],groups[0].roi.value[x][1]])
```
**Much shorter code!**
5. Rendering still done with opencv, but planning to switch to rasterio. 
6. Bioformats as new DICOM conversion library to be supported in Kaapana (currently mostly based on PixelMed.)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

This project is the continuation from last years project weeks.
[PW 38](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/IDC_DICOM_WSI_workflow/)
[PW 39](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/HistologyAiModelsImportedIntoIdc/)
[Kaapana](https://kaapana.readthedocs.io/en/stable/)
