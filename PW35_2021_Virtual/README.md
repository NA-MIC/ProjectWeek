

## Welcome to the web page for the 35th Project Week!

This event will be held virtually June 28-July 2, 2021.

## Numbers and Introduction
- **121** Registered Attende. **44%** First Timers!
- **23** countries.
  - Bimodal Time Zone Distribution (UTC-4 and UTC+1.
- **29** Projects.
- All sessions except for work in project teams will happen on Zoom.  Please see google calendar entries for links for both zoom and discord.
- Begin with the good old recipe of in-person Project Weeks.
  - Each team delegates a member to present the project in a maximum of 90 seconds using the project page.
  - Hope your project page is ready and any image you want to show is up there. There will not be enough time to share your screen, we will simply share your project page on the zoom session.
- Presenters - please stick with the allocated time, if your internet connection has problems during your presentation, we will move to the next speaker and we can accommodate your talk at the, end time permitting.
- Audience - please ask the speaker questions using zoom chat or the discord server chat.
- Work in project teams will happen throughout the week.
  - A Discord server has been set up with a voice/video channel and a text channel for every project on the main webpage.
  - We will have a walkthrough of the discord server and project channels as the last project presentation today.
  - You can use the channels to coordinate the work of your team.
  - It is recommended to hold a first meeting of the team on the voice channel of the project after project presentations on Monday.
  - Please do everything you can to accommodate all team members in terms of schedule, especially the ones with family constraints living in time zones that are less favored by the schedule of Project Week.
- The program includes optional introductory lectures (8-9:30 Tue-Wed-Thu) and breakout sessions (10-12 Tue-Wed-Thu), all happening on Zoom.
  - Tuesday: AI-assisted annotations (lectures), What’s new in Slicer and a QnA session that was very popular last year
  - Wednesday: Image Guided Surgery lectures and breakout session on the same topic
  - Thursday: Web-based tools lecture, and breakout session on Human Brain Atlases
- We will end the week with project results presentation. A member from each team will present their results in a maximum of 90 seconds minutes using project page as a visual support for the presentation, so please make sure it is up to date with your latest results by Friday morning.


### Attendees
- **Step 0**: **REGISTER** [here](https://forms.gle/evnWqMu4dnsx3Mei9)
- **Step 1**: Sign-up on the **[discourse forum](https://discourse.slicer.org/c/community/project-week)** to get updates and ask questions.
- **Step 2** (optional): Join the **Discord** server to help prepare and work on your project: [Invite Link](https://discord.gg/5TC5H2g63e)


##  Agenda

<div id="calendar-container">
</div>

<!--
Adapted from https://stackoverflow.com/questions/31821974/support-user-time-zone-in-embedded-google-calendar
-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jstimezonedetect/1.0.7/jstz.min.js" integrity="sha512-pZ0i46J1zsMwPd2NQZ4IaL427jXE2RVHMk3uv/wPTNlBVp9AbB1L65/4YdrXRPLEmyZCkY9qYOOsQp44V4orHg==" crossorigin="anonymous"></script>

<!--
<iframe id="calendar-container" src="https://calendar.google.com/calendar/embed?src=kitware.com_sb07i171olac9aavh46ir495c4%40group.calendar.google.com&ctz=Atlantic&mode=WEEK&dates=20210628%2f20210702" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
-->
<script type="text/javascript">
  var timezone = jstz.determine();
  var iframe_src = 'https://calendar.google.com/calendar/embed?src=kitware.com_sb07i171olac9aavh46ir495c4%40group.calendar.google.com&mode=WEEK&dates=20210628%2f20210702&ctz=' + timezone.name()
  var iframe_html = '<iframe src="' + iframe_src + 'style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>'
  document.getElementById('calendar-container').innerHTML = iframe_html;
</script>

[How to add this calendar to your own?](../common/Calendar.md)

<a name="ProjectsList"/>

## Breakout sessions complementary material
* [What's new in Slicer](https://docs.google.com/presentation/d/19LIMkLDmTmuJoA-5CFNjWNosoAYB4OoyvyUNryurMSE/edit?usp=sharing)(Andras Lasso, Jean-Christophe Fillion-Robin, Sam Horvath, Steve Pieper)
* [MONAI introductory presentation](https://drive.google.com/file/d/1haqTUNLGVeE0V-qBVuuFqIhKXZFpkBAf/view) (Wenqi Li, NVIDIA)
* [MONAI Label introductory presentation](https://docs.google.com/presentation/d/1FYv23AbFPloTKcsTrP75bKI1XStULVlUSI6ZF3VCp-Y/edit?usp=sharing) (Andres Diaz-Pinto, King's College London)
* [DICOM Overview](supplementary-material/DICOM-Overview.pdf) (Steve Pieper)
* [OHIF v3 and a glance into Cornerstone 3D](https://docs.google.com/presentation/d/1KYNjuiI8lT1foQ4P9TGNV0lBhM6H-5KBs0wkYj4JJbk/edit?usp=sharing) (Erik Ziegler, Alireza Sedghi)
* [NCI Data Commons](https://docs.google.com/presentation/d/1-_oHDbYqArylwF2K2aAy1mD0-C0F9gu-UFvJ8lpDWS4/edit?usp=sharing) (Andrey Fedorov)

## Projects [(How to add a new project?)](Projects/README.md)
### VR/AR and Rendering
1. [PRISM volume rendering](Projects/PRISM_volume_rendering/README.md) (Simon Drouin, Steve Pieper, Kyle Sunderland, Andrey Titov, Rafael Palomar)
1. [SlicerVR build and in-VR widgets](Projects/SlicerVR/README.md) (Csaba Pinter, Adam Rankin, Jean-Christophe Fillion-Robin)
1. [Virtual cameras](Projects/VirtualCameras/README.md) (Étienne Léger, Tamas Ungi, Andras Lasso)
1. [TMS Visualization in Slicer](Projects/TMS_Slicer_Module/Readme.md) (Loraine Franke, Lipeng Ning, Yogesh Rathi, Steve Pieper, Raymond Yang, Daniel Haehn)
1. [AR in Slicer](Projects/ARinSlicer/README.md) (Alicia Pose Díez de la Lastra, Javier Pascau, Csaba Pinter)
1. [Interactive Slice Intersections](Projects/InteractiveSliceIntersections/README.md) (David García-Mato, Kyle Sunderland, Csaba Pinter)
1. [VR for Birth Delivery Training](Projects/VRBirthDeliveryTraining/README.md) (Mónica García-Sevilla, David García-Mato, Abián Hernández-Guedes, Juan Ruiz Alzola, Javier Pascau, Nayra Pumar, Csaba Pinter)
1. [VR display plugin for PyDBS using a zSpace device](Projects/VRDisplayPluginForPyDBSUsingZspace/README.md) (Marine Camba, Sara Fernandez Vidal, Sinan Haliyo)

### IGT
1. [NousNav](Projects/NousNav/README.md) (Alexandra Golby, Sam Horvath, Sarah Frisken, David Allemang, Tina Kapur, Steve Pieper, Jean-Christophe Fillion-Robin, Sonia Pujol)
1. [DBS Navigation](Projects/DBSNavigation/README.md) (Simon Oxenford)
1. [Slicer module for planning MR-guided focal cryoablation of prostate cancer](Projects/ProstateCryoablationPlanning/README.md) (Pedro Moreira)
1. [Slicer-Liver: planning liver resections in 3D Slicer](Projects/Slicer-Liver/README.md) (Rafael Palomar, Gabriella d'Albenzio, Ole Vegard Solberg, Geir Arne Tangen)
1. [ROS2 - 3D Slicer Integration](Projects/ROSMED/README.md) (Junichi Tokuda, Tamas Ungi, Axel Krieger, Simon Leonard, Mark Fuge)
1. [IGT training material for francophone countries](Projects/IGTrain/README.md) (Nayra Pumar, Mohamed El Moctar Septy, Yahya Tfeil, Asmaa Skareb, Marilola Afonso, Juan Ruiz Alzola)
1. [GPU Rigid Registration](Projects/GPURigidRegistration/README.md) (Gelel Rezig, Houssem Eddine Gueziri, Simon Drouin)
1. [Planar Osteotomies Virtual Surgical Planning And Patient-Specific Surgical Guides](Projects/PlanarOsteotomiesVSPAndSurgicalGuides/README.md) (Mauro I. Dominguez, Manjula Herath)
1. [Marklerless Tracking for Low-Cost neuronavigation for TMS](Projects/MarkerlessTrackingWithRGBDCamerasForLowCostNeuronavigation/README.md) (Julie Alvarez (Neurotrauma Center), Gabriel Vargas Grau (Universidad de Santander), Juan Camilo Gamboa (Mc Gill University), Andrés Gamboa (Neurotrauma/Universidad Politécnica de Valencia/))
1. [IGT Equipment for ReUse](https://docs.google.com/spreadsheets/d/1MNkcZFz4GulkjOL4V5PYLzRwrgUT3rNB_mnKSHBq7aw/edit?usp=sharing) (Tina Kapur, Gabor Fichtinger, +)
1. [OpenIGTLink](Projects/OpenIGTLink/README.md) (Junichi Tokuda)
1. [US-CT Vertebra Registration](Projects/US_CT_VertebraRegistration) (Houssem Gueziri, Tamas Ungi)

### Deep learning and segmentation
1. [DeepHeart MONAILabel integration](Projects/DeepHeart/README.md) (Matthew Jolley, Christian Herz, Danielle F. Pace, Andras Lasso)
1. [Registration for Deep Learning](Projects/TimeSequenceRegistration/README.md) (Curtis Lisle, Neha Goyal, Greg Sharp)
1. [Integration of PyTorch and Slicer](Projects/PyTorchIntegration/README.md) (Fernando Pérez-García, Andrés Díaz-Pinto, Andras Lasso, Curtis Lisle, Rebecca Hisey, Steve Pieper, Tamas Ungi)
1. [Development of Deep Learning Segmentation for Spines with Metastatic Disease](Projects/SpineSegmentation/README.md) (Ron Alkalay, Curtis Lisle, Andres Diaz-Pinto)
1. [Development of Deep Learning Based Brain Masking](Projects/CNN_Brain_Masking/README.md) (Raymond Yang, Lipeng Ning, Yogesh Rathi, Steve Pieper, Loraine Franke, Daniel Haehn)
1. [Deep Learning for Subcortical Brain Segmentation](Projects/DeepLearningforSubcorticalBrainSegmentation/README.md) (Jarrett Rushmore, Elizabeth Kenneally, Sylvain Bouix, Kyle Sunderland, Nikos Makris)
1. [Time-Series Segmentation Module](Projects/Time-Series%20Segmentation%20Module/README.md)(Rebecca Hisey, Tamas Ungi, Andras Lasso, Andres Diaz-Pinto, Tina Kapur)
1. [MONAI Label](https://github.com/NA-MIC/ProjectWeek/tree/master/PW35_2021_Virtual/Projects/MONAILabel)(Andres Diaz-Pinto, Fernando Pérez-García, Sachidanand Alle, Alvin Ihsani, Vishwesh Nath)

### Cloud, open data and annotation
1. [SlicerOnDemand](Projects/SlicerOnDemand/README.md) (Steve Pieper, Curt Lisle, Andrey Fedorov, Theodore Aptekarev)
1. [NCI Imaging Data Commons](Projects/NCIImagingDataCommons/README.md) (Andrey Fedorov, Markus Herrmann, Theodore Aptekarev, Steve Pieper, Ron Kikinis)
1. [mpReview: Development of a streamlined Slicer module for (manual) image annotation](Projects/mpReview/README.md) (Andrey Fedorov, Dora Szasz, Masoom Haider, Aytek Oto, Andras Lasso, Fiona Fennessy)
1. [DICOM-SR: Extending DICOM-SR support in dcmjs and adding test cases](Projects/DICOM-SR/README.md) (Emel Alkim, Steve Pieper, Andrey Fedorov)
1. [Slicer for Microscopy Data](Projects/SlicerForMicroscopyData/README.md) (Sindhura Thirumal, Steve Pieper, Tina Kapur)
1. [Discourse Meet and Greet](https://discord.com/invite/5TC5H2g63e)(Simon Drouin)

## Registrants

Do not add your name to this list below. It is maintained by the organizers based on your registration. [Register here](https://forms.gle/evnWqMu4dnsx3Mei9).

List of registered participants so far (names will be added here after processing registrations):

1.	Mónica García Sevilla	,	Universidad de Las Palmas de Gran Canaria	,	Gran Canaria	,	Spain
1.	ZhenXiao Yu	,	University Of Western Ontario	,	Ontario	,	Canada
1.	Shreyas Chandra Sekhar	,	WPI	,	CA	,	USA
1.	Tina Kapur	,	Brigham and Women's Hospital and Harvard Medical School	,	MA	,	United States
1.	Sam Horvath	,	Kitware	,	North Carolina	,	United States
1.	Steve Pieper	,	Isomics, Inc.	,	MA	,	US
1.	Simon Oxenford	,	Charite Berlin	,	Berlin	,	Germany
1.	Theodore Aptekarev	,	None	,	Moscow/Tel Aviv	,	Israel/Russia
1.	Samuelle St-Onge	,	École de Technologie Supérieure ,	Montreal	,	Canada
1.	Csaba Pinter	,	Ebatinca / Pixel Medical	,	Canarias	,	Spain
1.	Miguel Xochicale	,	King's College London	,	London	,	UK
1.	Thibault Pelletier	,	Kitware	,	Rhône-Alpes	,	France
1.	Saima Safdar	,	UWA	,	Western australia	,	Australia
1.	Juan Ruiz-Alzola	,	University of Las Palmas de Gran Canaria	,	Canarias	,	Spain
1.	David García Mato	,	Ebatinca S.L.	,	Las Palmas	,	Spain
1.	Mario Banfoldy	,	Banfoldy and Partners	,	SP	,	Brasilien
1.	Simon Drouin	,	École de Technologie Supérieure	,	Montreal	,	Canada
1.	Ron Kikinis	,	Harvard Medical School	,	Boston	,	United States
1.	Herbert Shin	,	University of Western Ontario 	,		,	Canada
1.	Ahmedou Moulaye IDRISS	,	Faculty of Medicine / University of Nouakchott Al Aasriya	,	Nashville	,	Mauritania
1.	Ron Alkalay	,	Beth Israel Deaconess Medical Center	,	Bosotn	,	US
1.	Alicia Pose Díez de la Lastra	,	Universidad Carlos III de Madrid	,	Leganés	,	España
1.	Chenglin Zhu	,	Cornell University	,	Ithaca	,	Study in US, live in China
1.	Jarrett Rushmore	,	BU/BWH/MGH	,	Boston	,	USA
1.	Walia Farzana	,	Old Dominion University	,	Norfolk	,	United States of America
1.	Mamadou Samba Camara	,	University Cheikh Anta Diop of Dakar	,	Dakar	,	Senegal
1.	Fernando Pérez-García	,	UCL & King's College London	,		,	United Kingdom
1.	Curtis Lisle	,	KnowledgeVis, LLC	,	Altamonte Springs	,	United States
1.	Tamas Ungi	,	Queen's University	,	Kingston	,	Canada
1.	Andras Lasso	,	PerkLab, Queen's University	,	Kingston	,	Canada
1.	Junichi Tokuda	,	Brigham and Women's Hospital	,	Boston	,	United States
1.	Maximilian Fischer	,	German Cancer Research Center	,		,	Germany
1.	Marilola Afonso	,	Universidad de Las Palmas de Gran Canaria	,	Las Palmas de Gran Canaria	,	Spain
1.	Étienne Léger	,	Concordia University	,	Montréal	,	Canada
1.	Idafen Santana-Perez	,	University of Las Palmas de Gran Canaria	,	Las Palmas de Gran Canaria	,	Spain
1.	Loraine Franke	,	University of Massachusetts Boston	,	Boston	,	United States
1.	Varun Kumar Agarwal	,	Bareilly International University	,	Bareilly	,	India
1.	Christian Herz	,	Children's Hospital of Philadelphia	,		,	United States
1.	Mohamed El Moctar SEPTY	,	Medical School of Nouakchott- UNA	,	Nouakchott	,	Mauritania
1.	TFeil Yahya	,	Faculty of Medicine of University of Nouakchott Al Aasriya	,	Nouakchott	,	Mauritania
1.	Joshua Bierbrier	,	McGill University	,	Montreal	,	Canada
1.	Leah Groves	,	Western University 	,	London 	,	Canada
1.	Alfredo Morales Pinzon	,	BWH	,	Boston	,	United States
1.	Sylvain Bouix	,	BWH	,	Boston	,	USA
1.	Ahmedou Moulaye IDRISS	,	Faculty of Medicine - University Nouakchott Al Aasriya	,	Nouakchott	,	Mauritania
1.	Sonia Pujol	,	Brigham and Women's Hospital, Harvard Medical School	,	Boston	,	USA
1.	Raymond Yang	,	University of Massachusetts Boston	,	Edison	,	United States of America
1.	Sarah Frisken	,	Brigham and Women's Hospital	,	Boston	,	USA
1.	Pedro Moreira	,	Brigham and Women's Hospital	,	Boston	,	USA
1.	Rebecca Hisey	,	Queen's University	,	Kingston	,	Canada
1.	Andrey Titov	,	École de technologie supérieure	,	Saint-Bruno-de-Montarville	,	Canada
1.	Li Zhenzhu	,	HuaMei Hospital, University of Chinese Academy of Sciences	,	NingBo	,	China
1.	Ed Yeterian	,	Colby College	,	Pineville	,	USA
1.	Renzo Phellan Aro	,	McGill University	,	Montreal	,	Canada
1.	Fahd Derkaoui Hassani	,	Cheikh Zaid international University Hospital / UIASS	,	Rabat	,	Morocco
1.	Elizabeth Kenneally	,	Tufts University	,	Somerville	,	United States
1.	Lidia Al-Zogbi	,	Johns Hopkins University	,	Baltimore	,	United States
1.	Andrey Fedorov	,	Brigham and Women's Hospital	,	Cambridge	,	United States
1.	Jayender Jagadeesan	,	Brigham and Women's Hospital	,	Boston	,	US
1.	Gelel Rezig	,	Ecole de Technologie Supérieure	,	Montréal	,	Canada
1.	Souleymane Diao 	,	Cheikh Anta Diop University	,	Dakar 	,	Sénégal
1.	Rafael Palomar	,	Oslo University Hospital / NTNU	,	Oslo	,	Norway
1.	Gabriella d' Albenzio	,	Oslo University Hospital	,	Oslo	,	Norway
1.	Ole Vegard Solberg	,	SINTEF	,	Trondheim	,	Norway
1.	Mauro I. Dominguez	,	M3Dical	,	Hughes	,	Argentina
1.	Adam Rankin	,	Robarts Research Institute	,	London	,	Canada
1.	Javier Pascau	,	Universidad Carlos III de Madrid	,	Madrid	,	Spain
1.	Yoga Balagurunathan	,	Moffitt Cancer Center	,	Tampa	,	USA
1.	Zhouping Wei	,	Moffitt Cancer Center	,	Tampa	,	US
1.	Abián Hernández	,	Universidad de Las Palmas de Gran Canaria (ULPGC)	,	Las Palmas de Gran Canaria	,	Spain
1.	Andinet Enquobahrie	,	Kitware	,	CARY	,	United States
1.	Andrés Gamboa	,	Neurotrauma Center/Universidad Politécnica de Valencia	,	Bucaramanga/Valencia	,	Colombia/España
1.	Marine CAMBA	,	CENIR, Paris Brain Institute	,	Paris	,	France
1.	Teodora Szasz	,	The University of Chicago	,	Chicago	,	United States
1.	Geir Arne Tangen	,	SINTEF	,	Trondheim	,	Norway
1.	John Witt	,	Georgetown University, CHOP	,	Philadelphia	,	United States
1.	Andres Diaz-Pinto	,	KCL	,	London	,	United Kingdom
1.	Masoom Haider	,	University of Toronto	,	Toronto	,	Canada
1.	Neha Goyal	,	University of Massachusetts Boston 	,	Boston 	,	United States
1.	Batuhan Gundogdu	,	University of Chicago	,	Chicago	,	United States
1.	Caio A Neves	,	University of Brasilia	,	Brasilia	,	Brazil
1.	Laleh Seyyed-Kalantari	,	Mount Sinai health	,	Toronto 	,	Canada
1.	Nayra Pumar	,	EBATINCA	,	Las Palmas de Gran Canaria	,	Spain
1.	Emel Alkim	,	Stanford University	,	MOUNTAIN VIEW	,	United States
1.	Jean-Christophe Fillion-Robin	,	Kitware	,	Carrboro	,	USA
1.	Lucas Gandel	,	Kitware	,	Villeurbanne	,	France
1.	Sara Fernandez Vidal	,	ICM	,	Paris	,	France
1.	Daniel Haehn	,	University of Massachusetts Boston	,	Boston	,	United States
1.	Alberto Santamaria-Pang	,	Microsoft	,	Redmond	,	United States
1.	Jameson Merkow	,	Microsoft	,	San Diego	,	USA
1.	Risto Rangel	,	Microsoft	,	Redmond	,	United States
1.	David Allemang	,	Kitware, Inc.	,	Carrboro	,	USA
1.	Rudolf Bumm	,	Cantonal Hospital Graubünden, Department of Surgery	,	Chur	,	Switzerland
1.	Gordon Harris	,	Massachusetts General Hospital	,	Boston	,	United States
1.	Amber Wood-Bailey	,	University of Liverpool	,	Liverpool	,	United Kingdom
1.	Lucia Cevidanes	,	University of Michigamn	,	Ann Arbor	,	United States
1.	Ernest Namdar	,	University of Toronto 	,	Toronto 	,	Canada
1.	Belkis Abufaur 	,	The Cyprus Institute 	,		,	Turkey
1.	Niral	,	Johns Hopkins University	,	Baltimore	,	USA
1.	Rohan Vijayan	,	Johns Hopkins University	,	Baltimore	,	United States of America
1.	Miguel Xochicale	,	King's College London	,	London	,	United Kingdom
1.	Nayra Pumar	,	Ebatinca	,	Las Palmas de Gran Canaria	,	Spain
1.	Izabel Rubira-Bullen	,	Bauru Dental School - University Sao Paulo	,	Bauru - Sao Paulo	,	Brazil
1.	Paolo Zaffino	,	Magna Graecia University of Catanzaro	,	Lamezia Terme	,	Italy
1.	Nadya Shusharina	,	Massachusetts General Hospital	,	Boston	,	United States
1.	Greg Sharp	,	Massachusetts General Hospital	,	Boston	,	USA
1.	Nick Jowkar	,	Brigham and Women's Hospital	,	Boston	,	USA
1.	leo zekelman	,	Harvard Medical School	,	Boston	,	USA
1.	Parikshit Juvekar	,	Brigham & Women's Hospital	,	Boston	,	USA
1.	Axel Krieger	,	Johns Hopkins University	,	Baltimore	,	United States
1.	Abby Recko	,	Colby College	,	Waterville	,	USA
1.	YuhJong Liu	,	University of Pennsylvania	,	Philadelphia	,	US
1.	Houssem Gueziri	,	Montreal Neurological Institute 	,	Montreal	,	Canada
1.	Kyle Sunderland	,	Queen's University	,	Kingston	,	Canada
1.	Manjula Herath	,	Malmo University	,	Malmö	,	Sweden
1.	Badiaa Ait Ahmed	,	Abdelmalek Essaâdi University	,	Tétouan	,	Morocco
1.	Lipeng Ning	,	Brigham and Women's Hospital	,	Boston	,	USA
1.	Sindhura Thirumal	,	Queen's University	,	Kingston	,	Canada
1.	Swajan Paul	,	McGill University	,	Montreal	,	Canada
1.	Jesse Thompson	,	University of Hawaii John A Burns School of Medicine	,	Honolulu	,	Hawaii
1.	Michael Halle	,	Brigham and Women's Hospital	,	Boston	,	MA
1.	Chenglin Zhu	,	Cornell University	,	Ithaca	,	USA/China
1.	Onder Erin	,	Johns Hopkins University	,	Baltimore	,	United States
1.	Eberto Benjumea	,	Universidad Tecnológica de Bolívar	,	Cartagena	,	Colombia
1.	Clare Tempany 	,	BWH	,	Boston	,	USA
1.	Nicholas Fordham	,	Boston University School of Medicine	,	Boston 	,	United States
1.	Dr. Gerard Rushingabigwi	,	University of Rwanda	,		,	Rwanda
1.	Joanna James	,	Beth Israel Deaconess Center	,	Boston	,	USA
1.	Mick Ganza	,	University of Rwanda, CEBE	,	Kigali	,	Rwanda
1.	Xiaolong Liu	,	Johns Hopkins University	,	Baltimore	,	United States
1.	Mushimiyimana Sophie	,	University of Rwanda	,		,	Rwanda
1.	UWIZEYIMANA MEDIATRICE	,	UR/NYARUGENGE CAMPUS	,	KIGALI	,	RWANDA
1.	Erik Ziegler	,	Radical Imaging / Open Health Imaging Foundation	,		,	France
1.	Alireza Sedghi	,	Radical Imaging / Open Health Imaging Foundation	,	Toronto	,	Canada
1.	Laleh Seyyed-Kalantari	,	Sinai Health	,	Thornhill	,	Canada
1.	FELIX HARERIMANA 	,	UNIVERSITY OF RWANDA	,	RWAMAGAN	,	RWANDA
1.	Xavier Riobé	,	Certis Therapeutics	,	Bordeaux	,	France
1.	Lucas Ewing	,	Harvey Mudd College	,	Boston	,	US
1.	Naghmeh Ansari	,	Concordia University	,	Montreal	,	Canada
1.	Randy Gollub	,	MGH	,	Lexington	,	USA

## Statistics

<!-- for ref, stats from PW 34
* 204 registered attendees
* 26 countries
* 101 institutions (82 academic, 18 industry, and 1 goverment)

<img src="pw-registrants-country-stats-final.png" width="600" />
-->


## History
Please read about our experience in running these events since 2005: [Increasing the Impact of Medical Image Computing Using
Community-Based Open-Access Hackathons: the NA-MIC and 3D Slicer Experience](http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Kapur2016.pdf).

## Logistics
- **Dates:** June 28-July 2, 2021.
- **Location:** THE INTERNET
