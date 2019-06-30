Back to [Projects List](../../README.md#ProjectsList)

# Slicer in Google Cloud Platform (GCP) with GPU support

## Key Investigators

- Steve Pieper (Isomics)
- Christian Herz (Children's Hospital of Philadelphia)

# Project Description

<!-- Add a short paragraph describing the project. -->
Running Slicer on Google Cloud Platform with GPU support WITHOUT using dockerized images

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Replicate Slicer running GCP machine with instructions and write them down for the public

**Important notes:**

* The instructions don't account for security concerns so **don't put any data or passwords on the virtual machine** if you need to keep them secret.
* The Google Cloud Platform costs real money once your free trial is over.  **Be sure to shut down anything you aren't using** or your credit card will eventually be charged.
* Be careful with your login information.  If someone takes over your account they **could run up a huge bill that you will be responsible for paying**.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Replicate installation process on machines
2. Write detailed instructions

## Progress and Next Steps

1. Sign up for 300$ free credit on GCP
2. Go to https://console.cloud.google.com/home
3. Select left sidebar "Compute Engine --> VM instances"
4. Create Instance with the configuration as you wish
5. Machine type —> Customize and select GPU 
6. Firewall --> allow HTTP and HTTPS
7. Select “Ubuntu 18.04” boot disk
8. Finish creation of VM
9. (Optional) Create instance templates for repeated creation


### Configure Firewall

1. Select left sidebar "VPC network --> Firewall rules"
2. Select "CREATE FIREWALL RULE"
3. Set Source ip ranges: 0.0.0.0/0
4. Protocols and ports: tcp: 6080


#### (Important) GPU usage prerequisites
1. Go to sidebar —> IAM & admin —> Quotas
2. Select metrics —> None and search for GPU
3. Select GPUs (all regions)
4. Check and click EDIT Quotas
5. Enter your information and click next
6. Set limit to 2
7. Request process might take up to 2 business days, but if you send them an email, they could be faster with it (at least for me it was)

#### Configure machine via SSH

Start VM by clicking on SSH and execute the following

#### Installation of prerequisites

```
sudo apt-get update
sudo apt install ubuntu-drivers-common
sudo ubuntu-drivers autoinstall
sudo apt install xinit
sudo apt-get install x11vnc
sudo apt-get install xterm
sudo xinit
sudo nvidia-xconfig
```

Execute the following and take not of the BusID

```
nvidia-xconfig --query-gpu-info
```


```
sudo vim /etc/X11/xorg.conf
```

Insert the following lines including the BusID you retrieved earlier
```
Section "Device"
   Identifier     "Device0"
   Driver         "nvidia"
   VendorName     "NVIDIA Corporation"
   BusID          "PCI:0:4:0"
EndSection
```


### Start noVNC server

Do this install once
```
sudo apt-get install python
git clone https://github.com/novnc/noVNC
```

Note that once you have done these configs the machine is set up and you can shut it down when you aren't using it.


Each reboot (e.g. after doing 'start' on the google cloud console).  The commands below are set up so you can cut and paste them into the ssh terminal from the google interface, but if you want to debug more easily them you might want to paste each in its own terminal. 
```
sudo xinit -- +extension GLX &
./noVNC/utils/launch.sh --vnc localhost:5900 &
while true; do x11vnc -forever; sleep 1; done
```

### Download and unpack Slicer for linux

Here using a specific revision, but any version should work

```
wget http://slicer.kitware.com/midas3/download/item/435293/Slicer-4.10.2-linux-amd64.tar.gz
tar xvzf Slicer-4.10.2-linux-amd64.tar.gz
```
### Connect VNC

1. Connect to http://{VM_External_IP}:6080/vnc.html

```
cd Slicer-4.10.2-linux-amd64
./Slicer
```

Note: this is a very raw linux machine and you are running as root.  There is also a user account under your name that is automatically created by the google VM boot process.  Pretty much anything from the last few decades of linux development should run the same here as it does on a local workstation.

# TODO
If anyone works on these issues please write them up and let us know:
* Add instructions for setting up TLS / HTTP (e.g. with [letsencrypt.org](https://letsencrypt.org/)
* Add instructions for setting up reverse proxy with OAuth
* Add a window manager and other utilities to the X environment, (e.g. with [OpenBox](http://openbox.org), as is [done here](https://github.com/pieper/SlicerDockers/tree/master/x11))
  * running `sudo apt-get install openbox && openbox-session` in the terminal window is one way to start.  A lot of things won't work out of the box but you can configure the files in `/opt/xdg/openbox`.  Also you can access the NVidia X server settings to change the screen resolution.
* Describe other VNC options
* Come up with similar instructions for AWS and Azure (and other computer rental providers).


## Troubleshooting

If you have trouble with the x11 server disconnecting when openning menus or resizing files, you are probably hitting [this bug](https://github.com/LibVNC/x11vnc/issues/61) which is not yet fixed in ubuntu.

You can replace with a patched version like this (as root):
```
curl "https://drive.google.com/uc?id=1FCTxYPAPf58AqchST0SLYfZFZoVANCfL&export=download" -o x11vnc -L
cp x11vnc /usr/bin/x11vnc
```
