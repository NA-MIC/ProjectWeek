Back to [Projects List](../../README.md#ProjectsList)

# Visual DICOM browser

## Key Investigators

- Davide Punzo (Freelancer, France) 
- Andras Lasso (Perk Labs, Canada)
- Gabriel Kwiecinski Antunes (WebKriativa, Brazil)
- Ralf Floca (German Cancer Research Center, Germany; remote)
- Anyone is welcome to join

# Project Description

Implement a visual DICOM browser with thumbnails and query/retrieve/store capabilities for DICOM databases.

## Objective

Have a simple user-friendly interface to query/retrieve/store from a DICOM server.
The user interface would render series thumbnails so the users can easily navigate the DICOM database
(see illustrations for a first UI Design prototype).
Moreover, perfomance needs to be boosted as much as possible: 

1) fetch metadata only when strictly required (e.g. get series metadata only when the user clicks and opens a study item of the list)

2) the fetch should be performed in async with Qthreads/workers and parallelized.


## Approach and Plan

1) Get feedback: ask feedback on the UI prototype (e.g., Osirix, MITK, Weasis, cloud UIs)

2) Design the solution: 
   we implement in CTK:
   - UI: display list of studies per patient with thumbnails. Show server and local content together
   - improvement of the networking API:
      - methods to retrieve instances metadata and DICOM files
      - allow to query study and series metadata separately
   - async query/retrieve/store

3) Start implementation

## Progress and Next Steps

1) Meeting done on Tuesday (31/01/2023)

2) We will proceed with the pure C++ CTK implementation.
   - First we will implement the self-contained visual CTK component. 
   - Then we will design/implement how to stream/load data into Slicer (into the volumeNode) in an asynch way
   - NOTE: experiment with websocket from Marco https://github.com/nolden/CTK/commit/16ee8d0773ce37290636000d836ad107b4526085
   - NOTE: web project from Stefan ([link](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/KaapanaFastViewingAndTaggingOfDICOMImages/)). This is very nice and we could use this and comunicate between jvascript/C++. However the project uses cornerstone -> dicomwebclient and our requirement is that the solution has to work for any server (not only dicomweb servers).

3) In progress

# Illustrations
<img alt="CTKDICOMQueryRetrievePanel" src="CTKDICOMQueryRetrievePanel.png" width="800"/>
<img alt="" src="PrototypeDICOMQueryRetrievePanel.png" width="800"/>

# Background and References
[CTK class](https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMQueryRetrieveWidget.cpp)
