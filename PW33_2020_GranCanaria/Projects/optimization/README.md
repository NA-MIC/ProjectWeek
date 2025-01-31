Back to [Projects List](../../README.md#ProjectsList)

# Software for finding optimal weigths for extracting Spherical Harmonics components from a spherical distribution.

## Key Investigators
## Hans Knutsson, Carl-Fredrik Westin
Linkoping University, Sweden
Radiology, Brigham and Women’s Hospital, Boston, MA, US
Harvard Medical School, Boston, MA, US

## Corresponding author:
Hans Knutsson (hans.knutsson@liu.se )

# Project Description
The goal of this project is to provide a tool for finding optimal weigths for extracting Spherical Harmonics components from a spherical distribution. The set of coordinades on the sphere can be given as input or chosen from one of a number of precomputed sets.

One good example where this approach is useful is restoring rotation invariance of diffusion MRI estimators in the presence of missing or corrupted measurements

## Objective
<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Introduce a tool for analysis of signal distributions on a sphere to the diffusion MRI community.
2. Provide a tool for visualization of 3D point distributions.

<!-- ## Approach and Plan
Describe here HOW you would like to achieve the objectives stated above. -->

<!-- 1. Discuss / demo the CMB platform
2. Integrate ITK into the CMB plaform
3. Integrate display of oriented image data in VTK
4. Basic thresholding -->

<!--## Progress and Next Steps-->
## Progress  (pw 33)
<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->
1. Made project page nicer.
2. Added link to hansknutsson GitHub.
3. Added explanations of paremeters used.
4. Impoved code comments.
5. Added ISMRM reference.

## Illustrations
<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![Opt_SPH_fig1](https://raw.githubusercontent.com/hansknutsson/HK_library_test/master/Complementary_material/Opt_SPH_fig1.jpg)

This figure shows the result of the weight optimization for the case of 120 uniformly distributed orientations with 12 missing measurements. The rows show results for spherical harmonic (SPH) degrees 0, 2 and 4. Colors indicate filter weight values, blue is most positive and red is most negative. The missing measurement locations are shown in white.

![SPHerrors_120_12missing](https://github.com/hansknutsson/HK_library_test/raw/master/Complementary_material/SPHerrors_120_12missing.png)

The figure shows the estimated error distribution for the case of 120 uniformly distributed orientations with 12 missing measurements. The error is given as a function of the maximum SPH degree of the measured signal and the degree of the measurement filter. The left plot shows the result for a signal with equal energy for all SPH's up to the degree indicated on the x-axis. The right plot shows the result using the much more realistic case where the energy decreases for higher SPH degrees. The dashed lines show the errors using SPH function values as weights. The continuous lines show the result using the optimized weights.

## Background
I developed the upploaded code as tools in my research towards finding optimal sets of waveforms for analysis of microstructural tissue features using diffusion weighted MRI (dMRI). The code can be used for optimization and visualisation of a number of aspects in dMRI.

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

## References
[ISMRM_poster_2019](https://github.com/hansknutsson/HK_library_test/blob/master/Complementary_material/ISMRM_poster_2019.pdf)

## Related resources can be found at [HK_library_test](https://github.com/hansknutsson/HK_library_test)
