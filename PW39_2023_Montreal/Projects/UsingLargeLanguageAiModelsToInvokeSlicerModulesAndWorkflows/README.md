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

- name: Justin Johnson
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Theodore Aptekarev
  affiliation: Slicer Community
  country: Montenegro

- name: Rudolf Bumm
  affiliation: Kantonsspital Graubünden
  country: Switzerland

---

# Project Description

3D Slicer is built with a powerful core to load, transform, and store manage medical images and derived datasets. Slicer has a catalog of loadable extensions that assist with or automate task-specific workflows. Slicer's web API provides remote access to invoke many of the processing steps which are available through its very complete user interface.

The recent explosion of generative LLMs (large language models) from the AI community has demonstrated that these language models can, in some cases, translate task or problem descriptions into sequences of operations. Wouldn't it be powerful if 3D Slicer could be verbally instructed to perform operations or process datasets as requested? Theoretically, an embedded LLM could be trained on Slicer's modules, including under what circumstances the modules could be applied to transform a Slicer scene as needed to solve a problem presented by the user.

As one example, in Operating Theaters during surgical procedures, the Slicer user interface is hard or impossible to access due to sterility restrictions and other factors. It would be helpful if clinicians could control Slicer's functions through an alternative method than the interactive user interface. For example, "Let me see the lung lesions more clearly" could be translated into increased transparency of the lung segmentation and an orientation repositioning to make a lesion segmentation visible in-situ.

## Objective

The goal of this project proposal is to schedule a meeting during Project Week to discuss this idea, assess the level of interest in the Slicer community, discuss early technical approaches, and decide who might be interested in working together to seek funding or pursue this together. Both clinicians with a problem to solve and AI technicians are invited to participate.

## Approach and Plan

*   Schedule a meeting of interested parties during PW39
*   Discuss applicable existing open-source tools
*   Access the value to the community and define a plan to continue if this idea has merit
*   Possibly experiment with a proof of concept to connect to Slicer's API

## Progress and Next Steps

*   There is already work underway in our community with large language models.  Some of this work was demonstrated during our meeting this week.
*   We researched several open-source LLM repositories that allow connection to external APIs (Application Programming Interfaces), such as what Slicer has with the web interface
*   A productive meeting was held this week.  Rudolf showed how Slicer documentation could be used to fine tune a LLM as a question-answering system (see attached notebook shared on Slicer discourse).  Justin discussed the work on LLMs for IDC Query.  We discussed training LLMs on documentation will be easier in the short term, since changes in the Slicer state (change in the MRML tree after running a model) is hard to represent semantically. Theodore demonstrated how the browser extension of GPT4 gives better answers than the base model.
*   We achieved our goal of an initial meeting. During the meeting we discussed the "nearer term" goals of training an LLM to answer questions about 3D Slicer.  General invocation of Slicer modules in a workflow is farther off yet, since it is hard to define the semantics of Slicer modules. Therefore, the LLM wouldn't be able to reliably learn how to compose a workflow of Slicer API calls.
*   Thanks for everyone's contributions to this brainstorming session.  The interactive demonstrations were appreciated.


# Illustrations
The technology to train and inference large language models is changing.  Formerly, all data was in the permanent training set and used to directly train internal model weights.  Now documents are vectorized and used for searching during the inference process, as illustrated below. LLMs are developing to have APIs that can be used to incorporate these run-time searchable documents
![LLMTechStack](https://data.kitware.com/api/v1/file/648af6ae488633cbb1275d6a/download)

In addition to this trend, some LLMs (Gorilla, for example)) are designed to be able to search pre-processed API descriptions and then invoke external APIs during the inferencing step.  The photo below shows how external APIs to convert speech to text, generate images, etc. are available for the LLM to use during inferencing:

![GorillaUsesAPIs](https://data.kitware.com/api/v1/file/648af695488633cbb1275d67/download)


# Background and References

Hugging Face has a new API called "Agents" that is designed to use tools according to their descriptions of the I/O they handle. The Agent API puts together a workflow of tools to accomplish the users request. This is not exactly what I was thinking, as there are issues related to how to identify and return a changed MRML scene, but it inspired my thinking somewhat: <https://huggingface.co/docs/transformers/transformers_agents>.

**Gorilla:** Work that seems more directly towards a way to invoke Slicer modules via API is Gorilla, a LLAMA model fine-tuned to invoke external APIs to accomplish a requested task: <https://github.com/ShishirPatil/gorilla>. I just started reading the paper referenced on the repository site.

Thoughts on how the advent of LLMs can change our interface to complex software: <https://nickarner.com/notes/llm-powered-assistants-for-complex-interfaces-february-26-2023/>

Early work in the commmunity to automatically generate Imaging Data Commons BigQueries from free text prommpts: <https://discourse.canceridc.dev/t/text2cohort-a-new-llm-toolkit-to-query-idc-database-using-natural-language-queries/>.  This solution exhibits some hallucination, which has been addressed by the work Justin is engaged with.

**Using Slicer documentation as searchable content for GPT:** A link to Rudolf's ipython notebook that he presented during our meeting. Slicer docs were vectorized and used by the Langchain tools to assist GPT to provide better answers:
https://discourse.slicer.org/t/langchain-query-the-complete-3d-slicer-documentation-script-repository-and-faq-pdf-and-html-with-openai-llm/28746/6
