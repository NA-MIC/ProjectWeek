Back to [Projects List](../../README.md#ProjectsList)

# Simple deployment of OHIF DICOM Viewer and Dcm4chee within Kubernetes

## Key Investigators

- Jonas Scherer (DKFZ)
- Andrey Fedorov (BWH)
- Erik Ziegler (Radical Imaging) 

# Project Description

The aim of this project is to provide a simple environment in which a PACS (Dcm4chee) and the OHIF Dicom Viewer interact with each other. The whole system should be build of Docker containers inside an Kubernetes cluster.


## Objective

1. Working Kubernetes deployment files for all components.
2. OHIF <-> PACS communication: Show dicoms from the pacs in OHIF
3. User authentication
5. A package for easy installation

## Approach and Plan

1. Setup Minikube with infrastructure components (Calico,Traefik...) 
2. Deploy OHIF and DCM4CHEe
3. Add authentication with Keycloak and Security Proxy
4. Create Helm chart for easy installation
5. Testing

## Progress and Next Steps

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

Info websites:

[OHIF Dicom Viwer](https://docs.ohif.org/)
[DCM4Chee](https://github.com/dcm4che/dcm4chee-arc-light)
[Keycloak](https://www.keycloak.org/about.html)
[Security Proxy](https://www.keycloak.org/docs/3.3/server_installation/topics/proxy.html)

[Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
[Minikube](https://kubernetes.io/docs/setup/minikube/)
[Helm](https://helm.sh/)
