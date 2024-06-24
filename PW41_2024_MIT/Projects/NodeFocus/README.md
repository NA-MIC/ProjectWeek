---
layout: pw41-project

permalink: /:path/

project_title: Node focus in views
category: Infrastructure
presenter_location: In-person

key_investigators:
- name: Kyle Sunderland
  affiliation: Queen's University
  country: Canada
---

# Project Description

3D software applications often provide feedback mechanisms for selecting objects and showing users which objects they have selected, or are interacting with. This allows some visualizations to be hidden when the object is not in focus.

During PW39, we worked on the initial visualization and implementation, however it has since become clear that we will need to account for additional use-cases such as VR and muli-user interaction.

## Objective

Analyze the existing prototype implementation and discuss ways that the design could be improved to account for the expanded use-cases.

This new implementation should be able to handle the existing use-cases:
- See the nodes that they are hovering over or interacting with in the various subject hierarchy trees or node selectors.
- Select nodes by clicking on them in one of the views.

As well as the new use-cases:
- Multi-controller highlighting in VR.
- Allow highlighting by multiple users.

If you would like to offer suggestions or feedback on the current prototype, then come see me in-person.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Analyze and discuss how the current design can be improved to work with the additional use-cases.
2. Continue development of the node focus infrastructure.

## Progress and Next Steps

- Prototype implementation can be found here: https://github.com/Sunderlandkyl/Slicer/tree/focus_node_prototype
- Brainstorm how the implementation can be improved to support the new use-cases.

# Illustrations

Example showing segmentations:

![Atlas node focus](https://github.com/NA-MIC/ProjectWeek/assets/9222709/cd0fd740-2aee-4010-b73d-dc8a53f8e58e)

Example showing markups:

![Markups node focus](https://github.com/NA-MIC/ProjectWeek/assets/9222709/2ecbef2b-e7a2-4317-9e9d-1191f5a75d4f)

Example showing models using a combobox:

![Combobox model node focus](https://github.com/NA-MIC/ProjectWeek/assets/9222709/7450c678-f8eb-482b-97c2-e0b95d4e05bc)

# Background and References

- [Development branch](https://github.com/Sunderlandkyl/Slicer/tree/focus_node_prototype)
