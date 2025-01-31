Back to [Projects List](../../README.md#ProjectsList)

# Maxillofacial Surgery Virtual Planning Applications based on Slicer

## Key Investigators

- Miguel Ángel Rodriguez-Florido, PhD (GTMA, University of Las Palmas de Gran Canaria and Children’s, Women’s and General Hospital Insular)
- Christian Buritica, MD (Children’s, Women’s and General Hospital Insular)
- Mauro Domínguez (Software Developer of BoneReconstructionPlanner)
- Thank you Sam Horvath for her help and support with Osteotomy Planner and other functionalities in Slicer.

# Project Description

This project proposes to study the capabilities of two extensions of Slicer (Osteotomy Planner and BoneReconstructionPlanner) to be included at the classes at the Medical School in our University and to the planning tools used for clinical maxillofacial cases.

## Objective

1. To know and test the features and parameters of both extensions for trying them with our own clinical requisites and datasets.
2. To detect needs to improve the capabilities of both extensions.
3. To get ability for using both extensions in real clinical cases.

## Approach and Plan

1. To Install and run the software with our own clinical cases, checking if [BoneReconstructionPlanner videotutorial](https://youtu.be/g9Vql5h6uHM) should be updated and executing the [automatic-tests](https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/issues/68). Later we'll play with the features of this extesion.
2. To discuss with extension’s developers the best configuration of the software for our clinical cases.
3. Beta testing of the extensions in our environment and send feedback to the community.

## Progress and Next Steps

1. We discussed with Sam Horvath about the Osteomy Planner extension and how to use it to get our goals. We have learnt how it works in the last release of Slicer and we learnt more general surfaces/meshes operators that can help us for teaching general concepts of the surgery technique to medical students.
2. We have checked that the BoneReconstructionPlanner extension is running at the current stable release of Slicer and we have been using it for one of our own clinical cases.
3. We worked with our own clinical case and we got some encouraging results. We can try to include this extension in the daily work of the hospital (support at clinical cases).

# Illustrations of results

1. We used the Osteotomy planner extension, and other functionalities of Slicer, to work with some of our own cases. We understand how the software works in order to explain the procedure's concepts to the medical students:

<p float="center">

 <img src="https://user-images.githubusercontent.com/123319626/216994628-4e6d623f-d075-4ec0-9615-1f4b82e7feb4.png" width="30%">
 <img src="https://user-images.githubusercontent.com/123319626/216994676-03a68842-8c7d-42d8-8d06-5cdea97130c0.png" width="30%">
 <img src="https://user-images.githubusercontent.com/123319626/216994713-38778310-c4d2-4eb2-afb7-bd4b74037f79.png" width="30%">
</p>

<p float="center">
 <img src="https://user-images.githubusercontent.com/123319626/216994739-19bb701a-f620-46c4-9cbf-412c738a8df4.png" width="30%">
 <img src="https://user-images.githubusercontent.com/123319626/216994778-a79d37fc-0f19-4c54-aaa0-5953350c8f5f.png" width="30%">
</p>

Now, we can improve the use of the Slicer in our Medical School and include more features for our technological teaching.

2. We followed the instructions of the videotutorial and we got some points where, perphaps, it could be good to include more information for new users of Slicer (more in the case of clinical users). In any case, we got the next results with our own case:

a. 3D models segmented for the mandible and the fibula:

<p float="center">
<img src="https://user-images.githubusercontent.com/123319626/216999790-606192bb-1b64-4b9f-ae8f-86683e750d49.png" width="30%">
<img src="https://user-images.githubusercontent.com/123319626/216999829-5964547e-9b48-4fbb-8488-232388173e7c.png" width="30%">
</p>

b. Fibula and mandible guides:

<p float="center">
<img src="https://user-images.githubusercontent.com/123319626/217000315-eafb494d-b0dc-4776-98d8-ab27822b9e54.png" width="305">
<img src="https://user-images.githubusercontent.com/123319626/217000357-fdf499c2-f689-4b0b-91dd-2ad1908dd0ca.png" width="30%">
</p>

c. Final result:

<p float="center">
<img src="https://user-images.githubusercontent.com/123319626/217000479-bc93a100-258a-4ced-a36e-31ca61a9e58e.png" width="30%">
</p>

Of course, we'll print in 3D these models for teaching to our medical students.

# Background and References

1. Osteotomy planner: https://www.kitware.com/osteotomy-planner-2-0-release/
2. Continue with the project: https://projectweek.na-mic.org/PW36_2022_Virtual/Projects/MandibleReconstructionAutomaticPlanning/
