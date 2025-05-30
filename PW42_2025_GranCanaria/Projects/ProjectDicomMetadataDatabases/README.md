---
layout: pw42-project

permalink: /:path/

project_title: 'DICOM metadata databases'
category: DICOM

key_investigators:

- name: Marco Nolden
  affiliation: German Cancer Research Center
  country: Germany

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->



Medical imaging applications and systems which manage  large collections of DICOM images usually need some kind of database to allow for browsing and selecting images or image collections, to support curation and control of ML training tasks, batch analysis etc.
Goal of the project is to investigate existing and new approaches to handle the metadata of large image collections for different purposes, create experimental setups, and report on results.

- DICOM objects contains rich metadata

- depending on the use case, record linkage to non-imaging data might be an additional requirement

- extracted metadata can be represented in different JSON styles, stored in document databases like CouchDB, Apache OpenSearch etc..

- there is a FHIR imaging study ([https://www.hl7.org/fhir/imagingstudy.html](https://www.hl7.org/fhir/imagingstudy.html)), FHIR data could be stored in FHIR stores, or regular SQL databases …

- custom approaches, like the CTK DICOM database, or IDC's representation in BigQuery; one has also observed flattened FHIR in SQL databases, combined with object stores etc.

- DICOM to JSON could be done according to the DICOM JSON model ([https://dicom.nema.org/medical/dicom/current/output/chtml/part18/chapter\_F.html](https://dicom.nema.org/medical/dicom/current/output/chtml/part18/chapter_F.html)) , e.g. using DCMTK, or custom approaches, but also generic metadata extractors like Apache Tika could be an option




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. A report on the experiments and their results.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. put DICOM JSON in JSON columns of sqlite or postgres, test jsonpath and similar
2. create FHIR imaging studies, put to FHIR endpoint or other databases
3. Connect with out-of-the-box visualization solutions for e.g. json documents




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Generate DICOM JSON representation of some TCIA datasets using pydicom
2. Read about JSON and JSONB columns in SQLite
3. Try different queries

> [!CAUTION]
> SQLite's [arrow operator ->](https://sqlite.org/json1.html#jptr) seems to behave differently if the key consists solely of digits. This can lead to surprises when working with DICOM tags whose hexadecimal representation sometimes contains letters, but sometimes only digits ...

### Count images per modality

```SQL
SELECT COUNT(*) AS [Number of records], json_extract(jsonb_data, "$.00080060.Value")
FROM dicom_files
GROUP BY json_extract(jsonb_data, "$.00080060.Value");
```
It's also possible to create an index on fields, e.g. for modality

```SQL
CREATE INDEX modality ON dicom_files (json_extract(jsonb_data, "$.00080060.Value") );
```

### Count number of series per modality

```SQL
-- Count number of series per modality
-- SQLite
SELECT
 json_extract(jsonb_data, "$.00080060.Value"),
 COUNT(DISTINCT(json_extract(jsonb_data, "$.0020000D.Value"))) AS num_series
FROM
 dicom_files
GROUP BY
 json_extract(jsonb_data, "$.00080060.Value")
ORDER BY
 num_series desc
```

```SQL
-- Count number of series per modality
-- IDC BigQuery
SELECT
 Modality,
 COUNT(DISTINCT(SeriesInstanceUID)) AS num_series
FROM
 `bigquery-public-data.idc_current.dicom_all`
GROUP BY
 Modality
ORDER BY
 num_series desc
```

### Find all series which contain a LOCALIZER ImageType

```SQL
-- Find all series which contain a LOCALIZER ImageType
-- SQLite JSON
SELECT DISTINCT
 json_extract(jsonb_data, "$.0020000D.Value")
FROM
 dicom_files, json_each (json_extract(jsonb_data, "$.00080008.Value") )
 WHERE
json_each.value IS 'LOCALIZER'
```


```SQL
-- Find all series which contain a LOCALIZER ImageType
-- IDC BigQuery
WITH
 ImageTypeAgg AS (
 SELECT
   ARRAY_TO_STRING(ImageType,'/') AS image_type_str,
   SeriesInstanceUID
 FROM
   `bigquery-public-data.idc_current.dicom_all` )
SELECT
 SeriesInstanceUID,
 image_type_str
FROM
 ImageTypeAgg
WHERE
 image_type_str LIKE "%LOCALIZER%"
```

### Findings and future experiments

- putting the standard JSON representation of DICOM files in SQLite works
- json functions of SQLite can be used to extract elements
- queries seem to be reasonably fast, database indices can be created on elements to speed this up, e.g. ~5x for modality

Ideas for future experiments:
- validate results by comparing them to IDC BigQuery results for selected collections
- measure performance in a systematic way
- replace numeric tag values with names, makes queries more readable but might also increase database size
- compare performance and size with PostgreSQL
- use alternative JSON structure from the proposed [DICOM Supplement 219](https://dicom.nema.org/medical/dicom/Supps/Frozen/sup219_fz_14_JSONSR.pdf) , [Presentation](https://dicom.nema.org/medical/dicom/Supps/Frozen/sup219_fz_JSONSR_TrialUse_Slides_20200116.pptx) . There is also a trial implementation by @dclunie which could be evaluated for this.
-
-







Sample code to do so could look like this:

```Python
#!/usr/bin/env python

"""Populate SQLite with DICOM metadata.

This code recursively crawls a directory and populates a SQLite database with JSON representations of
the DICOM files found.

Warning: highly experimental code, use at your own risk!

"""

import pydicom
import os
import sys
import sqlite3
import json

def bulk_data_handler(data_element):
    # we are not interested in any bulk data
    return None

crawl_directory = sys.argv[2]
db_path = sys.argv[1]

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS dicom_files (
    filename TEXT PRIMARY KEY NOT NULL,
    jsonb_data BLOB
)
''')

conn.commit()

# iterate over crawl directory, and insert json dumps of all files to the database
for root,dirs,files in os.walk(crawl_directory):
    for file_name in files:
        dicom_file_path = os.path.join(root,file_name)
        json_data = ""

        # check if file is already in the database
        cursor.execute("SELECT filename FROM dicom_files WHERE filename = ?", (dicom_file_path,))
        data=cursor.fetchone()

        if data:
            continue

        try:
            ds = pydicom.dcmread(dicom_file_path)
            json_data = ds.to_json_dict(bulk_data_element_handler=bulk_data_handler)

            # print(json_data)

        except pydicom.errors.InvalidDicomError:
            print("Skipped %s", dicom_file_path)
            continue

        cursor.execute('''
        INSERT INTO dicom_files (filename, jsonb_data )
        VALUES ( ? , jsonb( ? ) )
        ''', (dicom_file_path, json.dumps(json_data) ) )

        conn.commit()

        print(f"Inserted DICOM file: {dicom_file_path}")

conn.close()
```

https://github.com/nolden/namic-pw24/


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![Image](https://github.com/user-attachments/assets/45f6c2d3-4ad6-44f2-a88b-749c0a815333)

![Image](https://github.com/user-attachments/assets/83248ec0-1531-477c-9792-da0be11cb502)

![Image](https://github.com/user-attachments/assets/66e5c440-b634-4e14-9fd0-e457de6eab34)

_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->



- Opensearch dashboards
- [https://www.metabase.com/](https://www.metabase.com/)
- [https://superset.apache.org/](https://superset.apache.org/)
- [https://python.langchain.com/v0.1/docs/modules/model\_io/output\_parsers/types/json/](https://python.langchain.com/v0.1/docs/modules/model_io/output_parsers/types/json/)
- [https://echarts.apache.org/examples/en/index.html\#chart-type-line](https://echarts.apache.org/examples/en/index.html#chart-type-line)
- [https://projectweek.na-mic.org/PW41\_2024\_MIT/Projects/Dcm2Parquet/](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/Dcm2Parquet/)
- [\[2407.09064\] Multi-Modal Dataset Creation for Federated Learning with DICOM Structured Reports](https://arxiv.org/abs/2407.09064)
- [https://learn.microsoft.com/en-us/industry/healthcare/healthcare-data-solutions/dicom-data-transformation-mapping](https://learn.microsoft.com/en-us/industry/healthcare/healthcare-data-solutions/dicom-data-transformation-mapping)
- [https://github.com/pydicom/pydicom/issues/2187](https://github.com/pydicom/pydicom/issues/2187)
- Potential example queries for experiments: [https://docs.google.com/document/d/1qC5\_qUFBQ2HmEjfYQa9WaH1Y-erMlfis00bbU8UPnRs/edit?tab%3Dt.0%23heading%3Dh.ti11twc8h457\&sa=D](https://www.google.com/url?q=https://docs.google.com/document/d/1qC5_qUFBQ2HmEjfYQa9WaH1Y-erMlfis00bbU8UPnRs/edit?tab%3Dt.0%23heading%3Dh.ti11twc8h457&sa=D&source=docs&ust=1737743914441474&usg=AOvVaw0MsdEgNMafuMPSajRC6WNP)
- [https://learn.canceridc.dev/cookbook/bigquery](https://learn.canceridc.dev/cookbook/bigquery)
- [https://github.com/bebbi/dcm-organize](https://github.com/bebbi/dcm-organize)
