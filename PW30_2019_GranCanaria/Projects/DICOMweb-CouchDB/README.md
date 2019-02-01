Back to [Projects List](../../README.md#ProjectsList)

# Lightweight DICOMweb Server with CouchDB 

## Key Investigators

- Emel Alkim (Stanford)
- Steve Pieper (Isomics)
- Andrey Fedorov (BWH) - interested to deploy and test the resulting platform
- Markus Herrmann (CCDS)
- Tobias Stein (DKFZ)
- Marco Nolden (DKFZ) - optional CTK/C++ based client side testing 

# Project Description

This project aims to work on a prototype lightweight DICOM server that will support DICOMweb standard and host the DICOM files as JSON objects. It will leverage previous work on SlicerChronicle and dcmjs. 

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Provide prototype of a lightweight DICOM server that supports DICOMweb queries
2. Provide an example implementation of a proxy layer to transfer DICOMweb queries to CouchDB

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Review and define project ideas
    1. Consider how to encapsulate DICOMweb logic so that it facilitates use in servers, but also in testing and other scenarios
    1. Define a reasonable subset of DICOMweb that can be supported easily (at least basic QIDO/WADO/STOW RS)
    1. Pick a nice web server infastructure that can easily implement rest api proxies 
        1. maybe build on [express/pouchdb-server](https://github.com/pouchdb/pouchdb-server)
        1. also look at [fastify](https://www.fastify.io/)
    1. Find an easy way to host the service for development, testing, and demos
1. Implement an example translation of a DICOMweb query to CouchDB map/reduce statements
1. Implement translation of the CouchDB response to DICOMweb response
1. Build a bridge between SlicerChronicle and dcmjs to host the DICOM files as JSON files and support CSTORE

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. SlicerChronicle stores DICOM object instances as documents in CouchDB
1. Repository created in https://github.com/emelalkim/dicomweb-server-js using fastify node.js framework
1. DICOMweb queries and CouchDB views created for:
    1. QIDO
        1. {s}/studies endpoint: Query for studies
        1. {s}/studies/{study}/series endpoint: Query for series
        1. {s}/studies/{study}/series/{series}/instances endpoint: Query for instances
    1. WADO
        1. {s}/studies/{study}/series/{series}/instances/{instance} endpoint : WADO-URI Retrieve Instance 
        1. {s}/studies/{study}/metadata endpoint: Retrieve study metadata
 
1. JSON schemas defined for QIDO query responses for studies, series and instances level
1. Implemented STOW using some parts from Dicomweb-client (https://github.com/dcmjs-org/dicomweb-client) and dcmjs (https://github.com/dcmjs-org/dcmjs)


1. Improve code base with documentation, organization and testing
1. Handling different tag values throughout study
    1. If there are different values for different series: We are thinking of showing an interface to fix
    1. If same uid is used with different values: We will show user notification. Optinons are overwriting or letting the user fix. We will start with overwriting

1. Handling multiframes and frames endpoints
1. Handing compression
1. Integrate Dicomzero code to dcmjs utils
1. Message.js should be exported from dcmjs to be used in this project

*Side project C++* : this made some progress in parsing the JSON query results in C++, next steps will be to refactor some methods inside CTK to use JSON objects instead of relying on DcmDataset for internal storage and passing around of DICOM meta information. [experiment code](https://github.com/nolden/CTK/tree/wip-dicomweb)


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![Example sequence diagrams](DICOMweb%2BChronicle.png)
![STOW and WADO-URI example](dicomweb_stow_wadouri_v.png)
![WADO metadata example](dicomweb_metadata.png)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
- SlicerChronicle: https://github.com/pieper/Chronicle
- SlicerChronicle: https://github.com/pieper/SlicerChronicle
- dcmjs: https://github.com/dcmjs-org/dcmjs
