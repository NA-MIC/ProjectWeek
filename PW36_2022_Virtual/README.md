## Welcome to the web page for the 36th Project Week!

[This event](https://projectweek.na-mic.org/PW36_2022_Virtual/) will be held virtually January 17-21, 2022. 

If you have any questions, you can contact the [organizers](../README.md#who-to-contact).

## Before Project Week
1. Register [here](https://forms.gle/1zE3pDs59sJ4ENP96), it is free!
2. Attend one or more preparation meetings to present a project you intend to work on at PW, for which you are seeking collaborators or to join one of the projects proposed by others.
<!--3. Optionally attend a training workshop on the use of MONAILabel with 3D Slicer on AWS cloud resources on January 12 (the week before Project Week) 2-4pm EST.  To attend please [register here](https://forms.gle/sekN29otUGDrVALF6).-->
4. Join the [Discord server](https://discord.gg/d5Q6b5ug8u) that will be used to communicate with your team during Project Week. Go to [this page](../common/Discord.md) for more info on the use of Discord during PW.

## During Project Week
* The week will start at **9am on Monday Jan 17th** with informal conversations on **[Discord](https://discord.gg/d5Q6b5ug8u)**.
* Initial **project presentations** will start at **10am on Zoom**, using [this link](https://etsmtl.zoom.us/j/86211702920?pwd=TEl0ZTFDam90WVN5bjZhR05kNVRVZz09). Each team must delegate a member to present their projects in no more than 2 minutes using no other visual support than the project page on GitHub (we won’t have time to switch screen sharing)
* If you don’t have a project, look at the PW36 page to find a project you might be interested in and contact team members through their Discord channel.
* Breakout sessions start every day at **10am on Zoom** (link in the calendar below)
* Work in **project teams** will happen throughout the week with communication between team members taking place on **Discord**. If you want to schedule a meeting ahead you can "reserve" a meeting room in [this spreadsheet](https://docs.google.com/spreadsheets/d/1jrYSecdhg9XQ1Re_7yqOCYTMjX2mOe-GowAp3yfWS7g/edit?usp=sharing).
* We will end the week with **project results presentation (10am on Friday)**. Again, each team will delegate one member to present their results in a maximum of 2 minutes. We will use the project page as a visual support for the presentation, so please make sure it is up to date with your latest results by Friday morning.

<!--## Preparation meetings
We hold weekly preparation meetings at 10am on Tuesdays, starting Nov 9th, 2021 and ending on December 8. Please join at [this link](https://etsmtl.zoom.us/j/86211702920?pwd=TEl0ZTFDam90WVN5bjZhR05kNVRVZz09) if you have a project that you would like to present or work on during project week or to find out about projects you can join.

Tentative schedule (may change each week):
* Nov 9 2021 - Kickoff meeting
* Nov 16 2021 - Cancer Imaging with Machine Intelligence and Data Science
* Nov 23 2021 - Slicer in the cloud
* Nov 30 2021 - Slicer in the cloud (continued) + User interfaces for annotation of corresponding landmarks in a longitudinal time series
* Dec 7 2021 - Low cost IGT systems
* Dec 14 2021 - Low cost IGT systems (continued), other projects
* Dec 21 2022 - All projects, project pages
* Jan 4 2022 - All projects, project pages
* Jan 11 2022 - AR, VR and rendering
* Jan 12 2022 - MONAILabel 3D Slicer AWS workshop (see [item 3 above](#how-to-participate))-->

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
  var iframe_src = 'https://calendar.google.com/calendar/embed?src=kitware.com_sb07i171olac9aavh46ir495c4%40group.calendar.google.com&mode=WEEK&dates=20220117%2f20220121&ctz=' + timezone.name()
  var iframe_html = '<iframe src="' + iframe_src + 'style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>'
  document.getElementById('calendar-container').innerHTML = iframe_html;
</script>

[How to add this calendar to your own?](../common/Calendar.md)

## Projects [(How to add a new project?)](Projects/README.md)
    
### VR/AR and Rendering    
1. [Collaborative Slicer session](Projects/SlicerCollaboration/README.md) (Csaba Pinter, Mónica Garcia, Jean-Christophe Fillion-Robin)
2. [AR in Slicer](Projects/AR_in_Slicer/README.md) (Alicia Pose Díez de la Lastra, Javier Pascau, Gabor Fichtinger, Andras Lasso, Adam Rankin, Csaba Pinter, Lucas Gandel, Jean-Christophe Fillion-Robin)
3. [Slicer TMS Module](Projects/SlicerTMS_Module/README.md) (Loraine Franke, Lipeng Ning, Yogesh Rathi, Steve Pieper, Raymond Yang, Daniel Haehn)
4. [PRISM Rendering](Projects/PRISMRendering/Readme.md) (Simon Drouin, Steve Pieper, Andrey Titov, Rafael Palomar)
1. [Echo VolumeRender UI](Projects/EchoVolumeRenderUI/README.md) (Samuelle St-Onge, Simon Drouin, Andrey Titov)
1. [Integration of Flir Thermal Camera](Projects/FlirCameraInSlicer) (Juan Bautista Ruis Alzola, Robabeh Salehiozoumchelouei, Mónica García Sevilla, Yousef Rajaeitabrizi)

### Image-guided therapy and low cost systems   
1. [Low-Cost Ultrasound Training](Projects/LowCostUltrasoundTraining/README.md) (David Garcia, Csaba Pinter, Rebecca Hisey, Leah Groves, Ahmed Mahran, Matt McCormick, Steve Pieper, ...)
1. [Slicer-Liver](Projects/SlicerLiver/README.md) (Rafael Palomar, Ole V. Solberg, Geir Arne Tangen, Gabriella D'Albenzio, Javier Pérez de Frutos)
1. [Visualization of catheter path based on an electromagnetic tracking with TMR sensors](Projects/TMRCatheterNavigation/README.md) (Wenran Cai, Kazuaki Hara, Rina Nagano, Junichi Tokuda
1. [Integration of ROS and 3D Slicer using OpenIGTLink](Projects/ROS-MED/README.md) (Junichi Tokuda, Tamas Ungi, Simon Leonard, Axel Krieger, Mark Fuge)
1. [GPU Rigid Registration for Neuronavigation (Montreal IBIS System)](Projects/GPURigidRegistration/Readme.md) (Gelel Rezig, Houssem Gueziri, Simon Drouin)
1. [NousNav: Low-cost neuronavigation system](Projects/NousNav/README.md) (Étienne Léger, Alexandra Golby, Sam Horvath, Sarah Frisken, David Allemang, Tina Kapur, Steve Pieper, Jean-Christophe Fillion-Robin, Sonia Pujol, Kelly Wang)
1. [Skin Surface Extraction for NousNav Registration](Projects/SkinSegmentation/README.md) (Reuben Dorent, Tina Kapur, Sarah Frisken, Mohammad Jafari, Samantha Horvath, Jean-Christophe Fillion-Robin, Harneet Cheema, Fryderyk Kögl)
1. [MR-US Landmarking for Neuronavigated surgery](Projects/AnnotationMR-US/Readme.md) (Fryderyk Kögl, Harneet Cheema, Tina Kapur, Simon Drouin)
1. [Low-cost trackers](Projects/CheapTracking/README.md) (Steve Pieper, Gabor Fichtinger)
1. [sliCERR](Projects/sliCERR/README.md) (Aditya Apte, Aditi Iyer, Eve LoCastro, Harini Veeraraghavan)
1. [Mandible Reconstruction Automatic Planning](Projects/MandibleReconstructionAutomaticPlanning/README.md) (Mauro I. Dominguez, Andras Lasso, Manjula Herath)

### Segmentation/Classification
1. [Spine Segmentation](Projects/SpineSegmentation/README.md) (Ron Alkalay, Steve Pieper, ...)
1. [Multi-organ segmentation](Projects/MultiOrganSegmentation/README.md) (Murat Maga, Sara Rolfe, Andres Diaz-Pinto)
1. [Brain Mask Prediction](Projects/BrainPrediction/README.md) (Raymond Yang, Jax Luo, Lipeng Ning, Cathy Yang, Steve Pieper, Daniel Haehn)
1. [Automatic Landmark Identification in 3D Cone-Beam Computed Tomography scans](Projects/ALICBCT/README.md) (Maxime Gillot, Baptiste Baquero, Antonio Ruellas, Marcela Gurgel, Elizabeth Biggs, Marilia Yatabe, Jonas Bianchi, Lucia Cevidanes, Juan Carlos Prieto)
1. [ALIIOS - Automatic Landmarks Identification for Intra OralScans](Projects/ALIDDM/README.md) (Baptiste Baquero, Maxime Gillot, Lucia Cevidanes, Juan Carlos Prieto, Najla Al Turkestani, Marcela Gurgel, Camila Massaro, Aron Aliaga, Maria Antonia Alvarez Castrillon, Marilia Yatabe, Jonas Bianchi, Juan Fernando Aristizabal, Diego Rey, Antonio Ruellas)
1. [Automatic Segmentation of Teeth and Alveolar bone using MONAI Label](Projects/AutomaticSegmentationofTeethandAlveolarBone/README.md) (Daniel Palkovics, Csaba Pinter, Andrés Diaz-Pinto)
    
### SlicerDMRI
1. [Anatomically informed UKF tractography](Projects/UKF/README.md) (Fan Zhang, Yogesh Rathi, Lauren J O'Donnell)
1. [Deep Diffusion MRI Registration (DDMReg)](Projects/DDMReg/README.md) (Fan Zhang, William M. Wells III, Lauren J O'Donnell)
1. [SupWMA: consistent and efficient tractography parcellation of superficial white matter with deep learning](Projects/SupWMA/README.md) (Tengfei Xue, Fan Zhang, Chaoyi Zhang, Yuqian Chen, Yang Song, Nikos Makris, Yogesh Rathi, Weidong Cai, Lauren J. O’Donnell)
1. [Deep Fiber Clustering: Anatomically Informed Unsupervised Deep Learning for Fast and Effective White Matter Parcellation](Projects/DeepFiberClustering/README.md) (Yuqian Chen, Chaoyi Zhang, Yang Song, Tengfei Xue, Nikos Makris, Yogesh Rathi, Weidong Cai, Fan Zhang, and Lauren J. O’Donnell)

### Cloud
1. [Body Part Regression using IDC](Projects/IDCBodyPartRegression/README.md) (Deepa Krishnaswamy, Andrey Fedorov)
2. [OHIF Mode Gallery](Projects/OHIFModeGallery/Readme.md) (Alireza Sedghi, James Petts, Erik Ziegler)
3. [Kaapana and XNAT exploration on Google Cloud](Projects/KaapanaXNATExploration/README.md) (Nadya Shusharina, Andrey Fedorov)
4. [Static DICOM Web for AI Assissted Annotations on AWS](Projects/StaticDicomWeb/README.md) (Chris Hafey, Gang Fu, Jordan Kojouharov, Qing Liu, Dmitry Pavlov, Andres Diaz-Pinto, Sachidanand Alle)
5. [OHIF deployment on Google Cloud](Projects/OHIFonGCP/README.md) (Andrey Fedorov, Igor Octaviano, Steve Pieper)

### Infrastructure
1. [Slicer 5 Release](Projects/Slicer5/README.md) (Sam Horvath, Jean-Christophe Fillion-Robin, Steve Pieper, Andras Lasso)
1. [SlicerPipelines](Projects/SlicerPipelines/README.md) (Connor Bowley, Sam Horvath)
1. [Slicer Internationalization](Projects/SlicerInternationalization/README.md) (Sonia Pujol, Steve Pieper, Andras Lasso, Mamadou Camara, Jean-Christophe Fillion-Robin, Ibrahima Fall, Samba Diaw, Aissa Mboup, Fryderyk Kögl, Attila Nagy, Adriana Vilchis Gonzalez, Theodore Aptekarev, Pedro Moreira, Andrey Fedorov, Ahmedou Moulaye, Yahya Tfeil)
1. [Update the Chest Imaging Platform extension to support Slicer 5](Projects/CIP_Update/README.md) (Rudolf Bumm, Raul San Jose Estepar, Andras Lasso, Steve Pieper)
1. [Batch Anonymization](Projects/DSCIAnonymize/README.md)(Hina Shah, Juan Carlos Prieto, Fryderyk Kögl)

## Registrants

Do not add your name to this list below. It is maintained by the organizers based on your registration. [Register here](https://forms.gle/1zE3pDs59sJ4ENP96).

List of registered participants so far (names will be added here after processing registrations):
    
1.	Steve Pieper	,	Isomics, Inc.	,	USA
1.	HINA SHAH	,	UNC Chapel Hill	,	USA
1.	YAHYA TFEIL	,	UNIVERSITY OF NOUAKCHOTT ALASSRIYA	,	Mauritania
1.	Monica García Sevilla	,	Universidad de Las Palmas de Gran Canaria	,	Spain
1.	Rafael Palomar	,	Oslo University Hospital / NTNU	,	Norway
1.	Ismail Irmakci	,	Feinberg School of Medicine - Northwestern University	,	USA
1.	Miguel Xochicale	,	King's College London	,	United Kingdom
1.	Adama Rama WADE	,	École Supérieure Polytechnique (ESP)	,	Senegal
1.	Li Zhenzhu	,	Department of Neursosurgery, Hwa Mei Hospital, University of Chinese Academy of Sciences, Ningbo, China；	,	China
1.	Gang Fu	,	Amazon	,	USA
1.	Maxime Gillot	,	University of Michigan	,	USA
1.	Baptiste Baquero	,	University of Michigan	,	USA
1.	Simon Drouin	,	École de technologie supérieure	,	Canada
1.	Tina Kapur	,	Brigham and Women's Hospital, Harvard Medical School	,	USA
1.	Loraine Franke	,	University of Massachusetts Boston	,	USA
1.	Harneet Cheema 	,	Brigham and Women's Hospital and Harvard Medical School, U Ottawa	,	Canada
1.	Fryderyk Kögl	,	Brigham and Women's Hospital and Harvard Medical School, Technical University of Munich	,	USA
1.	Sonia Pujol	,	Brigham and Women's Hospital,  Harvard Medical School	,	USA
1.	Daniel Haehn	,	University of Massachusetts Boston	,	USA
1.	Juan Ruiz-Alzola	,	Universidad de Las Palmas de Gran Canaria	,	Spain
1.	Felix von Haxthausen	,	University of Lübeck	,	Germany
1.	Deepa Krishnaswamy	,	Brigham and Women's Hospital	,	USA
1.	Antonio Cartón	,	Hospital Universitario La Paz	,	Spain
1.	Yi Shen	,	HIT	,	China
1.	Ahmedou Moulaye IDRISS	,	Faculty of Medicine, University of Nouakchott Al Asriya	,	Mauritania
1.	Csaba Pinter	,	EBATINCA / Pixel Medical	,	Spain
1.	Adam Wittek	,	The University of Western Australia	,	Australia
1.	Reuben Dorent	,	King's College London	,	United Kingdom
1.	David García-Mato	,	Ebatinca S.L.	,	Spain
1.	Rebecca Hisey	,	Queen's University	,	Canada
1.	Leah Groves	,	Queens University 	,	Canada
1.	xi cao	,	changshu hospital of chinese medicine	,	China
1.	Sen Li	,	École de Technologie Supérieure	,	Canada
1.	Khaled Younis 	,	Philips 	,	United States 
1.	Lina Mekki	,	Johns Hopkins University	,	United states
1.	Yahia Megahed	,	University of Central Florida	,	USA
1.	Étienne Léger	,	Brigham and Women's Hospital	,	Canada
1.	Lipeng Ning	,	Brigham and Women's Hospital	,	USA
1.	Ahmed Mahran	,	Toronto General hosptial 	,	Canada
1.	Nirav Patel	,	IIT Madras	,	India
1.	Saidou TALLA	,	École Supérieure Polytechnique (ESP)	,	Sénégal
1.	Rudolf Bumm	,	Kantonsspital Graubünden	,	Switzerland
1.	Andras Lasso	,	PerkLab, Queen's University	,	Canada
1.	Lucia Cevidanes	,	Univ. of Michigan	,	USA
1.	Gabor Fichtinger	,	Queen's University	,	Canada
1.	Ron Kikinis	,	Harvard Medical School	,	USA
1.	Yousef Rajaeitabrizi	,	IAC	,	Spain
1.	Kate Kazlovich	,	Toronto General Hospital	,	Canada
1.	Raymond Yang	,	University of Massachusetts Boston	,	USA
1.	Joaquin Olivares	,	Universidad de Córdoba	,	Spain
1.	Xiang Chen	,	Memorial University of Newfondland	,	China
1.	Motoki Katsube	,	Kyoto University	,	Japan
1.	Sarah Frisken	,	Brigham and Women's Hospital	,	USA
1.	Adam Rankin	,	Robarts Research Institute	,	Canada
1.	Connor Haberl	,	Carleton University	,	Canada
1.	Alexandra Golby	,	Brigham and Women's Hospital/Harvard Medical School	,	USA
1.	Ron Kikinis	,	Harvard Medical School	,	USA
1.	Badiaa	,	Abdelmalek Essaadi University	,	Morocco
1.	Ole Vegard Solberg	,	SINTEF	,	Norway
1.	Geir Arne Tangen	,	SINTEF	,	Norway
1.	Javier Perez deFrutos	,	SINTEF	,	Norway
1.	Andrey Fedorov	,	Brigham and Women's Hospital/Harvard Medical School	,	USA
1.	Nadya Shusharina	,	Mass General Brigham /Harvard Medical School	,	USA
1.	Kumar Punithakumar	,	University of Alberta	,	Canada
1.	Junichi Tokuda	,	Brigham and Women's Hospital	,	USA
1.	Masoom Haider	,	Univ of Toronto	,	Canada
1.	Souleymane Diao	,	Cheikh Anta Diop University	,	Sénégal
1.	Mo Alsad	,	Research Associate 	,	United Kingdom
1.	Sara Rolfe	,	Seattle Children's Research Institute and University of Washington	,	USA
1.	Samantha Horvath	,	Kitware Inc	,	USA
1.	Theodore Aptekarev	,	Slicer Community	,	Russia
1.	Pedro Moreira	,	Brigham and Women's Hospital/Harvard Medical School	,	USA
1.	Eve LoCastro	,	Memorial Sloan Kettering Cancer Center	,	USA
1.	Tamas Ungi	,	Queen's University	,	Canada
1.	Mauro Ignacio Dominguez	,	Independent	,	Argentina
1.	Erik Ziegler	,	Open Health Imaging Foundation / Radical Imaging 	,	Netherlands
1.	Antonio	,	Hospital Universitari Arnau de Vilanova	,	Spain
1.	Alicia Pose Díez de la Lastra	,	Universidad Carlos III de Madrid	,	Spain
1.	Alireza Sedghi	,	OHIF	,	Canada
1.	James Hanks	,	MGH/OHIF	,	USA
1.	Sanket Deshpande	,	Carpl.ai	,	India
1.	Rohit Takhar	,	NSIT	,	India
1.	Mónica Iturrioz	,	Brigham and Women's hospital	,	USA
1.	Ruben San Jose Estepar	,	BWH	,	USA
1.	Michael Dada	,	Federal University of Technology, Minna	,	Nigeria
1.	Ron Alkalay	,	Beth Israel Deaconess Medical Center	,	USA
1.	Sanni Henry Ananyi	,	Federal University of Technology Minna	,	Nigeria
1.	Wenran Cai	,	University of Tokyo	,	Japan
1.	Suleiman Jamila 	,	Federal University of Technology, Minna. 	,	Nigeria 
1.	Idowu Abdulsemiu Babatunde	,	Federal University of Technology Minna Niger State	,	Nigeria
1.	Nayra Pumar Carreras	,	Ebatinca	,	Spain
1.	Manjula Herath	,	Malmo University	,	Sweden
1.	Robabeh Salehiozoumchelouei	,	Instituto de Astrofísica de Canarias (IAC)	,	Spain
1.	jonas bianchi	,	University of the Pacific	,	USA
1.	Houssem Gueziri	,	Montreal Neurological Institute / McGill University	,	Canada
1.	Attila Nagy	,	University of Szeged, Department of Medical Physics and Informatics	,	Hungary
1.	Juan María Piñera Parrilla	,	SurgicalWorks	,	Spain
1.	Kazuaki Hara	,	The University of Tokyo	,	Japan
1.	Mamadou Samba CAMARA	,	University of Dakar	,	Senegal
1.	Dániel Palkovics	,	Semmelweis University	,	Hungary
1.	Parikshit Juvekar	,	Brigham & Women's Hospital, Department of Neurosurgery	,	USA
1.	James Petts	,	Ovela Solutions	,	United Kingdom
1.	Fan Zhang	,	Brigham and Women's Hospital	,	USA
1.	Keita	,	École Supérieure Polytechnique (ESP) de Dakar	,	Sénégal 
1.	Mamadou Moustapha DIAGNE 	,	ESP	,	Senegal
1.	Gregory Fischer	,	WPI	,	USA
1.	Javier Pascau	,	Universidad Carlos III de Madrid	,	Spain
1.	Ariela Shahvar	,	Western University	,	Canada
1.	Samuelle St-Onge	,	École de technologie supérieure (ÉTS)	,	Canada
1.	Andrey Titov	,	École de technologie supérieure	,	Canada
1.	Tengfei Xue	,	Harvard Medical School/University of Sydney	,	Australia
1.	Yiwei Jiang	,	Worcester Polytechnic Institute	,	USA
1.	Yuqian Chen	,	Harvard Medical School	,	USA
    
## Statistics
* 115 Registered attendees
  * 43% first time attendees
* 20 countries
    
<img src="images/attendees-per-country.png" alt="Attendees per country" width="600"/>
<img src="images/timezones.png" alt="Attendees timezones" width="600"/>
    
## History
Please read about our experience in running these events since 2005: [Increasing the Impact of Medical Image Computing Using
Community-Based Open-Access Hackathons: the NA-MIC and 3D Slicer Experience](http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Kapur2016.pdf).
