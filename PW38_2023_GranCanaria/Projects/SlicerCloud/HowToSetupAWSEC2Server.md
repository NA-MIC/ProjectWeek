https://aws.amazon.com/de/console/

Go to login page


Setup an EC2 instance to use MONAI label and Slicer

Step 1. Deploy the CloudFormation template

Log into AWS console, select the region you’d like to use




In the search bar, type cloudformation, and select CloudFormation service




In CloudFormation console, click Create stack




Select Upload a template file, and then select the WIndowsServer2019-NICE-DCV.yaml file that is on your computer.
Click Next.





	• Enter a few parameters for the stack
	• Enter a name for this stack you are deploying, e.g. MONAI-Stack
	• Select instance type you’d like to use, e.g. g5.xlarge
	• You can enter a name for the EC2 instance, or leave the default value
	• Set the IP address of the machine that you will use to connect to the EC2 instance. To find out your IP address, you can visit https://checkip.amazonaws.com if your IP address is 1.2.3.4, please enter 1.2.3.4/32 as the parameter

The screen should look similar to this:





	• click Next
	• Accept default settings and click Next
	• On the summary page, check I acknowledge that AWS CloudFormation might create IAM resources., and click
	• Submit
	• It should take 15 ~ 20 mins for the stack to get deployed


Step 2. Connect to the environment


1. After the stack is deployed successfully, select the stack in CloudFormation console and then select Outputs tab


	• Set your login password. In the Outputs tab, open the SSMsessionManager link in a new browser tab
	• In the new browser tab (Windows Powershell session), type net user administrator my-strong-password,
	• please change my-strong-password to your own password, and hit Enter
	• Go back to the Outputs tab, open DCVwebConsole link in a new browser tab (accepts the security warning)


	• In NICE DCV login screen, enter administrator as the Username, and the previously set password as Password
	• You should be able to log into the Windows EC2 instance

Step 3. Delete the environment

When the environment is no longer needed, you can delete all deployed resources.
Go to the CloudFormation console, select the deployed stack, and then click Delete



![image](https://user-images.githubusercontent.com/18140094/210726456-d8618174-9bb2-4c21-9617-db6e97725cf7.png)
