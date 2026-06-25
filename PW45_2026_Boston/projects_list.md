# Project Week# 45, June 22-26, 2026 @ MIT, Boston, USA

1. **[AI-Agent for SlicerAutomatedDentalTools](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiAgentForSlicerautomateddentaltools/)** (Paul Dumont @ University of North Carolina at Chapel Hill, +) ([DCBIA-OrthoLab/SlicerAutomatedDentalTools](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiAgentForSlicerautomateddentaltools/"><img src="https://github.com/user-attachments/assets/32b13db1-2e45-4067-8fd6-1d18a84fd662" style="max-width:480px;width:100%"></a>

**Problem**: The Slicer Automated Dental Tools extension provides robust craniofacial analysis, but complex module selection and parameter tuning create a steep learning curve for users.

**Solution**: This project introduces an AI Agent and chatbot UI integrated into 3D Slicer to streamline the workflow. By allowing drag-and-drop inputs and natural language prompts, users can easily request complex tasks (e.g., segmentation, landmarking, or orientation on CBCT/IOS). The agent autonomously translates these requests into actions, selecting the right tools and automatically configuring the parameters to execute the workflow.


2. **[AI driven interface for SlicerTMS](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiDrivenInterfaceForSlicertms/)** (SangHyuk Kim @ BWH & UMass Boston, +) (no github repo yet)

SlicerTMS is a 3DSlicer module for patient-specific transcranial stimulation. It integrates several functions, including neuronavigation, electric field modeling, real-time EEG streaming and recording, and TMS control. These functions involve a complex user interface, and some tasks, such as neuronavigation registration, may need more than one user. To simplify the interface and improve the user experience, we will develop a new version leveraging LLM models and Slicer AI Agent tools. Specifically, we will eliminate LLM hallucinations at the infrastructure level by executing medical software APIs through human-verified Markdown Cookbooks and local Vector RAG technologies. Furthermore, the system establishes a next-generation intelligent environment featuring a self-evolving Auto-Correction engine that tracks and learns directly from clinician adjustment patterns, all while seamlessly supporting the trusted clinical interfaces medical professionals already use.


3. **[AI model development for lung ultrasound analysis](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiModelDevelopmentForLungUltrasoundAnalysis/)** (Alexandre Banks Gadbois @ BWH, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiModelDevelopmentForLungUltrasoundAnalysis/"><img src="https://github.com/user-attachments/assets/e2c235c9-7abe-4a63-a6a0-512143757eb2" style="max-width:480px;width:100%"></a>

One of the primary indicators of acute heart failure is the presence of pulmonary congestion. To detect fluid build up quickly in the emergency room, lung ultrasound exams are taken of the patient. Clinicians look for hyperechoic artifacts (B-lines) that appear in the image, where the more they see the more congested the patient is. 

Unfortunately, manual detection of these B-lines is difficult due to the image quality, which depends on the type of transducer and the expertise of the clinician. Therefore, AI models have started to be developed to quickly detect these B-lines. Our group, over the past few years, has developed multiple methods [1], [2], [3]. One of the drawbacks though, is that existing models do not compute the pleural percentage, the ratio of the B-line sectors to the pleural line sectors, which is strongly associated with extravascular lung water and consistent with other semi-quantitative clinical scores [4]. 

Therefore, we have started to develop detection models to automatically find pleural lines and B-lines and compute the percentage pleura. Our goal for this project week is to train and validate keypoint detection models such as ViTPose++, [5], and HRNet with UDP, [6], and talk to clinicians about the performance.


4. **[Automatic segmentation of priority collections from Imaging Data Commons](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AutomaticSegmentationOfPriorityCollectionsFromImagingDataCommons/)** (Kyle Sunderland @ Queen's, +) ([ENHANCE-PET/MOOSE](https://github.com/ENHANCE-PET/MOOSE))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AutomaticSegmentationOfPriorityCollectionsFromImagingDataCommons/"><img src="https://github.com/user-attachments/assets/5a146049-09b6-4aea-8298-4f8d79b7e5eb" style="max-width:480px;width:100%"></a>

**Questions? Want to participate remotely? Join our project [Discord channel](https://discord.gg/TTFGUYGdsZ)!**

The goal of this project is to further increase availability of anatomic segmentations and accompanying radiomics features for the images available in Imaging Data Commons.


5. **[Cast interface extension for  Slim and 3D Slicer: Hub,  Resource Servers and Image Display client.](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/CastInterfaceModuleFor3DSlicerServiceProvidersImageDisplayClientAndHub/)** (Martin Bellehumeur @ Radical Imaging, +) ([mbellehumeur/SlicerCastInterface](https://github.com/mbellehumeur/SlicerCastInterface))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/CastInterfaceModuleFor3DSlicerServiceProvidersImageDisplayClientAndHub/"><img src="https://github.com/user-attachments/assets/76dbe891-9ef5-49c9-839c-827d4a13cc88" style="max-width:480px;width:100%"></a>

Try the new “Cast Interface” 3D slicer extension to integrate different AI engines with VolView and OHIF without a DICOM server.  

Cast is  an offshoot of FHIRcast (<https://fhircast.hl7.org/>)and is focused on desktop integration workflows for healthcare providers and researchers. It provides a secure event messaging infrastructure using a hub with websocket subscriptions.

The project also integrated with a new IDC MCP server to search for studies in the Imaging Data Commons repository and added cast to the Slim whole slide imaging viewer, VolView, OHIF and the 3D slicer viewer. 

The repository for the slicer extension is here: https://github.com/mbellehumeur/SlicerCastInterface


6. **[Clinical Information Extraction via Locally Fine-Tuned LLMs](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ClinicalInformationExtractionViaLocallyFineTunedLlms/)** (Paul Dumont @ University of North Carolina at Chapel Hill, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ClinicalInformationExtractionViaLocallyFineTunedLlms/"><img src="https://github.com/user-attachments/assets/ab930885-cd8a-4af6-9f1b-c9d12d150dcb" style="max-width:480px;width:100%"></a>

This project develops a privacy-preserving extraction framework using locally deployable open-weight LLMs to structure dense clinical narratives. We aim to bypass expensive and non-private cloud APIs by fine-tuning models to extract Common Data Elements (CDEs) from Orthodontic and TMJ progress notes entirely offline.


7. **[Exploring Ultrasound Multi-frame Image Storage Structured Report support for Slicer/OHIF](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExploringUltrasoundMultiFrameImageStorageStructuredReportSupportForSlicerOhif/)** (Deepa Krishnaswamy @ BWH, +) ([SlicerUltrasound/SlicerUltrasound](https://github.com/SlicerUltrasound/SlicerUltrasound))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExploringUltrasoundMultiFrameImageStorageStructuredReportSupportForSlicerOhif/"><img src="https://github.com/user-attachments/assets/6574e377-dc30-4454-9938-78fb3db31f39" style="max-width:480px;width:100%"></a>

Our team has built a 3D Slicer extension for ultrasound anonymization, annotation, and adjudication (https://github.com/SlicerUltrasound/SlicerUltrasound). We are currently trying to port the functionality of these tools to OHIF in order to make the processing more streamlined for clinicians and avoid the downloading of additional tools. 

However, we currently store all of our annotations as JSON. This can be problematic as JSON can be prone to misinterpretation; we had to write specialized software to load these annotations into Slicer, and we are missing much of the metadata to associate the file with the referenced image. 

In this project, I want to see if using DICOM Structured Reports (SR) will help our use case. Having our files as SRs would help us to utilize the cloud and retain all important metadata. But it might also make processing more complicated. Therefore, the goal of this week is to see how much effort is needed to add functionality to Slicer/OHIF for Ultrasound Multi-frame Image Storage.


8. **[Extracting deep learning features from CT images of the thoracic region for lung cancer](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExtractingDeepLearningFeaturesFromCtImagesOfTheThoracicRegionForLungCancerApplications/)** (Renzo Phellan Aro @ Lunenfeld-Tanenbaum Research Institute, +) ([AIM-Harvard/TumorImagingBench](https://github.com/AIM-Harvard/TumorImagingBench))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExtractingDeepLearningFeaturesFromCtImagesOfTheThoracicRegionForLungCancerApplications/"><img src="https://github.com/user-attachments/assets/5fd64d0e-fcba-4efd-90b5-b508bec70fc5" style="max-width:480px;width:100%"></a>

This project focuses on using existing foundational deep learning models in 3D Slicer to process CT images of the thoracic region. The objective is to extract features that can be used for lung cancer applications, such as classification, screening, and risk prediction.


9. **[Fan mask and OCR bound box editing for OHIF-based DICOM De-Identification verification](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/FanMaskAndOcrBoundBoxEditingForOhifBasedDicomDeIdentificationVerificationMode/)** (Dave Dinh @ BWH, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/FanMaskAndOcrBoundBoxEditingForOhifBasedDicomDeIdentificationVerificationMode/"><img src="https://github.com/user-attachments/assets/b95e956f-f422-494c-8c52-91b3d1fbd174" style="max-width:480px;width:100%"></a>

Optimal DICOM de-identification for downstream research requires balancing removal and retention. We must scrub embedded PHI in both tags and pixels while preserving valuable non-PHI metadata (e.g., scan settings like depth). Even with both addressed, human review is still needed to catch misses.

We’re building a closed-loop system with two components:
- an automated pipeline that scrubs DICOM tags (PS3.15 with configurable overrides), masks pixel PHI by manufacturer, extracts non-PHI pixel data, and produces deterministic, reproducible outputs
- an OHIF-based reviewer for human verification. Each review records passes, failures, and false positives/misses, which feed back as rule updates so errors don’t recur.

The pipeline handles most de-identification automatically, but reviewers still face significant cognitive load when inspecting every metadata diff, OCR-flagged region, and fan crop. The OHIF mode currently surfaces areas in the DICOM metadata that require verification based on predefined rules but reviewers also need tools to edit PHI masks, OCR bounding boxes for non-PHI extraction, and fan geometry for fan-only pixel extraction.


10. **[Fine-tuning SimCortex Using Manually Corrected Cortical Annotations](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/FineTuningSimcortexUsingManuallyCorrectedCorticalAnnotations/)** (Kaveh Moradkhani @ École de technologie supérieure, +) ([Neuro-iX/SimCortex](https://github.com/Neuro-iX/SimCortex))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/FineTuningSimcortexUsingManuallyCorrectedCorticalAnnotations/"><img src="https://github.com/user-attachments/assets/d3d4cd33-8c13-46a2-a59a-b5af894be9e8" style="max-width:480px;width:100%"></a>

SimCortex v2 is a deep learning pipeline for cortical surface reconstruction from brain MRI. In this project, we will fine-tune the existing SimCortex v2 model using manually corrected segmentations and cortical surfaces.

The goal is to evaluate whether manual supervision can improve the reconstructed white and pial surfaces compared with the current SimCortex v2 baseline.

As a practical outcome, we will also prepare a 3D Slicer extension for SimCortex. The extension runs SimCortex through Docker from a native T1-weighted MRI and loads the reconstructed cortical surfaces back into Slicer for visualization.


11. **[Image visualization in Google Colab](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ImageVisualizationInGoogleColab/)** (Andrey Fedorov @ BWH, +) ([KitwareMedical/trame-slicer](https://github.com/KitwareMedical/trame-slicer))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ImageVisualizationInGoogleColab/"><img src="https://github.com/user-attachments/assets/dbfdd42e-8f9c-4b62-a98b-b0e0e4ba99c4" style="max-width:480px;width:100%"></a>

In this project we will experiment with different approaches to implementing 3d visualization of radiology images and overlaying segmentations in [Google Colab](https://colab.research.google.com/). The primary motivation for this project is to support visualization of images from Imaging Data Commons along with user-generated analysis results in Google Colab, which has zero prereqisites for installing software on user's computer.


12. **[Improving QC protocols for AMP SCZ Clinical and MRI Data](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ImprovingQcProtocolsForAmpSczClinicalAndMriData/)** (Sylvain Bouix @ école de technologie supérieure, +) (no github repo yet)

We will be adding anomaly detection algorithms to clinical data and MRI data in the AMP SCZ project.


13. **[Integrating a Parallel Robot into SlicerROS2 with MoveIt-Based Planning for Image-Guided](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/IntegratingAParallelRobotIntoSlicerros2WithMoveitBasedPlanningForImageGuidedNeedleProcedures/)** (Mariana Bernardes @ BWH, +) ([rosmed/slicer_ros2_module](https://github.com/rosmed/slicer_ros2_module))

This project aims to integrate a Stewart-platform parallel robot into the [SlicerROS2](https://github.com/rosmed/slicer_ros2_module) ecosystem for image-guided biopsy and ablation procedures. The robot, developed by collaborator Dr. Joonho Seo at KIMM, will be controlled using [ROS2](https://www.ros.org/) and and can align a needle or ablation probe based on patient intraoperative imaging. By integrating robot visualization and motion-planning preview into the 3D Slicer interface, we aim to allow the user to visualize the planned robot motion and probe trajectory before execution. This integration will also provide a foundation for future closed-loop robotic control using medical imaging feedback.


14. **[Interactive Workflow Replay and Step-Back Navigation for Slicer Agent](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/InteractiveWorkflowReplayAndStepBackNavigationForSlicerAgent/)** (Puxun Tu @ Brigham and Women's Hospital, +) ([puxuntu/Slicer_agent](https://github.com/puxuntu/Slicer_agent))

The Slicer AI Agent is a scripted extension that lets users use natural-language instructions and have the system autonomously generate, validate, and execute Python code within the 3D Slicer scene. For complex multi-step operations, such as extension-specific surgical planning workflows, the agent enters a deterministic workflow runtime that executes a sequence of predefined steps (automated code execution, interactive 3D mark-up placement, user choices, and branching logic) with a progress bar tracking completion.

Currently this progress bar is forward-only: once a step completes, there is no way to go back, inspect what happened at an earlier step, or modify a previous choice and re-run the downstream pipeline. This limits both transparency (users cannot easily understand what was done and why) and usability (a wrong choice means restarting the entire workflow from scratch).

We propose adding a workflow replay timeline that records per-step state and allows users to go back to any completed step, inspect the code and choices that were made, optionally modify parameters, and re-execute the workflow from that point onward.


15. **[Testing Local LLMs for Agentic Tasks via Slicer Skills](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/LocalAiCopilotForSlicerMedicalImagingWorkflows/)** (Paul Dumont @ University of North Carolina at Chapel Hill, +) ([jumbojing/slicerClaw](https://github.com/jumbojing/slicerClaw))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/LocalAiCopilotForSlicerMedicalImagingWorkflows/"><img src="https://github.com/user-attachments/assets/a51aecf1-e9fe-48a1-985c-b1b0caa23a0a" style="max-width:480px;width:100%"></a>

This project will attempt to build a free, confidential, and fully local alternative to cloud-based LLMs for medical imaging workflows. To bypass expensive and non-private cloud models, we will attempt to create an AI Agent for 3D Slicer designed to run entirely offline. We aim to enable private models powered by Ollama to accurately query the Slicer API without relying on external cloud infrastructure.


16. **[Low-Cost Tracked 3D Ultrasound Reconstruction with GE Vscan Air and NousNav](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/LowCostTracked3DUltrasoundReconstructionWithGeVscanAirAndNousnav/)** (Amirali Azimi @ Brigham and Women's Hospital, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/LowCostTracked3DUltrasoundReconstructionWithGeVscanAirAndNousnav/"><img src="https://github.com/user-attachments/assets/5172f187-588a-4f4a-872a-edb60e255742" style="max-width:480px;width:100%"></a>

Intraoperative brain shift reduces the accuracy of neuronavigation systems that rely on preoperative imaging. Updated intraoperative imaging can help restore navigation accuracy, but technologies such as intraoperative MRI and conventional cart-based ultrasound systems are not available in many surgical environments.

We are developing a lower-cost workflow for tracked three-dimensional ultrasound reconstruction using the wireless GE Vscan Air CL ultrasound probe and NousNav, an open-source neuronavigation platform implemented in 3D Slicer. During an ultrasound sweep, NousNav uses an optical tracking system to record the position and orientation of both the ultrasound probe and a patient reference frame. The goal is to associate each two-dimensional ultrasound frame with the corresponding tracking transform, position the frames correctly in three-dimensional space, and reconstruct them as a navigable three-dimensional ultrasound volume.

A proof-of-concept reconstruction has already been performed using ultrasound images acquired through the Vscan Air mobile application and tracking data transmitted using the PLUS Toolkit and SlicerIGT. However, the current workflow relies on screen-recorded ultrasound video, which reduces image quality and makes precise synchronization between ultrasound frames and tracking data difficult. Several additional components remain unresolved, including calibration of the ultrasound image plane relative to the tracked probe, registration of the reconstructed ultrasound volume to the patient coordinate system using the tracked reference frame, and integration of the current Python-based NIfTI reconstruction process directly into the 3D Slicer environment.

During Project Week, we aim to develop and evaluate a more reliable and integrated workflow for ultrasound image acquisition, timestamp synchronization, probe calibration, patient registration, three-dimensional reconstruction, and visualization within 3D Slicer and the broader open-source image-guided therapy ecosystem.


17. **[MR2CBCT: Restoring and Extending Automated CBCT-MRI Registration for TMJ Analysis](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Mr2CbctRestoringAndExtendingAutomatedCbctMriRegistrationForTmjAnalysis/)** (Eduardo Duarte Caleme @ University of North Carolina, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Mr2CbctRestoringAndExtendingAutomatedCbctMriRegistrationForTmjAnalysis/"><img src="https://github.com/user-attachments/assets/6ff6b1e8-a796-4fd8-8bec-5be64b6bd389" style="max-width:480px;width:100%"></a>

MRI-to-CBCT registration remains a pressing challenge in medical imaging. Simultaneous visualization of hard and soft tissue structures benefits both clinicians and patients in the diagnosis of temporomandibular degenerative joint disease. Challenges remain in accurately registering these two modalities due to differences in intensity distributions that complicate mutual information optimization, as well as the necessity for initial manual alignment, which can prove unintuitive and challenging for clinicians using current 3D Slicer tools.


18. **[Multi-material meshing with Slicer for orbital fracture repair FEM simulation](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/MultiMaterialMeshingWithSlicerForOrbitalFractureRepairFemSimulation/)** (Chi Zhang @ Texas A&M College of Dentistry, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/MultiMaterialMeshingWithSlicerForOrbitalFractureRepairFemSimulation/"><img src="https://github.com/user-attachments/assets/2f1898dc-92df-477f-8124-294e97ed6f7b" style="max-width:480px;width:100%"></a>

Creating a volumetric mesh is essential for FEM simulation. However, meshing for orbital tissue with fracture is challenging due to multiple thin structures confined in a bony orbit, low CT contrast, and presence of trauma. To ease the process, we prepared a unified multi-material mesh for orbital tissue to avoid dealing with tissue boundaries. We are currently training a preliminary model using MONAI-nnUNet for orbital tissue segmentation using 13 specimens, each of which augmented to 5 additional volumns using TorchIO. We then created a unified orbital tissue segmentation, converted to a surface model, and created a tetrahedral mesh using gmsh. Sub-tissue regions were then selected in SOFA using specific tisssue surface models. Overall, though much easier than creating multiple tissue meshes, this step still requires many manual steps, including segmentation refinement and surface model downsampling and uniform remeshing, in Slicer and gmsh. Furthermore, due to the coarseness of interior tetrahedra, the selected tetrahedra could not accurately reflect internal tissue geometry, creating errors in tissue geometry tracking in simulation. Mesh refinement was used to create finer elements at interior tissue surface but it led to a over-detailed mesh with too many elements.


19. **[New 3D Slicer Module to predict surgery movement for maxillofacial surgery](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/New3DSlicerModuleToPredictSurgeryMovementForMaxillofacialSurgery/)** (Alexandre Buisson @ University of North Carolina at Chapel Hill, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/New3DSlicerModuleToPredictSurgeryMovementForMaxillofacialSurgery/"><img src="https://github.com/user-attachments/assets/40e31807-6507-4743-b3e6-e130736a4ab1" style="max-width:480px;width:100%"></a>

Predicting surgical movements and bone displacement vectors in virtual surgical planning software remains an expert-intensive task, requiring surgeons to simulate osteotomies and manually adjust bone segments. Although statistical shape models and deep learning regression networks have been explored to automate this phase, they output dense deformation fields that lack the geometric interpretability needed to guide clinical or surgical decisions.

This project introduces a dedicated 3D Slicer module driven by a Machine Learning Stacking model, trained on a robust dataset of 1,496 patients. The module simplifies the clinical workflow by allowing users to upload an input file (e.g., Excel/CSV containing clinical parameters) and instantly receive accurate, data-driven predictions of the required maxillofacial bone movements.


20. **[NousNav Project Updates](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/NousnavProjectUpdates/)** (Sam Horvath @ Kitware, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/NousnavProjectUpdates/"><img src="https://github.com/user-attachments/assets/812490c5-0213-45fd-86dd-ea734efcb55b" style="max-width:480px;width:100%"></a>

The NousNav project is an initiative led by Dr Alexandra Golby to develop a low-cost neuronavigation system designed for use in low- and middle-income countries. We are developing a 3D Slicer based application focused on supporting segmentation, registration and navigation tasks.

The project will also include the development of open source hardware desgins for these applications.

This week will include continued development on the NousNav project, in preparation for work with new collaborators.  This includes new usability features, UI refinement and updating the guidance images for the patient registration.


21. **[Porting lung ultrasound analysis software from 3D Slicer to OHIF](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/PortingLungUltrasoundAnalysisSoftwareFrom3DSlicerToOhif/)** (Dave Dinh @ BWH, +) ([SlicerUltrasound/SlicerUltrasound](https://github.com/SlicerUltrasound/SlicerUltrasound))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/PortingLungUltrasoundAnalysisSoftwareFrom3DSlicerToOhif/"><img src="https://github.com/user-attachments/assets/00192df6-e400-4f88-8c45-7a2d66feb4e8" style="max-width:480px;width:100%"></a>

Our team has been developing various 3D Slicer modules for lung ultrasound analysis (https://github.com/SlicerUltrasound/SlicerUltrasound), from de-identification to annotation and adjudication. However, we have slowly started porting the extensions developed in Slicer to OHIF, as this is easier for the clinicians and other researchers to use. It doesn't require them to install any additional software, and they can access OHIF from the web. 

Initial work has been performed by the Radical Imaging team to update OHIF with the B-line quantification tools that our team requires. However, there are some improvements that still need to be made: 
- We need to make sure annotation of the pleural lines and B-lines are supported, and that the resulting files are saved appropriately. 
- We would like to have single-rater vs multi-rater modes, where the multi-raters can work together to discuss a case, or adjudicate the annotations.


22. **[Qt6 and arm64 Slicer builds on the factory machines](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Qt6AndArm64SlicerBuildsOnTheFactoryMachines/)** (Sam Horvath @ Kitware, +) ([Slicer/Slicer](https://github.com/Slicer/Slicer))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Qt6AndArm64SlicerBuildsOnTheFactoryMachines/"><img src="https://github.com/user-attachments/assets/4fd30f74-7d08-4eef-ac51-5879955f6e7c" style="max-width:480px;width:100%"></a>

This week we will be finalizing the 5.12 release, and then working on moving the factory builds to Qt6 and arm64 (for macOS). These are the critical changes for the next major release Slicer 6.


23. **[Recon-all correction script based on manual subcortical segmentation files](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ReconAllCorrectionScriptBasedOnManualSubcorticalSegmentationFiles/)** (Jarrett Rushmore @ Center for Morphometric Analysis, +) (no github repo yet)

White and pial surfaces and parcellation from recon-all pipeline (7.4.1) need quite a few manual corrections.
At the same time, 100 cases from HCP-YA dataset were manually segmented using HOA2 atlas (subcortical areas).
The goal of the project is to leverage the latter to get better results with recon-all.


24. **[Redesigned REST API and MCP server for Imaging Data Commons](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/RedesignedRestApiAndMcpServerForImagingDataCommons/)** (Andrey Fedorov @ BWH, +) ([ImagingDataCommons/imaging-data-commons-skill](https://github.com/ImagingDataCommons/imaging-data-commons-skill))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/RedesignedRestApiAndMcpServerForImagingDataCommons/"><img src="https://github.com/user-attachments/assets/83ba0f17-ed92-4066-85f2-cfcd0a4eeb7a" style="max-width:480px;width:100%"></a>

**Questions? Want to participate remotely? Join our project [Discord channel](https://discord.gg/TTFGUYGdsZ)!**

TL;DR: Work on v3 of [Imaging Data Commons (IDC)](https://portal.imaging.datacommons.cancer.gov/) REST API simultaneously with the development of the IDC [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) server.

IDC already offers a customized agent skill in [https://github.com/ImagingDataCommons/imaging-data-commons-skill](https://github.com/ImagingDataCommons/imaging-data-commons-skill), which is very powerful in helping with the use of IDC. However, in order to use it effectively, the user needs to have access to an LLM platform that supports code execution, and needs to suffer the "cold start" cost of setting up the environment. IDC MCP interface can provide "zero startup cost" solution for answering at least some of the queries, optimized for the use by agents. At the same time, MCP interface will need to rely on IDC API, which in its current v2 form is not useful at all. We are in the process of simultaneous redesign of IDC API and design of the MCP interface. Since we do not have expertise on the team doing something like this before, we would appreciate community feedback.


25. **[Robust Segmentation Experience in OHIF Viewer](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/RobustSegmentationExperienceInOHIFViewer/)** (Jaeyoung Cho @ University Hospital Bonn, +) ([cornerstonejs/cornerstone3D](https://github.com/cornerstonejs/cornerstone3D))

OHIF Viewer is a widely used web-based medical image viewer built on Cornerstone3D. Segmentation is central to many clinical and research workflows, yet reliability and robustness in OHIF/Cornerstone still lag behind user expectations — with recurring errors and edge cases in everyday use ([OHIF/Viewers#5453](https://github.com/OHIF/Viewers/issues/5453)).

During Project Week 45, I would like to focus on improving the stability and user experience of segmentation in OHIF/Cornerstone. I am looking forward to collaborating with others interested in segmentation, digital pathology, and web-based imaging viewers.

This project targets two complementary areas:

- **DICOM-SEG landscape** — Understand the development and history of DICOM Segmentation, current standard direction (including label-map encodings), and recommended usage for save/load and interchange with research formats.
- **Overlapping segments in OHIF** — Ensure overlapping segmentations work reliably across **Stack Viewport + MPR**, **Volume Viewport**, and downstream tools — **segmentation statistics** and **bidirectional measurements**.

Several related gaps remain in the broader stack: overlapping segmentations are not always handled reliably across viewport types, DICOM persistence paths are still evolving ([PR #5806](https://github.com/OHIF/Viewers/pull/5806), [#4875](https://github.com/OHIF/Viewers/issues/4875)), and contour ↔ labelmap conversion is not yet exposed end-to-end in OHIF. This project aims to advance solutions within Cornerstone3D and OHIF toward a more dependable segmentation experience.

For DICOM persistence, standards context, and recommended interchange with research formats (NIfTI), see [Background and References](#background-and-references).


26. **[Slicer Chest Imaging Platform Reboot](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicerChestImagingPlatformReboot/)** (Kalysta Makimoto @ Brigham and Women's Hospital, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicerChestImagingPlatformReboot/"><img src="https://github.com/user-attachments/assets/821d8abe-1044-4bcf-a92c-3ab0d0e98efd" style="max-width:480px;width:100%"></a>

`The Chest Imaging Platform (CIP)` is an open-source software suite developed by the `Applied Chest Imaging Laboratory (ACIL)` at Brigham and Women's Hospital (Harvard Medical School). Slicer CIP is designed for quantitative chest CT analysis, helping clinicians and researchers identify and measure phenotypes for Chronic Obstructive Pulmonary Disease (COPD), Interstitial Lung Disease (ILD), Acute Lung Injury (ALI), Pulmonary Vascular Pruning, and Lung Cancer.


27. **[Slicer-to-Action for surgical robot imitation learning](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicerToActionForSurgicalRobotImitationLearning/)** (Taewoo Yoon @ AIRS Inc, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicerToActionForSurgicalRobotImitationLearning/"><img src="https://github.com/user-attachments/assets/09d40dbd-0033-45a7-8e0d-324c90201013" style="max-width:480px;width:100%"></a>

We are developing a robotic system for fracture reduction using SlicerROS2. The goal of this project is to investigate whether recent imitation learning approaches, such as visuomotor policies or Vision-Language-Action (VLA) models, can be applied to this robot system.
In this project, 3D Slicer functions as a tool to display real-time object movements in a 3D view. 
We intend to utilize this **3D view as training data for robotic motion**.
The 3D Slicer view will function just like a real camera mounted on the robot.
Furthermore, it will allow us to build **custom simulation environments to generate and train on virtual data**.


28. **[SlicerSOFA simulation for predicting soft tissue restoration after orbital fracture](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicersofaSimulationForPredictingSoftTissueRestorationAfterOrbitalFractureRepair/)** (Chi Zhang @ Texas A&M College of Dentistry, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicersofaSimulationForPredictingSoftTissueRestorationAfterOrbitalFractureRepair/"><img src="https://github.com/user-attachments/assets/096f4d10-3875-4754-9553-9726e2a7bec2" style="max-width:480px;width:100%"></a>

Orbital fractures are typically caused by blunt-force trauma. Fracture repair frequently requires placing a titanium plate to reconstruct bony orbit and restore tissue position and function from disturbed conditions, such as enophthalmos ("sunken eye") and muscle entrapment & conformational changes. 

This project aims to develop a reproducible and scalable patient-specific SOFA/SlicerSOFA FEM simulation workflow to predict orbital soft tissue restoration after fracture repair using a preformed titanium plate.The simulation processes span across multiple scenes from retracting orbital tissue to place a plate and then let the tissue fall onto the plate. The only deformable object is a unified multi-material orbital tissue mesh. Tetrahedrons inside different tissue regions to assign with different material properties. The retracting tool, plate, and bony orbit are all simulated as rigid bodies.

Currently, it still relies on many steps of manual set up in Slicer, including retraction plane position and moving trajectory and distances, attachment points, input/output across staged scenes, and tissue-bone attachment points.


29. **[SlicerVirtualReality - OpenXR Update, Passthrough Support, Interactions Refactor](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicervirtualrealityOpenxrUpdateAndPassthroughSupport/)** (Kyle Sunderland @ Queen's University, +) ([Sunderlandkyl/VTK](https://github.com/Sunderlandkyl/VTK))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicervirtualrealityOpenxrUpdateAndPassthroughSupport/"><img src="https://github.com/user-attachments/assets/c1e406e5-4887-4c43-b370-694434bd1fcc" style="max-width:480px;width:100%"></a>

Currently SlicerVirtualReality is compiled using an older version of OpenXR. This project aims to finalize the integration of the latest version of OpenXR, as well as adding requested features such as passthrough using Meta Quest headsets.


30. **[Standardizing DICOM De-ID with Actionable Rules and Tests](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/StandardizingDicomDeIdWithActionableRulesAndTests/)** (Dave Dinh @ BWH, +) ([clintools/dicom-curate](https://github.com/clintools/dicom-curate))

DICOM de-identification (De-ID) efforts often overlap in the rules used to process DICOM metadata. This project aims to translate [an existing DICOM De-ID standard](https://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_E.1.1) into a set of actionable rules that can serve both as an implementation guide and as a verifiable audit trail for tools and AI systems.
For example, a standard may permit multiple actions for a given metadata field. A baseline reference can recommend a default action, while still allowing users to specify alternative behaviors as needed. The proposed generator will take user input and produce:

- A reference list of itemized, actionable rules
- A unit and end-to-end test specification that users can apply to their specific use cases

The initial user interface for the generator will be a command-line (CLI) tool. It will operate based on a predefined decision tree and output rules and test specifications in formats suitable for humans, AI systems, and supported programming languages.

In practice, DICOM De-ID outputs can vary depending on modality, imaging protocols, contractual requirements, and application domains. However, there remains a consistent need to validate that outputs conform to a predefined set of rules. This library represents a step forward in programmatically generating verifiable rules for reliable and consistent implementation.


31. **[That Rendering Thing](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ThatRenderingThing/)** (Steve Pieper @ Isomics, +) ([pieper/SlicerCL](https://github.com/pieper/SlicerCL))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ThatRenderingThing/"><img src="https://github.com/user-attachments/assets/2fc3ddb2-f485-40a6-b8e1-241e4fe4d155" style="max-width:480px;width:100%"></a>

I've been experimenting with [wgpu-py](https://github.com/pygfx/wgpu-py), an implementation of WebGPU that you can pip_install directly into Slicer.

The work in progress in [SlicerWGPU](https://github.com/pieper/SlicerWGPU), which is now working pretty nicely in demo mode.

#### Key Features
* Easy to install, can work with any recent Slicer release.  Don't even need to restart Slicer.
* Can write shader code easily that works on Vulkan, DirectX, and Metal.
* It supports multi-volume rendering with full quality compositing
* It can directly render segmentations and provides instant updates in response to edits
* It supports interactive rendering of volumes under non-linear transforms
* Interactive elements like transform handles and markups are still handled by VTK and seamlessly composited

#### Current status
* Currently in demo mode.  Some things are integrated to work with the MRML scene while, others work alongside.
* The VTK OpenGL render window is tapped into so that most rendering works cleanly, but SlicerWGPU uses a different method to composite multiple translucent surfaces (A-Buffer compared to Depth Peeling) so those aren't currently combined.
* Performance seems about the same as VTK's GPU renderer, but no extensive testing has been done. 

#### How to try it
* Clone the [SlicerWGPU](https://github.com/pieper/SlicerWGPU) repository
* Drag and drop the folder onto a running Slicer (5.10.0 or really any version should work).
* Be sure to load the `Scene Rendering` module (you can ignore the others)
* Go to the `Scene Rendering` module and try the buttons.  The top block of buttons (the "VTK Injection" block) are the current demos and the "Dual View" bock are some older experiments.


32. **[Vox2SegLAM: Protocol-Guided Subcortical Segmentation in 3D Slicer](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Vox2SeglamProtocolGuidedSubcorticalSegmentationIn3DSlicer/)** (Ahmed Rekik @ École de technologie supérieure, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Vox2SeglamProtocolGuidedSubcorticalSegmentationIn3DSlicer/"><img src="https://github.com/user-attachments/assets/d4ad19a7-6048-4d48-aa48-f893331e8d80" style="max-width:480px;width:100%"></a>

3D SlicerVox2SegLAM is an extension that brings an AI-assisted, protocol-guided workflow to subcortical brain segmentation and landmarking. A joint CNN+GNN model predicts 26 subcortical structures and 20 anatomical landmarks directly from a T1 MRI, following the Harvard-Oxford Atlas (HOA 2.0) neuroanatomical protocol.

