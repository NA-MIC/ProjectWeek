Back to [Projects List](../../README.md#ProjectsList)

# Automatic Standardize Orientation IOS

## Key Investigators

- Nathan Hutin (University of Michigan)
- Luc Anchling (University of Michigan)
- Marcela Gurgel (University of Michigan)
- Felicia Miranda (University of Michigan)
- Najla Al Turkestani (University of Michigan)
- Selene Barone (University of Michigan)
- Lucia Cevidanes (Univerisity of Michigan)
- Juan Prieto (University of North Carolina)

# Project Description

 A correct relationship of the teeth in upper and lower dental arches of IntraOral Surface (IOS) scans depends on standardized spatial orientation 
in an antero-posterior (yaw rotation), lateral (pitch rotation), and axial  (roll rotation) planes induced by  differences in acquisiton of  scans, growth and treatment. Serial IOSs have been used for evaluation and understanding of the changes resulting from
interactions of groiwth and treatment, as dental position and movement can be quantified by 3D linear and angular measurements based on homologous landmarks.

Reliable and accurate measurements should be used for a precise diagnosis and for assessment of treatment outcomes. Inconsistency in the orientation fo the IOs can lead to errors in measurements at diffferent time points for the smae patient and can adversely affect research conclusions and treatment plans. Up to now  IOS  orientation in Slicer has been manually perfomed using the Slicer Transforms module, but the manual orientation is time consuming and prone to inconsistencies.


This project develops a Slicer extension for Automated Standardized Orientation of IOS (ASOIOS). The Automated Standardized Orientation (ASO) tool presented in this project includes the follwoing image processign steps:
1. Automatic identificatio of the centroid of the right  and left first molar and the centroid of the buccal and lingual surfaces of one the central incisors that  determine perpendicular lines, and then determine a third  line perpendiculr to these first two.
2. Computation of the difference between the angles of these 3 lines and a new IOS and an IOS in a gold stardand orientation.
3. Apply transform matrix to approximate the scans spatial orientation (pre-orientation)
4. Compute ICP between the centroid of the 3 reference  teeth in each scan.
5. Automatically Ccmpute occlusal landmarks on IOS r, using a deep learning landmark identification algorithm (ALIIOS). 
6. ASOIOS  then uses a landmark-based registration approach (ICP of he landmarks identified with ALIIOS) to automatically orient an IOS in a  standardized spatial orientation. Availabble options includes, user choice of orienting each IOS separately or by pair of dental arches in occlusion;users can also choose which tooth to use to orient the scan.

Link to GitHub repository https://github.com/lucanchling/ASO

## Objective


1. Automatically orient IOS scans without failures
2. Receive feedback to improve my code and facilitate future maintenance
3. Display error window
4. Improve progress bar
5. Document the code and read me file. 
6. Includetest cases

## Approach and plan
1. Develop in collaboration with Luc Anchling [ASO_CBCT](../ASO_CBCT/REAMDED.md) a Slicer Module,ASO, that will be deployed as part of Slicer Automated  Dental Tools. 


## Progress and Next Steps

### Progress
1.  Add user documentation in [README](https://github.com/lucanchling/ASO/blob/main/README.md)

### Next Step

1.  Receive feedback to improve my code and facilitate future maintenance
2.  Beta Extension for internal users testing prior to deployment 

# Illustrations
### User interface
![aso_user_interface](https://user-images.githubusercontent.com/72212416/214947035-c955bbc0-4a6a-4687-9ed0-2ece672f8284.png)
### Oriented Output Example
![aso_demonstation](https://user-images.githubusercontent.com/72212416/214982300-d9174a64-5c28-41dd-b26c-9264bf3d852b.png)
Green : scan without orientation.
Red : Scan at the 5th step.
Yellow : Final Orientation.




