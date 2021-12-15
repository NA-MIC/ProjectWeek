## Welcome to the web page for the 36th Project Week!

[This event](https://projectweek.na-mic.org/PW36_2022_Virtual/) will be held January 17-21, 2022. The location is expected to be online. This page will be updated later with more information.

There is an in-person component of the project week taking place in Las Palmas de Gran Canaria, Canary Islands, Spain. Please [see this page](LocalParticipation.md) for more information

If you have any questions, you can contact the [organizers](../README.md#who-to-contact).

## How to participate
1. Register [here](https://forms.gle/1zE3pDs59sJ4ENP96), it is free!
2. Attend one or more preparation meetings (see next section) to present a project you intend to work on at PW, for which you are seeking collaborators or to join one of the projects proposed by others.

## Preparation meetings
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
1. [Collaborative Slicer session](Projects/SlicerCollaboration/README.md) (Csaba Pinter, Mónica Garcia, ?)
2. [AR in Slicer](https://github.com/NA-MIC/ProjectWeek/tree/master/PW36_2022_Virtual/Projects/AR%20in%20Slicer) (Alicia Pose Díez de la Lastra, Javier Pascau, Gabor Fichtinger, Andras Lasso, Adam Rankin, Csaba Pinter, Lucas Gandel, Jean-Christophe Fillion-Robin)    
    
### Image-guided therapy and low cost systems   
1. [GPU Rigid Registration](Projects/GPURigidRegistration/Readme.md) (Gelel Rezig, Houssem Gueziri, Simon Drouin)
2. [Low-Cost Ultrasound Training](Projects/LowCostUltrasoundTraining/README.md) (David Garcia Mato, Csaba Pinter, Rebecca Hisey, ...)
   
### Cloud
   
### Annotation
1. [Spine Segmentation](Projects/SpineSegmentation/README.md) (Ron Alkalay, Steve Pieper, ...)
   
## Registrants

Do not add your name to this list below. It is maintained by the organizers based on your registration. [Register here](https://forms.gle/1zE3pDs59sJ4ENP96).

List of registered participants so far (names will be added here after processing registrations):

## History
Please read about our experience in running these events since 2005: [Increasing the Impact of Medical Image Computing Using
Community-Based Open-Access Hackathons: the NA-MIC and 3D Slicer Experience](http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Kapur2016.pdf).
