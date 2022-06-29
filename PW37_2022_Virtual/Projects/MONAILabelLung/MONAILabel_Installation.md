## MONAI Label installation 

_as prepared for the Virtual MONAI Label workshop_  
_June 22nd, 2022_  
_Rudolf Bumm (KSGR)  and Andres Diaz-Pinto (Nvidia)_

The [Monailabel GitHub page is here.](https://github.com/Project-MONAI/MONAILabel)

GPU compatibility:

[https://developer.nvidia.com/cuda-gpus](https://developer.nvidia.com/cuda-gpus)

## Installation in Windows 11 step by step:

Install Python 3.9 from Windows Store

[Enable long path names in Windows 11](https://thegeekpage.com/make-windows-11-accept-file-paths-over-260-characters/)

Use an elevated Powershell (admin mode)   
cd userdirectory

```
python -m pip install --upgrade pip setuptools wheel
```

Install latest stable version for pytorch

```
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
```

Check if cuda enabled

```
python -c "import torch; print(torch.cuda.is_available())"
```

True

_\# if false troubleshoot_

[Pytorch get started page](https://pytorch.org/get-started/locally/)

![](https://lh6.googleusercontent.com/6YITAKuz-Ap3IKQGt_6keytnR62ySZ2H-eSMw5NS7CGb5JYewbqdO_vUEfJP8KaSjliBXx3S8bha71WyYHd-pHu8aphc-CmMoAHoOJcpyp_2b4RVeXzcBYX6wpa2-oifHr-Hkrqcm1S77V75rg)

Install latest monailabel version from Github

```
git clone https://github.com/Project-MONAI/MONAILabel
```

```
pip install -r MONAILabel/requirements.txt
```

Set MONAILabel script paths

```
$Env:PATH += ";C:\Users\yourname\MONAILabel\monailabel\scripts"
```

Download sample apps

```
monailabel apps # List sample apps
monailabel apps --download --name radiology --output apps
```

Download MSD Datasets

```
monailabel datasets # List sample datasets
monailabel datasets --download --name Task06_Lung --output datasets
```

Run Segmentation Model.  
Options can be (deepedit|deepgrow|segmentation|segmentation\_spleen|all) in case of radiology app.  
You can also pass comma separate models like --conf models deepedit,segmentation

```
monailabel start_server --app apps/radiology --studies datasets/Task06_Lung/imagesTr --conf models segmentation
```

Once you start the MONAI Label Server, by default it will be up and serving at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Open the serving URL in browser. It will provide you the list of Rest APIs available.
