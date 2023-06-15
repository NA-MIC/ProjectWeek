---
layout: pw39-project

permalink: /:path/

project_title: SystoleOS
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

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Over a span of more than ten years, 3D Slicer has paved the way for cutting-edge biomedical research. Its unprecedented success is pushing the frontiers of research, leading numerous research groups and corporations to recognize 3D Slicer as a credible software for designing medical devices. These devices not only have the potential to support routine clinical workflows but may also evolve into marketable products. Although 3D Slicer's development has been largely research-focused, its modular architecture fosters the creation of industrial prototypes.

Systole OS envisions a harmonious integration of 3D Slicer and its associated software, such as the Plus Toolkit, MONAI Label, and others, within a freely accessible, open-source operating system based on GNU/Linux. This aims to facilitate the development and deployment of medical devices.

![](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SystoleOS/systole.png)

The following are key features we aim to leverage with Systole OS:

## Objective

1.  **Updating Packages:** We are planning to ensure the timely update and maintenance of existing packages, targeting specifically the release Slicer-5.3.0.

2.  **Integration and Testing Infrastructure:** Develop a robust infrastructure that supports seamless integration and rigorous testing to maintain the highest quality standards.

3.  **Generation of Containers and VMs:** Establish a systematic approach for generating containers and Virtual Machines (VMs) that can effectively support both development and testing processes.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  **Package Assessment:** Review the status of existing packages and identify necessary updates for the release Slicer-5.3.0.

2.  **Update Planning:** Develop a plan and timeline for implementing the necessary updates.

3.  **Update Implementation:** Carry out the plan to update packages in line with the established timeline.

4.  **Kubernetes Infrastructure Setup:** Begin the process of setting up a Kubernetes-based infrastructure to support our integration and testing needs.

5.  **Testing Protocol Development:** With the Kubernetes infrastructure ready, establish systematic protocols for integration and testing to ensure high quality standards.

6.  **Container and VM Generation:** Implement a systematic approach for creating containers and Virtual Machines (VMs) for development and testing, ensuring this approach is scalable as needed.

## Progress and Next Steps

🚀 Here is an overview of our progress so far:

1. 🔜 We have partially completed a Kubernetes infrastructure to build containers and virtual machines with pre-installed Systole. This infrastructure is based on [ArgoCD](https://argoproj.github.io/argo-cd/), [ArgoWorkflow](https://argoproj.github.io/argo-workflows/), and [Bitnami Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets).
2. We are currently in the planning phase for updating the packages to target the release Slicer-5.3.0.
3. We are continuing the setup process for the Kubernetes infrastructure to support integration and testing needs.

## Next Steps

Moving forward, our next steps include:

1. Implementing the necessary updates to the packages in line with our plan and timeline.
2. Finalizing the setup of the Kubernetes infrastructure for building containers and virtual machines.
3. Initiating testing and production of SystoleOS containers and virtual machines for use by other researchers.

## Illustrations

*No response*

# Background and References

- [SystoleOS Gentoo Overlay Repository](https://github.com/SystoleOS/gentoo-overlay): Repository for the SystoleOS Gentoo overlay.
- [SystoleOS Infrastructure Repository](https://github.com/SystoleOS/infrastructure): Repository for the SystoleOS infrastructure project.
- [SystoleOS Workflows Repository](https://github.com/SystoleOS/workflows): Repository for the SystoleOS workflows project.

