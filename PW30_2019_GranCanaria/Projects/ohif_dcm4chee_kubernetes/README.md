Back to [Projects List](../../README.md#ProjectsList)

# Simple deployment of OHIF DICOM Viewer and Dcm4chee within Kubernetes

## Key Investigators

- Jonas Scherer (DKFZ)
- Andrey Fedorov (BWH)
- Erik Ziegler (Radical Imaging) 

# Project Description

The aim of this project is to provide a simple environment in which a PACS (Dcm4chee) and the OHIF Dicom Viewer interact with each other. The whole system should be build of Docker containers inside an Kubernetes cluster.


## Objective

1. Working Kubernetes deployment files for all components.
2. OHIF <-> PACS communication: Show dicoms from the pacs in OHIF
3. User authentication
5. A package for easy installation

## Approach and Plan

1. Setup Minikube with infrastructure components (Calico,Traefik...) 
2. Deploy OHIF and DCM4CHEe
3. Add authentication with Keycloak and Security Proxy
4. Create Helm chart for easy installation
5. Testing

## Progress and Next Steps

1. Andrey attempted to reproduce the minikube based setup from Erik, unsuccessfully:

I've been working on this on and off, but so far with limited
success. It seems like the minikube thing is not quite stable. The
first time I went through the steps, I was able to get all the way to
the step to start "minikube dashboard", and indeed could see "pods
going live" slowly, but at some point dashboard stopped responding,
and attempts to restart it didn't work (nothing happening when trying
"minikube dashboard" from the console).

Then I tried to restart minikube, and got error:

```shell
Machine exists, restarting cluster components...
E0111 17:27:45.646056    4826 start.go:349] Error restarting cluster:
restarting kube-proxy: updating configmap: Put
https://192.168.99.100:8443/api/v1/namespaces/kube-system/configmaps/kube-proxy:
http2: server sent GOAWAY and closed the connection; LastStreamID=5,
ErrCode=NO_ERROR, debug=""; some request body already written
================================================================================
An error has occurred. Would you like to opt in to sending anonymized crash
information to minikube to help prevent future errors?
To opt out of these messages, run the command:
minikube config set WantReportErrorPrompt false
================================================================================
```

I then tried to restart it the next day, and restart worked, but when
I did "kubectl apply", I got a bunch of those below:

```shell
$ kubectl apply -f ./
service "crowds-cure-cancer-service" unchanged
deployment.apps "crowds-cure-cancer" unchanged
service "dcm4chee-service" unchanged
deployment.apps "dcm4chee" unchanged
deployment.extensions "default-http-backend" created
service "default-http-backend" created
service "elasticsearch-service" unchanged
deployment.apps "elasticsearch" unchanged
namespace "ingress-nginx" configured
service "ingress-nginx" unchanged
service "keycloak-proxy-kibana-service" unchanged
Error from server (Timeout): error when retrieving current configuration of:
&{0xc420193080 0xc4202d5340 default keycloak-proxy-kibana
keycloak-proxy-kibana.yaml 0xc4200983c0  false}
from server for: "keycloak-proxy-kibana.yaml": the server was unable
to return a response in the time allotted, but may still be processing
the request (get deployments.apps keycloak-proxy-kibana)
Error from server (Timeout): error when retrieving current configuration of:
&{0xc420090840 0xc420354fc0 default keycloak-service keycloak.yaml
0xc420bb0668  false}
from server for: "keycloak.yaml": the server was unable to return a
response in the time allotted, but may still be processing the request
(get services keycloak-service)
error when retrieving current configuration of:
&{0xc420090300 0xc420415dc0 default keycloak keycloak.yaml 0xc420bb0038  false}
from server for: "keycloak.yaml": Get
https://192.168.99.100:8443/apis/apps/v1beta1/namespaces/default/deployments/keycloak:
dial tcp 192.168.99.100:8443: getsockopt: connection refused
```

and again "minikube dashboard" has no effect. Does this mean minikube died?

Am I missing something basic in the setup or steps, or is minikube an
experimental thing that is not really intended to run on a mac? What
platform did you use to test those steps? I am on macOS 10.14.2.


### Status of the project

- Basic infrastructure running
- Keycloak running
- Basic user authentication running
- We changed plans to change the "old" OHIF viewer to the newer react-based implementation
- Work in progress to dockerize the viewer and get it runnung with a url- prefix

### Project repo and information

You can find the project deployment in a **[GitHub Repo](https://github.com/jonasscherer/namic_project_week_30)**

### Basic steps of installation:

1) Get **Minikube** and all dependencies running: <https://kubernetes.io/docs/setup/minikube/>

2) Go in the repository
```cd /deployment```
```kubectl apply -f ./* ```

3) Watch  ```kubectl get pods --all-namespaces``` 
-> all pods should be in the "running" state.
This could take some time - don't worry if something is crashing - it will be restarted automatically..

4) Go to <https://192.168.99.100:30443/>
You should see the the login-page. 
The default credentials are:
- For the normal login:
username: **namic**
password: **namic**

- For the keycloak admin login:
username: **admin**
password: **admin**

You can change all passwords with the Keycloak management:
<https://192.168.99.100:30033/auth>

### How to use?

The components have the the following urls:
1) OHIF: <https://192.168.99.100:30443/> (root)
2) DCM4CHe <https://192.168.99.100:30443/dcm4chee-arc/ui2>
3) Keycloak: <https://192.168.99.100:30033/auth>
4) Dicom receiver port is ```192.168.99.100:31112```
5) All data is stored inside the minikube vm (**/data_deployment**)

To push an example image to DCM4CHE with the **dcm4che-tools docker container**:
```sudo docker run --rm --network=host dcm4che/dcm4che-tools:5.15.1 storescu -cDCM4CHEE@192.168.99.100:31112 /opt/dcm4che/etc/testdata/dicom ```


### Further steps
- The HELM deployment is still missing - we will add this later
- Right now, this will just work in Minikube (IPs, ports etc. are hard-coded)
- Minikube is pretty slow
 We should make this compatible with any Kubernetes setup
- OHIF viewer will be updated 
- Instructions how to add a tls certificate



# Background and References

Info websites:

[OHIF Dicom Viwer](https://docs.ohif.org/)
[DCM4Chee](https://github.com/dcm4che/dcm4chee-arc-light)
[Keycloak](https://www.keycloak.org/about.html)
[Security Proxy](https://www.keycloak.org/docs/3.3/server_installation/topics/proxy.html)

[Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
[Minikube](https://kubernetes.io/docs/setup/minikube/)
[Helm](https://helm.sh/)
