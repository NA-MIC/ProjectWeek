Back to [Projects List](../../README.md#ProjectsList)

# SlicerHeartVR Extension Development

## Key Investigators

- [Andras Lasso](http://perk.cs.queensu.ca/users/lasso) (PerkLab, Queen's University)
- [Matthew Jolley](http://www.chop.edu/doctors/jolley-matthew-a) (Children's Hospital of Philadelphia)
- [Steve Pieper](http://www.spl.harvard.edu/pages/People/pieper) (Isomics)
- [Mark Asselin](http://perk.cs.queensu.ca/users/asselin) (PerkLab, Queen's University)

## Project Description
Extending the exiting functionality of SlicerHeart to leverage the emerging capabilities of virtual reality.

## Objective

1. Build Slicer and necessary extensions (SlicerIGT, SlicerOpenVR, SlicerHeart) to do an initial demonstration of SlicerHeartVR.
2. Try loading 4D ultrasound frames into video memory to improve frame rate of volume rendering playback.

## Progress

- Slicer build succeeded with VTK9 and Qt 5.10.0 - all necessary extensions were updated to build with these settings.

- Initial demonstration of SlicerHeart functionality in VR (showing a valve, showing a single volume rendered frame with correct colours) was accomplished.

- Steve Pieper successfully improved the frame rate of volume rendering playback prompting the use of a never before heard phrase, "Can we please slow down the volume rendering!"

# Next Steps
- Define the interactions possible in VR to help facilitate the placement of the assorted valve types.
- Continue contributing to SlicerOpenVR to improve Slicer support for VR applications.
