# Setup an AWS EC2 instance to use MONAI label, deep learning tools and 3D Slicer

*   Rudolf Bumm (KSGR)
*   Qing Liu (AWS)
*   Steve Pieper (Isomics)
*   Gang Fu (AWS)

Go to the Amazon Console

[https://aws.amazon.com/de/console/](https://aws.amazon.com/de/console/)

Go to login page

![](https://user-images.githubusercontent.com/18140094/210726738-883715be-d8c0-4432-b78b-ef2ac8a5da35.png)

# Step 1. Deploy the CloudFormation template

Log into AWS console, select the region you’d like to use

![](https://user-images.githubusercontent.com/18140094/210726739-a1f70591-3ceb-49db-b12b-4ea0c819a7f6.png)

In the search bar, type cloudformation, and select CloudFormation service

![](https://user-images.githubusercontent.com/18140094/210726732-c54e062b-3178-4dfc-84a1-c4b38d42a6aa.png)

*   In CloudFormation console, click Create stack

![](https://user-images.githubusercontent.com/18140094/210726731-9c9641a9-1f06-46b0-a59b-ffb2e98103f4.png)

*   Select Upload a template file, and then select the WIndowsServer2019-NICE-DCV.yaml file that is on this Github.
*   Click Next.

![](https://user-images.githubusercontent.com/18140094/210726733-c02aacd7-460a-43da-bb5d-7fb10e2972b7.png)

*   Enter a few parameters for the stack
*   Enter a name for this stack you are deploying, e.g. MONAI-Stack
*   Select the instance type you’d like to use, e.g. g5.xlarge
*   You can enter a name for the EC2 instance, or leave the default value
*   Set the IP address of the machine that you will use to connect to the EC2 instance. To find out your IP address, you can visit [https://checkip.amazonaws.com](https://checkip.amazonaws.com) if your IP address is 1.2.3.4, please enter 1.2.3.4/32 as the parameter

The screen should look similar to this:

![](https://user-images.githubusercontent.com/18140094/210726735-c46427e8-8411-4af7-b4ce-54b433605052.png)

*   Click Next
*   Accept default settings and click Next
*   On the summary page, check I acknowledge that AWS CloudFormation might create IAM resources., and click
*   Submit
*   It should take 15 ~ 20 mins for the stack to get deployed

# Step 2. Connect to the environment

1\. After the stack is deployed successfully, select the stack in CloudFormation console and then select Outputs tab

![](https://user-images.githubusercontent.com/18140094/210726734-8595cd3f-c6ee-4987-bbea-186a38747e2a.png)

*   Set your login password. In the Outputs tab, open the SSMsessionManager link in a new browser tab
*   In the new browser tab (Windows Powershell session), type net user administrator my-strong-password,
*   please change my-strong-password to your own password, and hit Enter
*   Go back to the Outputs tab, open DCVwebConsole link in a new browser tab (accepts the security warning)

![](https://user-images.githubusercontent.com/18140094/210726736-6c4a83b2-2580-4b4f-86e7-b4ead4f46082.png)

*   In the NICE DCV login screen, enter administrator as the Username, and the previously set password as Password
*   You should be able to log into the Windows EC2 instance

# Step 3. Delete the environment

*   When the environment is no longer needed, you can delete all deployed resources.
*   Go to the CloudFormation console, select the deployed stack, and then click Delete

![](https://user-images.githubusercontent.com/18140094/210726737-0adb6986-49cb-4b3e-a67e-85c9decff817.png)
