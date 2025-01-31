Back to [Projects List](../../README.md#ProjectsList)

# Lightweight DICOMweb Server with CouchDB

## Key Investigators

- Emel Alkim (Stanford)
- Steve Pieper (Isomics)
- Hans Meine
- Erik Ziegler

# Project Description

This project aims to build on prototype [lightweight DICOM server that was developed last year](https://projectweek.na-mic.org/PW30_2019_GranCanaria/Projects/DICOMweb-CouchDB/)

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

* Develop easy to install and test recipes / scripts
* Compare functionality and performance with other DICOMweb implementations
* Brainstorm about non-standard extensions of utility to the community
  * search by reference (e.g. find all segmentations of this image)
  * extract cohorts by tag (e.g. find all CTs with .5mm pixel spacing)
  * represent workflow state (e.g. give list of all studies that do not have manual segmentations)
* Work on improving performance


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


## Progress and Next Steps

Hans tested the server successfully, in order to try out DICOMWeb and get a feel for what's possible and how to integrate with other tools. Here's one quick guide on how to possibly reproduce:

* Hans used CouchDB via Docker (Steve & Emel recommended running [PouchDB](https://pouchdb.com/guides/setup-pouchdb.html) via NodeJS):

      docker run --rm -d --name couchdb -p 5984:5984 apache/couchdb

  (This is for one-off experiments; one should really mount a DB directory.)

* The [dicomweb-server-js README](https://github.com/dcmjs-org/dicomweb-server/blob/master/README.md) contains instructions on how to start the server and index DICOM files via the Python [dicomweb_client](https://github.com/clindatsci/dicomweb-client).

* Subsequently, one may test the Rest API directly (e.g. via [httpie](https://httpie.org) on the default port 5985), look at the underlying CouchDB (UI at http://localhost:5984/_utils), or try the OHIFViewer.

  * [test_ohifviewer.html](test_ohifviewer.html) is a standalone file with the necessary JS snippet to configure an OHIFViewer. Adapt the URLs to your server if necessary.
  * Use a HTTP server to serve that file and show it in a browser:

        python -m http.server 9000
        xdg-open http://localhost:9000/test_ohifviewer.html

Performance Improvements:
* Extended the dicomweb codebase with parallel execution for database processes which lets us limit the number of concurrent database calls and manage workload

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
- dicomweb-server: https://github.com/dcmjs-org/dicomweb-server
- SlicerChronicle: https://github.com/pieper/Chronicle
- SlicerChronicle: https://github.com/pieper/SlicerChronicle
- dcmjs: https://github.com/dcmjs-org/dcmjs
