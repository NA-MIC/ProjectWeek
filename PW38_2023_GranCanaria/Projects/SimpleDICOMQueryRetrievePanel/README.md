Back to [Projects List](../../README.md#ProjectsList)

# Simple DICOM Query/Retrieve Panel

## Key Investigators

- Davide Punzo (Freelancer, France) 
- Andras Lasso (Perk Labs, Canada)
- Anyone is welcome to join

# Project Description

Implement a Query/Retrieve panel for DICOM databases.

## Objective

Have a simple user-friendly interface to query/retrieve from a DICOM server.
The user interface would render series thumbnails so the users can easily navigate the DICOM database
(see illustrations for a first UI Design prototype).
Moreover, perfomance needs to be boosted as much as possible: 

1) fetch metadata only when strictly required (e.g. get series metadata only when the user clicks and opens a study item of the list)

2) the fetch should be performed in async with Qthreads/workers and parallelized.


## Approach and Plan

1) Get feedback

2) Design the solution

3) Start implementation

## Progress and Next Steps


# Illustrations
<img alt="CTKDICOMQueryRetrievePanel" src="CTKDICOMQueryRetrievePanel.png" width="800"/>
<img alt="" src="PrototypeDICOMQueryRetrievePanel.png" width="800"/>

# Background and References

