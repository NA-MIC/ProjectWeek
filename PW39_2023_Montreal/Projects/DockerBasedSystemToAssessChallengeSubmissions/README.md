---
layout: pw39-project

permalink: /:path/

project_title: Docker-based system to assess challenge submissions
category: Infrastructure
presenter_location: Online

key_investigators:

- name: Roya Khajavibajestani
  affiliation: Brigham and Women’s hospital
  country: USA

- name: Erik Ziegler
  affiliation: Yunu
  country: Netherland

- name: Ron Kikinis
  affiliation: Harvard Medical School
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Project Description:

Our project is focused on developing a Docker-based submission mechanism for challenge participants. To maintain fairness and make sure that the test set is not used in the training process, the test set will not be released to the participants. Instead, participants will be required to containerize their methods using Docker and submit their Docker containers for evaluation.

Docker provides an excellent solution for running algorithms in isolated environments known as containers. In our project, we will leverage Docker to create a container that replicates the participants' pipeline requirements and executes their inference script. By encapsulating the entire environment within a container, we can ensure consistent execution and reproducibility.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

- Create a sample docker container for submission
- Create an evaluation mechanism on the challenge website
- Create documentation, guidelines, and tutorial for participants

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

- Design the docker container, input/output mechanism, requirements, and methods to perform inference using a subset of the validation set.
- Create an evaluation mechanism on the challenge website
- Create a sample submission docker for the test phase and test it on the challenge website
- Create documentation to publish in phase 2 of the challenge.

## Progress and Next Steps

<!-- Update this section as you make progress, describing what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->
We created a baseline algorithm to assist participants with their submissions.
We used evalutils to develop a code template that participants can customize with their specific algorithms.
We will work with Grand Challenges to create the input and output interface standards for participants which aids us in creating clear instructions on how to format and provide the necessary data.
Participants have to follow the guidelines for building their Docker containers. We will link to the guideline on the original [challenge website](https://lnq2023.grand-challenge.org/).

**Evaluator container**:

For Generating The Project Structure we will use Evautils.
Evalutils contains a project generator based on CookieCutter that I can use to generate the boilerplate for our evaluation.

We will also generate our project with docker by running a container and sharing our current user id:
````
docker run -it --rm -u `id -u` -v $(pwd):/usr/src/myapp -w /usr/src/myapp python:3 bash -c "pip install evalutils && evalutils init evaluation LNQ2023"
````

Either of these commands will generate a folder called LNQ2023 with everything we need to get started.

The .gitattributes file at the root of the repository specifies all the files which should be tracked by git-lfs. By default all files in the ground truth and test directories are configured to be tracked by git-lfs, but they will only be registered once the git lfs extension is installed on my system and the git lfs install command has been issued inside the generated repository.

The structure of the project will be:

````
└── LNQ2023
    ├── build.sh            # Builds your evaluation container
    ├── Dockerfile          # Defines how to build your evaluation container
    ├── evaluation.py       # Contains your evaluation code - this is where you will extend the Evaluation class
    ├── export.sh           # Exports your container to a .tar file for use on grand-challenge.org
    ├── .gitattributes      # Define which files git should put under git-lfs
    ├── .gitignore          # Define which files git should ignore
    ├── ground-truth        # A folder that contains your ground truth annotations
    │   └── reference.csv   # In this example the ground truth is a csv file
    ├── README.md           # For describing your evaluation to others
    ├── requirements.txt    # The python dependencies of your evaluation container - add any new dependencies here
    ├── test                # A folder that contains an example submission for testing
    │   └── submission.csv  # In this example the participants will submit a csv file
    └── test.sh             # A script that runs your evaluation container on the test submission
````
evaluation.py.  is the file where we will extend the Evaluation class and implement the evaluation for our challenge. In this file, a new class has been created, and it is instantiated and run with:

````
if __name__ == "__main__":
   LNQ2023().evaluate()
````
This is all that is needed for evalutils to perform the evaluation and generate the output for each new submission.

# Background and References

<!-- If you developed any software, include a link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
The generated code for segmentation tasks:
````
class Myproject(ClassificationEvaluation):
    def __init__(self):
        super().__init__(
            file_loader=SimpleITKLoader(),
            validators=(
                NumberOfCasesValidator(num_cases=2),
                UniquePathIndicesValidator(),
                UniqueImagesValidator(),
            ),
        )

    def score_case(self, *, idx, case):
        gt_path = case["path_ground_truth"]
        pred_path = case["path_prediction"]

        # Load the images for this case
        gt = self._file_loader.load_image(gt_path)
        pred = self._file_loader.load_image(pred_path)

        # Check that they're the right images
        assert self._file_loader.hash_image(gt) == case["hash_ground_truth"]
        assert self._file_loader.hash_image(pred) == case["hash_prediction"]

        # Cast to the same type
        caster = SimpleITK.CastImageFilter()
        caster.SetOutputPixelType(SimpleITK.sitkUInt8)
        gt = caster.Execute(gt)
        pred = caster.Execute(pred)

        # Score the case
        overlap_measures = SimpleITK.LabelOverlapMeasuresImageFilter()
        overlap_measures.Execute(gt, pred)

        return {
            'ASSD': overlap_measures.GetASSD(),
            'DiceCoefficient': overlap_measures.GetDiceCoefficient(),
        }

````
The next step is Building and testing, exporting the evaluation container and working on the Algorithm container.
