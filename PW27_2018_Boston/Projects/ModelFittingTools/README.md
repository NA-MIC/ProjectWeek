Back to [Projects List](../../README.md#ProjectsList)

# Refactoring of Model Fitting Tools into Extension Suite

## Key Investigators

- Michael Schwier (BWH/HMS)
- Sharon Peled (BWH/HMS)
- Andrey Fedorov (BWH/HMS)
- Andrew Beers (MGH/HST)
- Hans Meine (MEVIS)

# Project Description

## Objective

1. Refactor model fitting tools (like Pkmodeling, T1Mapping, DSC Analysis, ...)
    1. Reduce duplicate code
    2. Combine in one Slicer extension
    3. Clear Interface for adding new modules
    4. Good test coverage
    5. Common Framework
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

1. Identified main components in processing pipline to be separated and made open for extension.
1. Discussed refactoring options/software architecture.
1. Identified errors in current computations.
1. Refactored main component.
1. Next steps:
    1. Finish refactoring
    1. Fix computations

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Projects considered to be (possibly) part of the refactored extension :
    - https://github.com/millerjv/PkModeling
    - https://github.com/QIICR/T1Mapping
    - https://github.com/SlicerProstate/SlicerProstate/tree/master/DWModeling
    - https://github.com/QIICR/DSC_Analysis
    - https://github.com/gattia/Slicer-T2mapping
    - https://github.com/gti-fing/SlicerPetSpectAnalysis/tree/master/dPetBrainQuantification
    - ...
