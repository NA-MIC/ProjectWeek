---
layout: pw42-project

permalink: /:path/

project_title: JSON based scene file format
category: Infrastructure

key_investigators:

- name: Davide Punzo
  affiliation: freelancer, DNA-HIVE
  country: France

- name: Andras Lasso
  affiliation: Queens University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

#### **Overview**

The primary objective of this feature is to introduce support for **JSON format** to enable writing and reading the full MRML scene file and its nodes. This serves as preparatory work for:

1. Supporting a more structured format for the MRML file with explicit datatypes.
2. Providing APIs in Slicer to facilitate collaborative features, such as retrieving and updating the status of individual nodes.

With this setup, we would start a first step for future adoption and compatibility with standards like OpenUSD and real-time collaborative toolkits (e.g. Omniverse). For example, having MRML structured in JSON will make it much easier to convert nodes to OpenUSD.

---

#### **Implemented Features**

- **Node Status Printing**:
  Nodes can now output their state in JSON format using the `WriteJSONToString` method. For example, in the Python console:

  ```python
  crosshairNode.WriteJSONToString()
  ```
  Output:
  ```json
  {
    "Crosshair": {
      "id": "vtkMRMLCrosshairNodedefault",
      "name": "Crosshair",
      "hideFromEditors": true,
      "selectable": true,
      "selected": false,
      "singletonTag": "default",
      "crosshairMode": "NoCrosshair",
      "crosshairBehavior": "OffsetJumpSlice",
      "crosshairThickness": "Fine",
      "crosshairRAS": [0.0, 0.0, 0.0]
    }
  }
  ```

- **Node State Reading/Updating**:
  Nodes can now read or update their state (either fully or partially) from a JSON string. For example:

  ```python
  a.ReadJSONFromString('{"Crosshair":{"crosshairRAS":[100.0,100.0,100.0]}}')
  ```

- **Scene-Level JSON Format Support**:
  The format for the entire MRML scene is controlled by a macro:

  ```cpp
  vtkMRMLScene::SetUseJSONFormat(true);
  ```

  When enabled, the scene file will be output in JSON format. For example, the attached [sample file](https://github.com/user-attachments/files/18457210/2025-01-17-Scene.zip) demonstrates the current output structure.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Get feedback on the current preliminary implementation [PR](https://github.com/Slicer/Slicer/pull/8141) and work a final design for the JSON based node status/scene file format.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Have a meeting/demo with people interested for colletting feedback.
1. Work on the final design of the JSON based node status/scene file format.


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->
 


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[PR](https://github.com/Slicer/Slicer/pull/8141)




