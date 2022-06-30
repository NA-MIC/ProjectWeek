Back to [Projects List](../../README.md#ProjectsList)

# MONAI Label lung and airway segmentation

## Key Investigators

*   Rudolf Bumm, MD (KSGR)
*   Andres Diaz-Pinto (Nvidia)

# Project Description

MONAI Label is a server-client system that facilitates interactive medical image annotation by using AI. It is an open-source and easy-to-install ecosystem that can run locally on a machine with single or multiple GPUs. Both server and client work on the same/different machine. It shares the same principles with MONAI.

The aim of the project is to set up, train and evaluate a lung and airway server model in MONAI Label

## Objective

*   set up MONAI Label on a PC with moderate to high-end Nvidea GPU
*   load MONAI Label apps and datasets
*   use Lung CT Segmenter for rapid creation of detailed CT Lung labels in MONAI Label for
    *   right lung
    *   left lung
    *   airways
*   do training with the server model 
*   evaluate the AI´s auto-segmentation performance

## Approach and Plan

fine tune the MONAI Label server  
provide links

## How to set up a MONAI Label in Windows 11

*   [Please refer to this document](./MONAILabel_Installation.md) 

## Progress and Next Steps

*   Demonstration of the current workflow at the MONAI Label Workshop June 22nd 2022
*   Youtube Video: [https://www.youtube.com/watch?v=wtiEe_jiUzg](https://www.youtube.com/watch?v=wtiEe_jiUzg) 

# Illustrations / Results

![](https://lh4.googleusercontent.com/qDgKazWsVFylsaoVOcR87y2OwPsTuMRULtLIZ5dDpppktTaG5rKrFUpC3PQj0Js7Ow2TPMa1ixEP2J8qnKFrzCrY2Nv99W4g9Q33omjdvfxT7jeCysN_wGN_rxLgSLzfQLGWgixZsm8yC9aN5r-img)

Fig 1: MONAI Label inference after providing 2 high quality samples and training (50 epochs): Not usable

![](https://lh3.googleusercontent.com/DmJb1FLEcoDjGLF0VkVvT7JIicjt10KYGdRbE1NSpvoXFH-CANWPuboDzpTehbe48iKEl9AQITmrd7XuwrQpefu7QeqbM4Q5soPRKyK8V6ZouS3js62eUNZ4BxIzhXgI5BPWHVI2cUBrQtI-ENNvBg)

Fig 2: Status after providing 5 more high-quality labels and  training 1000 epochs /  5 iterations (1 h with RTX 3070 Ti), "deepedit" model:    
ML is able to divide right and left lungs as well as airways, but resolution is low.   

![](https://lh5.googleusercontent.com/MJwUyGBtI15UYL2OPc6LLyCUpKNpk_0G9GddXcovVYWKD_EXOlIWuWXthbkE-n4FPC-Ay_F-bNZ1EtWz5o9bR3Wzjf7OoUgMJZnejxoLejLW46gvxpUzCgDyx8nIEl3aI4U3T_biYB0Vm4tT7Mq0fQ)

Fig 3: Status after labelling 17 more datasets, training another 1000 epochs /  22 iterations (6 h with RTX 3070 Ti), "segmentation" model:   
Much better resolution.  

# ![](https://lh5.googleusercontent.com/kN_jvl7i-Osv662Yhh69wRg5nMS4PzdYQarTBGYe6gTyq6-1A-xAcxkUSdIlFiSdyr3WXxk_WQGfQKAuwCp2OAiHcN2irQfeW1-DsWDgx31aRzVDy6KwIQo1Yf955Dh3k4K0YuLEVfwNkOG9kPkjPQ)

Fig 4: Autosegmentation after label correction, 500 epochs / 22 iterations training (1.5h RTX 3070 Ti):  
Good result! 

# Background and References

https://github.com/Project-MONAI/MONAILabel

https://github.com/rbumm/SlicerLungCTAnalyzer
