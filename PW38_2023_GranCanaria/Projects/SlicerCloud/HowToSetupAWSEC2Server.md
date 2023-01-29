# How-to setup AWS EC2 Windows instances to use MONAILabel, deep learning tools, and 3D Slicer

_by Rudolf Bumm (KSGR), Qing Liu (AWS), Steve Pieper (Isomics), Gang Fu (AWS)_


# Benefits

*   Setup a powerful 3D Slicer instance on AWS Cloud
*   Have different servers for each project
*   Let coworkers remotely log on to that servers
*   Share your 3D Slicer results from that server via the S3 bucket or your own 3dviewer.net instance 
*   Up- or downscale your machine according to the required GPU power
*   Access your EC2 machine with low-cost hardware, even tablets
*   Switch off (pause), and finally, delete the instance if you do not need it and only pay for what you use

# Things to consider

We will be running a Windows EC2 instance. 

Small EC2 Windows instances without GPU support can be created and run nearly free of charge on AWS. You could use an instance type "t2.small". 

At least EC2 "g" instance types (with GPU support) will be needed to work with 3D Slicer and deep learning tools. All our testing has been on a "g5.xlarge". 

For more information about GPU options see the [Amazon Deep Learning GPU Guide](https://docs.aws.amazon.com/dlami/latest/devguide/gpu.html).

*Important note:* You may be running into "limit"  errors when you create and run your EC2 instance with GPU, because your Amazon account may need to get enabled for using a GPU first. The first step to increase your GPU instance quota is to request an instance using the steps below, and then if it's denied follow the instructuctions to request a quota increase.  If you have an institutional email account (company or university) it may be easier to get a quota increase compared to a generic gmail or yahoo type of email account.

The approximate cost of an EC2 instance with NVIDIA A10G support is around 1-2 $ per hour. 

# Step 1. Deploy the CloudFormation template

The CloudFormation template will automatically perform the following tasks when you create the EC2 instance:

*   Install the latest NVIDIA drivers
*   Install git
*   Install MONAILabel
*   Install TotalSegmentator
*   Install lungmask
*   Download the 3D Slicer stable installer
*   Install Firefox
*   Install and connect an S3 bucket

Go to the Amazon Console

[https://aws.amazon.com/de/console/](https://aws.amazon.com/de/console/)

and go to login page

|![](https://user-images.githubusercontent.com/18140094/210726738-883715be-d8c0-4432-b78b-ef2ac8a5da35.png)|
|-|


Log into the AWS console, select the region you’d like to use

|![](https://user-images.githubusercontent.com/18140094/210726739-a1f70591-3ceb-49db-b12b-4ea0c819a7f6.png)|
|-|

In the search bar, type cloudformation, and select CloudFormation service

|![](https://user-images.githubusercontent.com/18140094/210726732-c54e062b-3178-4dfc-84a1-c4b38d42a6aa.png)|
|-|

*   In the CloudFormation console, click Create stack

|![](https://user-images.githubusercontent.com/18140094/210726731-9c9641a9-1f06-46b0-a59b-ffb2e98103f4.png)|
|-|

*   Download the [WIndowsServer2019-NICE-DCV.yaml file](./WindowsServer2019-NICE-DCV.yaml).
*   "Upload it as a template file". 
*   Click Next.

|![](https://user-images.githubusercontent.com/18140094/210726733-c02aacd7-460a-43da-bb5d-7fb10e2972b7.png)|
|-|

*   Enter a few parameters for the stack
*   Enter a name for this stack you are deploying, e.g. MONAI-Stack
*   Select the instance type you’d like to use, e.g. g5.xlarge
*   You can enter a name for the EC2 instance, or leave the default value
*   Set the IP address of the machine that you will use to connect to the EC2 instance. To find out your IP address, you can visit [https://checkip.amazonaws.com](https://checkip.amazonaws.com) if your IP address is 1.2.3.4, please enter 1.2.3.4/32 as the parameter.  *Note:* This is a security measure so that the machine can only be reached from the IP address of the client machine you are currently using.  Standard AWS networking tools can be used to add other IP addresses for access after the instance is created.

The screen should look similar to this:

|![](https://user-images.githubusercontent.com/18140094/210726735-c46427e8-8411-4af7-b4ce-54b433605052.png)|
|-|

*   Click Next
*   Accept default settings and click Next
*   On the summary page, check I acknowledge that AWS CloudFormation might create IAM resources., and click
*   Submit
*   Status: "CREATE\_IN\_PROGRESS". It should take 15 ~ 20 mins for the stack to get deployed

|![](https://user-images.githubusercontent.com/18140094/210744034-a4f668f6-d286-4ac3-953a-b12bec5fc022.png)|
|-|

# Step 2. Connect to the environment

1\. After the stack is deployed successfully, select the stack in CloudFormation console and then select Outputs tab

|![](https://user-images.githubusercontent.com/18140094/210726734-8595cd3f-c6ee-4987-bbea-186a38747e2a.png)|
|-|

*   Set your login password. In the Outputs tab, open the SSMsessionManager link in a new browser tab
*   In the new browser tab (Windows Powershell session), type net user administrator my-strong-password,
*   please change my-strong-password to your own password, and hit Enter
*   Go back to the Outputs tab, open DCVwebConsole link in a new browser tab (accepts the security warning)

|![](https://user-images.githubusercontent.com/18140094/210726736-6c4a83b2-2580-4b4f-86e7-b4ead4f46082.png)|
|-|

*   In the NICE DCV login screen, enter administrator as the Username, and the previously set password as Password
*   You should be able to log into the Windows EC2 instance

|![](https://user-images.githubusercontent.com/18140094/210756064-f6ff0e14-b325-48c5-b4b7-a55cd33e6281.png)|
|-|

speedtest.net on g5.xlarge:

|![](https://user-images.githubusercontent.com/18140094/210758504-4605146a-a51d-4aa6-8a73-acc33079eb58.png)|
|-|

Steam EZbench on g5.xlarge:

|![](https://user-images.githubusercontent.com/18140094/210760154-e3b3dec3-fe44-42b9-8960-a7b753221e19.png)|
|-|

# Step 3. Delete the environment

*   When the environment is no longer needed, you can delete all deployed resources.
*   Go to the CloudFormation console, select the deployed stack, and then click Delete

|![](https://user-images.githubusercontent.com/18140094/210726737-0adb6986-49cb-4b3e-a67e-85c9decff817.png)|
|-|
