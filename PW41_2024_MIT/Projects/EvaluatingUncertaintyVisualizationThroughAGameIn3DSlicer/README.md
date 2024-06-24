---
layout: pw41-project

permalink: /:path/

project_title: Evaluating Uncertainty Visualization through a game in 3D slicer
category: IGT and Training
presenter_location: In-person

key_investigators:

- name: Mahsa Geshvadi
  affiliation: ' Brigham and Women''s Hospital'
  country: USA

- name: Sarah Frisken
  affiliation: ' Brigham and Women''s Hospital'
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Uncertainty is present in all medical images and originates from different sources. Uncertainty is difficult to interpret due to its probabilistic nature, and communicating it is equally difficult. In this project, we developed an uncertainty visualization module on 3D Slicer, enabling users to explore different uncertainty visualization techniques. The key challenge now is evaluating these techniques for real-world applicability. To address this, we implemented a game for quantitative evaluation of uncertainty visualization. In the game, users perform tasks requiring decision-making under uncertainty, and we measure their performance with and without visualization using scores. Specifically, the game simulates decision-making during tumor resection surgery, where MRI images have uncertainty due to brain shifts. Users must decide whether to carve out the tumor at specific locations, reflecting the real surgical decision-making process.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A: Uncertainty visualization helps make better decisions under uncertainty.
2. Objective B: Exploring and evaluating the Uncertainty Visualization module with a game helps improve the understanding of uncertainty.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Training level:  helps participants become familiar with uncertainty in the game and explore different visualization techniques. Players can see the ground truth segmentation and their scores, allowing them to observe the impact of their decisions directly.

 <video
   controls muted
   src="https://github.com/NA-MIC/ProjectWeek/assets/34935139/940dcb5f-424f-4c54-820b-9c6053137df8"
   style="max-height:640px; min-height: 200px">
 </video>






3. The challenge phase builds on skills learned during training, where players perform tasks without seeing the ground truth segmentation or their scores and cannot undo actions. It consists of two steps: first, making decisions without uncertainty visualizations on a different case, and second, repeating the task with uncertainty visualizations on the same case, without any prior feedback or guidance.




 <video
   controls muted
   src="https://github.com/NA-MIC/ProjectWeek/assets/34935139/694791d0-b8e2-4a51-8695-60166ba24652"
   style="max-height:640px; min-height: 200px">
 </video>



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Explore uncertainty visualization evaluation through a game in more scenarios.
2. Make the game more complex by adding new levels.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [https://github.com/mahsageshvadi/UncertaintyVisualization](https://github.com/mahsageshvadi/UncertaintyVisualization)

