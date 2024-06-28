---
layout: pw41-project

permalink: /:path/

project_title: dcm2parquet
category: DICOM
presenter_location: In-person

key_investigators:

- name: Vamsi Thiriveedhi
  affiliation: BWH
  country: USA

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA
---

# Project Description

As of now, we are not aware of a tool other than Google Cloud's HealthCare API that can extract DICOM Header for a dataset and enable querying the metadata via SQL. We aim to explore if it is possible to do this 'in-house' so that those researchers who can not upload their data to Google DICOM stores or do not have access to Google Cloud can benefit. To that end, we found duckdb, a fast in-process analytical database/client to be able to query highly complex nested data. Using duckdb, and pydicom, our goal is extract DICOM header in a way that is similar to Bigquery export feature in Google Cloud's HealthCare API.

## Objective

1. Convert DICOM header to parquet preserving the nesting 
2. Figure out a way to dynamically update schema and data manipulations necessary
3. Make the tool available on Hugging Face by integrating with idc-index, to seamlessly experiment with existing data in IDC


## Approach and Plan

1. Create a function to extract metadata at the series level first, assuming schema is consistent with in a series.
2. Identify which columns and fields in the nested hierarchy, have inconsistent schema in a dataset, and choose most exhaustive datatype. For example b/w a string and array of strings, string datatype will be updated to array. Fill the missing columns, fields with nulls


## Progress and Next Steps

1. Able to extract metadata at series level with out any problems. The [app](https://huggingface.co/spaces/vkt1414/dcm2parquet) reflects the progress made up to this point
2. Next, inspired from how Bigquery displays the schema, we aim to replicate that. After, we will compare the common columns between Image series and determine if any data manipulation is necessary.
   ![image](https://github.com/NA-MIC/ProjectWeek/assets/115020590/b18deb90-5934-436b-a04d-0a047b8e017c)
3. Able to replicate how Bigquery displays the schema locally now.
4. Found several blogs on how others were thinking about schema evolution.
   - https://kontext.tech/article/381/schema-merging-evolution-with-parquet-in-spark-and-hive
   - https://blog.devgenius.io/data-processing-with-spark-schema-evolution-4d6032e3737c
   - https://spark.apache.org/docs/latest/sql-data-sources-parquet.html
   - https://medium.com/@shenoy.shashwath/performance-optimization-in-apache-spark-with-parquet-file-format-994273742c4f
   - https://github.com/mplacko/ParquetSchemaMerging
   - https://medium.com/analytics-vidhya/building-a-notebook-based-etl-framework-with-spark-and-delta-lake-b0eee85a8527


# Illustrations
We hosted the app on Hugging Face space at https://huggingface.co/spaces/vkt1414/dcm2parquet

![image](https://github.com/NA-MIC/ProjectWeek/assets/115020590/30a0d0b3-13f7-4ad4-8ee1-0b8eb9a4c98a)


# Background and References


- [https://medium.com/expedia-group-tech/practical-schema-evolution-with-avro-c07af8ba1725](https://medium.com/expedia-group-tech/practical-schema-evolution-with-avro-c07af8ba1725)

