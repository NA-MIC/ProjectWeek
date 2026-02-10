---
layout: pw44-project

permalink: /:path/

project_title: claude-scientific-skill for Imaging Data Commons
category: AI
presenter_location: 

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Lalith Kumar Shiyam Sundar
  affiliation: LMU
  country: Germany

- name: Andras Lasso
  affiliation: Queen's U
  country: Canada

- name: Leonard Nürnberg
  affiliation: AIM Lab
  country: USA

- name: Michael Halle
  affiliation: SPL/BWH
  country: USA

- name: Justin Kirby
  affiliation: Frederick National Lab
  country: USA

- name: Leonard Nürnberg
  affiliation: AIM Lab
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Agent Skills are folders of instructions, scripts, and resources that agents can load when relevant to perform specialized tasks. [claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) introduces a development pattern to describe such skills for tools and resources usable in scientific research via a human-readable document, accompanied by code samples and recipes covering key functionality of the resource. Further, the company maintaining that repository makes the resulting skills accessible via MCP server, which could be connected with an agentic dev platform to improve quality of responses. The goal of this project is to add a new skill to the aforementioned repo to cover [Imaging Data Commons](https://learn.canceridc.dev/).



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. IDC skill is available 
2. Feedback and use cases collected from the community



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Analyze existing skills, understand best practices.
2. Develop the IDC skill.
3. Submit a PR with the IDC skill.
4. Compare responses of LLM with and without using the `claude-scientific-skills` MCP server.
5. Evaluate usability of the skill using the questions from IDC forum, or any other questions from the community.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

**It is best to use the standalong skill available at [https://github.com/ImagingDataCommons/idc-claude-skill](https://github.com/ImagingDataCommons/idc-claude-skill) to reduce LLM confusion!**

1. Set up Claude.AI with the `claude-scientific-skills` MCP server, experiment.
2. Started setting up the skill layout and deciding what should be covered.
3. Submitted PR with the initial skill: [claude-scientific-skills PR #35](https://github.com/K-Dense-AI/claude-scientific-skills/pull/35) (this has now been merged!)
4. Published standalone skill [https://github.com/ImagingDataCommons/idc-claude-skill](https://github.com/ImagingDataCommons/idc-claude-skill)
5. Discussed with Mike (who merged it with his own skill for IDC!); suggestions for improvement:
  * keep the main skill small, break out details into references
  * look into Mike's skill for managing skill versioning
  * need to investigate improvements to how IDC BigQuery parquet files are organized, noted in [https://github.com/ImagingDataCommons/etl_flow/issues/130](https://github.com/ImagingDataCommons/etl_flow/issues/130)
  * need to work on idc-index improvements: publish indices in GCS bucket ([idc-index #229](https://github.com/ImagingDataCommons/idc-index/issues/229)), add radiomics features table ([idc-index #230](https://github.com/ImagingDataCommons/idc-index/issues/229)), support search via remote parquet file ([idc-index #331](https://github.com/ImagingDataCommons/idc-index/issues/231).
  * it is a known issue that Claude struggles dealing with too many skills (incorrect skill matching etc)
6. Tested to address use case from Leo (how many CT scans does NLST have, how many of those are segmented with TotalSegmentator); lessons learned:
  * GPT-4o model is useless (eg, within the same response corrects its own mistake in one code snippet but not the other)!
  * GPT-5-codex was able to answer the questions correctly, supported by correct python code, from the first try
7. Discussed usage issues with K-Dense-AI devs (via slack)
  * they are aware of Claude struggling when number of skills grows over 300 (although in my experience, even 140+ seems to be too much already, at least when accessed via their MCP)
  * discussed issues related to managing skill independently vs as part of their repo
  * see [https://k-densecommunity.slack.com/archives/C09RL3JRBSB/p1769554262310839](https://k-densecommunity.slack.com/archives/C09RL3JRBSB/p1769554262310839) to join the discussion and learn more


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

* standalone skill: [https://github.com/ImagingDataCommons/idc-claude-skill](https://github.com/ImagingDataCommons/idc-claude-skill)
* [IDC forum post on finding fractional DICOM SEG in IDC](https://discourse.canceridc.dev/t/locating-fractional-dicom-segmentations-in-idc/776) put together using the developed skill

Coding agents learning materials:
* [agents.md](https://github.com/agentsmd/agents.md)
* [How to write a great agents.md: lessons from over 2,500 repositories](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
* [everything-claude-code](https://github.com/affaan-m/everything-claude-code)

Mike Halle's IDC skill (works with Claude Code and Claude platform/web/mobile)
 * [https://github.com/mhalle/idc-skill/](https://github.com/mhalle/idc-skill/)
 * [https://github.com/mhalle/idc-skill/releases/latest/download/idc-skill.skill](https://github.com/mhalle/idc-skill/releases/latest/download/idc-skill.skill)


