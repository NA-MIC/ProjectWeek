---
layout: pw39-project

permalink: /:path/

project_title: Using large language AI models to invoke Slicer modules and workflows
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Curtis Lisle
  affiliation: KnowledgeVis
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

- name: Andrey Federov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

3D Slicer is built with a powerful core to load, transform, and store manage medical images and derived datasets. Slicer has a catalog of loadable extensions that assist with or automate task-specific workflows. Slicer's web API provides remote access to invoke many of the processing steps which are available through its very complete user interface.

The recent explosion of generative LLMs (large language models) from the AI community has demonstrated that these language models can, in some cases, translate task or problem descriptions into sequences of operations. Wouldn't it be powerful if 3D Slicer could be verbally instructed to perform operations or process datasets as requested? Theoretically, an embedded LLM could be trained on Slicer's modules, including under what circumstances the modules could be applied to transform a Slicer scene as needed to solve a problem presented by the user.

As one example, in Operating Theaters during surgical procedures, the Slicer user interface is hard or impossible to access due to sterility restrictions and other factors. It would be helpful if clinicians could control Slicer's functions through an alternative method than the interactive user interface. For example, "Let me see the lung lesions more clearly" could be translated into increased transparency of the lung segmentation and an orientation repositioning to make a lesion segmentation visible in-situ.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

A goal of this project proposal is to schedule a meeting during Project Week to discuss this idea, assess the level of interest in the Slicer community, discuss early technical approaches, and decide who might be interested in working together to seek funding to pursue this together. Both clinicians with a problem to solve and AI technicians are invited to participate.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

*   Schedule a meeting of interested parties during PW39
*   Discuss applicable existing open-source tools
*   Access the value to the community and define a plan to continue if this idea has merit
*   Possibly experiment with a proof of concept to connect to Slicer's API

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

*   Researched several open-source LLM repositories that allow connection to external APIs (Application Programming Interfaces), such as what Slicer has with the web interface
*   Productive meeting on Tuesday.  Rudolf Bumm showed how Slicer documentation could be used to fine tune a LLM as a question-answering system (see attached notebook shared on Slicer discourse).  Justin discussed the work on LLMs for IDC Query.  We discussed the documentation will be easier in the short term, since changes in the Slicer state (change in the MRML tree after running a model) is hard to represent semantically. Theodore demonstrated how the browser extension of GPT4 gives better answers than the base model. 

 
# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Hugging Face has a new API called "Agents" that is designed to use tools according to their descriptions of the I/O they handle. The Agent API puts together a workflow of tools to accomplish the users request. This is not exactly what I was thinking, as there are issues related to how to identify and return a changed MRML scene, but it inspired my thinking somewhat: <https://huggingface.co/docs/transformers/transformers_agents>.

Work that seems more directly towards a way to invoke Slicer modules via API is Gorilla, a LLAMA model fine-tuned to invoke external APIs to accomplish a requested task: <https://github.com/ShishirPatil/gorilla>. I just started reading the paper referenced on the repository site.

Here's a related post: <https://nickarner.com/notes/llm-powered-assistants-for-complex-interfaces-february-26-2023/>

Somewhat related development applied to selection of data in IDC using LLM: <https://discourse.canceridc.dev/t/text2cohort-a-new-llm-toolkit-to-query-idc-database-using-natural-language-queries/>.

(link to Rudolf's ipython notebook discussion)
https://discourse.slicer.org/t/langchain-query-the-complete-3d-slicer-documentation-script-repository-and-faq-pdf-and-html-with-openai-llm/28746/6
