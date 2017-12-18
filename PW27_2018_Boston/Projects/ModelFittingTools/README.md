Back to [Projects List](../../README.md#ProjectsList)

# Refactoring of Model Fitting Tools into Extension Suite

## Key Investigators

- Michael Schwier (BWH/HMS)
- Sharon Peled (BWH/HMS)
- Andrey Fedorov (BWH/HMS)

# Project Description

## Objective

1. Refactor model fitting tools (like Pkmodeling, T1Mapping, DSC Analysis, ...)
    1. Reduce duplicate code
    2. Combine in one Slicer extension
    3. Clear Interface for adding new modules
    4. Good test coverage
2. Long-term: Become standard toolset

## Approach and Plan

1. Analyze current status
    1. Identify common functionality
    2. Identify common process flow
2. Debug Mouse Error Case
2. Refactor Bolus Arrival Time
    1. Replace hard coded part with generic approach allowing to use different methods for BAT estimate
    2. Implement Sharon's approaches to BAT estimate
2. Design framework architecture
3. Implement/plan refactoring of exssting modules

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

![Description of picture](Example2.jpg)

![Some more images](Example2.jpg)

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: 
    - https://github.com/millerjv/PkModeling
    - https://github.com/QIICR/T1Mapping
    - https://github.com/SlicerProstate/SlicerProstate/tree/master/DWModeling
    - https://github.com/QIICR/DSC_Analysis
    - ...

<!--Link for editing page when displayed in GitHub pages-->
<a href="https://github.com/NA-MIC/ProjectWeek/edit/master/PW27_2018_Boston/Projects/ModelFittingTools/README.md">Edit this page on GitHub</a>
