---
layout: pw40-project

permalink: /:path/

project_title: Improving Project Page infrastructure
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The Project Week team will continue to make improvements to the project page generation process

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Decrease complexity of project page creation
2.  Increase speed of site deployment

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Test out current page infrastructure
2. Identify any issues and pain points

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Identified a significant bug in the page generation for complicated pages: [issue](https://github.com/NA-MIC/ProjectWeek/issues/960).
    1. Content sections with multiple types of content (headings, lists, html) were being discarded by the parser
3. Reworked the issue parsing to be more flexible wrt the content of each section

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
