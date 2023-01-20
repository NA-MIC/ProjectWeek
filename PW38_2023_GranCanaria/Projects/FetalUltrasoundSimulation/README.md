# Fetal Ultrasound Simulation for Delivery Training

## Key Investigators

- Felix von Haxthausen (University of Lübeck, Lübeck, Germany)
- David García Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- Tolga-Can Çallar (University of Lübeck, Lübeck, Germany)
- José Carlos Mateo Pérez (ULPGC, Las Palmas de Gran Canaria, Spain) 
- ...

## Clinical collaboration

- Dr. Juan de León Luis (Head of Obstetrics and Gynecology Department, Hospital General Universitario Gregorio Marañón, Madrid, Spain)

## Medical Background
Intrapartum assessment of the **fetal head position** and pelvic station  are  essential  in  the  management  of  labor.  Precise knowledge of these parameters will assist in the correct identification of normal vs. abnormal labor patterns, and among the latter indicate when medical or operative intervention may be required.

Identifying the fetal position is specially important during forceps-assisted delivery. Forceps are slick metal objects that resemble big spoons or tongs. They are contoured to fit the baby's head and are placed around the infant's head. Depending on the position of the fetus's head, the techniques and manouvers used by obstetricians are different.

**Ultrasound imaging** is commonly used to estimate the fetal position. In a first step, the clinician identifies the fetus spine using ultrasound to infer the position of the fetus body. Then, the occiput is localized to determine the exact position of the head.

<img src="https://user-images.githubusercontent.com/10816661/213690390-b934d36d-67f4-4bbe-b888-6ba5dc4129d8.png" alt="drawing" width="650"/>

<img src="https://user-images.githubusercontent.com/10816661/213690550-6a314e62-ad51-4233-b02f-619ca85c56e2.png" alt="drawing" width="650"/>

## Project Description
The goal of this project is to generate fake ultrasound images that can be used during medical training. These images should be as realistic as possible to enable trainees to correctly identify the fetus position in the simulated ultrasound images.

PLUS Toolkit already offers a [tool](http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceUsSimulator.html) to generate fake ultrasound images based on 3D models. However, a general problem is that one needs to provide acoustic properties of each 3D model/tissue for the ultrasound image generation. 

## Objective
1. Test ultrasound simulation tool offered by PLUS Toolkit and visualize simulated images and models in 3D Slicer.
2. Create a tool that automatically assigns acoustic properties to each 3D model and generates the according config file for the PLUS ultrasound image generation server.
3. Calculate acoustic properties for fetal ultrasound simulation and improve realism of simulated ultrasound images.
4. Discuss ultrasound simulation technology with the 3D Slicer community. Other methods? AI?

## Approach and Plan
Development of tool to assign tissue acoustic properties:
1. Use the Total Segmentator to create the 3D models with assigned organ definition based on CT data.
2. Create and define a lookup table (LUT) that assigns the accoustic propeerties to each organ label. 
3. Develop a tool or module that generates the config file based on the models and the LUT.

## References

- Related project from 35th NA-MIC Project Week: [VR for Birth Delivery Training](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/VRBirthDeliveryTraining/)

- Training system for forceps-assisted delivery developed in 3D Slicer by Universidad Carlos III de Madrid: [VIDEO](https://www.youtube.com/watch?v=EEasWbH1jZI)

- García-Sevilla, M. et al. (2018). Performance Evaluation to Improve Training in Forceps-Assisted Delivery. In: , et al. OR 2.0 Context-Aware Operating Theaters, Computer Assisted Robotic Endoscopy, Clinical Image-Based Procedures, and Skin Image Analysis. CARE CLIP OR 2.0 ISIC 2018 2018 2018 2018. Lecture Notes in Computer Science(), vol 11041. Springer, Cham. https://doi.org/10.1007/978-3-030-01201-4_9

- Sherer, D.M., Miodovnik, M., Bradley, K.S. and Langer, O. (2002), Intrapartum fetal head position II: comparison between transvaginal digital examination and transabdominal ultrasound assessment during the second stage of labor. Ultrasound Obstet Gynecol, 19: 264-268. https://doi.org/10.1046/j.1469-0705.2002.00656.x
