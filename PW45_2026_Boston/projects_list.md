# Project Week# 45, June 22-26, 2026 @ MIT, Boston, USA

1. **[AI-Agent for SlicerAutomatedDentalTools](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiAgentForSlicerautomateddentaltools/)** (Paul Dumont @ University of North Carolina at Chapel Hill, +) ([DCBIA-OrthoLab/SlicerAutomatedDentalTools](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiAgentForSlicerautomateddentaltools/"><img src="https://github.com/user-attachments/assets/32b13db1-2e45-4067-8fd6-1d18a84fd662" style="max-width:480px;width:100%"></a>

**Problem**: The Slicer Automated Dental Tools extension provides robust craniofacial analysis, but complex module selection and parameter tuning create a steep learning curve for users.

**Solution**: This project introduces an AI Agent and chatbot UI integrated into 3D Slicer to streamline the workflow. By allowing drag-and-drop inputs and natural language prompts, users can easily request complex tasks (e.g., segmentation, landmarking, or orientation on CBCT/IOS). The agent autonomously translates these requests into actions, selecting the right tools and automatically configuring the parameters to execute the workflow.

**Progress and Next Steps**

**Current Progress**
The backend retrieval system is completely operational. The Cross-Encoder model reliably identifies and selects the appropriate Slicer tool from natural language input.

**Next Steps**
- LLM Integration: Implement the logic for the local LLM to parse the user's prompt, auto-fill the required parameters, and trigger the tool execution.

- Slicer Deployment: Embed the interactive UI and connect the entire AI pipeline directly within the 3D Slicer environment.


2. **[AI driven interface for SlicerTMS](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiDrivenInterfaceForSlicertms/)** (SangHyuk Kim @ BWH & UMass Boston, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiDrivenInterfaceForSlicertms/"><img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW45_2026_Boston/Projects/AiDrivenInterfaceForSlicertms/surface%20registration.png" style="max-width:480px;width:100%"></a>

SlicerTMS is a 3DSlicer module for patient-specific transcranial stimulation. It integrates several functions, including neuronavigation, electric field modeling, real-time EEG streaming and recording, and TMS control. These functions involve a complex user interface, and some tasks, such as neuronavigation registration, may need more than one user. To simplify the interface and improve the user experience, we will develop a new version leveraging LLM models and Slicer AI Agent tools. Specifically, we will eliminate LLM hallucinations at the infrastructure level by executing medical software APIs through human-verified Markdown Cookbooks and local Vector RAG technologies. Furthermore, the system establishes a next-generation intelligent environment featuring a self-evolving Auto-Correction engine that tracks and learns directly from clinician adjustment patterns, all while seamlessly supporting the trusted clinical interfaces medical professionals already use.

**Progress and Next Steps**

- SlicerTMS Navigation workflow automated by integrating Local LLM.
- SlicerTMS Registration feature is controlled by cookbook: RAG router bypassing LLM logic for known tasks. Near zero-latency for defined commands.
- LLM does not write raw Python code. System runs on deterministic medical API execution.

 </br>


3. **[AI model development for lung ultrasound analysis](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiModelDevelopmentForLungUltrasoundAnalysis/)** (Alexandre Banks Gadbois @ BWH, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AiModelDevelopmentForLungUltrasoundAnalysis/"><img src="https://github.com/user-attachments/assets/22010591-075d-4910-9e31-184b91568813" style="max-width:480px;width:100%"></a>

One of the primary indicators of acute heart failure is the presence of pulmonary congestion. To detect fluid build up quickly in the emergency room, lung ultrasound exams are taken of the patient. Clinicians look for hyperechoic artifacts (B-lines) that appear in the image, where the more they see the more congested the patient is. 

Unfortunately, manual detection of these B-lines is difficult due to the image quality, which depends on the type of transducer and the expertise of the clinician. Therefore, AI models have started to be developed to quickly detect these B-lines. Our group, over the past few years, has developed multiple methods [1], [2], [3]. One of the drawbacks though, is that existing models do not compute the pleural percentage, the ratio of the B-line sectors to the pleural line sectors, which is strongly associated with extravascular lung water and consistent with other semi-quantitative clinical scores [4]. 

Therefore, we have started to develop detection models to automatically find pleural lines and B-lines and compute the percentage pleura. Our goal for this project week is to train and validate keypoint detection models such as ViTPose++, [5], and HRNet with UDP, [6], and talk to clinicians about the performance.

**Progress and Next Steps**

- We have trained some preliminary YOLO models for bounding box detection. We trained one oriented bounding box YOLO model for pleural lines, and another axis-aligned box YOLO model for B-lines. 
- We calculated the percent pleura and compared it to the experts.
- Implemented and validated a data preprocessing script: 1) parses data and formats into COCO-styled repository, 2) enables sector-to-scanline conversions, 3) enables filtering by metadata (_site, annotator, lung zone, patients, before/after diuretic, transducer type, transducer manufacturer_)
- Implemented a dataloader that allocates equal proportions of different metadata tags to train/vali/test datasets. Implemented k-fold validation and inclusion of data by various metadata tags.


4. **[Automatic segmentation of priority collections from Imaging Data Commons](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AutomaticSegmentationOfPriorityCollectionsFromImagingDataCommons/)** (Andrey Fedorov @ BWH, +) ([Sunderlandkyl/CloudSegmentator](https://github.com/Sunderlandkyl/CloudSegmentator))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/AutomaticSegmentationOfPriorityCollectionsFromImagingDataCommons/"><img src="https://github.com/user-attachments/assets/b793aaa1-0003-424a-9f48-895bca8d7aa9" style="max-width:480px;width:100%"></a>

**Questions? Want to participate remotely? Join our project [Discord channel](https://discord.gg/TTFGUYGdsZ)!**

The goal of this project is to further increase availability of anatomic segmentations and accompanying radiomics features for the images available in Imaging Data Commons.

**Progress and Next Steps**

This week we made progress on debugging/fixing/imporoving segmentation workflow and the associated tools.

- Refined post-processing component of the workflow - improved/fixed generation of DICOM SEG.
   * [https://github.com/Sunderlandkyl/CloudSegmentator/pull/1](https://github.com/Sunderlandkyl/CloudSegmentator/pull/1)
- Fixed handling of deflate transfer syntax in dcmqi, which was broken on windows (which was also broken in Slicer) [https://github.com/QIICR/dcmqi/pull/549](https://github.com/QIICR/dcmqi/pull/549)
- Adding SNOMED mapping upstream to the MOOSE segmentator [https://github.com/ENHANCE-PET/MOOSE/pull/241](https://github.com/ENHANCE-PET/MOOSE/pull/241)
- Started working on making the segmentation workflow applicable to segmentation of non-IDC data (via private Google bucket access)
- Added the option to allow Terra to access private Google buckets containing dicom files
- Added export of output DICOM SEG files into Google Cloud DICOM stores
- Added output CSVs containing performance metrics and structure metrics to the output


5. **[3D Slicer Cast interface extension: Hub,  Resource Servers and Image Display client.](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/CastInterfaceModuleFor3DSlicerServiceProvidersImageDisplayClientAndHub/)** (Martin Bellehumeur @ Radical Imaging, +) ([mbellehumeur/SlicerCastInterface](https://github.com/mbellehumeur/SlicerCastInterface))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/CastInterfaceModuleFor3DSlicerServiceProvidersImageDisplayClientAndHub/"><img src="https://github.com/user-attachments/assets/7c8aefc0-d697-4813-9193-53fe08944c99" style="max-width:480px;width:100%"></a>

The project is about desktop integration infrastucture for healthcare applications.  It introduces a new 3D Slicer extension that provides backend and front-end services to that effect. 


The extension repository is here: https://github.com/mbellehumeur/SlicerCastInterface

**Progress and Next Steps**

Three project week teams integrated their research:
  
   - Lung cancer screening with OHIF
     (https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExtractingDeepLearningFeaturesFromCtImagesOfTheThoracicRegionForLungCancerApplications/)
   - Subcortical segmentation: with VolView.
     (https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Vox2SeglamProtocolGuidedSubcorticalSegmentationIn3DSlicer/)
   - AI search agents for IDC data with the worklist example application.
     (https://projectweek.na-mic.org/PW45_2026_Boston/Projects/RedesignedRestApiAndMcpServerForImagingDataCommons/)


6. **[Clinical Information Extraction via Locally Fine-Tuned LLMs](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ClinicalInformationExtractionViaLocallyFineTunedLlms/)** (Paul Dumont @ University of North Carolina at Chapel Hill, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ClinicalInformationExtractionViaLocallyFineTunedLlms/"><img src="https://github.com/user-attachments/assets/ab930885-cd8a-4af6-9f1b-c9d12d150dcb" style="max-width:480px;width:100%"></a>

This project develops a privacy-preserving extraction framework using locally deployable open-weight LLMs to structure dense clinical narratives. A primary goal is to harmonize the diverse data and writing styles of different clinicians and doctors. Furthermore, we aim to bypass expensive and non-private cloud APIs by fine-tuning models to extract Common Data Elements (CDEs) from Orthodontic and TMJ progress notes entirely offline

**Progress and Next Steps**

Fine-tuned Llama-3.1-8B (LoRA) achieved a 0.740 F1 score on orthodontic notes , and fully fine-tuned Qwen-2.5-7B reached a 0.78 F1 score on TMJ records.
Next Steps: Deploy these trained models directly within 3D Slicer by developing a custom extension with a dedicated user interface (UI) for clinical application.


7. **[Exploring Ultrasound Multi-frame Image Storage Structured Report support for Slicer/OHIF](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExploringUltrasoundMultiFrameImageStorageStructuredReportSupportForSlicerOhif/)** (Deepa Krishnaswamy @ BWH, +) ([deepakri201/create_LUS_SR](https://github.com/deepakri201/create_LUS_SR))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExploringUltrasoundMultiFrameImageStorageStructuredReportSupportForSlicerOhif/"><img src="https://github.com/user-attachments/assets/6574e377-dc30-4454-9938-78fb3db31f39" style="max-width:480px;width:100%"></a>

Our team has built a 3D Slicer extension for ultrasound anonymization, annotation, and adjudication (https://github.com/SlicerUltrasound/SlicerUltrasound). We are currently trying to port the functionality of these tools to OHIF in order to make the processing more streamlined for clinicians and avoid the downloading of additional tools. 

However, we currently store all of our annotations as JSON. This can be problematic as JSON can be prone to misinterpretation; we had to write specialized software to load these annotations into Slicer, and we are missing much of the metadata to associate the file with the referenced image. 

In this project, I want to see if using DICOM Structured Reports (SR) will help our use case. Having our files as SRs would help us to utilize the cloud and retain all important metadata. But it might also make processing more complicated. Therefore, the goal of this week is to see how much effort is needed to add functionality to Slicer/OHIF for Ultrasound Multi-frame Image Storage.

**Progress and Next Steps**

- Converted our JSON annotation file to a DICOM SR 
- Confirmed the DICOM SR can load in OHIF 
- Added functionality to 3D Slicer to load, parse, and view these DICOM SRs
- Next week - will make a PR to Slicer
- WIP - deploying OHIF connected to a Google Cloud Platform DICOM datastore, with the usAnnotation plugin support (Thank you, Martin and Andrey, for your help!)


8. **[Extracting deep learning features from CT images of the thoracic region for lung cancer](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExtractingDeepLearningFeaturesFromCtImagesOfTheThoracicRegionForLungCancerApplications/)** (Renzo Phellan Aro @ Lunenfeld-Tanenbaum Research Institute, +) ([AIM-Harvard/TumorImagingBench](https://github.com/AIM-Harvard/TumorImagingBench))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExtractingDeepLearningFeaturesFromCtImagesOfTheThoracicRegionForLungCancerApplications/"><img src="https://github.com/user-attachments/assets/5fd64d0e-fcba-4efd-90b5-b508bec70fc5" style="max-width:480px;width:100%"></a>

This project focuses on using existing foundational deep learning models in 3D Slicer to process CT images of the thoracic region. The objective is to extract features that can be used for lung cancer applications, such as classification, screening, and risk prediction.

**Progress and Next Steps**

- Worked on identifying members of the 3D Slicer community interested in participating in the project.
- Used Claude AI to generate the graphical interface in 3D Slicer to process medical images using the [Tangerine](https://github.com/niccolo246/3D-MAE-MedImaging) model.
- Created a stand-alone command-line interface to access the model via OHIF.
- Uploaded the code to a Github [repo](https://github.com/rphellan/slicerW45).


9. **[Fan mask and OCR bound box editing for OHIF-based DICOM De-Identification verification](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/FanMaskAndOcrBoundBoxEditingForOhifBasedDicomDeIdentificationVerificationMode/)** (Dave Dinh @ BWH, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/FanMaskAndOcrBoundBoxEditingForOhifBasedDicomDeIdentificationVerificationMode/"><img src="https://github.com/user-attachments/assets/f4a099f4-5f71-40a3-a22f-f84ace253d0e" style="max-width:480px;width:100%"></a>

Optimal DICOM de-identification for downstream research requires balancing removal and retention. We must scrub embedded PHI in both tags and pixels while preserving valuable non-PHI metadata (e.g., scan settings like depth). Even with both addressed, human review is still needed to catch misses.

We’re building a closed-loop system with two components:
- an automated pipeline that scrubs DICOM tags (PS3.15 with configurable overrides), masks pixel PHI by manufacturer, extracts non-PHI pixel data, and produces deterministic, reproducible outputs
- an OHIF-based reviewer for human verification. Each review records passes, failures, and false positives/misses, which feed back as rule updates so errors don’t recur.

The pipeline handles most de-identification automatically, but reviewers still face significant cognitive load when inspecting every metadata diff, OCR-flagged region, and fan crop. The OHIF mode currently surfaces areas in the DICOM metadata that require verification based on predefined rules but reviewers also need tools to edit PHI masks, OCR bounding boxes for non-PHI extraction, and fan geometry for fan-only pixel extraction.

**Progress and Next Steps**

Deploy to testing environment and iterate on user feedback.


10. **[Fine-tuning SimCortex Using Manually Corrected Cortical Annotations](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/FineTuningSimcortexUsingManuallyCorrectedCorticalAnnotations/)** (Kaveh Moradkhani @ École de technologie supérieure, +) ([Neuro-iX/SimCortex](https://github.com/Neuro-iX/SimCortex))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/FineTuningSimcortexUsingManuallyCorrectedCorticalAnnotations/"><img src="https://github.com/user-attachments/assets/d3d4cd33-8c13-46a2-a59a-b5af894be9e8" style="max-width:480px;width:100%"></a>

SimCortex v2 is a deep learning pipeline for cortical surface reconstruction from brain MRI. In this project, we will fine-tune the existing SimCortex v2 model using manually corrected segmentations and cortical surfaces.

The goal is to evaluate whether manual supervision can improve the reconstructed white and pial surfaces compared with the current SimCortex v2 baseline.

As a practical outcome, we will also prepare a 3D Slicer extension for SimCortex. The extension runs SimCortex through Docker from a native T1-weighted MRI and loads the reconstructed cortical surfaces back into Slicer for visualization.

**Progress and Next Steps**

- SimCortex v2 is already available as an open-source cortical surface reconstruction pipeline.
- Manually corrected segmentations and cortical surfaces are available for fine-tuning.
- A local prototype of the SimCortex 3D Slicer extension has been developed.
- The extension can run SimCortex through Docker from a T1-weighted MRI and load the reconstructed white and pial surfaces back into Slicer.
- Next steps are to finalize the fine-tuning workflow, run initial experiments, evaluate the results, and prepare the Slicer extension for public release.


11. **[Image visualization in Google Colab](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ImageVisualizationInGoogleColab/)** (Andrey Fedorov @ BWH, +) ([KitwareMedical/trame-slicer](https://github.com/KitwareMedical/trame-slicer))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ImageVisualizationInGoogleColab/"><img src="https://github.com/user-attachments/assets/dbfdd42e-8f9c-4b62-a98b-b0e0e4ba99c4" style="max-width:480px;width:100%"></a>

In this project we will experiment with different approaches to implementing 3d visualization of radiology images and overlaying segmentations in [Google Colab](https://colab.research.google.com/). The primary motivation for this project is to support visualization of images from Imaging Data Commons along with user-generated analysis results in Google Colab, which has zero prereqisites for installing software on user's computer.

**Progress and Next Steps**

- Prepared notebooks demonstrating the use of `trame-slicer`, `ipyniiview` and Steve's `desktopia`: [https://github.com/ImagingDataCommons/IDC-Tutorials/pull/104](https://github.com/ImagingDataCommons/IDC-Tutorials/pull/104)
  * `ipyniiview` appears to be most robust, lightweight and fast viewer to use in Colab notebook (not tested outside of Google)
  * `trame-slicer` developers [identified directions to improve performance and simplify usage](https://github.com/KitwareMedical/trame-slicer/issues/81#issuecomment-4660192264), will monitor
- Contributed new tutorials to IDC-Tutorials repo, updated "getting started" with using `ipyniiview`: [https://github.com/ImagingDataCommons/IDC-Tutorials/pull/104](https://github.com/ImagingDataCommons/IDC-Tutorials/pull/104)
  * [updated intro tutorial](https://github.com/ImagingDataCommons/IDC-Tutorials/blob/master/notebooks/getting_started/part2_searching_basics.ipynb) with visualization


12. **[Improving QC protocols for AMP SCZ Clinical and MRI Data](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ImprovingQcProtocolsForAmpSczClinicalAndMriData/)** (Sylvain Bouix @ école de technologie supérieure, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ImprovingQcProtocolsForAmpSczClinicalAndMriData/"><img src="https://github.com/user-attachments/assets/ea7915eb-1a4a-4dd0-86b2-3be1369fda8c" style="max-width:480px;width:100%"></a>

We will be adding anomaly detection algorithms to clinical data and MRI data in the AMP SCZ project.

**Progress and Next Steps**

- Scanned the database for site distribution outliers, string anomalies, and time series anomalies that allowed several new quality control rules to be developed.
- Created a web interface for MRI data that allowed various synthetic anatomical and scanner features to be visualized.
- Used the synthetic anatomical and scanner augmentations to train a robust MRI QC model.
- Next steps involve calculating the correlation between the automatic MRI QC and scores by human raters.


13. **[Integrating a Parallel Robot into SlicerROS2 with MoveIt-Based Planning for Image-Guided](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/IntegratingAParallelRobotIntoSlicerros2WithMoveitBasedPlanningForImageGuidedNeedleProcedures/)** (Mariana Bernardes @ BWH, +) ([maribernardes/ros2_kimm_robot](https://github.com/maribernardes/ros2_kimm_robot))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/IntegratingAParallelRobotIntoSlicerros2WithMoveitBasedPlanningForImageGuidedNeedleProcedures/"><img src="https://github.com/user-attachments/assets/8ae6776e-d66d-4ec7-b534-601c1b0343a2" style="max-width:480px;width:100%"></a>

This project aims to integrate a Stewart-platform parallel robot into the [SlicerROS2](https://github.com/rosmed/slicer_ros2_module) ecosystem for image-guided biopsy and ablation procedures. The robot, developed by collaborator Dr. Joonho Seo at KIMM, will be controlled using [ROS2](https://www.ros.org/) and and can align a needle or ablation probe based on patient intraoperative imaging. By integrating robot visualization and motion-planning preview into the 3D Slicer interface, we aim to allow the user to visualize the planned robot motion and probe trajectory before execution. This integration will also provide a foundation for future closed-loop robotic control using medical imaging feedback.

During Project Week, we created an initial ROS 2 package for the KIMM Stewart-platform robot, integrated it with SlicerROS2, and developed a Slicer-side custom-control workflow for sending desired platform poses from 3D Slicer to the robot through ROS 2. The project also motivated a generalizable interface for related medical Stewart-platform robots, including the [AIRS RONAVIS-RD platform](https://airsurgical.net/RONAVIS-RD/) for orthopedic fracture reduction.

**Progress and Next Steps**

- Created an initial ROS2 package for the KIMM Stewart-platform robot.  
   The package includes a robot description, TF frame representation, virtual joint-state representation for visualization of the closed-chain platform, and command interfaces needed to represent and control the robot from ROS2. Because standard URDF/TF representations do not directly solve closed-chain parallel-robot kinematics, the package uses robot-specific kinematic calculations to update the platform state.

- Integrated the KIMM robot package with SlicerROS2.  
   The robot can be visualized through the SlicerROS2 workflow, and desired platform poses can be sent from 3D Slicer to ROS2 using a Slicer-side custom-control workflow.

- Developed a reusable custom-control pattern for Stewart-platform-like medical robots.  
   The 3D Slicer-side interface was structured to separate user-defined planning transforms in 3D Slicer, pose command publication, robot state visualization, and robot-specific command execution. This same pattern is being aligned with the AIRS orthopedic robot platform.

- Identified two complementary planning levels for parallel robots in SlicerROS2.  
   The first level is pose-space planning of the moving platform, followed by custom IK-based validation of actuator feasibility and execution constraints. This is the current practical approach for the KIMM robot because IK is available, while FK is not currently exposed to the integration. The second level is a more MoveIt-native integration through custom kinematics and control interfaces, which is still ongoing work being explored with the AIRS robot.

- Identified platform-specific differences that affect planning and control.  
   For the KIMM robot, IK is available and pose-space commands are the current practical pathway, but full joint-space planning is limited by the available kinematic interface. For the AIRS robot, joint-state commands are available, enabling a complementary joint-control workflow and supporting ongoing development toward a MoveIt plugin.

Next steps include refining the KIMM pose-space planning and IK-validation workflow, improving visualization of current and desired platform poses in Slicer, adding clearer robot-state and command-status feedback, and continuing development/testing of custom MoveIt integration strategies for Stewart-platform robots.


14. **[Interactive Workflow Replay and Step-Back Navigation for Slicer Agent](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/InteractiveWorkflowReplayAndStepBackNavigationForSlicerAgent/)** (Puxun Tu @ Brigham and Women's Hospital, +) ([puxuntu/Slicer_agent](https://github.com/puxuntu/Slicer_agent))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/InteractiveWorkflowReplayAndStepBackNavigationForSlicerAgent/"><img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW45_2026_Boston/Projects/InteractiveWorkflowReplayAndStepBackNavigationForSlicerAgent/workflow_replay_demo.png" style="max-width:480px;width:100%"></a>

The Slicer AI Agent is a scripted extension that lets users use natural-language instructions and have the system autonomously generate, validate, and execute Python code within the 3D Slicer scene. For complex multi-step operations, such as extension-specific surgical planning workflows, the agent enters a deterministic workflow runtime that executes a sequence of predefined steps (automated code execution, interactive 3D mark-up placement, user choices, and branching logic) with a progress bar tracking completion.

Currently this progress bar is forward-only: once a step completes, there is no way to go back, inspect what happened at an earlier step, or modify a previous choice and re-run the downstream pipeline. This limits both transparency (users cannot easily understand what was done and why) and usability (a wrong choice means restarting the entire workflow from scratch).

We propose adding a workflow replay timeline that records per-step state and allows users to go back to any completed step, inspect the code and choices that were made, optionally modify parameters, and re-execute the workflow from that point onward.

**Progress and Next Steps**

Implemented workflow replay with step-back navigation. [Watch demo video](https://github.com/user-attachments/assets/8aa53cd2-9cd1-49ff-8a26-e07cdafba7a4)


15. **[Testing Local LLMs for Agentic Tasks via Slicer Skills](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/LocalAiCopilotForSlicerMedicalImagingWorkflows/)** (Paul Dumont @ University of North Carolina at Chapel Hill, +) ([jumbojing/slicerClaw](https://github.com/jumbojing/slicerClaw))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/LocalAiCopilotForSlicerMedicalImagingWorkflows/"><img src="https://github.com/user-attachments/assets/9ab35d03-7c82-4825-ae67-9ca98d443329" style="max-width:480px;width:100%"></a>

This project develops a free, confidential, and fully local alternative to cloud-based LLMs for medical imaging workflows. To bypass expensive and non-private cloud infrastructure, we are building an offline AI Agent for 3D Slicer powered by Ollama. Specifically, we aim to evaluate the capability of these local models to leverage existing "Slicer skills" to execute agentic user tasks via the Slicer API. Finally, we will benchmark the performance, context-awareness, and reliability of these local models against established cloud baselines like Claude.

**Progress and Next Steps**

Progress: Reviewed current cloud-reliant MCP integrations (slicer-skill, mcp-slicer) and local LLM baselines (SlicerChat).


16. **[Low-Cost Tracked 3D Ultrasound Reconstruction with GE Vscan Air and NousNav](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/LowCostTracked3DUltrasoundReconstructionWithGeVscanAirAndNousnav/)** (Amirali Azimi @ Brigham and Women's Hospital, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/LowCostTracked3DUltrasoundReconstructionWithGeVscanAirAndNousnav/"><img src="https://github.com/user-attachments/assets/5172f187-588a-4f4a-872a-edb60e255742" style="max-width:480px;width:100%"></a>

Intraoperative brain shift reduces the accuracy of neuronavigation systems that rely on preoperative imaging. Updated intraoperative imaging can help restore navigation accuracy, but technologies such as intraoperative MRI and conventional cart-based ultrasound systems are not available in many surgical environments.

We are developing a lower-cost workflow for tracked three-dimensional ultrasound reconstruction using the wireless GE Vscan Air CL ultrasound probe and NousNav, an open-source neuronavigation platform implemented in 3D Slicer. During an ultrasound sweep, NousNav uses an optical tracking system to record the position and orientation of both the ultrasound probe and a patient reference frame. The goal is to associate each two-dimensional ultrasound frame with the corresponding tracking transform, position the frames correctly in three-dimensional space, and reconstruct them as a navigable three-dimensional ultrasound volume.

A proof-of-concept reconstruction has already been performed using ultrasound images acquired through the Vscan Air mobile application and tracking data transmitted using the PLUS Toolkit and SlicerIGT. However, the current workflow relies on screen-recorded ultrasound video, which reduces image quality and makes precise synchronization between ultrasound frames and tracking data difficult. Several additional components remain unresolved, including calibration of the ultrasound image plane relative to the tracked probe, registration of the reconstructed ultrasound volume to the patient coordinate system using the tracked reference frame, and integration of the current Python-based NIfTI reconstruction process directly into the 3D Slicer environment.

**Progress and Next Steps**

- Developed an initial proof-of-concept application for recording Vscan Air ultrasound video and NousNav tracking data during the same acquisition.
- Implemented collection of ultrasound probe and reference-frame tracking transforms through PLUS and OpenIGTLink.
- Created an initial workflow for extracting ultrasound frames from the recorded video and approximately matching them with tracking timestamps.
- Developed a preliminary Python-based reconstruction method for placing ultrasound frames in 3D space and exporting the result as a NIfTI volume.


17. **[MR2CBCT: Restoring and Extending Automated CBCT-MRI Registration for TMJ Analysis](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Mr2CbctRestoringAndExtendingAutomatedCbctMriRegistrationForTmjAnalysis/)** (Eduardo Duarte Caleme @ University of North Carolina, +) ([Slicer/Slicer](https://github.com/Slicer/Slicer))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Mr2CbctRestoringAndExtendingAutomatedCbctMriRegistrationForTmjAnalysis/"><img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW45_2026_Boston/Projects/Mr2CbctRestoringAndExtendingAutomatedCbctMriRegistrationForTmjAnalysis/Screenshot01.jpg" style="max-width:480px;width:100%"></a>

MRI-to-CBCT registration remains a pressing challenge in medical imaging. Simultaneous visualization of hard and soft tissue structures benefits both clinicians and patients in the diagnosis of temporomandibular degenerative joint disease. Challenges remain in accurately registering these two modalities due to differences in intensity distributions that complicate mutual information optimization, as well as the necessity for initial manual alignment, which can prove unintuitive and challenging for clinicians using current 3D Slicer tools.

**Progress and Next Steps**

- Fixed a critical bug in AREG_MRI.py where process_images() was never called.
- Fixed naming convention restrictions throughout the pipeline that proved unintuitive for clinicians.
- Fixed a mask size mismatch crash in apply_mask.py and a left/right label swap in TMJ crop side detection.
- Implemented clinician-friendly manual approximation tools, featuring options to freely translate the volume by dragging in slice views, rotate by dragging the circle edge, set a custom center of rotation, and center the MRI at the CBCT center of mass for extremely distant cases. This makes registration significantly easier and more accessible to clinicians and students.
- Successfully ran the registration pipeline on 25 cases outside of the initial validation sample, yielding clinically satisfying results.
- Implemented new registration mode (drag the image anywhere in the slice view) - https://github.com/Slicer/Slicer/pull/9258
- *Next Steps:* Robust automated approximation, increased Elastix capture range, and quantitative validation utilizing Target Registration Error (TRE).


18. **[Multi-material meshing with Slicer for orbital fracture repair FEM simulation](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/MultiMaterialMeshingWithSlicerForOrbitalFractureRepairFemSimulation/)** (Chi Zhang @ Texas A&M College of Dentistry, +) ([pieper/slicer-skill](https://github.com/pieper/slicer-skill))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/MultiMaterialMeshingWithSlicerForOrbitalFractureRepairFemSimulation/"><img src="https://github.com/user-attachments/assets/d9eef697-56aa-488f-8461-06ff95257839" style="max-width:480px;width:100%"></a>

Creating a volumetric mesh is essential for FEM simulation. However, meshing for orbital tissue with fracture is challenging due to multiple thin structures confined in a bony orbit, low CT contrast, and presence of trauma. To ease the process, we prepared a unified multi-material mesh for orbital tissue to avoid dealing with tissue boundaries. We are currently training a preliminary model using MONAI-nnUNet for orbital tissue segmentation using 13 specimens, each of which augmented to 5 additional volumns using TorchIO. We then created a unified orbital tissue segmentation, converted to a surface model, and created a tetrahedral mesh using gmsh. Sub-tissue regions were then selected in SOFA using specific tisssue surface models. Overall, though much easier than creating multiple tissue meshes, this step still requires many manual steps, including segmentation refinement and surface model downsampling and uniform remeshing, in Slicer and gmsh. Furthermore, due to the coarseness of interior tetrahedra, the selected tetrahedra could not accurately reflect internal tissue geometry, creating errors in tissue geometry tracking in simulation. Mesh refinement was used to create finer elements at interior tissue surface but it led to a over-detailed mesh with too many elements.

**Progress and Next Steps**

Using claude slicer-skill [https://github.com/pieper/slicer-skill](https://github.com/pieper/slicer-skill) to create a prompt to streamline a segmentation to meshing workflow. Overall it took me five hours. 

Initially, I tried to teach it step-by-step. Giving sample outcomes from my own manual preprocessing as ground truth helped.

Steps:
- Create a combined orbital tissue segment from individual segments
- Create a 0.5 mm gap between tissue segment & bony orbit: expand the skull by 0.5mm and subtract tissue segment from it
- Smoothing the segment, fill all internal holes, and removing isolated voxels.
- Convert combined orbital tissue segment to a surface model and downsample + uniform remesh it to about 1.5k pts
- Using a customized gmsh script to do the meshing. Redo surface remesh and/or gmsh spacing set up until getting around 10 to 15K tetrahedra.


19. **[New 3D Slicer Module to predict surgery movement for maxillofacial surgery](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/New3DSlicerModuleToPredictSurgeryMovementForMaxillofacialSurgery/)** (Alexandre Buisson @ University of North Carolina at Chapel Hill, +) ([DCBIA-OrthoLab/SlicerAutomatedDentalTools](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/New3DSlicerModuleToPredictSurgeryMovementForMaxillofacialSurgery/"><img src="https://github.com/user-attachments/assets/40e31807-6507-4743-b3e6-e130736a4ab1" style="max-width:480px;width:100%"></a>

Predicting surgical movements and bone displacement vectors in virtual surgical planning software remains an expert-intensive task, requiring surgeons to simulate osteotomies and manually adjust bone segments. Although statistical shape models and deep learning regression networks have been explored to automate this phase, they output dense deformation fields that lack the geometric interpretability needed to guide clinical or surgical decisions.

This project introduces a dedicated 3D Slicer module driven by a Machine Learning Stacking model, trained on a robust dataset of 1,496 patients. The module simplifies the clinical workflow by allowing users to upload an input file (e.g., Excel/CSV containing clinical parameters) and instantly receive accurate, data-driven predictions of the required maxillofacial bone movements.

**Progress and Next Steps**

The core Stacking ML model has been successfully trained and validated using a dataset of 1,496 patient cases.

During the project week we'll build an interactive UI and backend pipeline within 3D Slicer to handle file inputs and run the model's prediction pipeline.
Also, we'll verify the accuracy of the outputs within the Slicer environment and explore intuitive ways to display the predicted movements to the user.


20. **[NousNav Project Updates](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/NousnavProjectUpdates/)** (Sam Horvath @ Kitware, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/NousnavProjectUpdates/"><img src="https://github.com/user-attachments/assets/812490c5-0213-45fd-86dd-ea734efcb55b" style="max-width:480px;width:100%"></a>

The NousNav project is an initiative led by Dr Alexandra Golby to develop a low-cost neuronavigation system designed for use in low- and middle-income countries. We are developing a 3D Slicer based application focused on supporting segmentation, registration and navigation tasks.

The project will also include the development of open source hardware desgins for these applications.

This week will include continued development on the NousNav project, in preparation for work with new collaborators.  This includes new usability features, UI refinement and updating the guidance images for the patient registration.

**Progress and Next Steps**

- Generate installers for NousNav 1.1
    - In progress, pending IGSIO build fixes
- 1.2 tasks finished:
  - Add recenter views toolbar button — New toolbar button (Google Material "my_location" icon) next to the screenshot button that recenters all 2D slice views and resets 3D cameras.
  - Update registration guidance images — Updated images used during the registration workflow.
  - Fix picture layout image scaling to maintain aspect ratio — Replaced ctkThumbnailLabel with QLabel and added a resize event filter to scale images proportionally using KeepAspectRatio.
  - Fix tab bars to fit all tabs without scrolling — Disabled scroll buttons on primary and secondary tab bars, removed min-width: 200px from tab QSS rules, and zeroed spacer stretch factors so tabs share available space. Closes #322.
  - Reduce module panel width to give more space to central layout — Scaled down per-page widget sizes by ~5% (fonts, margins, min-heights) and set minimum size policy on the module panel.
  - Add user-settable RMSE error thresholds in settings dialog — Added a new "Error Thresholds" section to the settings dialog with spin boxes for pivot, spin, registration, initial registration, and conditional registration RMSE thresholds, persisted via QSettings.
  - Replace flake8 with ruff for pre-commit linting — Swapped flake8 for ruff (v0.15.17) in .pre-commit-config.yaml, created ruff.toml with equivalent rules adapted from Slicer, and auto-fixed 89 whitespace issues.
- Work on addressing licensing concerns from MGB


21. **[Porting lung ultrasound analysis software from 3D Slicer to OHIF](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/PortingLungUltrasoundAnalysisSoftwareFrom3DSlicerToOhif/)** (Dave Dinh @ BWH, +) ([SlicerUltrasound/SlicerUltrasound](https://github.com/SlicerUltrasound/SlicerUltrasound))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/PortingLungUltrasoundAnalysisSoftwareFrom3DSlicerToOhif/"><img src="https://github.com/user-attachments/assets/00192df6-e400-4f88-8c45-7a2d66feb4e8" style="max-width:480px;width:100%"></a>

Our team has been developing various 3D Slicer modules for lung ultrasound analysis (https://github.com/SlicerUltrasound/SlicerUltrasound), from de-identification to annotation and adjudication. However, we have slowly started porting the extensions developed in Slicer to OHIF, as this is easier for the clinicians and other researchers to use. It doesn't require them to install any additional software, and they can access OHIF from the web. 

Initial work has been performed by the Radical Imaging team to update OHIF with the B-line quantification tools that our team requires. However, there are some improvements that still need to be made: 
- We need to make sure annotation of the pleural lines and B-lines are supported, and that the resulting files are saved appropriately. 
- We would like to have single-rater vs multi-rater modes, where the multi-raters can work together to discuss a case, or adjudicate the annotations.

**Progress and Next Steps**

- Describe specific steps you **have actually done**.


22. **[Qt6 and arm64 Slicer builds on the factory machines](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Qt6AndArm64SlicerBuildsOnTheFactoryMachines/)** (Sam Horvath @ Kitware, +) ([Slicer/Slicer](https://github.com/Slicer/Slicer))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Qt6AndArm64SlicerBuildsOnTheFactoryMachines/"><img src="https://github.com/user-attachments/assets/4fd30f74-7d08-4eef-ac51-5879955f6e7c" style="max-width:480px;width:100%"></a>

This week we will be finalizing the 5.12 release, and then working on moving the factory builds to Qt6 and arm64 (for macOS). These are the critical changes for the next major release Slicer 6.

**Progress and Next Steps**

- Release Slicer 5.12 ✔️
    1. Ensure macOS signing is working properly ✔️
- Create qt build image: https://github.com/Slicer/SlicerBuildEnvironment/tree/main/Docker ✔️
    1. Initial image has been built successfully: https://hub.docker.com/r/slicer/buildenv-qt6-almalinux8-gcc14
- Install Qt6 on Windows factory
- Begin setting up arm64 factory machine


23. **[Recon-all correction script based on manual subcortical segmentation files](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ReconAllCorrectionScriptBasedOnManualSubcorticalSegmentationFiles/)** (Jarrett Rushmore @ Center for Morphometric Analysis, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ReconAllCorrectionScriptBasedOnManualSubcorticalSegmentationFiles/"><img src="https://github.com/user-attachments/assets/4a51c349-5b44-49f5-895e-b5648b22506d" style="max-width:480px;width:100%"></a>

White and pial surfaces and parcellation (aparc+aseg) from recon-all pipeline (FreeSurfer 7.4.1) need quite a few manual corrections.
At the same time, 100 cases from HCP-YA dataset were manually segmented using HOA2 atlas.
The goal of the project is to leverage the latter to get better results with recon-all.

**Progress and Next Steps**

- merge_hoa_into_aseg.py works properly
- Final result is good: surfaces and parcellation are HOA compatible (minimal corrections needed)
- nnUNet trained model didn't segment properly WM/GM
  - add HOA subcortical labels to help segmentation
  - compare with other models (like Unest)


24. **[Redesigned REST API and MCP server for Imaging Data Commons](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/RedesignedRestApiAndMcpServerForImagingDataCommons/)** (Andrey Fedorov @ BWH, +) ([ImagingDataCommons/imaging-data-commons-skill](https://github.com/ImagingDataCommons/imaging-data-commons-skill))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/RedesignedRestApiAndMcpServerForImagingDataCommons/"><img src="https://github.com/user-attachments/assets/83ba0f17-ed92-4066-85f2-cfcd0a4eeb7a" style="max-width:480px;width:100%"></a>

**Questions? Want to participate remotely? Join our project [Discord channel](https://discord.gg/TTFGUYGdsZ)!**

TL;DR: Work on v3 of [Imaging Data Commons (IDC)](https://portal.imaging.datacommons.cancer.gov/) REST API simultaneously with the development of the IDC [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) server.

IDC already offers a customized agent skill in [https://github.com/ImagingDataCommons/imaging-data-commons-skill](https://github.com/ImagingDataCommons/imaging-data-commons-skill), which is very powerful in helping with the use of IDC. However, in order to use it effectively, the user needs to have access to an LLM platform that supports code execution, and needs to suffer the "cold start" cost of setting up the environment. IDC MCP interface can provide "zero startup cost" solution for answering at least some of the queries, optimized for the use by agents. At the same time, MCP interface will need to rely on IDC API, which in its current v2 form is not useful at all. We are in the process of simultaneous redesign of IDC API and design of the MCP interface. Since we do not have expertise on the team doing something like this before, we would appreciate community feedback.

**Progress and Next Steps**

- Developed v3 of IDC REST API and the initial version of MCP server - [repo and overview](https://github.com/fedorov/IDC-API/blob/idc-api-v3/docs/user-guide.md)
- Shared MCP server endpoint with interested users, collected feedback (in particular, identified the need to improve support of clinical data)
- Improved MCP integration with Martin's project [https://github.com/mbellehumeur/vtk-js/pull/1](https://github.com/mbellehumeur/vtk-js/pull/1)
- Implemented support for clinical tables query.
  * [public linkt to a conversation with Claude](https://claude.ai/share/85b9d201-1f85-4492-9b9b-311bf98b09f5) demonstrating the capabilities of clinical data exploration with the updated IDC MCP server
- Summarized (but not benchmarked!) differences between using "vanilla" Claude vs Claude + IDC skill vs Claude + IDC MCP.
- 3rd party security review by Ryan completed.


25. **[Robust Segmentation Experience in OHIF Viewer](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/RobustSegmentationExperienceInOHIFViewer/)** (Jaeyoung Cho @ University Hospital Bonn, +) ([CCI-Bonn/OHIF-AI](https://github.com/CCI-Bonn/OHIF-AI))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/RobustSegmentationExperienceInOHIFViewer/"><img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW45_2026_Boston/Projects/RobustSegmentationExperienceInOHIFViewer/ohif-segmentation-stats-mpr.png" style="max-width:480px;width:100%"></a>

OHIF Viewer is a widely used web-based medical image viewer built on Cornerstone3D. Segmentation is central to many clinical and research workflows, yet reliability and robustness in OHIF/Cornerstone still lag behind user expectations — with recurring errors and edge cases in everyday use ([OHIF/Viewers#5453](https://github.com/OHIF/Viewers/issues/5453)).

During Project Week 45, I would like to focus on improving the stability and user experience of segmentation in OHIF/Cornerstone. This builds on ongoing work in [OHIF-AI](https://github.com/CCI-Bonn/OHIF-AI) — an OHIF-based viewer with server-side AI integration (SAM2, nnInteractive, MedSAM2, and related tools) at University Hospital Bonn — where segmentation workflows are central to day-to-day use. I am looking forward to collaborating with others interested in segmentation, digital pathology, and web-based imaging viewers.

This project targets two complementary areas:

- **DICOM-SEG landscape** — Understand the development and history of DICOM Segmentation, current standard direction (including label-map encodings), and recommended usage for save/load and interchange with research formats.
- **Overlapping segments in OHIF** — Ensure overlapping segmentations work reliably across **Stack Viewport + MPR**, **Volume Viewport**, and downstream tools — **segmentation statistics** and **bidirectional measurements**.

Several related gaps remain in the broader stack: overlapping segmentations are not always handled reliably across viewport types, DICOM persistence paths are still evolving ([PR #5806](https://github.com/OHIF/Viewers/pull/5806), [#4875](https://github.com/OHIF/Viewers/issues/4875)), and contour ↔ labelmap conversion is not yet exposed end-to-end in OHIF. This project aims to advance solutions within Cornerstone3D and OHIF toward a more dependable segmentation experience.

For DICOM persistence, standards context, and recommended interchange with research formats (NIfTI), see [Background and References](#background-and-references).

**Progress and Next Steps**

- **DICOM-SEG review** — Summarize standard history (binary SEG → label-map Sup 243), tooling roles (dcmjs, highdicom, dcmqi, etc.), and recommended save/load paths; validate against [PR #5806](https://github.com/OHIF/Viewers/pull/5806) ([background notes](#dicom-seg-and-format-interchange)).
- **Reproduce overlapping-segment issues** — Triage reports (e.g. [#5453](https://github.com/OHIF/Viewers/issues/5453), [Cornerstone3D PR #2170](https://github.com/cornerstonejs/cornerstone3D/pull/2170)) across Stack + MPR and Volume viewports.
- **Fix overlapping segment rendering** — Investigate segment blending/ordering in Cornerstone3D so multiple overlapping segments render and interact correctly in all target viewport types.
- **Connect stats and bidirectional measurements** — Verify segmentation statistics (volume, HU stats, voxel count) and bidirectional tool output remain correct when segments overlap and when switching between Stack/MPR and Volume layouts.


26. **[Slicer Chest Imaging Platform Reboot](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicerChestImagingPlatformReboot/)** (Kalysta Makimoto @ Brigham and Women's Hospital, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicerChestImagingPlatformReboot/"><img src="https://github.com/user-attachments/assets/821d8abe-1044-4bcf-a92c-3ab0d0e98efd" style="max-width:480px;width:100%"></a>

`The Chest Imaging Platform (CIP)` is an open-source software suite developed by the `Applied Chest Imaging Laboratory (ACIL)` at Brigham and Women's Hospital (Harvard Medical School). Slicer CIP is designed for quantitative chest CT analysis, helping clinicians and researchers identify and measure phenotypes for Chronic Obstructive Pulmonary Disease (COPD), Interstitial Lung Disease (ILD), Acute Lung Injury (ALI), Pulmonary Vascular Pruning, and Lung Cancer.

**Progress and Next Steps**

Progress
- Reviewed the current SlicerCIP modules to identify which modules could be used as a template.
- Installed the TotalSegmentator extension and tested to ensure segmentations are generated.
- Developed the CIP Rib Analysis Module to align with the developed methodology.
- Tested the CIP Rib Analysis Module with an existing segmentation and a segmentation generated using the slicer TotalSegmentation module.
- Developed the CIP SYBIL Module.
- Tested the CIP SYBIL Module in the most recent Slicer version. 

Next Steps
- Update the CIP Rib Analysis Module to accept segmentations from additional methods (e.g. MOOSE).

Issues
- SYBIL is dependent on torch 1.13 (2 years old) with no plans to update to newer torch versions due to lightening inferance issues. CIP SYBIL Module is dependent on Slicer version 5.8 or lower.


27. **[Slicer-to-Action for surgical robot imitation learning](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicerToActionForSurgicalRobotImitationLearning/)** (Taewoo Yoon @ AIRS Inc, +) ([huggingface/lerobot](https://github.com/huggingface/lerobot))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicerToActionForSurgicalRobotImitationLearning/"><img src="https://github.com/user-attachments/assets/99518a87-4d88-4dd1-acc5-0b851af118d4" style="max-width:480px;width:100%"></a>

We are developing a robotic system for fracture reduction using SlicerROS2. The goal of this project is to investigate whether recent imitation learning approaches, such as visuomotor policies or Vision-Language-Action (VLA) models, can be applied to this robot system.
In this project, 3D Slicer functions as a tool to display real-time object movements in a 3D view. 
We intend to utilize this **3D view as training data for robotic motion**.
The 3D Slicer view will function just like a real camera mounted on the robot.

**Progress and Next Steps**

**1. Synthetic Training Data Generation**   
Randomly generate diverse bone fragment configurations.  
Generate and apply a reduction trajectory that reduces each configuration.  
During the reduction process, capture images from four views (Axial, Lateral, Medial, ISO) in 3D Slicer, and store the corresponding strut lengths as an episode.  
Save the data as a dataset of 100+ episodes.  
**2. Training Policy**  
Feed the stored dataset into the LeRobot visuomotor policy framework.  
Train an ACT (Action Chunking with Transformers) policy to obtain the policy network (100K steps, loss < 0.03).  
**3. Run Reduction**  
Randomly generate an arbitrary bone fragment configuration.  
(1) Capture the four views in Slicer and feed them, together with the corresponding strut lengths, into the policy as the observation.  
(2) Infer strut lengths.  
(3) Perform forward kinematics analysis and update the robot's pose.  
(4) Return to (1) and iterate.


28. **[SlicerSOFA simulation for predicting soft tissue restoration after orbital fracture](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicersofaSimulationForPredictingSoftTissueRestorationAfterOrbitalFractureRepair/)** (Chi Zhang @ Texas A&M College of Dentistry, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicersofaSimulationForPredictingSoftTissueRestorationAfterOrbitalFractureRepair/"><img src="https://github.com/user-attachments/assets/241d7938-4b61-42e1-b402-16a42be4b926" style="max-width:480px;width:100%"></a>

Orbital fractures are typically caused by blunt-force trauma. Fracture repair frequently requires placing a titanium plate to reconstruct bony orbit and restore tissue position and function from disturbed conditions, such as enophthalmos ("sunken eye") and muscle entrapment & conformational changes. 

This project aims to develop a reproducible and scalable patient-specific SOFA/SlicerSOFA FEM simulation workflow to predict orbital soft tissue restoration after fracture repair using a preformed titanium plate.The simulation processes span across multiple scenes from retracting orbital tissue to place a plate and then let the tissue fall onto the plate. The only deformable object is a unified multi-material orbital tissue mesh. Tetrahedrons inside different tissue regions to assign with different material properties. The retracting tool, plate, and bony orbit are all simulated as rigid bodies.

Currently, it still relies on many steps of manual set up in Slicer, including retraction plane position and moving trajectory and distances, attachment points, input/output across staged scenes, and tissue-bone attachment points.

**Progress and Next Steps**

- Convert a SOFA scene into a Slicer scene and created a prototype module using SlicerSOFA infrastructure
- Use sequence module to generate a playback sequence recording.<br>

- Newton Physics demo

Next steps
- Continue improve workflow reproducibility and gui for fracture cases
- Compare outcome with post-op images for more optimization and improvment.


29. **[SlicerVirtualReality - OpenXR Update, Passthrough Support, Interactions Refactor](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicervirtualrealityOpenxrUpdateAndPassthroughSupport/)** (Kyle Sunderland @ Queen's University, +) ([Sunderlandkyl/VTK](https://github.com/Sunderlandkyl/VTK))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SlicervirtualrealityOpenxrUpdateAndPassthroughSupport/"><img src="https://github.com/user-attachments/assets/c1e406e5-4887-4c43-b370-694434bd1fcc" style="max-width:480px;width:100%"></a>

Currently SlicerVirtualReality is compiled using an older version of OpenXR. This project aims to finalize the integration of the latest version of OpenXR, as well as adding requested features such as passthrough using Meta Quest headsets.

**Progress and Next Steps**

- Initial implementations can be found here:
   - https://github.com/Sunderlandkyl/VTK/tree/openxr_passthrough_slicer-v9.6.2-2026-05-15-f49a1dbaf
   - https://github.com/Sunderlandkyl/SlicerVirtualReality/tree/openxr_passthrough_update

- Discussion on updating interaction events:
    - VR Event Handling Levels
      1. Json file maps device specific buttons to device independent buttons ex. Button 1, Button 2, Joystick1, Trigger1, Grip1 etc.
      2. SlicerVirtualReality handles mapping from device independent events to interaction events ex. Pick3DEvent, Pick3DLineEvent, etc.
      3. Displayable managers handle events in the same way that they handle mouse and keyboard interaction events.

- Summary of code changes:
   - **OpenXR runtime update & passthrough**: updated the bundled OpenXR SDK to 1.1.60 and added AR passthrough (`XR_ENVIRONMENT_BLEND_MODE_ALPHA_BLEND`) to `vtkMRMLVirtualRealityViewNode`/`qMRMLVirtualRealityView`. Also implemented environment-depth occlusion (`XR_META_environment_depth`), debug visualization, and VR scene/depth volume capture; these controls are hidden in the module UI for now since depth occlusion isn't functional with the current Meta runtime.
   - **Generic controller actions**: `SetupActions()` now registers the 28 generic Oculus Touch actions directly (5 default to the legacy VTK 3D events they replace, to preserve existing behavior; the rest keep their own generic event IDs for raw observability). All are rebindable from Python via the existing `AddAction()` helper, and are now invoked on the interactor.
   - **Interaction fixes**: grip button mapped to the "move prop" event; fixed complex gesture handling; added trigger click actions; fixed a bug where grabbed objects would slowly drift ("crawl away") during manipulation (root cause: `vtkTransform::SetMatrix()` updates internal state but never calls `Modified()`, so MRML's observer notifications weren't firing -- switched to `vtkMRMLTransformNode::SetMatrixTransformToParent()`, which does).
   - **UI**: the VR toolbar button now toggles the hardware connection (useful for exiting immersive mode or resetting the connection) instead of toggling rendering enable, which wasn't useful.
   - **Controller render models**: OpenXR has no API for rendering controller models, so vtkRenderingOpenXR falls back to a profile-to-asset JSON lookup table that has to be located next to the VTK build/install tree. Added a JSON mapping entry and a bundled glTF model for the Meta Quest Touch Plus controllers (previously only a generic placeholder rendered in headset), and moved the whole controller-models setup (Meta Quest Touch Plus, HTC Vive, Valve Index) into the module's own `Resources/ControllerModels/`, deployed via CMake and wired up through `vtkOpenXRRenderWindow::SetModelsManifestDirectory()`, so it survives a clean rebuild instead of depending on files manually placed in the VTK build tree.
   - Documentation ([DeveloperGuide](https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md#controller-event-ids), and [User guide](https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/README.md)) updated to match the above. List of observable/overridable controller events is available [here](https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md#controller-event-ids).


30. **[Slicey - an AI coding agent built into 3D Slicer](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SliceyAiCodingAgentFor3DSlicer/)** (Andras Lasso @ Queen's University, +) ([PerkLab/SlicerSandbox](https://github.com/PerkLab/SlicerSandbox))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/SliceyAiCodingAgentFor3DSlicer/"><img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW45_2026_Boston/Projects/SliceyAiCodingAgentFor3DSlicer/SliceyScreenshot01.jpg" style="max-width:480px;width:100%"></a>

Slicey is a new scripted module (in the [SlicerSandbox](https://github.com/PerkLab/SlicerSandbox) extension) that embeds an AI coding agent directly inside 3D Slicer. Instead of copy-pasting code snippets into the Python console or running a separate MCP server, the user chats with Claude in a panel docked in Slicer, and Claude can read/write files in folders the user explicitly shares, and write and execute Python code in a real, running Slicer session (either the user's current window or an isolated companion instance) to carry out the request.

**Progress and Next Steps**

Built over the course of the project week, mostly generated by Claude Sonnet. The [Slicey module](https://github.com/PerkLab/SlicerSandbox/tree/master/Slicey) module is available in the Sandbox extension for Slicer-5.12 and later. Details:

- **Add Slicey AI chatbot** - initial module: chat panel embedded in Slicer, Claude API integration, and the first tool set giving the agent shared-folder file access plus the ability to run Python code in Slicer.
- **Improve Slicey user interface** - added a live billing/cost-estimate display and an improved UI layout.
- **Improved Slicey GUI** - simplified the layout further and added a section for appending custom instructions to the system prompt.
- **Fix Slicey tool-call bugs, add chat logging and console output access**:
   - Raised `max_tokens` and added actionable error messages so large tool calls (e.g. writing a whole file) don't get silently truncated.
   - Fixed conversation corruption when Stop is clicked mid tool-call, and made the chat self-heal histories that were already stuck in that state.
   - Made the Execution setting (current Slicer window vs. separate companion instance) actually control where `run_python_in_slicer` runs, instead of Claude picking "current" regardless of the user's choice.
   - Added per-chat Markdown logging (to a configurable folder, updated live as messages come in) and renamed "Clear chat" to "New chat".
   - Added `getPythonConsoleOutput()` so Claude can inspect recent activity in Slicer's own Python console, including output from the user's manual GUI interactions.

Next steps: gather feedback from other Project Week participants on the chat UX and tool set, consider additional tools (e.g. scene-introspection helpers, screenshot capture), and continue hardening the agent loop.


31. **[Standardizing DICOM De-ID with Actionable Rules and Tests](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/StandardizingDicomDeIdWithActionableRulesAndTests/)** (Dave Dinh @ BWH, +) ([clintools/dicom-curate](https://github.com/clintools/dicom-curate))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/StandardizingDicomDeIdWithActionableRulesAndTests/"><img src="https://github.com/user-attachments/assets/323d698e-72f9-49c7-8b62-e578f381987b" style="max-width:480px;width:100%"></a>

DICOM de-identification (De-ID) efforts often overlap in the rules used to process DICOM metadata. This project aims to translate [an existing DICOM De-ID standard](https://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_E.1.1) into a set of actionable rules that can serve both as an implementation guide and as a verifiable audit trail for tools and AI systems.
For example, a standard may permit multiple actions for a given metadata field. A baseline reference can recommend a default action, while still allowing users to specify alternative behaviors as needed. The proposed generator will take user input and produce:

- A reference list of itemized, actionable rules
- A unit and end-to-end test specification that users can apply to their specific use cases

The initial user interface for the generator will be a command-line (CLI) tool. It will operate based on a predefined decision tree and output rules and test specifications in formats suitable for humans, AI systems, and supported programming languages.

In practice, DICOM De-ID outputs can vary depending on modality, imaging protocols, contractual requirements, and application domains. However, there remains a consistent need to validate that outputs conform to a predefined set of rules. This library represents a step forward in programmatically generating verifiable rules for reliable and consistent implementation.

**Progress and Next Steps**

Open source project and integrate with two existing de-id projects: pipeline for batch dicom de-id and an OHIF mode for verifying de-id DICOMs.


32. **[That Rendering Thing](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ThatRenderingThing/)** (Steve Pieper @ Isomics, +) ([pieper/SlicerCL](https://github.com/pieper/SlicerCL))

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ThatRenderingThing/"><img src="https://github.com/user-attachments/assets/7a71cf08-c4db-494b-90ef-c7292b4dfa00" style="max-width:480px;width:100%"></a>

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

**Progress and Next Steps**

* Volume render automatically on load
* Render 3D during segmentation
* Instant 3D editing feedback - no surface model built
* Nicer compositing


33. **[Vox2SegLAM: Protocol-Guided Subcortical Segmentation in 3D Slicer](https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Vox2SeglamProtocolGuidedSubcorticalSegmentationIn3DSlicer/)** (Ahmed Rekik @ École de technologie supérieure, +) (no github repo yet)

<a href="https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Vox2SeglamProtocolGuidedSubcorticalSegmentationIn3DSlicer/"><img src="https://github.com/user-attachments/assets/51fcdf47-e1a7-4318-ac84-38637db7b6bc" style="max-width:480px;width:100%"></a>

3D SlicerVox2SegLAM is an extension that brings an AI-assisted, protocol-guided workflow to subcortical brain segmentation and landmarking. A joint CNN+GNN model predicts 26 subcortical structures and 20 anatomical landmarks directly from a T1 MRI, following the Harvard-Oxford Atlas (HOA 2.0) neuroanatomical protocol.

**Progress and Next Steps**

**Done:**
- Trained the joint CNN+GNN model: mean Dice = 0.908 ± 0.010 across 26 subcortical structures .
- Achieved a mean landmark localization error of 1.4 mm under strict point-to-point evaluation, improving to 1.1 mm under an anatomically-tolerant evaluation that accounts for legitimate placement ambiguity (e.g., any voxel along the correct structure boundary or within the correct coronal region counts as correct), across the 20 predefined HOA2.0 landmarks.

**Next steps (at/after PW45):**
- Built the core of the Slicer extension: inference adapter, protocol rule parser for the HOA protocol and the geometry engine (plane and landmarks fitting.
- Validated qualitatively on in-domain test data and on out-of-domain scans, confirming anatomically plausible predictions outside the training distribution.
- Work with Dr. Rushmore to refine the protocol rule set and run a usability/annotation-time study comparing manual vs. AI-assisted annotation.

