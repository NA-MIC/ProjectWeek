Back to [Projects List](../../README.md#ProjectsList)

# Using VolView with data in Google Storage buckets / IDC buckets

## Key Investigators

- Andrey Fedorov (Brigham and Women’s Hospital, USA)
- Forrest Li (Kitware, USA)
- Stephen Aylward (Kitware, USA)

# Project Description
<!-- Add a short paragraph describing the project. -->

[VolView](https://volview.kitware.com/) is an open source radiological viewer developed by Kitware that excels in 3D visualization. Currently, this viewer can be used to visualize files uploaded into the browser.

[NCI Imaging Data Commons](https://imaging.datacommons.cancer.gov/) is a cloud-based repository of cancer imaging data, which among other features provides free access to the DICOM files curated in Google Storage public buckets. 

While IDC integrates OHIF and Slim viewers, the instances of the viewers maintained by IDC can only be used to visualize data in IDC. Users that want to visualize analysis results they produce in OHIF or Slim need to deploy their own instances of the viewers. That process is documented, but involves many steps and can be too difficult for many users. Furthermore, OHIF Viewer v2 used in IDC does not have any functionality to support 3D visualization.

In this project we want to investigate the use of existing VolView instance maintained by Kitware at [https://volview.kitware.com/](https://volview.kitware.com/) to visualize data in public Google Storage buckets. This will allow:
1. 3D visualization of public data in IDC.
2. Not only "zero footprint", but more importantly "zero deployment" and "zero maintenance" viewer that can be used by IDC users to visualize analysis results.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Investigate ability of VolView to pull data from Google Storage public buckets - in IDC and/or from user projects.
2. Investigate representation of the manifest to be used to define VolView input.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Experiment with CORS settings on a public "test" bucket.
2. Define minimum necessary settings for CORS configuration.
3. Coordinate with GCP support and other GCP experts as needed.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Defined steps for setting up GCS bucket to be accessible by VolView, defined the format of the manifest:
  * install GCP SDK (or use Colab), initialize GCP, create project, set up billing (billing required for creating buckets!) - can use [this IDC tutorial](https://github.com/ImagingDataCommons/IDC-Examples/blob/master/notebooks/getting_started/part1_prerequisites.ipynb)
  * Create a public GCS storage bucket
  * Set up CORS configuration using these settings:
  ```
  [
    {
      "origin": ["https://volview.netlify.app/"],
      "method": ["*"],
      "responseHeader": ["Content-Type"],
      "maxAgeSeconds": 3600
    }
  ]
  ```
  * update CORS configuration for the bucket using this command:
  ```$ gcloud storage buckets update gs://<YOUR_BUCKET> --cors-file=./idc-volview-pilot-cors.json```
    * you may need to wait for several hours for the CORS configuration to propagate
  * create JSON manifest that refers to the files corresponding to the specific study/series in your bucket that you want to visualize in VolView using this format, and put the manifest in the bucket alongside the files:
  ```
  {"resources":[{"url":"gs://<YOUR_BUCKET>/lymph/000cdc4d-7700-46be-82ec-7eff30eacd63.dcm"},{"url":"gs://<YOUR_BUCKET>/lymph/00187779-6957-48c5-ad00-8aeaa8f34642.dcm"},{"url":"gs://<YOUR_BUCKET>/lymph/0024f696-98a8-4251-8702-c9bb690e281a.dcm"},{"url":"gs://<YOUR_BUCKET>//lymph/00c78534-a63f-46cd-abbc-32003a58d3ec.dcm"},{"url":"gs://<YOUR_BUCKET>//lymph/01e2fad8-386b-4e04-8a74-9f52c9af9919.dcm"}
  [...]
  ```
  * when CORS config is propagated, you should be able to open the images in Kitware hosted VolView instance using this URL format: `https://volview.netlify.app/?urls=https://storage.googleapis.com/<YOUR_BUCKET>/<YOUR_MANIFEST>.json`
  2. Reached out to Google Public Datasets Program support asking if CORS can be configured for the public IDC buckets to allow GET from VolView, waiting for the response.
  
# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

![CT series in GCS bucket loaded in VolView via manifest in GCS bucket](https://github.com/NA-MIC/ProjectWeek/raw/master/PW38_2023_GranCanaria/Projects/IDC_with_VolView/gcs-bucket-volview.gif) Link to try out: [https://volview.netlify.app/?urls=https://storage.googleapis.com/idc-volview-pilot/idc-test.json](https://volview.netlify.app/?urls=https://storage.googleapis.com/idc-volview-pilot/idc-test.json)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

