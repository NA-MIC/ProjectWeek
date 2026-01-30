---
layout: pw44-project

permalink: /:path/

project_title: Updating SlicerSOFA
category: Infrastructure
presenter_location: 

key_investigators:

- name: Rafael Palomar
  affiliation: NTNU / OUH
  country: Norway

- name: Paul Baksic
  affiliation: Inria
  country: France

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

---

# Project Description

SlicerSOFA is a 3D Slicer extension integrating the simulation framework SOFA in 3D Slicer. The extension packages the SOFA-framework, together with `SofaPython3` and exposes SOFA to 3D Slicer through Python. In addition, SlicerSOFA provides functionality to connect and transfer data between 3D Slicer objects and SOFA objects. In this project, we plan to update SlicerSOFA to have better cross-platform coverage (currently a macOS version is not available) and work with the latest 3D Slicer and SOFA versions, as well as integrating external execution of simulations through RPyC.

## Objective

- ⬆️ Update SlicerSOFA to use SOFA v25.12 (latest available) — delivered in 🔀 [PR #60](https://github.com/Slicer/SlicerSOFA/pull/60)
- 🧪 Update SlicerSOFA to run on the latest 3D Slicer stable and development versions — in review (🔀 [PR #60](https://github.com/Slicer/SlicerSOFA/pull/60))
- 🍏 Fix SlicerSOFA macOS integration — next
- ✅ Enable loading a regular SOFA scene in SlicerSOFA — delivered via SOFASceneLoader (🔀 [PR #60](https://github.com/Slicer/SlicerSOFA/pull/60))
- 🔌 Integrate RPyC external execution — next
- 📝 Update project documentation — delivered in 🔀 [PR #60](https://github.com/Slicer/SlicerSOFA/pull/60)

## Approach and Plan

The core SOFA library will be updated first to its latest version (v25.12) and tested on the latest Slicer (stable+dev). After an updated working version for Windows and GNU/Linux, a fix for macOS will be provided. Finally, a new executor using RPyC will be provided (tests will be performed in external processes (local + remote machine)). The updates and the new additions will be documented.

## Progress and Next Steps

### ✅ Results (PW44)
- ✨ New SOFASceneLoader module to open any Python-based SOFA scene exposing `createScene()`
- 🔁 Added SOFA↔️MRML mapping for polydata topologies
- ⬆️ Updated SOFA core and related plugins to v25.12
- 🔧 Forced CMake minimum version policy on GLEW for reliable builds
- 📝 Documentation updates

📎 All the above are included in: 🔀 [PR #60](https://github.com/Slicer/SlicerSOFA/pull/60)  
(Previous SOFASceneLoader work: [PR #58](https://github.com/Slicer/SlicerSOFA/pull/58))

### 🔜 Next steps
- 🍏 macOS packaging and integration fixes
- 🔌 RPyC executor integration and local/remote testing
- 🧪 CI and validation on latest Slicer stable and nightly
- 📚 Expand documentation and examples

# Illustrations

🎥 SlicerSOFA `.py` scene loading demo: 

[SlicerSOFA.webm](https://github.com/user-attachments/assets/6ce15869-eb69-4be1-adad-87db3bb91d46)

# Background and References

- Source code: https://github.com/Slicer/SlicerSOFA
- 🔀 [PR #60 (PW44 results)](https://github.com/Slicer/SlicerSOFA/pull/60)
- [PR #58 (SOFASceneLoader)](https://github.com/Slicer/SlicerSOFA/pull/58)
