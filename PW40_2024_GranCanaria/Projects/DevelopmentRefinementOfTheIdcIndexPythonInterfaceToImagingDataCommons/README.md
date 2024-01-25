---
layout: pw40-project

permalink: /:path/

project_title: Development/refinement of the idc-index python interface to Imaging Data Commons
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Vamsi Thiriveedhi
  affiliation: BWH
  country: USA

- name: Daniela Schacherer
  affiliation: Fraunhofer MEVIS
  country: Germany

- name: Leonard Nürnberg
  affiliation: Maastricht University
  country: Netherlands

---

# Project Description

<!-- Add a short paragraph describing the project. -->

[`idc-index`](https://github.com/ImagingDataCommons/idc-index) is a lightweight python package that wraps mini-index of the data available in Imaging Data Commons and the s5cmd download tool. With this package, one can search basic attributes of IDC data, build subset and download corresponding files without login, and without setting up any prerequisites specific to either Google or AWS as easy as below:

```bash
$ pip install 'idc-index==0.2.8'
```

```python
from idc_index import index

client = index.IDCClient()
client.download_from_selection(collection_id="nsclc_radiomics", downloadDir="./my_copy")
```

Its basic functionality is demonstrated in this tutorial: <https://github.com/ImagingDataCommons/IDC-Tutorials/blob/master/notebooks/labs/idc_rsna2023.ipynb>.

[SlicerIDCBrowser](https://github.com/ImagingDataCommons/SlicerIDCBrowser) already relies on `idc-index` for searching and downloading data from IDC.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Raise awareness about 
2.  Improve functionality
3.  Collect feedback to prioritize future developments

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  collect feedback about what functionality would be useful to add or how to refine the API
2.  discuss capabilities that would be needed to support digital pathology use cases
3.  refine organization of the underlying index and exposed metadata attributes
4.  finish setting up GitHub actions to simplify updates and python package publishing
5.  documentation
6.  discuss with python packaging experts what is the recommended practice handling attachments/binary dependencies for a python package (ie, see [https://github.com/ImagingDataCommons/idc-index/issues/3](https://github.com/ImagingDataCommons/idc-index/issues/3) and [https://github.com/ImagingDataCommons/idc-index/issues/27](https://github.com/ImagingDataCommons/idc-index/issues/27))

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

*No response*

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   [NCI Imaging Data Commons](https://imaging.datacommons.cancer.gov)
*   [`idc-index`](https://github.com/ImagingDataCommons/idc-index)
