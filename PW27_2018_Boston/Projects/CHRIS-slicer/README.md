Back to [Projects List](../../README.md#ProjectsList)

# Running Slicer Apps in the Cloud in the CHRIS Framework

## Key Investigators

- Rudolph Pienaar (Boston Children's Hospital)
- Jorge Bernal (Boston Children's Hospital)
- Nicolas Rannou (Eunate Technology)
- Anneke Meyer (University of Magdeburg, Germany)

# Project Description

## Objective

1. Introduce the CHRIS platform.
2. Containerize a slicer app
3. Run app in CHRIS framework on the Massachusetts Open Cloud

## Approach and Plan

1. Identify a candidate slicer app to use.
2. Containerize app in CHRIS-compliant structure.
3. Deploy to CHRIS distributed instance running locally.
4. Deploy to CHRIS distributed instance running on the Massachusetts Open Cloud.

## Progress and Next Steps

1. Identified a trained prostate segmenter from Anneke Meyer.
1. Created a CHRIS plugin repository and docker hub build for this app:
* [Plugin repo](https://github.com/FNNDSC/pl-neuproseg)
* [Dockerhub automated build](https://hub.docker.com/r/fnndsc/pl-neuproseg/)
1. Successfully ran the segmenter plugin using CHRIS services distributed across localhost and a manager listening on lab website.

## Command used

```bash
pfurl --verb POST --raw --http ${HOST_IP}:5005/api/v1/cmd \
      --httpResponseBodyParse --jsonwrapper 'payload'     \
      --msg \
'{
      "action": "coordinate",
            "threadAction":     true,
            "meta-store": {
                        "meta":         "meta-compute",
                        "key":          "jid"
            },

            "meta-data": {
                "remote": {
                        "key":          "%meta-store"
                },
                "localSource": {
                        "path":         "/home/rudolphpienaar/src/pl-neuproseg/data/ProstateX-0029"
                },
                "localTarget": {
                        "path":         "/home/rudolphpienaar/tmp/output",
                        "createDir":    true
                },
                "specialHandling": {
                        "op":           "plugin",
                        "cleanup":      true
                },
                "transport": {
                    "mechanism":    "compress",
                    "compress": {
                        "encoding": "none",
                        "archive":  "zip",
                        "unpack":   true,
                        "cleanup":  true
                    }
                },
                "service":              "fnndsc"
            },

            "meta-compute":  {
                "cmd":      "$execshell $selfpath/$selfexec --multistream /share/incoming /share/outgoing",
                "auid":     "rudolphpienaar",
                "jid":      "89",
                "threaded": true,
                "container":   {
                        "target": {
                            "image":            "fnndsc/pl-neuproseg",
                            "cmdParse":         true
                        },
                        "manager": {
                            "image":            "fnndsc/swarm",
                            "app":              "swarm.py",
                            "env":  {
                                "meta-store":   "key",
                                "serviceType":  "docker",
                                "shareDir":     "%shareDir",
                                "serviceName":  "89"
                            }
                        }
                },
                "service":              "fnndsc"
            }
        }
```

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->
<p align='center'>
<img src='https://raw.githubusercontent.com/FNNDSC/pl-neuproseg/master/docs/chris_pl-neuproseg.png'/>
</p>


# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/FNNDSC/pl-neuproseg
- Documentation: https://github.com/FNNDSC/pl-neuproseg/wiki
- Test data: https://github.com/FNNDSC/pl-neuproseg
