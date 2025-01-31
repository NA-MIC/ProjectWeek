---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/SlicerFlatpak/README.html

project_title: 'Slicer Flatpak'
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Rafael Palomar
  affiliation: Oslo University Hospital
  country: Norway

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware, Inc.
  country: USA

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

- name: Sam Horvath
  affiliation: Kitware, Inc.
  country: USA

---

# Project Description

📄 Slicer Flatpak is a project focused on packaging the 3D Slicer software as a Flatpak. This initiative aims to offer an easy and universal way to install and run 3D Slicer on any Linux distribution that supports Flatpak. By doing this, it seeks to reduce installation complexities and improve compatibility across different systems. The distribution of 3D Slicer as a Flatpak has potential benefits.

The convenience of having a 3D Slicer Flatpak has been long discussed in the 3D Slicer Discourse platform ([source](https://discourse.slicer.org/t/interest-to-create-flatpak-for-3d-slicer-have-issue-with-guisupportqtopengl-not-found/16532)). Soon after PW38, we started a renewed discussion on the topic and initiated efforts to make 3D Slicer Flatpak a reality. We have completed the first distribution of 3D Slicer as a Flatpak, making progress towards our objectives.

## Objective

🎯 The objective of this project is to:

1. Consolidate the 3D Slicer Flatpak build infrastructure.
2. Resolve the issue with SimpleITK and enable its deployment along with 3D Slicer Flatpak.
3. Test and verify 3D Slicer extensions for compatibility with the Flatpak version.
4. Discuss and plan the integration and release strategy, including the possibility of submission to flathub.

## Approach and Plan

📝 Our approach to achieving the objectives is as follows:

1. Continuously develop and refine the 3D Slicer Flatpak, addressing limitations and improving its functionality.
2. Work towards resolving the SimpleITK problem and ensure seamless deployment of SimpleITK along with 3D Slicer Flatpak.
3. Enable the use of the Slicer Extension Manager and explore options for deploying extensions, considering sandboxed environments and local deployments.
4. Plan a strategy for integration and release, including the submission of patches to the Slicer repository, maintaining the flatpak generator and repository under [RafaelPalomar/Slicer-Flatpak](https://github.com/RafaelPalomar/Slicer-Flatpak), and evaluating the possibility of integration with flathub.

## Progress and Next Steps

🚀 Here is an overview of our progress so far:

1. ✅ Completed the first distribution of the 3D Slicer Flatpak, providing users with an initial version to test and provide feedback. A repository with documentation can be found at [https://github.com/RafaelPalomar/org.slicer.Slicer-flatpak-repository](https://github.com/RafaelPalomar/org.slicer.Slicer-flatpak-repository)
2. ❌ Currently, we are still working on resolving the SimpleITK problem and ensuring proper integration with 3D Slicer Flatpak.
3. ❌ Testing and verification of 3D Slicer extensions are ongoing. We are actively exploring ways to improve compatibility.
4. 📅 We recently met to plan a strategy for integration and release:
   - Some patches will be submitted to the Slicer repository to enhance the flatpak generator and improve the Slicer CMake infrastructure. Reference: [RafaelPalomar/Slicer-Flatpak](https://github.com/RafaelPalomar/Slicer-Flatpak)
   - For the time being, the flatpak generator, manifest, and flatpak repository will continue under [https://github.com/RafaelPalomar](https://github.com/RafaelPalomar). We need to evaluate the cost of maintenance and the impact of the package before considering a move.
   - We will assess the maintenance effort and impact on the Slicer community before deciding on potential integration with flathub.

# Background and References

- Slicer Flatpak Repository: [RafaelPalomar/Slicer-Flatpak](https://github.com/RafaelPalomar/Slicer-Flatpak)
- Slicer Flatpak Manifest and Repository: [RafaelPalomar/org.slicer.Slicer-flatpak-repository](https://github.com/RafaelPalomar/org.slicer.Slicer-flatpak-repository)
- Flathub: [flathub.org](https://flathub.org)
