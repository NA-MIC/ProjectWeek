---
layout: pw44-project

permalink: /:path/

project_title: Hands-on tutorials extension
category: IGT and Training
presenter_location: 

key_investigators:

- name: Alejandro Rodríguez Moreno
  affiliation: Ebatinca SL
  country: Spain

- name: Csaba Pinter
  affiliation: Ebatinca SL
  country: Spain

- name: Interested people welcome!
  affiliation: Andriy
  country: Tina, Andras?

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Unfortunately the issue of useful and up-to-date tutorials is quite difficult, because
- Slide-based tutorials need to be updated manually (see that many tutorials are pre-5.0 in the [training material](https://training.slicer.org))
- Video tutorials are impossible to update
- In the above two cases it is next to impossible to offer them in different languages
- In-repo markdown files are quite limited in format and usefulness

We have developed a tutorials infrastructure and some basic tutorials for a commercial project, which could be repurposed for Slicer core. Basically it consists of a curriculum that is described by a JSON file, with dependencies among the tutorials, and a set of hands-on tutorials that can be started from this home screen.

The hands-on tutorials guide the users through a certan sequence of steps using targeted tooltips and a mechanism detecting if the current step has been completed successfully. This way we could offer some basic tutorials for Slicer core in multiple languages, which is easier to maintain than the current modalities. Of course maintenance will remain an issue, because if API changes the tutorials will break, but the basic functions of Slicer has not really changed in the last decade, and hopefully there won't be much maintenance necessary.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A: Reach a common understanding about the necessity of this in general
2. Objective B: Get started with the extension



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Discuss the proposal, hopefully in a breakout session, but in any case involving the interested people
    a. Decide if the basics are sensible, feasible, and useful, or not
    b. Define an initial set of tutorials
2. Start to adapt the tutorials infrastructure to the proposed goals



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Development of the tutorial extension was initiated and is currently hosted in the following repository: https://github.com/xskere/SlicerTutorial.

2. A dependency system was used to control tutorial accessibility and to build the tutorial tree, ensuring that tutorials which depend on others (e.g., `Tutorial_002` depending on `Tutorial_001`) can only be accessed once their prerequisites are completed.

3. The tutorial system is built around a state machine structure; initially, all step logic was implemented inside the `enter()` function with setup and validator functions defined elsewhere, which made maintenance and updates difficult.

4. Based on feedback (notably from Andras), the tutorial authoring model was refactored to improve readability, sustainability, and maintainability while preserving the original state machine design.

5. Each tutorial is now defined as a fixed sequence of steps written linearly, where every step has a dedicated setup function and a validator function.

6. For each step, the setup function prepares the tutorial state, followed by a validator function that determines whether the step has been successfully completed.

7. Each step is appended to a `steps` array as a dictionary that contains required metadata describing how the step behaves and how it is validated:
Each step dictionary includes a pointer to the setup function, a pointer to the validator function, a `completed` boolean flag (defaulting to `False`), and a short textual `description` used to guide the user if validation fails.
An optional `module` field can also be included in the step dictionary to restrict tooltip visibility to a specific module, which is only necessary when the tooltip is attached to widgets that exist in that module.

8. Each tutorial step operates in one of two validation modes: continuous validation, where the validator function runs repeatedly until the condition is met, or manual validation, where the validator is only triggered when the user clicks “Go next step”.

9. Continuous validation is enabled by calling `self.timerCheck()` at the end of the step’s setup function.

10. At present, two simple mock tutorials are fully functional: one demonstrates continuous validation and the other demonstrates manual, user-triggered validation.

11. Three additional tutorials currently exist as placeholders, containing three steps each where the validator always returns `True`.

12. Tutorial progress is persisted locally in the file `%LOCALAPPDATA%/NA-MIC/Slicer/Tutorials/tutorialProgress.json`.

13. The progress file stores a JSON object where each tutorial has a `completed` state and an `enabled` flag that controls whether the tutorial appears in the tutorial tree.

14. If a tutorial is disabled, it is hidden from the tutorial tree, and any tutorials that depended on it will instead inherit its dependency chain.

15. Investigation was done to augment the functionality of these tutorials, for example:

- The TutorialMaker extension could be extended to automatically generate review slides after each step once validation succeeds, allowing users to revisit completed steps without rerunning the entire tutorial.
- Tutorials are currently linear and do not support navigating back to previous steps.
- Non-linear navigation could be implemented in the future using scene views to save and restore the application state at each step.
- Scene views can be created and restored programmatically, enabling step-by-step state restoration by index or by name.


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="1642" height="595" alt="Image" src="https://github.com/user-attachments/assets/92e1aa2e-c6ab-4ed5-affc-285a2336cb72" />
Part of the curriculum tree in the commercial app that we propose to adapt to Slicer core



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


* The commercial app in question: [https://ebatinca.com/productos/start](https://ebatinca.com/productos/start)
* The current training material for Slicer core: [https://training.slicer.org/](https://training.slicer.org/)

