# Segmentation and annotation storage format

NA-MIC Project Week 2020-12-17, 11am-12pm EST

In this breakout session we try to come up with a consensus on how to best store image segmentation and annotations that is convenient for many workflows and software tools.

## Attendees

1. Andras Lasso (Queen's University)
1. Steve Pieper (Isomics)
1. Matt McCormick (Kitware)
1. Hans Johnson (University of Iowa)
1. Mike Halle (BWH)
1. Alexis Girault (Kitware)
1. Ron Kikinis (BWH)
1. Theodore Aptekarev
1. Mehran Azimbagirad
1. Sam Horvath (Kitware)
1. add your name here

## Current State

### Commonly used formats for image segmentation

- 3D image + colormap file: nrrd/nift and separate file in custom file format for storing segment names and color (3D Slicer, ITK-Snap, ...)
- 3D Slicer seg.nrrd file: standard nrrd with custom fields ([specification](https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.h#L68-L102), [example](https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header))
- DICOM segmentation object
- DICOM SR (see this [white paper by David Clunie](https://docs.google.com/document/d/1bR6m7foTCzofoZKeIRN5YreBrkjgMcBfNA7r9wXEGR4/edit#heading=h.fgs65rsvrdy3))
- Legacy DICOM RT parallel contours, and other weird things (overlay, …)
- Label JSON compatible with or using the [OME-NGFF "image-label" metadata](https://ngff.openmicroscopy.org/latest/#label-md)
  - two files (json sidecar)
  - python, c++, javascript, rust, java
  - [zarr](https://zarr.readthedocs.io/en/stable/), n5 (not-hdf5)
  - relies on “folder” structure (similar to BIDS)
    - when working with local filesystem, this facilitates parallel write
    - easy mapping to web hosting to request partial data components
    - also support for zipping into single file for transport, reading on local filesystems

### Commonly used formats for annotation (markups - points, lines, curves, ...)

- Slicer fcsv: good for problem-specific export, not well suited as archival format
- Slicer markups json (https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.0.json)
- DICOM SR: limited and complicated, but standard
- AIM: did not really take off, a new json format is being created
- MetaIO:
  - frame of references were nicely defined
  - [Confusions between coordinate system and transform](https://discourse.slicer.org/t/bug-when-reading-mha-file-with-anatomicalorientation/7038)

## Requirements

- Scope:
  - Use shared data model, can be used in different file format
  - Interchange format (not high-performance)
- Easy reading/writing in Python, C++, JavaScript
- Compatibility with 3D Slicer, ITK, DICOM, ...
- Web friendly (JSON)
- a python module for Slicer I/O
- non iteratively running segment editor: It makes sense to use the module interactively for workflow/parameter exploration, but once a methodology to process a certain dataset is clear, I would love to be able to run through command line in batch. Right now I use the segment editor interactively and then move to Jupyter and/or C++ CLIs that use analogous functionality, but that I can batch-ify. It's really annoying.
- separate style, semantic, representation
- Allow specifying hierarchies
- provenance (optional reference to source images, operator, date/time)
- Frame of reference UID
- Compression
- Tiling

## Suggested solutions

- NRRD with single json object in a custom field
- Label JSON compatible with or using the [OME-NGFF "image-label" metadata](https://ngff.openmicroscopy.org/latest/#label-md)
- NRRD replacement modeled after glTF
- Use glTF and create a standard extension, see [TRAKO](https://github.com/bostongfx/trako) as an example. Why?
  - NRRD taught us many things, but in 2020 we don’t need ad-hoc parsing. We have JSON.
  - Even if you have a robust parser for NRRD, extra key values need to be parsed manually.
  - NRRD was designed to be w2not just human readable, but human writable. It permits all sorts of duplicate fields and values (signed long long int vs int64_t.  Really?  Keys with optional spaces in them?  Really?  “centers” and “centerings” as synonyms?  Really?).
  - It most likely isn’t UTF-8 compliant, so it can’t be internationalized. That’s important for segmentation labels from other languages.
  - It has corner cases in parsing. For example, if a field value has a space in front of it, it will get eaten.
  - It has extensibility, but it is limited.
  - NRRD is a little tricky to parse efficiently in JavaScript because there’s no guarantee that the image data is aligned to the data type.  For instance, floats might not be on a four byte boundary. This may lead to unnecessary copying of potentially large datasets.
  - Support for only one buffer. glTF has multiple. This isn’t a big deal, but it’s nice to be able to have multiple datasets together.

## Appendix

### Seg.nrrd header example:

<pre>
NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: unsigned char
dimension: 4
space: left-posterior-superior
sizes: 2 256 256 112
space directions: none (0.93750000000000022,0,0) (0,0.93750000000000022,0) (0,0,1.4000000000000001)
kinds: list domain domain domain
encoding: gzip
space origin: (-119.53100000000005,-119.53099999999999,-77.700000000000003)
Segment0_Color:=0.694118 0.478431 0.396078
Segment0_ColorAutoGenerated:=1
Segment0_Extent:=40 210 3 235 0 111
Segment0_ID:=Segment_1
Segment0_LabelValue:=1
Segment0_Layer:=0
Segment0_Name:=Head
Segment0_NameAutoGenerated:=0
Segment0_Tags:=Segmentation.Status:notstarted|TerminologyEntry:Segmentation category and type - 3D Slicer General Anatomy list~SCT^123037004^Anatomical Structure~SCT^69536005^Head~^^~Anatomic codes - DICOM master list~^^~^^|
Segment1_Color:=0.564706 0.933333 0.564706
Segment1_ColorAutoGenerated:=1
Segment1_Extent:=113 148 80 115 64 89
Segment1_ID:=Segment_2
Segment1_LabelValue:=1
Segment1_Layer:=1
Segment1_Name:=Mass
Segment1_NameAutoGenerated:=0
Segment1_Tags:=Segmentation.Status:inprogress|TerminologyEntry:Segmentation category and type - 3D Slicer General Anatomy list~SCT^49755003^Morphologically Altered Structure~SCT^4147007^Mass~^^~Anatomic codes - DICOM master list~^^~^^|
Segmentation_ContainedRepresentationNames:=Binary labelmap|Closed surface|
Segmentation_ConversionParameters:=Collapse labelmaps|1|Merge the labelmaps into as few shared labelmaps as possible 1 = created labelmaps will be shared if possible without overwriting each other.&Compute surface normals|1|Compute surface normals. 1 (default) = surface normals are computed. 0 = surface normals are not computed (slightly faster but produces less smooth surface display).&Crop to reference image geometry|0|Crop the model to the extent of reference geometry. 0 (default) = created labelmap will contain the entire model. 1 = created labelmap extent will be within reference image extent.&Decimation factor|0.0|Desired reduction in the total number of polygons. Range: 0.0 (no decimation) to 1.0 (as much simplification as possible). Value of 0.8 typically reduces data set size by 80% without losing too much details.&Fractional labelmap oversampling factor|1|Determines the oversampling of the reference image geometry. All segments are oversampled with the same value (value of 1 means no oversampling).&Joint smoothing|0|Perform joint smoothing.&Oversampling factor|1|Determines the oversampling of the reference image geometry. If it's a number, then all segments are oversampled with the same value (value of 1 means no oversampling). If it has the value "A", then automatic oversampling is calculated.&Reference image geometry|-0.9375000000000001;0;0;119.53100000000003;0;-0.9375000000000001;0;119.53099999999999;0;0;1.4000000000000001;-77.7;0;0;0;1;0;255;0;255;0;111;|Image geometry description string determining the geometry of the labelmap that is created in course of conversion. Can be copied from a volume, using the button.&Smoothing factor|0.2|Smoothing factor. Range: 0.0 (no smoothing) to 1.0 (strong smoothing).&Threshold fraction|0.5|Determines the threshold that the closed surface is created at as a fractional value between 0 and 1.&
Segmentation_MasterRepresentation:=Binary labelmap
Segmentation_ReferenceImageExtentOffset:=0 0 0
</pre>

### NGFF image-label example:

<pre>
"image-label":
  {
    "version": "0.1",
    "colors": [
      {
        "label-value": 1,
        "rgba": [255, 255, 255, 0]
      },
      {
        "label-value": 4,
        "rgba": [0, 255, 255, 128]
      },
      ...
      ],
    "properties": [
      {
        "label-value": 1,
        "area (pixels)": 1200,
        "class": "foo"

      },
      {
        "label-value": 4,
        "area (pixels)": 1650
      },
      ...
      ]
  },
  "source": {
    "image": "../../"
  }
]
</pre>

Store schema in top-level folder
