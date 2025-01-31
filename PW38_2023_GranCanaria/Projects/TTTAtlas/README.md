Back to [Projects List](../../README.md#ProjectsList)

# Development of Anatomy Atlases and Training Tools with 3D Slicer and Open Source Software

## Key Investigators

- Juan Ruiz (ULPGC)
- Idafen Santana (ULPGC)
- Mario Monzón (ULPGC)
- Aday Melián (ULPGC)
- Miguel Ángel Rodríguez (ULPGC)
- Pablo Castellano (ULPGC)
- Jose Carlos Mateo (ULPGC)
- Nayra Pumar
- Babacar Diao
- Christine Sokhna
- Magate Gueye
- Charles Diem
- Khedijetou Vilaly
- Bella Konan

# Project Description

With the help of 3D Slicer and open source software, anatomy atlases and training tools are becoming more accessible than ever. These tools allow medical professionals to gain a better understanding of the human body, from its organs and muscles to its bones and tissues. They also provide an opportunity for medical students to practice their skills in a virtual environment without risking any harm to real patients.

This project aims to provide the tools and knowledge for generating a comprehensive set of atlasses. Additionally, it will enable the development of innovative tools such as augmented reality (AR) applications and virtual reality (VR) simulations to further enhance the learning experience.

## Objectives

1. Objective A: Identify all resources and current state of open source atlases content so far and analyze the strength of Slicer 3D on this subject.

2. Objective B: Select different open source atlas (OpenAnatomy and z-Anatomy as starting points) and define common needs for atlas creation.

3. Objective C: Check and conclude what implementations or changes could improve our Virtual Dissection project and what is our best bet to use VR and AR with human anatomy.

## Approach and Plan

1. Research the state of the art of open source atlases meeting and discussing with previous atlas workers and get the current state and needs from different points of view.

2. Recopilate, test and identify open source atlases, how they work and what features and options they provide.

3. Check the inclusion of Slicer3D into the pipeline of open source atlases created for web access or standalone apps

4. Identify potential features from the atlases that can be used or improved with little effort: VR, AR, Collab...

## Progress and Next Steps

1. Attend to conference by Michael Halle about Open Anatomy atlases and the [Open ABrowser](https://github.com/mhalle/oabrowser) open source project to know more about it
    - Dedicated implementation of a WebGL project for easy access and user interactions
    - Import directly Slicer3D content (MRML) to render and use on every devices through web
    - Talked about the current state, next steps and challenges faced

2. Meet & discusions with Nayra Pumar, researcher who has already work in affordable custom atlases [PAPER: Affordable Custom Three-Dimensional Anatomy Atlases](https://ieeexplore.ieee.org/document/9033044)


3. Meet & discussion with [Babacar Diao](https://mt4sd.ulpgc.es/es/equipo/instituciones/babacar-diao/), physician who has created and used them as learning tools:
    - They work with Slicer3D for making the creation of 3D Models from real world CT images, segmentation and they use Slicer software as the atlas itself.

    - This is an affordable way of create and apply on student classes realistic atlases based on real life humans

    - The drawback of this way of using atlas is that it needs a little formation in the users on Slicer3D usage

    - In the other hand this allows students to be able to improve and make better atlases from the previous work

    - As conclussion, he has found out by several classes and teaching sessions that the students classifications improves while using atlases as learning tools comparing to others that don't use it

4. Technical deconstruction of an Atlas. We have divided the concept of digital atlas into these features/needs:
    - 3D Content provider
        - 3D Models ready or adaptable to be used into atlas

    - Content adaptation for the needs of the project
        -  Customized distribution (Taxonomy)
            - How do we divide/distribute the anatomy? Ex: We might need the full heart object but we have it divided into all its parts in small pieces. There is several ways to divide an object

        - 3D Content adapter (For custom use in apps)
            - 3D objects merge and retopolization in order to use it into the atlases fulfilling all the requisites and hardware specs.

    - Viewer (Engine/Renderer)
        - The software used to render the final atlases and add features for users work with the anatomy

    - Languages
        - Depending on the use we could have different language options or we may need only the native language

    - Data validation
        - If we are working with anatomic tools for learning, we cannot allow bad information, we need a system to check every model and pieces in the human body is well named and well modeled.

        - Using Slicer3D we have the certain that there is no wrong content because it comes directly from a human, not 3d modeled. The errors could come from the segmentation part, but we keep the editable capabilities.

6. We made a research of open source atlases and related content to anatomic learning tools and we have recopilated/developed this tools for each layer:
    - 3D Contents provider
        - [Slicer3D](https://www.slicer.org/)
        - [Open anatomy](https://www.openanatomy.org/)
        - [z-Anatomy](https://www.z-anatomy.com/)
        - [BodyParts](https://lifesciencedb.jp/bp3d/)

    - Content adapter
        - [BodyParts3D (Anatomography)](https://lifesciencedb.jp/bp3d/)

    - Languages
        - [Terminologia Anatomica](https://ta2viewer.openanatomy.org/)
        - [Wikipedia]()
        - Custom medical translations (Depends on medic profile for each iteration)

    - Content customized distribution (Taxonomy)
        - [BodyParts3D (Anatomography)](https://lifesciencedb.jp/bp3d/)
        - We have already created a little pipeline to reorder and merge 3d pieces of the anatomy from different systems into bigger objects more handy

    - Viewer (Engine/Renderer)
        - [Online 3D Viewer](https://github.com/kovacsv/Online3DViewer) - GLTF renderer
        - [OABrowser](https://github.com/mhalle/oabrowser) - Uses Slicer3D Content
        - We created some tests using z-Anatomy full body to check the power required on web rendering from mobile devices. (Image #4)

7. We have been working last year on creating atlas and human based apps using Unity3D as learning tools.
    - We have identified that the challenges we have faced are common challenges in this kind of content
    - We have created some helping software to aid us to modify and adapt the anatomy for our needs using web technologies:
        - Anatomic Tree Adapter: Web application to reorganize all z-Anatomy models as we need into our custom apps. (Image #3)

        - Human Viewer: Web application to render all z-Anatomy body to check the performance of Three.JS technology from mobile devices. (Image #4)

8. Conclusions and next steps:
    - When we started creating atlases, we decided to use Slicer with the OpenAnatomy only as exporter of all content for the use into Unity3D and Three.JS apps.
    - We have found out during this week that Slicer3D is more useful than we valued on the early stages of our projects:
        - It can be used as Atlas itself for teaching anatomy with succesful cases as we talked to Babacar Diao
        - It can create human anatomy models by CT segmentations and render them, then edit and polish to iterate and get the most realistic models of humans and then easily export to other engines or apps.
        - VR and AR experiences are features supported by Slicer3D natively
        - The amazing community behind it on continuous development makes it a reliable option to work in the future
    - We will go deep into the previous works on atlases to improve our dissection project (AVRIR) with everything we have learned during the PW38

# Illustrations
- Image #1 - Meeting with Babacar Diao in NAMIC Project week 38
![MeetingBabacar](https://user-images.githubusercontent.com/5611348/216622689-93eee25a-c7d1-44fc-bd5a-490e1379b417.jpeg)

- Image #3 - Anatomic Tree Adapter for readapt human anatomy
<img width="1506" alt="AnatomicTree" src="https://user-images.githubusercontent.com/5611348/216607199-7e4759cd-b16b-4aa8-9e61-09c4f70f2130.png">

- Image #4 - Human Viewer - Three.JS performance test
<img width="1512" alt="WebHumanViewer" src="https://user-images.githubusercontent.com/5611348/216622739-12c0afa8-6df4-43bf-8833-5499042bc608.png">

- Image #5 - Segmentation by Babacar Diao
<img width="447" alt="Capture d’eěcran 2023-02-03 aĚ 13 45 07" src="https://user-images.githubusercontent.com/5611348/216623961-4f78d948-266d-4c76-a896-8031e14919db.png">

- Image #6 - Segmentation by Babacar Diao
<img width="458" alt="Capture d’eěcran 2023-02-03 aĚ 13 45 20" src="https://user-images.githubusercontent.com/5611348/216623977-a06ac15e-e7b5-4658-b356-ca36db389cb6.png">

# Background and References
- Last two years we have been working with anatomic 3d models to create educative experiences like VRAINS (VR Anatomic atlas - ULPGC) and AVRIR (Collaborative VR dissection - ULPGC) using OpenAnatomy and z-Anatomy content imported into Unity3D.

- We have found several challenges with the adaptation of this kind of content for our objectives (Excess of polygons for target devices, too detailed anatomic distribution, language localization...).

- [The impacts of three-dimensional anatomical atlas on learning anatomy](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6449593/)

- [Commercial anatomic dissection app](https://www.medicalholodeck.com/en/)
