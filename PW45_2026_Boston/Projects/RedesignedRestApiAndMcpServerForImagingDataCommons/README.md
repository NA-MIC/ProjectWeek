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

TL;DR: Work on v3 of [Imaging Data Commons (IDC)](https://portal.imaging.datacommons.cancer.gov/) REST API simultaneously with the development of the IDC [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) server.

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


1. Developed v3 of IDC REST API and the initial version of MCP server - [repo and overview](https://github.com/fedorov/IDC-API/blob/idc-api-v3/docs/user-guide.md)
2. Shared MCP server endpoint with interested users, collected feedback (in particular, identified the need to improve support of clinical data)
3. Improved MCP integration with Martin's project [https://github.com/mbellehumeur/vtk-js/pull/1](https://github.com/mbellehumeur/vtk-js/pull/1)
4. Implemented support for clinical tables query.
  * [public linkt to a conversation with Claude](https://claude.ai/share/85b9d201-1f85-4492-9b9b-311bf98b09f5) demonstrating the capabilities of clinical data exploration with the updated IDC MCP server
5. Summarized (but not benchmarked!) differences between using "vanilla" Claude vs Claude + IDC skill vs Claude + IDC MCP.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Snippets from [this conversation](https://claude.ai/share/85b9d201-1f85-4492-9b9b-311bf98b09f5)

<img width="662" height="706" alt="image" src="https://github.com/user-attachments/assets/ca1b293f-ff98-4081-93be-1d678941ad77" />

<img width="670" height="721" alt="image" src="https://github.com/user-attachments/assets/3b1a8db0-ab9b-4f6b-b9c0-ad1ddd68a667" />

<img width="1134" height="639" alt="image" src="https://github.com/user-attachments/assets/83ba0f17-ed92-4066-85f2-cfcd0a4eeb7a" />


<img width="614" height="638" alt="image" src="https://github.com/user-attachments/assets/d9c93937-681e-4cbe-a4a6-649fce10f4db" />


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

