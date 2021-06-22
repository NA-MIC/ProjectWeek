Back to [Projects List](../../README.md#ProjectsList)

# Integration of PyTorch and Slicer

## Key Investigators

- Fernando Pérez-García (University College London & King's College London, UK)
- Andrés Díaz-Pinto (King's College London, UK)
- Andras Lasso (Queen's University, Canada)
- Curtis Lisle (KnowledgeVis, USA)
- Rebecca Hisey (Queen's University, Canada)

# Project Description

<!-- Add a short paragraph describing the project. -->

Investigate the potential issues faced by users who would like to use a trained
convolutional neural network (deep learning model) inside Slicer, using PyTorch.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Issues that will be addressed:

1. How to install PyTorch within Slicer. The main question is whether to install a version with GPU support and, if it does, which version of the CUDA toolkit to install.
1. How to handle the necessary conversion of Slicer nodes (e.g., `vtkMRMLScalarVolumeNode`) to PyTorch objects (e.g., `torch.Tensor`) and vice versa. Look into adding tools to `slicer.util`.
1. Write a tutorial with a toy example using a publicly available dataset.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Investigate issues related to [CUDA versions and GPU drivers](https://docs.nvidia.com/deploy/cuda-compatibility/index.html), and which installation method to use depending on the platform. Maybe, write a GUI to guide the user into choosing an appropriate installation type.
1. Once PyTorch has been installed, look into the best ways to prepare slicer nodes for inference and visualize the results in Slicer.
1. If necessary, write a tutorial (potentially a Jupyter Notebook using [SlicerJupyter](https://github.com/Slicer/SlicerJupyter))

<!-- ## Progress and Next Steps -->

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->



<!-- # Illustrations -->

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

## Post on Discourse

The first discussion about this project appeared on the [Slicer forum (PW35) Projects List](https://discourse.slicer.org/t/pw35-projects-list/17905/4).

## Discussion on GitHub

Some issues about installing PyTorch in Slicer were discussed in the [pull request](https://github.com/Slicer/ExtensionsIndex/pull/1710) to add [SlicerTorchIO](https://github.com/fepegar/SlicerTorchIO) to the Extensions Index.

## Example of a naive `pip` installation

Tried on Linux, driver 430.50 (`nvidia-smi --query-gpu=driver_version --format=csv`).

```python
>>> pip_install('torch')
Collecting torch
  Downloading torch-1.9.0-cp36-cp36m-manylinux1_x86_64.whl (831.4 MB)
Collecting dataclasses
  Downloading dataclasses-0.8-py3-none-any.whl (19 kB)
Requirement already satisfied: typing-extensions in ./opt/Slicer/Nightly/lib/Python/lib/python3.6/site-packages (from torch) (3.10.0.0)
Installing collected packages: dataclasses, torch
  WARNING: The scripts convert-caffe2-to-onnx and convert-onnx-to-caffe2 are installed in '/home/fernando/opt/Slicer/Nightly/lib/Python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed dataclasses-0.8 torch-1.9.0
WARNING: Running pip as root will break packages and permissions. You should install packages reliably by using venv: https://pip.pypa.io/warnings/venv
```

```python-traceback
>>> import torch
>>> torch.cuda.is_available()
/home/fernando/opt/Slicer/Nightly/lib/Python/lib/python3.6/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 10010). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:115.)
  return torch._C._cuda_getDeviceCount() > 0
False
```
