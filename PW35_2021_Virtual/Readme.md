

## Welcome to the web page for the 35th Project Week!

This event will be held virtually June 28-July 2, 2021.

## History
Please read about our experience in running these events since 2005: [Increasing the Impact of Medical Image Computing Using
Community-Based Open-Access Hackathons: the NA-MIC and 3D Slicer Experience](http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Kapur2016.pdf).

## Logistics
- **Dates:** June 28-July 2, 2021.
- **Location:** THE INTERNET

### Attendees
- **Step 0**: **REGISTER** [here](https://forms.gle/evnWqMu4dnsx3Mei9)
- **Step 1**: Sign-up on the **[discourse forum](https://discourse.slicer.org/c/community/project-week)** to get updates and ask questions.
- **Step 2**: Add a **project title** and people names in [this Google document](https://docs.google.com/document/d/1_uxClJYt7eFU4LUrDxbhuGXE_5jspPXWbjOkFmr1fJc/edit?usp=sharing) (before Tuesday, June 15)
- **Step 3**: Create a **project webpage** (see Projects section below) (before Tuesday June 22)
- **Step 4** (optional): Join the **Discord** server to help prepare and work on your project: [Invite Link](https://discord.gg/5TC5H2g63e)


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

## Projects [(How to add a new project?)](Projects/Readme.md)
### VR/AR and Rendering
1. [PRISM volume rendering](Projects/PRISM_volume_rendering/Readme.md) (Simon Drouin, Steve Pieper, Kyle Sunderland, Andrey Titov, Rafael Palomar)
1. [SlicerVR build and in-VR widgets](Projects/SlicerVR/README.md) (Csaba Pinter, Adam Rankin, Jean-Christophe Fillion-Robin)
1. [Virtual cameras](Projects/VirtualCameras/README.md) (Étienne Léger, Tamas Ungi, Andras Lasso)
1. [TMS Visualization in Slicer](Projects/TMS_Slicer_Module/Readme.md) (Lipeng Ning, Yogesh Rathi, Steve Pieper, Daniel Haehn, Raymond Yang, Loraine Franke)
1. [AR in Slicer](Projects/ARinSlicer/README.md) (Alicia Pose Díez de la Lastra, Javier Pascau, Csaba Pinter)
1. [Interactive Slice Intersections](Projects/InteractiveSliceIntersections/README.md) (David García-Mato, Kyle Sunderland, Csaba Pinter)
1. [VR for Birth Delivery Training](Projects/VRBirthDeliveryTraining/README.md) (Mónica García-Sevilla, David García-Mato, Abián Hernández-Guedes, Juan Ruiz Alzola, Javier Pascau, Nayra Pumar, Csaba Pinter)
1. [VR display plugin for PyDBS using a zSpace device](Projects/VRDisplayPluginForPyDBSUsingZspace/README.md) (Marine Camba, Sara Fernandez Vidal, Sinan Haliyo)
### IGT
1. [NousNav](Projects/NousNav/README.md) (Alexandra Golby, Sam Horvath, Sarah Frisken, David Allemang, Tina Kapur, Steve Pieper, Jean-Christophe Fillion-Robin, Sonia Pujol)
2. [DBS Navigation](Projects/DBSNavigation/README.md) (Simon Oxenford)
3. [ROS2 - 3D Slicer Integration](Projects/ROSMED/README.md) (Junichi Tokuda, Tamas Ungi, Axel Krieger, Simon Leonard, Mark Fuge)
4. [Slicer module for planning MR-guided focal cryoablation of prostate cancer](Projects/ProstateCryoablationPlanning/README.md) (Pedro Moreira)
5. [Slicer-Liver: planning liver resections in 3D Slicer](Projects/Slicer-Liver/README.md) (Rafael Palomar, Gabriella d'Albenzio, Ole Vegard Solberg, Geir Arne Tangen)
6. [IGT training material for francophone countries](Projects/IGTrain/README.md) (Nayra Pumar, Mohamed El Moctar Septy, Yahya Tfeil, Asmaa Skareb, Marilola Afonso, Juan Ruiz Alzola)
7. [GPU Rigid Registration](Projects/GPURigidRegistration/README.md) (Gelel Rezig, Houssem Eddine Gueziri, Simon Drouin)
9. [Planar Osteotomies Virtual Surgical Planning And Patient-Specific Surgical Guides](Projects/PlanarOsteotomiesVSPAndSurgicalGuides/README.md) (Mauro I. Dominguez, Manjula Herath)
10. [Low-Cost neuronavigation](Projects/MarkerlessTrackingWithRGBDCamerasForLowCostNeuronavigation/README.md) (Julie Alvarez (Neurotrauma Center), Gabriel Vargas Grau (Universidad de Santander), Juan Camilo Gamboa (Mc Gill University), Andrés Gamboa (Neurotrauma/Universidad Politécnica de Valencia/))
### Deep learning and segmentation
1. [DeepHeart MONAILabel integration](Projects/DeepHeart/README.md) (...)
1. [Registration for Deep Learning](Projects/TimeSequenceRegistration/Readme.md) (Curtis Lisle, Neha Goyal, Greg Sharp)
1. [Development of Deep Learning Segmentation for Spines with Metastaic Disease](Projects/SpineSegmentation/README.md) (Ron Alkalay, Curtis Lisle, Andres Diaz-Pinto)
1. [Integration of PyTorch and Slicer](Projects/PyTorchIntegration/README.md)
1. [Development of Deep Learning Based Brain Masking](Projects/CNN_Brain_Masking/README.md) (Raymond Yang)
### Cloud, open data and annotation
1. [SlicerOnDemand](Projects/SlicerOnDemand/README.md) (Steve Pieper, Curt Lisle)
1. [NCI Imaging Data Commons](Projects/NCIImagingDataCommons/README.md) (Andrey Fedorov, Markus Herrmann, Theodore Aptekarev, Steve Pieper, Ron Kikinis)
1. [mpReview: Development of a streamlined Slicer module for (manual) image annotation](Projects/mpReview/README.md) (Andrey Fedorov, Dora Szasz, Masoom Haider, Aytek Oto, Andras Lasso, Fiona Fennessy)
1. [DICOM-SR: Extending DICOM-SR support in dcmjs and adding test cases](Projects/DICOM-SR/README.md) (Emel Alkim, Steve Pieper, Andrey Fedorov)

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

## Statistics

<!-- for ref, stats from PW 34
* 204 registered attendees
* 26 countries
* 101 institutions (82 academic, 18 industry, and 1 goverment)

<img src="pw-registrants-country-stats-final.png" width="600" />
-->
