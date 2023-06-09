# Automatic Registration Intra Oral Scan

---
layout: pw39-project

permalink: /:path/

project_title: Automatic Registration Intra Oral Scan
category: Semgnetation / Classification / Landmarking
presenter_location: In-person

key_investigators:
- name: Nathan Hutin
  affiliation: University of Michigan

- name: Luc Anchling
  affiliation: University of Michigan
  country: France
  
- name: Lucia Cevidanes
  affiliation: University of Michigan
  country: USA
  
- name: Selene Barone
  affiliation: University of Catanzaro
  country: Italy
  
- name: Juan Prieto
  affiliation: University of North Carolina
  country: USA
  
- name: Jonas Bianchi
  affiliation: University of Pacifique
  country: USA
  
- name: Marcela Gurgel
  affiliation: University of Michigan
  country: USA
  
- name: Najla Al Turkestani
  affiliation: University of Michigan
  country: USA
  
- name: Felicia Miranda
  affiliation: University of Sao Paulo
  country: Brezil
  
- name: Denise Curado
  affiliation: University of Michigan
  country: USA
  
- name: Kinjal Mavani
  affiliation: University of Michigan
  country: USA
  
- name: Kinjal Mavani
  affiliation: University of Michigan
  country: USA

- name: Margaret Eason
  affiliation: University of Michigan
  country: USA
  
- name: Aron Aliage del Castilo
  affiliation: University of Michigan
  country: USA
  
---


# Project Description
This project propose a tool to automatically register intra oral scan of upper jaw. The method can register growth and non-growing patient. 
The registration method is based on neural network to create a region of interest on the palate, and ICP (Iterest Closest Point) to register. 
The neural network has been trained with extraction and non-extraction case, growing and non-growing patient to have robust neural network. 
We will leave the option to the users to also register the mandible by applying the transformation matrix of the maxilla to the mandible.

The actual code is on this [repository](https://github.com/HUTIN1/ALIDDM/tree/refactoring/py/Palete/CNN). 

## Objective 
1. Start to implement automatic registration of IOS in Slicer
2. Deploy Areg 

## Approach And Plan
1. Find a method to perform Automatic Registration of IOS
2. Train a neural network to create a region of interest
3. Implement automatic registration for region of interest


## Progress and Next Steps
1. Method and script working
2. Implement the script in [Areg](https://github.com/lucanchling/AREG)
3. Deploy Areg in [SlicerAutomatedDentalTools](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools) to be available to all users

# Illustrations


![Screenshot from 2023-06-09 11-45-14](https://github.com/NA-MIC/ProjectWeek/assets/72212416/8f2ee89a-9801-4f60-ace8-a7778779c009)

Region of interest make by neural network

![Screenshot from 2023-06-09 13-48-29](https://github.com/NA-MIC/ProjectWeek/assets/72212416/90cc7bb6-995b-4046-84c3-5ac118abc04c)

Legend :
- pink : initial scan
- blue : clinician registration
- yellow : automatic registration
