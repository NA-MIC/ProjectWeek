---
layout: pw42-project

permalink: /:path/

project_title: 'Update PyRadiomics and SlicerRadiomics build and CI'
category: Quantification and Computation

key_investigators:

- name: Joost van Griethuysen
  affiliation: The Netherlands Cancer Institute
  country: The Netherlands

---

# Project Description

<!-- Add a short paragraph describing the project. -->


PyRadiomics was first introduced in 2017 and remains a very popular python package
to compute radiomics features. It is integrated into 3D slicer via the SlicerRadiomics module.
However, both projects are not heavily maintained anymore, causing the CI chain and build tools
to be out of date.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Update build tools and CI pipelines for both PyRadiomics and SlicerRadiomics to be up to date
with the latest python versions and build tools



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

- Scikit-ci is deprecated and should be replaced
- Invesitate option of using `cibuildwheel`
- Update metadata to adhere to new standards.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


- Update `pyproject.toml` and remove deprecated files (e.g. `setup.py`, `setup.cfg`, `requirements*.txt`, `MANIFEST`)
- Run cookiecutter from [Scientific Python Library Development Guide](https://learn.scientific-python.org/development/) separately and use it to update pyradiomics
  structure.
  - Change build system to scikit-build-core
  - Build C-extensions using CMake
  - Moves CI/CD from CircleCI/AppVeyor to GitHub Actions.
- Create [PR #203](https://github.com/Grokzen/pykwalify/pull/203) in pykwalify to deal with deprecation warning. Ignore
  this warning in the build process of pyradiomics for the time being.
- Disable pre-commit part of CI pending the correct setup of CI/CD.
- Local build & test now passing.

ToDo:
- [ ] Update CI configuration to match supported python versions enabled in CircleCI/AppVeyor builds.
- [ ] Currently, CI is failing on METADATA mismatch in wheel generation. This is due to a mismatch in generated
  version string (a version parsed from a metadata dir doesn't contain the date suffix, whereas the on in the generated
  wheel does). Fix the version string error to allow CI to pass.
- [ ] Add exceptions for style errors in pre-commit to allow it to pass initially. 
- [ ] Later, apply style changes to make pyradiomics adhere to the configured style.
- [ ] Review readthedocs documentation generation.
- [ ] Review CD configuration to publish releases on tags pushed onto the master branch in the main repo.


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Documentation
- [https://pyradiomics.readthedocs.io](https://pyradiomics.readthedocs.io)
- [https://cibuildwheel.pypa.io](https://cibuildwheel.pypa.io)

Source code
- [https://github.com/AIM-harvard/pyradiomics](https://github.com/AIM-harvard/pyradiomics)
- [https://github.com/AIM-harvard/slicerradiomics](https://github.com/AIM-harvard/slicerradiomics)

Misc
- [Scientific Python Library Development Guide](https://learn.scientific-python.org/development/)
