## MONAI Label installation

_as prepared for the Virtual MONAI Label workshop_  
_June 22nd, 2022_  
_Rudolf Bumm (KSGR)  and Andres Diaz-Pinto (NVIDIA)_

The [Monailabel GitHub page is here.](https://github.com/Project-MONAI/MONAILabel)

To run MONAI Label locally, you should have a computer with a medium/high-end NVIDIA GPU (16-24 GB totally available video RAM)  and CUDA available.   
MONAI Label can also be run on CPU, but the performance will lack.  

GPU compatibility:

[https://developer.nvidia.com/cuda-gpus](https://developer.nvidia.com/cuda-gpus)

## Installation in Windows 11 step by step:

Install Python 3.9 from Windows Store

[Enable long path names in Windows 11](https://thegeekpage.com/make-windows-11-accept-file-paths-over-260-characters/)

Use an elevated Powershell (admin mode)   
change to (cd) user directory (important, start in a directory with full read/write access) 

```
python -m pip install --upgrade pip setuptools wheel
```

Install the latest stable version for PyTorch

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

**Known problems:** 

**Monai model-zoo API request fails**

IF the git api request for a model fails due to an improperly formatted URL

(for example https://api.github.com/repos/Project-MONAI\model-zoo/releases 1)

THEN

Step 1: The model “.zip” file can be downloaded (via web browser, for example) with a properly formatted version of the URL (replace '' with ‘/’) and then expanded into a folder on your PC.

Step 2: Set values for two environment variable the server will use as an override:

$Env:MONAI\_ZOO\_SOURCE = ‘local’  
$Env:MONAI\_ZOO\_REPO = \< folder name >  
  
Step 3: Start monailabel server

## Docker-based step by step installation:

Running MonaiLabel through [docker conterization environment](https://docs.docker.com/get-started/overview/) will simply installation steps considerably. This is particularly true for GPU support, since Docker will require you to install only the NVIDIA GPU driver and you don't have to worry about the CUDA environment setup. However, for docker to function you need to have admin (sudo) priviledges on the computer. Instructions here are primarily tested on a Linux environment, but should be applicable to Windows docker as well.

1.  **Start \[from here and find your OS is supported\]**(https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html). Follow the rest of the instructions in the Nvidia documentation. The basic steps are:

*   Confirming/installing NVIDIA GPU driver
*   Confirming/installing Docker enginer and runtime libraries
*   Installing NVIDIA Docker runtime libraries
*   Testing that NVIDIA docker runtime enviroment is working correctly by running the command `sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi`. If this command doesn't work correctly, you won't be able to run MonaiLabel with GPU support.

Once you confirmed that NVIDIA docker runtime environment is working correctly for nvidia-smi command above, follow the instructions for [MonaiLabel Docker installation](https://github.com/Project-MONAI/MONAILabel#docker).

To test the dockerized MonaiLabel server, open a browser and connect to the http://127.0.0.1:8000. If everything is working correctly, this will provide the list of the REST APIs available. Note that, this assumes the docker engine is running on the same computer where you are using the web browser. If that's not the case, replace the http://127.0.0.1 with the IP address of the docker host.

### Docker specific considerations

Changes in docker environments are ephemeral, meaning if you restart your docker session all the changes you made to it will be lost. This would be true for any training session you might have done, any new segmentations you might have pushed to the MonaiLabel server. Therefore, after following the instructions above and confirming that your MonaiLabel docker session is working correctly, you need to modify the docker command to use persistent storage volumes so that changes can be retained. For example, create a Monai folder on your desktop, via command

```
mkdir $USER/Desktop/Monai
```

then you can modify your docker command such that this folder is mapped inside the Docker environment via -v option:

`sudo docker run -it --rm --gpus all --ipc=host --net=host -v $USER/Desktop/Monai/:/workspace/ projectmonai/monailabel:latest bash`

In this case, contents of $USER/Desktop/Monai will be visible under /workspace folder in docker enviroment. Next, you modify the MonaiLabel server startup scripts to make use of this persistent folder:

```
monailabel start_server --app /workspace/apps/radiology --studies /workspace/datasets/Task06_Lung/imagesTr --conf models segmentation
```
