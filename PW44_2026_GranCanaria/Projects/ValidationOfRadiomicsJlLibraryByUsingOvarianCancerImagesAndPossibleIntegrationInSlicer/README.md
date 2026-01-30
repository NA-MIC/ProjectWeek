---
layout: pw44-project

permalink: /:path/

project_title: Validation of Radiomics.jl library by using ovarian cancer images and possible integration
  in Slicer
category: Quantification and Computation
presenter_location: 

key_investigators:

- name: Paolo Zaffino
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Ciro Benito Raggio
  affiliation: Karlsruhe Institute of Technology
  country: Germany

- name: Francesca Spadeda
  affiliation: Karlsruhe Institute of Technology
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


[Radiomics.jl](https://github.com/pzaffino/Radiomics.jl) is a pure Julia library for radiomics feature extraction.
Being a pretty new library, we want to test and validate it by using CT of ovarian cancer patients.

We would also like to investigate the possibility of calling it from the embedded Python in Slicer.

Of course any suggestion is more than welcome.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Test Radiomics.jl on ovarian cancer CT 
2. Investigate the possibility of calling Radiomics.jl main function in Python




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Compare Radiomics.jl features with those computed by PyRadiomics (considered as the gold standard)
2. Create a shared library and call it from Python
3. Collect comments/suggestions



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Tested the library on ovarian cancer CT (a few features must be fixed)
2. Tested juliacall to use Radiomics.jl from Python (you don't need to install Julia)
```bash
pip install juliacall
```

```python
from juliacall import Main as jl
jl.seval('import Pkg; Pkg.add("Radiomics")')
```
```python
import SimpleITK as sitk
import numpy as np

from juliacall import Main as jl
jl.seval("using Radiomics")

ct_sitk = sitk.ReadImage('DATA_PATH/ct.nii.gz')
mask_sitk = sitk.ReadImage('DATA_PATH/mask.nii.gz')

ct = sitk.GetArrayFromImage(ct_sitk)
mask = sitk.GetArrayFromImage(mask_sitk)

spacing = list(ct_sitk.GetSpacing())

radiomic_features = dict(jl.Radiomics.extract_radiomic_features(ct, mask, spacing))
```
3. Created a shared library and used it both in Python and C++

```julia
using PackageCompiler

create_library(".", "radiomicsjl_build";
               lib_name="libradiomicsjl",
               force=true,
               incremental=true,
               filter_stdlibs=true)
```

4. Collected very useful comments, suggestions, and potential use-cases (thanks Andrey Fedorov!)


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Radiomics.jl](https://raw.githubusercontent.com/pzaffino/Radiomics.jl/refs/heads/main/Logo%20Radiomicsjl.png)

![](https://github.com/user-attachments/assets/1dc97ca0-90a1-4e5f-ae40-67730e3dae16)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- Radiomics.jl official page: [https://www.radiomicsjl.org](https://www.radiomicsjl.org)
- Radiomics.jl source code: [https://github.com/pzaffino/Radiomics.jl](https://github.com/pzaffino/Radiomics.jl)
- Pyradiomics documentation: [https://pyradiomics.readthedocs.io](https://pyradiomics.readthedocs.io)
- Pyradiomics source code: [https://github.com/AIM-Harvard/pyradiomics/tree/master](https://github.com/AIM-Harvard/pyradiomics/tree/master)
