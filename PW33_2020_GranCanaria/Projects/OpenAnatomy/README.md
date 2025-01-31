Back to [Projects List](../../README.md#ProjectsList)

# OpenAnatomy support in 3D Slicer

## Key Investigators

- [Andras Lasso](http://perk.cs.queensu.ca/users/lasso) (Queen's University, Canada)
- Michael Halle (Brigham and Women’s Hospital and Harvard Medical School)
- Steve Pieper (Isomics)
- [Kyle Sunderland](http://perk.cs.queensu.ca/users/sunderland) (Queen's University, Canada)

## Project Description

[OpenAnatomy](https://www.openanatomy.org/) is an initiative to change the anatomy atlas through open data, community-based collaborative development, and free distribution of medical knowledge. In the first phase of the project a few existing atlases were converted into a common format and made publicly accessible via a simple web application. The project is starting its next phase, which aims to design a storage format that is suitable for storing anatomical images, shapes, and descriptive information, and develop tools for viewing, creating, and editing these atlases.

3D Slicer supports importing, visualizing, and annotating medical images and export the resulting data in a variety of formats. Therefore, 3D Slicer could serve as a basis of an OpenAnatomy authoring tool.

OpenAnatomy project needs an authoring tool and 3D Slicer almost fulfills all the needs except specific import/export features and some improvements in data annotation capabilities.

## Objectives

Improve 3D Slicer's existing features to support glTF file format export/import and allow defining hierarchies and standard terminology for segmented structures. Tasks are shared between experienced Slicer core developers and junior software developers, and directed by OpenAnatomy experts.

Data to represent and describe:
* segmentations (binary masks)
* polygonal surface models
* white matter tracts

## Approach and Plan

1. Define what metadata should be saved into exported atlases (hierarchies, terminologies, etc.) and how (json sidecar, ...)
1. Implement storage of metadata in Slicer scene (save subject hiearchy to segmentation node, ...)
1. Implement metadata export: create metadata file, cross-reference exported GLTF objects

## Progress and Next Steps

1. Mapping between standard DICOM terminologies and TA2 (new generation of terminologia antomica)- plan ready: convert TA2 json to dcmqi json, create translation csv table

2. OpenAnatomy export proposed metadata schema:

```json
{
formatVersion: "0.01",
segments:[ {
	annotation: [{
		schema:
		label / code / modifier / modifierCode / whatever ...
	} ] // and if we can have multiple annotations in the future, then this is a list

	style: {
		color:
		opacity:
		visibility:
		other shading parameters ...
		materialUrl: (if model files are obj, point to the material)
	}

	shape {
		geometry {   /// can be a list if you want to provide information about the DICOM set
			type:
			url:
			orientation: LPS / RAS ...
			node: (if glTF, provide the node number of the geometry
		}
		labelMap {
			url:
			labelValue:
		}
	}
	....
]
volumes: [{
	type:
	url:  // or more complicated for DICOM, I guess, maybe a list of URLs

	annotation: {
		label:
	}
	style: {
		window:
		level:
		visibility:
		slicePosition: [r, a, s] // can be null if off
	}
}]

annotation: {
	label: "name of atlas"
	author: // list, do we have this?
	about: // URL, do we have this?
}
style: {   // for the atlas.  We'll add more later for scene views
	camera: {
		position:
		lookAt:
		viewAngle:
	}
}
}
```

## Background and References

+ [Open Antomy Browser](https://www.openanatomy.org/)
+ [Slicer Open Anatomy extension](https://github.com/PerkLab/SlicerOpenAnatomy)
+ https://github.com/KhronosGroup/glTF/tree/master/extensions#extensions-vs-extras
