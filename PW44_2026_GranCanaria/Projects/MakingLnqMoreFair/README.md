---
layout: pw44-project

permalink: /:path/

project_title: Making LNQ more FAIR
category: Quantification and Computation
presenter_location: 

key_investigators:

- name: Michael Halle
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The Lymph Node Quantification Project currently has no web presence, pointer to its data, or source of reference material. I plan to explore a set of traditional (web) and new (LLM and Claude Skill) technologies to make the project more findable, accessible, interoperable and reusable. This includes developing a searchable citation tree to improve search for information about lymph node quantification, and a roadmap (skill) to help LLMs look for LNQ resources.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. An LNQ web site/landing page
2. An SQLite database of citations in the citation tree rooted by seminal or otherwise important papers in the field
3. A Claude Skill that can search the database, the LNQ data stored in IDC, and the information from the MICCAI challenge



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Github website
2. Identify publications
3. Build citation tree
4. Write skill



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Built the website https://lnqproject.org  (mkdocs with material theme)
2. Wrote llms.txt for the site
3. added citation database with datasette browser: [Browse LNQ Citations](https://lite.datasette.io/?url=https://raw.githubusercontent.com/mhalle/LNQ-citations/master/citations.db&metadata=https://raw.githubusercontent.com/mhalle/s2cli/main/citetree-metadata.yaml#/citations/papers)


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

