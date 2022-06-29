MONAILabel installation 

prepared for the Virtual MONAI Label workshop June 22nd 2022

[Monailabel GitHub page](https://github.com/Project-MONAI/MONAILabel)

GPU compatibility: 

[https://developer.nvidia.com/cuda-gpus](https://developer.nvidia.com/cuda-gpus)

Installation in WIndows 11:

Install Python 3.9 from Windows Store

[Enable long path names in Windows 11](https://thegeekpage.com/make-windows-11-accept-file-paths-over-260-characters/)

Use Powershell  
cd userdirectory

python -m pip install --upgrade pip setuptools wheel

_\# Install latest stable version for pytorch_

pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

_\# Check if cuda enabled_

python -c "import torch; print(torch.cuda.is\_available())"

True

_\# if false troubleshoot_

[Pytorch get started page](https://pytorch.org/get-started/locally/)

![](https://lh6.googleusercontent.com/6YITAKuz-Ap3IKQGt_6keytnR62ySZ2H-eSMw5NS7CGb5JYewbqdO_vUEfJP8KaSjliBXx3S8bha71WyYHd-pHu8aphc-CmMoAHoOJcpyp_2b4RVeXzcBYX6wpa2-oifHr-Hkrqcm1S77V75rg)

_\# Install latest monailabel version from Github_

  
 

git clone https://github.com/Project-MONAI/MONAILabel

pip install -r MONAILabel/requirements.txt

$Env:PATH += ";C:\\Users\\yourname\\MONAILabel\\monailabel\\scripts"

  
_\# Download Sample Apps_

monailabel apps _\# List sample apps_

monailabel apps --download --name radiology --output apps

_\# Download MSD Datasets_

monailabel datasets _\# List sample datasets_

monailabel datasets --download --name Task06\_Lung --output datasets

_\# Run Segmentation Model._  
_\# Options can be (deepedit|deepgrow|segmentation|segmentation\_spleen|all) in case of radiology app._  
_\# You can also pass comma seperated models like --conf models deepedit,segmentation_

monailabel start\_server --app apps/radiology --studies datasets/Task06\_Lung/imagesTr --conf models segmentation

Once you start the MONAI Label Server, by default it will be up and serving at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Open the serving URL in browser. It will provide you the list of Rest APIs available.
