Back to [Projects List](../../README.md#ProjectsList)

# Markerless tracking with RGBD cameras for low cost neuronavigation

## Key Investigators

- Julie Alvarez (Neurotrauma Center)
- Gabriel Vargas Grau (Universidad de Santander)
- Juan Camilo Gamboa (Mc Gill University)
- Andrés Gamboa (Neurotrauma/Universidad Politécnica de Valencia/)
- Rebecca Hisey (Perk Lab/ Queen's University)

# Project Description

Neuronavigation guided TMS (nTMS) has become an increasingly used tool in neurosurgical clinical practice and has proven to be especially useful in preoperative brain mapping for surgical planning in brain tumor surgery.
However there are not many commercial neuronavigation systems available that meet all the needs for TMS applications, like estimating the electrical field over the cortex. Some other technical issues rela   ted to tracking functions are found in these systems. Because of their high cost (near $US 100.000) and technical requirements they remain out of reach for many institutions in low/middle income countries.
There are low-cost tools with which it is possible to implement a system with almost any function provided by commercial systems available today, and with the possibiity of continuos development and customization. -->

## Objective

Develop and validate a workflow  for the implementation of a prototype markless neuronavigation system for non-invasive functional mapping with nTMS, by combining low-cost optical sensors (INTEL REALSENSE) and open source software 3D SLICER 

1. Objective A  Validating a workflow for creating a TMS brain mapping scene in 3d slicer 
1. Objective B. Creating a  object/volume coregistration method
1. Objective C. Comparing preoperative non-invasive TMS brain mapping VS direct intraoperative cortical stimulation mapping   

## Approach and Plan

1. Defining a protocol for MRI acquisition for navigation (DWI, Opt T2, T1, FLAIR, proppeler...etc)
2. Setting up workflow for surface 3D scanning of patients
3. Creating a coregistration method for objects and volumes
4. Connecting Intel real sense cameras throught Plus server to 3d Slicer
5. Developing a algorithm/code for Depth streaming.
6. Fusion of RGBD and Depth streaming online (Inverse Projection Trasnformation?)
7. Trackin config (Creating virtual objects, trasnforms , pose..etc)
8. Create a dataset of camera data, for a machine learning algorithm
9. Validating tracking results with phantoms or against gold standard for brain mapping (intraoperatie direct cortical stimulation mapping)

## Progress and Next Steps

1. Defining a protocol for MRI acquisition for navigation (DWI, Opt T2, T1, FLAIR, proppeler...etc) We are working ina review article of NtMS for tumor surgery in order to define which one wul be more convinient
2. Setting up workflow for surface 3D scanning of patients: We have done few (three) scans of patients with a light and depth parameters obtain from literature. 
3. Creating a coregistration method for objects and volumes: We have upload obtained scans files as 3d objects with color using TexturetoModel. Also using volume rendering a volume models we have reconstruct 3d volumes of patients. We have reviw literatu in this regard and have don trials
4. WE have create a script for conecting a SR3600 intel real sense camera for Plus server, with RGB and depth streaming. Also created a module for setting up and recording data from intel real sense cameras.
5. Developing a algorithm/code for Depth streaming: Implemented a module for obtaining a point cloud from streamed depth images
6. https://towardsdatascience.com/inverse-projection-transformation-c866ccedef1c
7. A TMS virtual model was introduced in the scence with a niddle model that projects a point of supposedly site of stimulation in cortex
8. No progress
9. No progress
# Illustrations

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

# Frames to Points Module
Demonstrated with Central Line Data
![image](https://user-images.githubusercontent.com/22460517/124212338-cd6b4c00-dabc-11eb-93fc-41eac703377f.png)
![image](https://user-images.githubusercontent.com/22460517/124212411-ed9b0b00-dabc-11eb-8eb2-eee89f4a1058.png)

# Background and References

https://github.com/angamhi/Markless-nTMS/blob/main/intelrealsense.xml
https://github.com/darylclimb/cvml_project/tree/master/projections

Adams, H., Adams, H. H. H., Jackson, C., Rincon-Torroella, J., Jallo, G. I., &  Quiñones-Hinojosa, A. (2016). Evaluating extent of resection in pediatric  glioblastoma: a multiple propensity score-adjusted population-based analysis.  Child’s Nervous System : ChNS : Official Journal of the International Society  for Pediatric Neurosurgery, 32(3), 493–503. https://doi.org/10.1007/s00381- 015-3006-x 
Almeida, J. P., Chaichana, K. L., Rincon-Torroella, J., & Quinones-Hinojosa, A.  (2015). The value of extent of resection of glioblastomas: clinical evidence and  current approach. Current Neurology and Neuroscience Reports, 15(2), 517.  https://doi.org/10.1007/s11910-014-0517-x 
Barker, A. T., Jalinous, R., & Freeston, I. L. (1985). NON-INVASIVE MAGNETIC  STIMULATION OF HUMAN MOTOR CORTEX. The Lancet, 325(8437), 1106– 1107. https://doi.org/https://doi.org/10.1016/S0140-6736(85)92413-4 
Barnett-Page, E., & Thomas, J. (2009). Methods for the synthesis of qualitative  research: a critical review. BMC Medical Research Methodology, 9, 59.  https://doi.org/10.1186/1471-2288-9-59 
Butenschön, V. M., Ille, S., Sollmann, N., Meyer, B., & Krieg, S. M. (2018). Cost effectiveness of preoperative motor mapping with navigated transcranial  magnetic brain stimulation in patients with high-grade glioma. Neurosurgical  Focus, 44(6), E18. https://doi.org/10.3171/2018.3.FOCUS1830 
Chaichana, K. L., Cabrera-Aldana, E. E., Jusue-Torres, I., Wijesekera, O., Olivi, A.,  Rahman, M., & Quinones-Hinojosa, A. (2014). When gross total resection of a  glioblastoma is possible, how much resection should be achieved? World 
Neurosurgery, 82(1–2), e257-65. https://doi.org/10.1016/j.wneu.2014.01.019 Chaichana, K. L., Jusue-Torres, I., Navarro-Ramirez, R., Raza, S. M., Pascual Gallego, M., Ibrahim, A., Hernandez-Hermann, M., Gomez, L., Ye, X.,  Weingart, J. D., Olivi, A., Blakeley, J., Gallia, G. L., Lim, M., Brem, H., &  Quinones-Hinojosa, A. (2014). Establishing percent resection and residual  volume thresholds affecting survival and recurrence for patients with newly  diagnosed intracranial glioblastoma. Neuro-Oncology, 16(1), 113–122.  https://doi.org/10.1093/neuonc/not137 
Coburger, J., Musahl, C., Henkes, H., Horvath-Rizea, D., Bittl, M., Weissbach, C.,  & Hopf, N. (2013). Comparison of navigated transcranial magnetic stimulation  and functional magnetic resonance imaging for preoperative mapping in  rolandic tumor surgery. Neurosurgical Review, 36(1), 65–66.  
https://doi.org/10.1007/s10143-012-0413-2 
Conti, A., Raffa, G., Granata, F., Rizzo, V., Germanò, A., & Tomasello, F. (2014).  Navigated transcranial magnetic stimulation for “somatotopic” tractography of  the corticospinal tract. Neurosurgery, 10 Suppl 4, 542–554; discussion 554.  https://doi.org/10.1227/NEU.0000000000000502 
Diehl, C. D., Schwendner, M. J., Sollmann, N., Oechsner, M., Meyer, B., Combs,  S. E., & Krieg, S. M. (2019). Application of presurgical navigated transcranial  magnetic stimulation motor mapping for adjuvant radiotherapy planning in  patients with high-grade gliomas. Radiotherapy and Oncology : Journal of the  European Society for Therapeutic Radiology and Oncology, 138, 30–37.  https://doi.org/10.1016/j.radonc.2019.04.029 
Duffau, H. (2020a). Can Non-invasive Brain Stimulation Be Considered to Facilitate 
Reoperation for Low-Grade Glioma Relapse by Eliciting Neuroplasticity?  Frontiers in Neurology, 11, 582489. https://doi.org/10.3389/fneur.2020.582489 Duffau, H. (2020b). Functional mapping before and after low-grade glioma surgery:  A new way to decipher various spatiotemporal patterns of individual  neuroplastic potential in brain tumor patients. In Cancers (Vol. 12, Issue 9, pp.  1–21). MDPI AG. https://doi.org/10.3390/cancers12092611 
Flouty, O., Reddy, C., Holland, M., Kovach, C., Kawasaki, H., Oya, H., Greenlee,  J., Hitchon, P., & Howard, M. (2017). Precision surgery of rolandic glioma and  insights from extended functional mapping. Clinical Neurology and  Neurosurgery, 163, 60–66.  
https://doi.org/https://doi.org/10.1016/j.clineuro.2017.10.008 
Frey, D., Schilt, S., Strack, V., Zdunczyk, A., Rösler, J., Niraula, B., Vajkoczy, P., &  Picht, T. (2014). Navigated transcranial magnetic stimulation improves the  treatment outcome in patients with brain tumors in motor eloquent locations.  Neuro-Oncology, 16(10), 1365–1372. https://doi.org/10.1093/neuonc/nou110 
Jensen, R. L. (2014). Navigated transcranial magnetic stimulation: another tool for  preoperative planning for patients with motor-eloquent brain tumors. In Neuro oncology (Vol. 16, Issue 10, pp. 1299–1300).  
https://doi.org/10.1093/neuonc/nou213 
Koh, T. H., & Eyre, J. A. (1988). Maturation of corticospinal tracts assessed by  electromagnetic stimulation of the motor cortex. Archives of Disease in  Childhood, 63(11), 1347–1352. https://doi.org/10.1136/adc.63.11.1347 
Lefaucheur, J.-P., & Picht, T. (2016). The value of preoperative functional cortical  mapping using navigated TMS. Neurophysiologie Clinique = Clinical 
Neurophysiology, 46(2), 125–133. https://doi.org/10.1016/j.neucli.2016.05.001 McGirt, M. J., Chaichana, K. L., Gathinji, M., Attenello, F. J., Than, K., Olivi, A.,  Weingart, J. D., Brem, H., & redo Quiñones-Hinojosa, A. (n.d.). Independent  association of extent of resection with survival in patients with malignant brain  astrocytoma. Journal of Neurosurgery JNS, 110(1), 156–162.  
https://doi.org/10.3171/2008.4.17536 
McGirt, M. J., Mukherjee, D., Chaichana, K. L., Than, K. D., Weingart, J. D., &  Quinones-Hinojosa, A. (2009). Association of surgically acquired motor and  language deficits on overall survival after resection of glioblastoma  multiforme. Neurosurgery, 65(3), 463–470.  
https://doi.org/10.1227/01.NEU.0000349763.42238.E9 
Oppenlander, M. E., Wolf, A. B., Snyder, L. A., Bina, R., Wilson, J. R., Coons, S.  W., Ashby, L. S., Brachman, D., Nakaji, P., Porter, R. W., Smith, K. A.,  Spetzler, R. F., & Sanai, N. (2014). An extent of resection threshold for  
recurrent glioblastoma and its risk for neurological morbidity. Journal of  Neurosurgery, 120(4), 846–853. https://doi.org/10.3171/2013.12.JNS13184 Raffa, G., Picht, T., Scibilia, A., Rösler, J., Rein, J., Conti, A., Ricciardo, G.,  Cardali, S. M., Vajkoczy, P., & Germanò, A. (2019). Surgical treatment of  meningiomas located in the rolandic area: the role of navigated transcranial  magnetic stimulation for preoperative planning, surgical strategy, and  prediction of arachnoidal cleavage and motor outcome. Journal of  Neurosurgery, 1–12. https://doi.org/10.3171/2019.3.JNS183411 Raffa, G., Scibilia, A., Conti, A., Cardali, S. M., Rizzo, V., Terranova, C.,  Quattropani, M. C., Marzano, G., Ricciardo, G., Vinci, S. L., & Germanò, A. 
(2019). Multimodal Surgical Treatment of High-Grade Gliomas in the Motor  Area: The Impact of the Combination of Navigated Transcranial Magnetic  Stimulation and Fluorescein-Guided Resection. World Neurosurgery, 128,  e378–e390. https://doi.org/https://doi.org/10.1016/j.wneu.2019.04.158 
Seidel, K., Häni, L., Lutz, K., Zbinden, C., Redmann, A., Consuegra, A., Raabe, A.,  & Schucht, P. (2019). Postoperative navigated transcranial magnetic  stimulation to predict motor recovery after surgery of tumors in motor eloquent  areas. Clinical Neurophysiology : Official Journal of the International  Federation of Clinical Neurophysiology, 130(6), 952–959.  
https://doi.org/10.1016/j.clinph.2019.03.015 
Sollmann, N., Fratini, A., Zhang, H., Zimmer, C., Meyer, B., & Krieg, S. M. (2019).  Associations between clinical outcome and tractography based on navigated  transcranial magnetic stimulation in patients with language-eloquent brain  lesions. Journal of Neurosurgery, 132(4), 1033–1042.  
https://doi.org/10.3171/2018.12.JNS182988 
Takahashi, S., Vajkoczy, P., & Picht, T. (2013). Navigated transcranial magnetic  stimulation for mapping the motor cortex in patients with rolandic brain  tumors. Neurosurgical Focus, 34(4), E3.  
https://doi.org/10.3171/2013.1.FOCUS133 
Tarapore, P. E., Findlay, A. M., Honma, S. M., Mizuiri, D., Houde, J. F., Berger, M.  S., & Nagarajan, S. S. (2013). Language mapping with navigated repetitive  TMS: proof of technique and validation. NeuroImage, 82, 260–272.  https://doi.org/10.1016/j.neuroimage.2013.05.018 
Zhang, H., Julkunen, P., Schröder, A., Kelm, A., Ille, S., Zimmer, C., Pitkänen, M., 
Meyer, B., Krieg, S. M., & Sollmann, N. (2020). Short-Interval Intracortical  
