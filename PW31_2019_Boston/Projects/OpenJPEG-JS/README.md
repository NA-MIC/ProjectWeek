Back to [Projects List](../../README.md#ProjectsList)

# OpenJPEG-JS cross-compilation

## Key Investigators

- [Forrest Li][floryst] ([Kitware, Inc.][Kitware])
- [Danny Brown][danny] ([Radical Imaging][radical])
- [James A Petts][james] ([Institute for Cancer Research, London][icr-london])
- [Erik Ziegler][erik] ([Radical Imaging][radical])
- [Steve Pieper][steve] ([Isomics][isomics])

## Description

OpenJPEG is used in cornerstoneWADOImageLoader for loading JPEG2000 images. The current version of cross-compiled OpenJPEG in the cornerstone organization is quite out-dated, does not have good documentation, and does not actually build without modifications.

## Objective

Cross-compile OpenJPEG to JavaScript for the browser.

## Approach and Plan

I wasn't planning on doing this, but it somehow happened. I ended up starting the cross-compilation from scratch with the latest OpenJPEG sources.

## Progress and Next Steps

### Before Project Week:

This project didn't exist before this Project Week.

### At Project Week:

OpenJPEG was finally cross-compiled! You can find the repo here: [https://github.com/floryst/openjpeg-js](https://github.com/floryst/openjpeg-js)

#### Next Steps

Actually test the cross-compiled library in OHIF. cornerstoneWADOImageLoader tests pass, so that's a start.

## Illustrations

There aren't any screenshots for cross-compiled code.

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

<!--
    Links
-->

[Kitware]: https://kitware.com/
[radical]: http://radicalimaging.com/
[icr-london]: https://www.icr.ac.uk/
[isomics]: http://isomics.com/

[floryst]: https://github.com/floryst
[danny]: https://github.com/dannyrb
[james]: https://github.com/jamesapetts
[erik]: https://github.com/swederik
[steve]: https://github.com/pieper
