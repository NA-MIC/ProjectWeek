## Welcome to the web page for the 38th Project Week!

[This event](https://projectweek.na-mic.org/PW38_2023_GranCanaria/) will take place from January 30 to February 3rd, 2023 in Gran Canaria, Spain.

* Project Week 38 will be a hybrid event with a strong in-person component for the first time since 2020.
* The venue for in-person events is Hotel Cristina, Las Palmas, Gran Canaria (Spain).
* A block of rooms at [Hotel Cristina](https://www.dreamplacehotels.com/en/hotel-cristina/) is being held for PW attendees
  * To make reservations use code NAMIC23 in email to grupos.mice@dreamplacehotels.com
  * 40 rooms are being held for us at the rate of 108€ (single) and 135€ (double) until the end of November 
* Please [register](https://forms.gle/sh9jGJLJdBm4us3E7) as early as possible, indicating whether you plan on participating in person. It will greatly help the organizing committee to estimate the number of participants we need to accommodate in Las Palmas. Registration fees for in-person attendees will be determined and collected later using a separate form by the local organizing team.
* **For those attending virtually**: there will be no registration fee, and zoom/discord links will be provided during preparation meetings.
* **For those attending in person**: a registration fee of 400 Euros will be charged to cover for the workshop venue, lunch and coffee breaks. Use [this form](https://www.fulp.es/inscripcion-namic) to register your payment. Please do so by Tuesday, Jan 17th 2023, as we need to estimate the number of participants to finalize the booking of the room.

If you have any questions, you can contact the [organizers](#organizers).

<!-- to be added at the end of PW
## Screenshots, Illustrations & Photos Album

[Google Photos album from PW37](https://photos.app.goo.gl/PTJjQn5D33uShcLM9)
-->

## Before Project Week
1. Register [here](https://forms.gle/sh9jGJLJdBm4us3E7), it is free!
2. **If you plan to attend in person**, register you workshop fee of 400 Euros [here](https://www.fulp.es/inscripcion-namic).
3. Attend one or more [preparation meetings](#preparation-meetings) to present a project you intend to work on at PW, for which you are seeking collaborators or to join one of the projects proposed by others.
4. Join the [Discord server](https://discord.gg/yQsNVdVpS3) that will be used to communicate with your team during Project Week. Go to [this page](../common/Discord.md) for more info on the use of Discord during PW.
5. Consider joining the [MONAI Label Workshop](MONAILabel_Workshop.md) that will take place January 25th (the week before Project Week).

<!-- TBD
## During Project Week (All times US Eastern Daylight (Boston) Time)
* The week will start at **8:15am on Monday June 27th** with informal conversations on **[Discord](https://discord.gg/d5Q6b5ug8u)**.
* Initial **project presentations** will start at **9am on Zoom**, using [this link](https://etsmtl.zoom.us/j/86211702920?pwd=TEl0ZTFDam90WVN5bjZhR05kNVRVZz09). Each team must delegate a member to present their projects in no more than 2 minutes using no other visual support than the project page on GitHub (we won’t have time to switch screen sharing)
* If you don’t have a project, look at the PW37 page to find a project you might be interested in and contact team members through their Discord channel.
* Breakout sessions start every day at **9am on Zoom** (link in the calendar below)
* Work in **project teams** will happen throughout the week with communication between team members taking place on **Discord**. If you want to schedule a meeting ahead you can "reserve" a meeting room in [this spreadsheet](https://docs.google.com/spreadsheets/d/1jrYSecdhg9XQ1Re_7yqOCYTMjX2mOe-GowAp3yfWS7g/edit?usp=sharing).
* We will end the week with **project results presentation (9am on Friday)**. Again, each team will delegate one member to present their results in a maximum of 2 minutes. We will use the project page as a visual support for the presentation, so please make sure it is up to date with your latest results by Friday morning.
-->

## Preparation meetings
We hold weekly preparation meetings at 10am on Tuesdays, starting November 29, 2022. Please join at [this link](https://etsmtl.zoom.us/j/86211702920?pwd=TEl0ZTFDam90WVN5bjZhR05kNVRVZz09) if you have a project that you would like to present or work on during project week or to find out about projects you can join.

##  Agenda

<div id="calendar-container">
</div>

<!--
Adapted from https://stackoverflow.com/questions/31821974/support-user-time-zone-in-embedded-google-calendar
-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jstimezonedetect/1.0.7/jstz.min.js" integrity="sha512-pZ0i46J1zsMwPd2NQZ4IaL427jXE2RVHMk3uv/wPTNlBVp9AbB1L65/4YdrXRPLEmyZCkY9qYOOsQp44V4orHg==" crossorigin="anonymous"></script>

<script type="text/javascript">
  var timezone = jstz.determine();
  var iframe_src = 'https://calendar.google.com/calendar/embed?src=kitware.com_sb07i171olac9aavh46ir495c4%40group.calendar.google.com&mode=WEEK&dates=20230130%2f20230203&ctz=' + timezone.name()
  var iframe_html = '<iframe src="' + iframe_src + 'style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>'
  document.getElementById('calendar-container').innerHTML = iframe_html;
</script>

[How to add this calendar to your own?](../common/Calendar.md)

## Breakout sessions
[Panel: clinical uses of 3D Slicer](Projects/ClinicalPanel-BreakoutSession.md) (Rudolf Bumm)

## Projects [(How to add a new project?)](Projects/Readme.md)
Categories based on project list of PW37, will be updated as we populate the list of projects.

### VR/AR and Rendering
[SlicerVR - Restore Interactions](Projects/SlicerVRInteractions) (Csaba Pintér, Simon Drouin, Andrey Titov)

[SlicerTMS](Projects/SlicerTMS/README.md)

[ARinSlicer](Projects/ARinSlicer/README.md)

### IGT and Low cost
[Training system for US-guided lung interventions](Projects/US-guided_TrainingSystem) (Natalia Arteaga, David García, Javier González)
   
[Fetal Ultrasound Simulation for Delivery Training](Projects/FetalUltrasoundSimulation) (Felix von Haxthausen, David García, Tolga-Can Çallar)

[Slicer Liver](Projects/SlicerLiver/README.md) (Gabriella D'Albenzio, Ruoyan Meng, Geir A. Tangen, Ole V. Solberg, Rafael Palomar)

[Slicer Maxillofacial Surgery](Projects/Slicer4MaxillofacialSurgery/README.md)
   
### Segmentation/Classification
[Lung CT Segmentation and Analysis](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/LungSegmentation#readme)

[MONAI Label to MONAI bundle conversion](Projects/MONAILabel2bundle/README.md)
   
[Multi-stage dental segmentation using MONAI Label](Projects/TeethSegmentation) (David García, Yucheng Tang, Andres Diaz,...)
   
[Real-time ultrasound AI segmentation using Tensorflow and PyTorch models](Projects/RealTimeUltrasoundSegmentationAI) (María Rosa Rodríguez, Tamas Ungi, David García,...)

### Quantification

[MeshComparison](Projects/MeshComparison/README.md)

### Cloud and Infrastructure
[How-to setup and run 3D Slicer on an AWS server instance step by step](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/#readme) 

[ParameterNodeWrapper](Projects/ParameterNodeWrapper/README.md)

[SlicerPipelines](Projects/SlicerPipelines/README.md)

[MHub Integration](Projects/MHub_Integration/README.md)

[HOWTO: Using MONAI zoo bundle for prostate MRI cancer detection in IDC data](MONAI_IDC_PCa_detection/README.md)

[Kaapana related experiments/discussions/collaboratons](Projects/Kaapana_overall/README.md)
   
[FAIRification of medical imaging data and analysis tools](Projects/Metadata_IDC_HMC/README.md)

[3D Slicer Internationalization](Projects/3DSlicerInternationalization/README.md)

[Active Viewport](Projects/ActiveViewport/README.md)

[Simple DICOM Query/Retrieve Panel](Projects/SimpleDICOMQueryRetrievePanel/README.md)

[DICOM Segmentation Optimization](Projects/DICOMSEG/README.md)

[Measurement Panel](Projects/MeasurementPanel/README.md)

[SlicerAstro Update](Projects/SlicerAstroUpdate/README.md)

[Automated Landmarking Support](Projects/AutomatedLandmarkingSupport/README.md)

[SystoleOS](Projects/SystoleOS/README.md) (Rafael Palomar, Steve Pieper)

[Maxillofacial Surgery Virtual Planning Applications based on 3D Slicer](Projects/Slicer4MaxillofacialSurgery) (Miguel Ángel Rodríguez, Christian Buritica)

## Registrants

Do not add your name to this list below. It is maintained by the organizers based on your registration. Register [here](https://forms.gle/sh9jGJLJdBm4us3E7)

List of registered participants so far (names will be added here after processing registrations):

<!-- Participants list is updated programmatically, please don't remove the comments -->
<!-- Participants list start -->

1. Rafael Palomar, Norway, (In-person, Confirmed)
1. Csaba Pinter, Spain, (In-person)
1. Simon Drouin, Canada, (In-person, Confirmed)
1. Tina Kapur, USA, (Online)
1. Karol Miller, Australia, (In-person, Confirmed)
1. Andy Huynh, Australia, (In-person, Confirmed)
1. Sen Li, Canada, (Undecided)
1. Paolo Zaffino, Italy, (In-person, Confirmed)
1. Andrey Fedorov, USA, (In-person, Confirmed)
1. Steve Pieper, USA, (In-person)
1. hans knutsson, Sweden, (In-person)
1. Sonia Pujol, USA, (Undecided)
1. JUAN RUIZ-ALZOLA, Spain, (In-person)
1. Ron Kikinis, USA, (In-person, Confirmed)
1. Carl-Fredrik Westin, USA, (In-person, Confirmed)
1. Katie Mastrogiacomo, USA, (In-person, Confirmed)
1. Mamadou Samba CAMARA, Senegal, (In-person)
1. Pape Mady THIAO, Senegal, (In-person)
1. Alexandra Golby, USA, (In-person)
1. yahya tfeil tfeil, Mauritania, (In-person)
1. Javier Pascau, Spain, (In-person, Confirmed)
1. Idafen Santana Perezz, Spain, (In-person)
1. David García Mato, Spain, (In-person)
1. Alicia Pose Díez de la Lastra, Spain, (In-person)
1. Miguel Angel Rodriguez-Florido, Spain, (In-person)
1. Gabor FICHTINGER, Canada, (In-person, Confirmed)
1. Luděk Hynčík, Czech Republic, (Online)
1. Sen, Canada, (In-person)
1. Souleymane Diao, Senegal, (Online)
1. Ahmedou Moulaye IDRISS, Mauritania, (In-person)
1. Mouhamed DIOP, Senegal, (In-person)
1. Gabriella d' Albenzio, Norway, (In-person)
1. Dwijkumar Mistry, India, (Online)
1. Ruoyan Meng, Norway, (In-person, Confirmed)
1. Ahmedou Moulaye IDRISS, Mauritania, (In-person)
1. Francesca Spadea, Germany, (In-person)
1. Rudolf Bumm, Switzerland, (In-person, Confirmed)
1. Raul San Jose, USA, (In-person)
1. Kanoun Salim, France, (Undecided)
1. Abadie Celian, France, (Undecided)
1. Simon Oxenford, Germany, (In-person, Confirmed)
1. Andre , Brazil, (Online)
1. Felix von Haxthausen, Germany, (In-person, Confirmed)
1. Tamas Ungi, Canada, (Online)
1. Andres Diaz-Pinto, UK, (Online)
1. Michela Destito, Italy, (In-person, Confirmed)
1. Attila Nagy, Hungary, (In-person, Confirmed)
1. Zachary Baum, UK, (Undecided)
1. Jordan Ortega Rodríguez, Spain, (In-person, Confirmed)
1. Pablo Rubén, Spain, (In-person, Confirmed)
1. Yamilet Rivero López, Spain, (In-person, Confirmed)
1. Joshua García Montagut, Spain, (In-person, Confirmed)
1. Mario Monzón, Spain, (In-person, Confirmed)
1. Rubén Paz, Spain, (In-person, Confirmed)
1. Ben Zwick, Australia, (In-person)
1. Gara Ramos, Spain, (In-person)
1. Davide Punzo, France, (In-person, Confirmed)
1. Michael Halle, USA, (In-person, Confirmed)
1. Gerry Gralton, Australia, (In-person, Confirmed)
1. Natalia Arteaga-Marrero, Spain, (In-person)
1. Davide Punzo, France, (In-person, Confirmed)
1. Vamsi Krishna Thiriveedhi, USA, (Online)
1. Lucia Cevidanes, USA, (Online)
1. Luc Anchling, USA, (Online)
1. Nathan Hutin, USA, (Online)
1. Sam Horvath, USA, (In-person)
1. Andrey Titov, Canada, (In-person, Confirmed)
1. Kizzy Scott, USA, (In-person, Confirmed)
1. Rafael Nebot Medina, Spain, (In-person, Confirmed)
1. Paula Victoria, Spain, (In-person)
1. Alireza Sedghi, Canada, (Online)
1. Andrey Titov, Canada, (In-person, Confirmed)
1. Sara Rolfe, USA, (Undecided)
1. Geir Arne Tangen, Norway, (In-person, Confirmed)
1. Yaying Shi, USA, (Online)
1. Haythem Guermazi, Mauritania, (In-person)
1. Étienne Léger, Canada, (In-person, Confirmed)
1. Theodore Aptekarev, Montenegro, (In-person, Confirmed)
1. Gang Fu, USA, (Online)
1. Roya Khajavibajestani, USA, (Undecided)
1. Ole Vegard Solberg, Norway, (In-person, Confirmed)
1. Santhosh Parampottupadam, Germany, (In-person)
1. Brianna Burton, Belgium, (Undecided)
1. Cosmin Ciausu, USA, (In-person, Confirmed)
1. Charles DeLorey, USA, (Online)
1. Marco Nolden, Germany, (In-person, Confirmed)
1. Fernandez Vidal, France, (In-person)
1. Maria Sofia Sappia, Netherlands, (Online)
1. Yucheng Tang, USA, (Online)
1. Chris Yeung, Canada, (Online)
1. Prodipta Guha, Australia, (Online)
1. Daniel Haehn, USA, (Online)
1. Dennis Bontempi, USA, (In-person, Confirmed)
1. Leonard Nürnberg, USA, (In-person, Confirmed)
1. Loraine Franke, USA, (Online)
1. Ami Hashemi, USA, (Online)
1. Piotr Woznicki, Germany, (Online)
1. Andras Lasso, Canada, (In-person, Confirmed)
1. Connor Bowley, USA, (In-person, Confirmed)
1. Rafe McBeth, USA, (Undecided)
1. Linmin Pei, USA, (Online)
1. William Wells, USA, (In-person, Confirmed)
1. Sara Fernandez Vidal, France, (In-person, Confirmed)
1. Sara Fernandez Vidal, France, (In-person, Confirmed)
1. Zora Kikinis, USA, (In-person, Confirmed)
1. Fidèle AGOSSOU, Benin, (Online)
1. Jeremiah Richard, UK, (Online)
1. Deepa Krishnaswamy, USA, (In-person, Confirmed)
1. Hans Meine, Germany, (In-person, Confirmed)
1. MARTA LATORRE MIGUEZ, Spain, (In-person)
1. Attila Tanács, Hungary, (In-person, Confirmed)
1. Pablo Sergio Castellano Rodríguez, Spain, (In-person)
1. Andrea Mihaly, Spain, (In-person, Confirmed)
1. María Rosa Rodríguez Luque, Spain, (In-person)
1. Jose Carlos Mateo Pérez, Spain, (In-person)
1. Nikolaos Makris, USA, (In-person)
1. Aday Melián Carrillo, Spain, (In-person)
1. Marta Kersten, Canada, (In-person)
1. Connor Bowley, USA, (In-person, Confirmed)
1. Nicole Delgado, USA, (Online)
1. Brandon Konkel, USA, (Online)
1. Hanno Gao, Germany, (In-person, Confirmed)
1. Robabeh Salehiozoumchelouei, Spain, (Online)
1. Nayra Pumar, Spain, (Undecided)
1. Stefan Denner, Germany, (In-person, Confirmed)
1. Ünal Akünal, Germany, (In-person)
1. Benjamin Hamm, Germany, (In-person, Confirmed)
1. Klaus Kades, Germany, (In-person, Confirmed)
1. Umang Pandey, Spain, (In-person)
1. Yogesh Rathi, USA, (In-person)
1. Trinity Urban, USA, (Online)
1. Francisco J. Marcano Serrano, Spain, (In-person)
1. Philipp Schader, Germany, (In-person, Confirmed)
1. Ralf Floca, Germany, (Online)
1. Carlo Rondinoni, Brazil, (Online)
1. Adriana H. Vilchis González, Mexico, (Online)
1. Juan Carlos Avila Vilchis, Mexico, (Online)
1. Carley Tillett, Australia, (Online)
1. Rebeca Villarroel Ramírez, Spain, (In-person, Confirmed)
1. Luiz Murta, Brazil, (Online)
1. Alberto Cuadrado Hernández, Spain, (In-person)
1. Álvaro Navarro González , Spain, (In-person)
1. Markus Bujotzek, Germany, (In-person, Confirmed)
1. Gauthier DOT, France, (Online)
1. Elanchezhian Somasundaram, USA, (Online)
1. Chi Zhang, USA, (Online)
1. RODRIGO BASILIO, Brazil, (Online)
1. Saeed Arbabi, Netherlands, (Undecided)
1. Maximilian Fischer, Germany, (Undecided)
1. Kyle Sunderland, Canada, (Online)
1. Ghulam Rasool, USA, (Online)
1. Suraj Pai, USA, (Online)
1. Ibrahim Hadzic, USA, (Online)
1. Diana Alejandra Mendoza Mora , Mexico, (Online)
1. Li-Wei Yang, taiwan, (Online)
1. Maica Fernández, Spain, (In-person)
1. Allen Tannenbaum, USA, (Online)
1. Marina Elistratova Elistratova, Spain, (In-person)
1. Nadya Shusharina, USA, (Online)
1. Tamas Heffter , Hungary, (Online)
1. Khaled Younis, USA, (Online)
1. Rebecca Hisey, Canada, (Online)
1. Pedro Moreira, USA, (Online)
1. Jakob Wasserthal, Switzerland, (In-person)
1. Glauco Caurin, Brazil, (Online)
1. Eserval Rocha Junior, Brazil, (Online)
1. Djennifer Madzia-Madzou , Netherlands, (Online)
1. Rahul Kumar, Norway, (Online)
1. Mohamed Alalli BILAL, Senegal, (Online)
1. Fryderyk Kögl, Germany, (Online)
1. Carine Cindy Nguefack Tonleu, Canada, (Online)
1. Tamas Ungi, Canada, (Online)
1. Javier González-Fernández, Spain, (In-person)
1. Maximilian Fischer, Germany, (In-person)
1. Daniela Schacherer, Germany, (Online)
1. Jenna Kim, USA, (Online)
1. Kiran Sandilya , USA, (Online)
1. Kunal Jain, USA, (Online)
1. Mahsa Geshvadi, USA, (Online)
1. Daniel Palkovics, Hungary, (Online)
1. Keno Bressem, USA, (Online)
1. Nielsen , Brazil, (Online)

<!-- Participants list end -->

## Statistics

## Organizers
This edition of Project Week will be led by:
* [@tkapur](https://github.com/tkapur) ([Tina Kapur, PhD](http://www.spl.harvard.edu/pages/People/tkapur)),
* [@drouin-simon](https://github.com/drouin-simon) ([Simon Drouin, PhD](https://drouin-simon.github.io/ETS-web//))
* [@rafaelpalomar](https://github.com/rafaelpalomar) ([Rafael Palomar, PhD](https://www.ntnu.edu/employees/rafaelp))
* [@piiq](https://github.com/piiq) ([Theodore Aptekarev](https://discourse.slicer.org/u/pll_llq))
* [@sjh26](https://github.com/sjh26) Sam Horvath

## History
Please read about our experience in running these events since 2005: [Increasing the Impact of Medical Image Computing Using
Community-Based Open-Access Hackathons: the NA-MIC and 3D Slicer Experience](http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Kapur2016.pdf).
