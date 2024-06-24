---
layout: pw41-project

permalink: /:path/

project_title: Node focus in views
category: Infrastructure
presenter_location: In-person

key_investigators:
- name: Kyle Sunderland
  affiliation: Queen's University

- name: Person2 Doe2
  affiliation: University2
  country: Spain
---

# Project Description

3D software applications often provide feedback mechanisms for selecting objects and showing users which objects they have selected, or are interacting with. This allows some visualizations to be hidden when the object is not in focus.

## Objective

This project aims to implement a similar node selection system in 3D Slicer, allowing users to:

- See the nodes that they are hovering over or interacting with in the various subject hierarchy trees or node selectors.
- Select nodes by clicking on them in one of the views.

If you would like to offer suggestions or feedback on the current prototype, then come see me in-person.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Continue development of the node focus infrastructure.
2. Get feedback from hands-on use to better improve the implementation.
3. Improve visualization and performance.

## Progress and Next Steps

- Prototype implementation can be found here: https://github.com/Sunderlandkyl/Slicer/tree/focus_node_prototype
- Improve rendering of volumes + hard selection.
- Implement picking of node types other than markups.

# Illustrations


Example showing segmentations:

![Atlas node focus](https://github.com/NA-MIC/ProjectWeek/assets/9222709/cd0fd740-2aee-4010-b73d-dc8a53f8e58e)

Example showing markups:

![Markups node focus](https://github.com/NA-MIC/ProjectWeek/assets/9222709/2ecbef2b-e7a2-4317-9e9d-1191f5a75d4f)

Example showing models using a combobox:

![Combobox model node focus](https://github.com/NA-MIC/ProjectWeek/assets/9222709/7450c678-f8eb-482b-97c2-e0b95d4e05bc)

# Background and References

- [Development branch](https://github.com/Sunderlandkyl/Slicer/tree/focus_node_prototype)
