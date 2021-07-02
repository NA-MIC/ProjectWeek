
Back to [Projects List](../../README.md#ProjectsList)

# Markerless tracking with RGBD cameras for low cost neuronavigation

## Key Investigators

- Julie Alvarez (Neurotrauma Center)
- Gabriel Vargas Grau (Universidad de Santander)
- Juan Camilo Gamboa (Mc Gill University)
- Andrés Gamboa (Neurotrauma/Universidad Politécnica de Valencia/)
- Rebecca Hisey (Perk Lab/ Queen's University)
- Jhaczon Meza (Optilab/ Technological University of Cartagena)

# Project Description

Neuronavigation guided TMS (nTMS) has become an increasingly used tool in neurosurgical clinical practice and has proven to be especially useful in preoperative brain mapping for surgical planning in brain tumor surgery.
However there are not many commercial neuronavigation systems available that meet all the needs for TMS applications, like estimating the electrical field over the cortex. Some other technical issues rela   ted to tracking functions are found in these systems. Because of their high cost (near $US 100.000) and technical requirements they remain out of reach for many institutions in low/middle income countries.
There are low-cost tools with which it is possible to implement a system with almost any function provided by commercial systems available today, and with the possibiity of continuos development and customization. -->

## Objective

Develop and validate a workflow  for the implementation of a prototype markless neuronavigation system for non-invasive functional mapping with nTMS, by combining low-cost optical sensors (INTEL REALSENSE) and open source software 3D SLICER 

1. Objective A  Validating a workflow for markless nTMS motor mapping for neurosurgical preoperative planning 
1. Objective B. Comparing preoperative non-invasive TMS brain mapping VS direct intraoperative cortical stimulation mapping   

## Approach and Plan

1. Defining workflow for nTMS motor mapping in 3D slicer with low cost RGB-D cameras
2. Validating preoperative markless tracking nTMS motor mapping results with intraoperatie direct cortical stimulation mapping

## Progress and Next Steps

1. Prof of concept: convetional TMS cortical mapping and validating result with intraoperative direct cortical stimulation motor mapping (expert analisys)
2. Identified tools (Modules/extensions) in 3D slicer and designed offline approach for hand knob hotspot by markless nTMS motor mapping
3. Created module for Intel Realsense SR300 RGB and DEPTH streaming in slicer and TMS data recording
4. Created module for obtaning point cloud from depth streaming

# Illustrations
# Workflow for preoperative conventional(not navigated) TMS cortical mapping and Hand Knob estimation 
<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
![![image](https://user-images.githubusercontent.com/16233997/122260473-f07ce580-ce98-11eb-9e63-291c925b7761.png)
![image](https://user-images.githubusercontent.com/16233997/122260723-3639ae00-ce99-11eb-82c0-39fff6c6d88c.png)
![image](https://user-images.githubusercontent.com/16233997/122260754-3e91e900-ce99-11eb-8998-3f8fc8bc00ee.png)
![image](https://user-images.githubusercontent.com/16233997/122260792-49e51480-ce99-11eb-991a-3be64ac0a659.png)
![image](https://user-images.githubusercontent.com/16233997/122260835-56696d00-ce99-11eb-865e-2386a943ff87.png)
![image](https://user-images.githubusercontent.com/16233997/122260870-61bc9880-ce99-11eb-9310-d1fc46f77b9b.png)
![image](https://user-images.githubusercontent.com/16233997/122262646-3b97f800-ce9b-11eb-863e-8d83538097d4.png)
![image](https://user-images.githubusercontent.com/16233997/122262675-45216000-ce9b-11eb-9dfc-95906d70d363.png)

https://user-images.githubusercontent.com/16233997/122260947-7862ef80-ce99-11eb-8663-673c1054ffc8.mp4

https://user-images.githubusercontent.com/16233997/122261001-8a449280-ce99-11eb-8d87-6e3e497b1f62.mp4

# Record TMS Data Module
Demonstrated with Central Line Data

![image](https://user-images.githubusercontent.com/22460517/124212725-7619ab80-dabd-11eb-98a5-607b40df7d3f.png)
![image](https://user-images.githubusercontent.com/16233997/124270117-61f79d80-db01-11eb-9fde-3252b5647b82.png)

# Frames to Points Module
Demonstrated with Central Line Data

https://user-images.githubusercontent.com/22460517/124278099-d50a0f80-db13-11eb-989b-326994265966.mp4

![image](https://user-images.githubusercontent.com/22460517/124212338-cd6b4c00-dabc-11eb-93fc-41eac703377f.png)
![image](https://user-images.githubusercontent.com/22460517/124212411-ed9b0b00-dabc-11eb-8eb2-eee89f4a1058.png)

# Background and References
https://projectweek.na-mic.org/PW31_2019_Boston/Projects/RealSensePatientRegistration/

https://github.com/pieper/facenav

Barker, A. T., Jalinous, R., & Freeston, I. L. (1985). NON-INVASIVE MAGNETIC  STIMULATION OF HUMAN MOTOR CORTEX. The Lancet, 325(8437), 1106– 1107. https://doi.org/https://doi.org/10.1016/S0140-6736(85)92413-4 
Butenschön, V. M., Ille, S., Sollmann, N., Meyer, B., & Krieg, S. M. (2018). Cost effectiveness of preoperative motor mapping with navigated transcranial  magnetic brain stimulation in patients with high-grade glioma. Neurosurgical  Focus, 44(6), E18. https://doi.org/10.3171/2018.3.FOCUS1830 
Coburger, J., Musahl, C., Henkes, H., Horvath-Rizea, D., Bittl, M., Weissbach, C.,  & Hopf, N. (2013). Comparison of navigated transcranial magnetic stimulation  and functional magnetic resonance imaging for preoperative mapping in  rolandic tumor surgery. Neurosurgical Review, 36(1), 65–66.  
https://doi.org/10.1007/s10143-012-0413-2 
Conti, A., Raffa, G., Granata, F., Rizzo, V., Germanò, A., & Tomasello, F. (2014).  Navigated transcranial magnetic stimulation for “somatotopic” tractography of  the corticospinal tract. Neurosurgery, 10 Suppl 4, 542–554; discussion 554.  https://doi.org/10.1227/NEU.0000000000000502 
Diehl, C. D., Schwendner, M. J., Sollmann, N., Oechsner, M., Meyer, B., Combs,  S. E., & Krieg, S. M. (2019). Application of presurgical navigated transcranial  magnetic stimulation motor mapping for adjuvant radiotherapy planning in  patients with high-grade gliomas. Radiotherapy and Oncology : Journal of the  European Society for Therapeutic Radiology and Oncology, 138, 30–37.  https://doi.org/10.1016/j.radonc.2019.04.029 
Duffau, H. (2020a). Can Non-invasive Brain Stimulation Be Considered to Facilitate Reoperation for Low-Grade Glioma Relapse by Eliciting Neuroplasticity?  Frontiers in Neurology, 11, 582489. https://doi.org/10.3389/fneur.2020.582489 
Duffau, H. (2020b). Functional mapping before and after low-grade glioma surgery:  A new way to decipher various spatiotemporal patterns of individual  neuroplastic potential in brain tumor patients. In Cancers (Vol. 12, Issue 9, pp.  1–21). MDPI AG. https://doi.org/10.3390/cancers12092611 
Flouty, O., Reddy, C., Holland, M., Kovach, C., Kawasaki, H., Oya, H., Greenlee,  J., Hitchon, P., & Howard, M. (2017). Precision surgery of rolandic glioma and  insights from extended functional mapping. Clinical Neurology and  Neurosurgery, 163, 60–66.  
https://doi.org/https://doi.org/10.1016/j.clineuro.2017.10.008 
Frey, D., Schilt, S., Strack, V., Zdunczyk, A., Rösler, J., Niraula, B., Vajkoczy, P., &  Picht, T. (2014). Navigated transcranial magnetic stimulation improves the  treatment outcome in patients with brain tumors in motor eloquent locations.  Neuro-Oncology, 16(10), 1365–1372. https://doi.org/10.1093/neuonc/nou110 
Jensen, R. L. (2014). Navigated transcranial magnetic stimulation: another tool for  preoperative planning for patients with motor-eloquent brain tumors. In Neuro oncology (Vol. 16, Issue 10, pp. 1299–1300). https://doi.org/10.1093/neuonc/nou213 
Koh, T. H., & Eyre, J. A. (1988). Maturation of corticospinal tracts assessed by  electromagnetic stimulation of the motor cortex. Archives of Disease in  Childhood, 63(11), 1347–1352. https://doi.org/10.1136/adc.63.11.1347 
Lefaucheur, J.-P., & Picht, T. (2016). The value of preoperative functional cortical  mapping using navigated TMS. Neurophysiologie Clinique = Clinical Neurophysiology, 46(2), 125–133. https://doi.org/10.1016/j.neucli.2016.05.001 
Raffa, G., Picht, T., Scibilia, A., Rösler, J., Rein, J., Conti, A., Ricciardo, G.,  Cardali, S. M., Vajkoczy, P., & Germanò, A. (2019). Surgical treatment of  meningiomas located in the rolandic area: the role of navigated transcranial  magnetic stimulation for preoperative planning, surgical strategy, and  prediction of arachnoidal cleavage and motor outcome. Journal of  Neurosurgery, 1–12. https://doi.org/10.3171/2019.3.JNS183411 
Raffa, G., Scibilia, A., Conti, A., Cardali, S. M., Rizzo, V., Terranova, C.,  Quattropani, M. C., Marzano, G., Ricciardo, G., Vinci, S. L., & Germanò, A. (2019). Multimodal Surgical Treatment of High-Grade Gliomas in the Motor  Area: The Impact of the Combination of Navigated Transcranial Magnetic  Stimulation and Fluorescein-Guided Resection. World Neurosurgery, 128,  e378–e390. https://doi.org/https://doi.org/10.1016/j.wneu.2019.04.158 
Seidel, K., Häni, L., Lutz, K., Zbinden, C., Redmann, A., Consuegra, A., Raabe, A.,  & Schucht, P. (2019). Postoperative navigated transcranial magnetic  stimulation to predict motor recovery after surgery of tumors in motor eloquent  areas. Clinical Neurophysiology : Official Journal of the International  Federation of Clinical Neurophysiology, 130(6), 952–959. https://doi.org/10.1016/j.clinph.2019.03.015 
Sollmann, N., Fratini, A., Zhang, H., Zimmer, C., Meyer, B., & Krieg, S. M. (2019).  Associations between clinical outcome and tractography based on navigated  transcranial magnetic stimulation in patients with language-eloquent brain  lesions. Journal of Neurosurgery, 132(4), 1033–1042.  
https://doi.org/10.3171/2018.12.JNS182988 
Takahashi, S., Vajkoczy, P., & Picht, T. (2013). Navigated transcranial magnetic  stimulation for mapping the motor cortex in patients with rolandic brain  tumors. Neurosurgical Focus, 34(4), E3.  
https://doi.org/10.3171/2013.1.FOCUS133 
Tarapore, P. E., Findlay, A. M., Honma, S. M., Mizuiri, D., Houde, J. F., Berger, M.  S., & Nagarajan, S. S. (2013). Language mapping with navigated repetitive  TMS: proof of technique and validation. NeuroImage, 82, 260–272.  https://doi.org/10.1016/j.neuroimage.2013.05.018 

Source code for frame to point cloud module can be found here: https://github.com/RebeccaHisey/RGBD_Tracking
