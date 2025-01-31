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

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware
  country: US
  
- name: Andres Diaz-Pinto
  affiliation: NVIDIA
  country: UK
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

1. Get feedback on the current preliminary implementation [PR](https://github.com/Slicer/Slicer/pull/8141) and work a final design for the JSON based node status/scene file format.
2. Discuss real-time collaboration toolkits for medical application (e.g. Omniverse)


## Approach and Plan

1. Have a meeting/demo with people interested for colletting feedback.
1. Work on the final design of the JSON based node status/scene file format.


## Progress and Next Steps

### Progress
- Draft [PR](https://github.com/Slicer/Slicer/pull/8141) is already functional. The primary advantage of using JSON is that arrays are printed in a standardized format, unlike the XML format, which uses a Slicer-specific structure that can vary between arrays, subject hierarchy items attributes, etc. Below is an example comparing the scene in XML and JSON formats:
 
| XML | JSON |
|--- | ---|
|<img src="https://github.com/user-attachments/assets/44f93b00-e287-4018-a563-bbf78aaaa8c0" width="500"> | <img src="https://github.com/user-attachments/assets/dabe1c07-7520-4f0c-ba32-132e5876118f" width="500"> |

- Testing reading/writing perfomances for the **Scene-Level** use case with 100 markups lines:
   - XML: write 0.009117 ± 0.000674 sec, read 0.137960 ± 0.038905 sec
   - JSON: write 0.046738 ± 0.020891 sec, read 0.180462 ± 0.013206 sec
   - Relative performance factors are ~5.13x slower for writing and ~1.31x slower for reading when using JSON compared to XML.
   - Scene writing could be optimized further, although the time for processing 100 markup lines is < 0.05 seconds. Further investigation is needed to estimate perfomances on very large scenes.
- Meeting done on Tuesday. Key notes taken by JC:
https://github.com/Slicer/Slicer/pull/8141#issuecomment-2618876551
   - Supporting partial updates to the scene is an interesting direction, particularly with Node Status printing/updating to enable partial node modifications.
   - Introducing `macros` for automatic schema generation would be beneficial.
   - Exploring `GraphQL` support could enable batched updates through mutations. Integration could leverage libraries such as `cppgraphqlgen`, as `libgraphqlparser` appears unmaintained.
   - Investigate VTK serialization capabilities in recent versions, which might complement this work.
- The discussion with NVIDIA will be further explored to assess Slicer support and interoperability with OpenUSD/Omniverse for a medical real-time collaboration tool within Omniverse.

  
### Next Steps
1. When calling `WriteJSONToString` for `storageNodes`, we need to stringify certain parts of the node state information (for the single **Node Status - real-time collaboration** use case).  
   - **Markups** use `vtkMRMLMarkupsJsonStorageNode`, which already utilizes the JSON format. However, the current infrastructure only allows saving this information to a file. We need to refactor `vtkMRMLMarkupsNode` and `vtkMRMLMarkupsJsonStorageNode` to use `vtkMRMLMarkupsJsonWriter` for stringifying to a stream instead of a file, enabling access to its methods from Python. 
   - **Transforms** use `vtkMRMLTransformStorageNode` -> `itk::TransformFileWriter` has the the same issue of the Markups writer. We would need to refactor at the `vtkMRMLNode` to be able to switch between writing to file and to a stream. 
   - **Volumes/Segmentations/Models**: For now, storing the file location should suffice, but in the future, we may need to pass `imageData` as a blob.  

1. Add automated tests to cover all MRML nodes in Slicer core/modules.
1. Investigate each feedback point gathered during the Tuesday meeting.
  
# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[PR](https://github.com/Slicer/Slicer/pull/8141)



