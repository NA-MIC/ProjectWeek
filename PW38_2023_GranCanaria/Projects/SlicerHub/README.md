Back to [Projects List](../../README.md#ProjectsList)

# 3DSlicerHub

## Key Investigators

- Rafael Nebot (ITC - Instituto Tecnológico de Canarias)
- Paula Moreno (ITC)
- Juan Ruiz (ULPGC)
- Idafen Santana (ULPGC)
- Steve Pieper

# Project Description

Multiuser approach to Slicer in a browser, based on [Slicer Docker](https://github.com/pieper/SlicerDockers)

### Main Features

- Browser based 3D Slicer using [Slicer Docker](https://github.com/pieper/SlicerDockers), similar to AWS AppStream.
- Per-user workspace, with persistent data and configuration.
- Session control, including quick URL sharing convenience, for educational and collaborative purposes.
- Authentication using OpenLDAP.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Use private clouds with GPU virtual machines.
2. Make the software configuration persistent after deleting the container.
3. Migrate from Docker+DockerCompose to Kubernetes+podman.
4. Set the size of 3DSlicer web window to fit the size of the user's screen and other novnc settings.
5. USB over IP + OpenIGTLink + Slicer in Docker.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. (o.1) GPU in Slicer Image: modify Slicer image to add nVidia drivers.
2. (o.1) GPU using separate MONAI Label images: analyze and design how to improve session manager to allow users to launch "pod-sets" (e.g. Slicer+MONAI, Slicer, Slicer+Orthanc, ...).
3. (o.2) Share current status of the feataure with people knowing about Slicer to fix the issue "saving config in laptop works, in VM it does not".
4. (o.3) Play with "kubernetes" package to familiariaze ourselves with the capabilities.
5. (o.3) Rewrite parts of 3d slicer hub accessing to containers to be able to work with "kubernetes" Python package.
6. (o.3) Start testing
7. (o.4) Gather information with participants knowing about websockify.
8. (o.5) Compile information about IGT protocol with participants in NAMIC.
9. (o.5) Modify design of 3dslicerhub architecture to enable IGT capabilities for Slicer containers

## Progress and Next Steps

<!-- Up[README.md](..%2README.md)date this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Slicer in Docker with GPU.
  - Approach: modify root image to one by nVidia.
    - Slicer works and detects the GPU.
      - But X11 server and the window manager do not start correctly
  - Next:
    - from AWS/GCE instance image build scripts (https://github.com/pieper/SlicerMachines) extract X11 config sections to prepare nVidia configuration.
    - modify to ensure the image works on computers without GPU.
    - fork original repository (https://github.com/pieper/SlicerDockers), prepare pull request.
    - use as base image for SlicerHub spawner.
2. Persistence of configuration
  - A bug in the preparation of Slicer.ini was detected and solved.
  - A custom Slicer image is built using a Slicer.ini containing a connection to the Orthanc server of the OpenDx28 platform.
3. Migration from Docker Compose to Kubernetes
  - Study of Kubernetes. Two "technology scope" adjustments:
    - "podman" not ready for production, Docker used (also better for images with CUDA support).
    - Use of "kubectl" instead of Python package (direct REST calls).
  - Refactor current 3dslicerhub to enable switching between Container Orchestrator managers: baseline implementation, new implementation.
  - Efforts adapting for K8s concepts: because of the different scopes of Docker Compose and Kubernetes, concepts do not match exactly.
  - Next:
    - Find ways, using kubectl and resource files to (see diagram below):
      - Deploy NGINX service, using a volume containing “nginx.conf”.
      - Deploy SlicerHub service, using the same volume.
      - Execute "kubectl" from SlicerHub service to access its own K8s cluster.
    - Continue adaptation of Container Orchestrator implementation for Kubernetes.
    - Test locally.
    - Deploy at Teide VMs.

# Illustrations

<img alt="Docker Compose architecture" src="dc_architecture.png" width="400"/>

<img alt="K8s architecture" src="k8s_architecture.png" width="434"/>

<img alt="Docker Compose eschema" src="3dslicerhub_esquema_2.png" width="400"/>


<img alt="Docker Compose eschema" src="3dslicerhub_esquema.png" width="500"/>

## Screenshots

<img alt="SlicerHub Landing Page" src="main.png" width="400" />
-->
<img alt="SlicerHub login" src="login.png" width="200" />
-->
<img alt="SlicerHub user page" src="session_manager.png" width="200" />
-->
<img alt="3DSlicer" src="3dslicer.png" width="400" />






# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
