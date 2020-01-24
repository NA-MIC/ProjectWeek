Back to [Projects List](../../README.md#ProjectsList)

# Sarcopenia Quantification in Abdominal MR Images

## Key Investigators

- Hans Meine
- Mike Halle
- Ron Kikinis

# Project Description

In the context of our end-stage liver disease collaboration, we always planned to assess sarcopenia by measuring the [erector spinae](https://taviewer.openanatomy.org/?id=A04.3.02.002) at a certain height.

## Objective

* Performing some first actual experiments on this, for example
  * Segmenting the muscles with a CNN
  * Detecting the right height for the measurement (again, using some kind of CNN)

(Since this is just one of many projects, we don't expect to get everything done this week.)

## Approach and Plan

* For determining the height, maybe
  * use a bodypart regressor (SSBR), which Hans had success with on some other tasks, or
  * use a classification network trained to select a slice.

## Progress and Next Steps

1. Set up an annotation tool (SATORI) on the MEVIS cluster
2. Looked at the data together, determined suitability of CE 3D VIBE sequence for this
3. Annotated left & right erectors on a few cases (two cases with many slices, and one slice on a dozen more cases)
4. Verified annotations with Ron
5. Set up a training for that segmentation task, using the above sparse annotations
6. Set up inference, apply the model to some data

The slice selection task was not tackled yet at all.

# Illustrations

TODO

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
