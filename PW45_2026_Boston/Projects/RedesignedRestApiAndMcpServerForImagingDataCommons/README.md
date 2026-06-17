---
layout: pw45-project

permalink: /:path/

project_title: Redesigned REST API and MCP server for Imaging Data Commons
category: Cloud / Web
presenter_location: 

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Bill Clifford
  affiliation: Institute for Systems Biology
  country: USA

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

- name: Martin Bellehumeur
  affiliation: Radical Imaging
  country: Germany

- name: Ulrike Wagner
  affiliation: Leidos Biomedical Research
  country: USA

- name: Granger Sutton
  affiliation: National Cancer Institute
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

**Questions? Want to participate remotely? Join our project [Discord channel](https://discord.gg/TTFGUYGdsZ)!**

TL;DR: Work on v3 of IDC REST API simultaneously with the development of the MCP server.

IDC already offers a customized agent skill in [https://github.com/ImagingDataCommons/imaging-data-commons-skill](https://github.com/ImagingDataCommons/imaging-data-commons-skill), which is very powerful in helping with the use of IDC. However, in order to use it effectively, the user needs to have access to an LLM platform that supports code execution, and needs to suffer the "cold start" cost of setting up the environment. IDC MCP interface can provide "zero startup cost" solution for answering at least some of the queries, optimized for the use by agents. At the same time, MCP interface will need to rely on IDC API, which in its current v2 form is not useful at all. We are in the process of simultaneous redesign of IDC API and design of the MCP interface. Since we do not have expertise on the team doing something like this before, we would appreciate community feedback.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Maximize utility of the revised IDC API and new MCP server to IDC users, identify design flaws before public release.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Refine and deploy the initial implementation.
2. Provide test URL endpoints for interested users.
3. Test against use cases raised in the community.
4. Collect feedback from IDC users and those who have more expertise designing REST API and MCP interfaces.


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

