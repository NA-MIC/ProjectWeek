Back to [Projects List](../../README.md#ProjectsList)

# Cinematic rendering in Slicer leveraging VTK Physically Based Rendering (PBR)

## Key Investigators

- Shreeraj Jadhav, Kitware, USA
- Jiayi Xu, Kitware, USA
- Jean-Christophe Fillion-Robin Kitware, USA
- Andras Lasso (PerkLab, Queen's University, Canada)

# Project Description

<!-- Add a short paragraph describing the project. -->
- The goal of this project is to identify and evaluate Kitware's previous efforts on cinematic rendering and how these can be leveraged in Slicer.
- Slicer internally uses VTK as its rendering engine to display the 2D and 3D viewports in its interface. Since release 9.0, VTK has more enhanced rendering capabilities such as the Physically Based Rendering (PBR) lighting model and the integration of ray tracing backends such as the Nvidia OptiX and intel's OSPRay engine. These capabilities are already being leveraged in Paraview as discussed in the following blog posts [here](https://www.kitware.com/vtk-pbr/) and [here](https://www.kitware.com/physically-based-rendering-improvements-in-paraview/).

- Primary focus will be on VTK's PBR capabilities and ray tracing backends (OptiX, OSPRay). Since Slicer already uses VTK rendering pipeline, and it will be significantly easier to incorporate/leverage these capabilities from within Slicer.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Review accessible offerings on cinematic rendering (VTK PBR, VTK backends: OSPRay and OptiX, omniverse, etc) that can be utilized inside Slicer.
2. Develop prototypes showing how these can be enabled and used in Slicer.
   - Start with surface rendering (PBR, ambient occlusion, global ilumination)
   - Investigate what capabilities can be enabled for volume rendering (perhaps OSPRay).
   - Tradeoffs: Performance vs Image Quality without degrading user experience.
   - Changes to user interface, parameters tuning, simplification.
3. Review existing Slicer modules (such as [Light Module](https://discourse.slicer.org/t/new-module-to-customize-lighting-in-3d-view/8804)) that enhance Slicer's rendering capabilities and evaluate how these can be included in the current effort.
4. Evaluate how integrating these in Slicer will affect other modules such as LookingGlass, OpenXR, etc.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->
Use of `vtkSSAOPass` class to generate ambient occlusion (AO) for volumes:
 - Volume mapper cannot directly work when AO pass is enabled, need further investigations to understand how this could be done.
 - Initial attempt encountered OpenGL State errors (see error dump below) trigger by [this](https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/OpenGL2/vtkOpenGLState.cxx#L1755).
 ```
 Generic Warning: In C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkOpenGLState.cxx, line 1069
Error glEnable/Disable1 OpenGL errors detected
  0 : (1282) Invalid operation

 with stack trace of
 at vtksys::SystemInformationImplementation::GetProgramStack in C:\D\slicer-d1\VTK\Utilities\KWSys\vtksys\SystemInformation.cxx line 3979
 at vtksys::SystemInformation::GetProgramStack in C:\D\slicer-d1\VTK\Utilities\KWSys\vtksys\SystemInformation.cxx line 829
 at `anonymous namespace'::reportOpenGLErrors in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkOpenGLState.cxx line 294
 at vtkOpenGLState::SetEnumState in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkOpenGLState.cxx line 1069
 at vtkOpenGLState::ScopedglEnableDisable::~ScopedglEnableDisable in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkOpenGLState.h line 299
 at vtkOpenGLState::vtkglBlitFramebuffer in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkOpenGLState.cxx line 1758
 at vtkOpenGLGPUVolumeRayCastMapper::vtkInternal::CaptureDepthTexture in C:\D\slicer-d1\VTK\Rendering\VolumeOpenGL2\vtkOpenGLGPUVolumeRayCastMapper.cxx line 817
 at vtkOpenGLGPUVolumeRayCastMapper::GPURender in C:\D\slicer-d1\VTK\Rendering\VolumeOpenGL2\vtkOpenGLGPUVolumeRayCastMapper.cxx line 3102
 at vtkGPUVolumeRayCastMapper::Render in C:\D\slicer-d1\VTK\Rendering\Volume\vtkGPUVolumeRayCastMapper.cxx line 171
 at vtkVolume::RenderVolumetricGeometry in C:\D\slicer-d1\VTK\Rendering\Core\vtkVolume.cxx line 380
 at vtkProp::RenderFilteredVolumetricGeometry in C:\D\slicer-d1\VTK\Rendering\Core\vtkProp.cxx line 324
 at vtkDefaultPass::RenderFilteredVolumetricGeometry in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkDefaultPass.cxx line 167
 at vtkVolumetricPass::Render in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkVolumetricPass.cxx line 44
 at vtkSequencePass::Render in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkSequencePass.cxx line 71
 at vtkCameraPass::Render in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkCameraPass.cxx line 145
 at vtkRenderStepsPass::Render in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkRenderStepsPass.cxx line 207
 at vtkSSAOPass::RenderDelegate in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkSSAOPass.cxx line 240
 at vtkSSAOPass::Render in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkSSAOPass.cxx line 499
 at vtkOpenGLRenderer::DeviceRender in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkOpenGLRenderer.cxx line 285
 at vtkRenderer::Render in C:\D\slicer-d1\VTK\Rendering\Core\vtkRenderer.cxx line 385
 at vtkRendererCollection::Render in C:\D\slicer-d1\VTK\Rendering\Core\vtkRendererCollection.cxx line 53
 at vtkRenderWindow::DoStereoRender in C:\D\slicer-d1\VTK\Rendering\Core\vtkRenderWindow.cxx line 347
 at vtkRenderWindow::Render in C:\D\slicer-d1\VTK\Rendering\Core\vtkRenderWindow.cxx line 306
 at vtkOpenGLRenderWindow::Render in C:\D\slicer-d1\VTK\Rendering\OpenGL2\vtkOpenGLRenderWindow.cxx line 2345
 at main in C:\D\Shadows\Shadows.cxx line 132
 ```

Adapt `vtkSSAOPass` to create local ambient occlusion (LAO) implementation for volumes:
 - `ComputeKernel()` in vtkSSAOPass can be modified to adapted for LAO of volumes [Jiayi]
 - Possibly, only compute an occlusion volume once (pre-compute), use this for shading in raycaster

Through discussions with the VTK team (Timothee Chabat, Mathieu Westphal), we identified another feature which could help improve shading in volume rendering:
 - https://gitlab.kitware.com/vtk/vtk/-/merge_requests/9231
 - an accurate ambient occlusion effect can be achieved with the current VTK master, setting the `GlobalIllumationReach` to `0` and setting `VolumetricScatteringBlending` to something `>= 1.0`
![](https://gitlab.kitware.com/vtk/vtk/uploads/397286f8f4fc59281174e51ad639fae7/demo_shadows.gif)
<img width="543" alt="3" src="https://user-images.githubusercontent.com/22624785/176828212-5e468e30-d3d3-4d24-aba3-65ef7927dc3a.png">

<img width="192" alt="4" src="https://user-images.githubusercontent.com/22624785/176828232-9755661b-a46b-4fcf-9050-d6acdbd0f5c7.png">

_Image Courtesy: Gaspard Thevenon_

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

Related modules:
- Models: In recent Slicer versions, PBR interpolation can be selected and PBR material properties can be edited.
- Lights (in [Sandbox extension](https://github.com/PerkLab/SlicerSandbox#lights)): it can configure lighting, PBR, image based lighting, ambient shading (SSAO)

![](https://camo.githubusercontent.com/69b7b0e1828a78bd1e19bacfec1d4ecb22a0070e035284ce75c30be60753cb8c/68747470733a2f2f617773312e646973636f757273652d63646e2e636f6d2f7374616e6461726431372f75706c6f6164732f736c696365722f6f7074696d697a65642f32582f642f643362626532316637636435393339346366396264303065366262353133626136666261333065305f325f31303335783632382e6a706567)

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
Slicer Discourse References:
1. [https://discourse.slicer.org/t/how-to-perform-3d-cinematic-rendering/7313](https://discourse.slicer.org/t/how-to-perform-3d-cinematic-rendering/7313)
1. [https://discourse.slicer.org/t/is-there-interest-in-higher-quality-rendering-for-slicer/6862/5](https://discourse.slicer.org/t/is-there-interest-in-higher-quality-rendering-for-slicer/6862/5)
1. [https://discourse.slicer.org/t/2021-01-19-hangout/15585/2](https://discourse.slicer.org/t/2021-01-19-hangout/15585/2)

VTK References:
1. VTK PBR [https://www.kitware.com/vtk-pbr/](https://www.kitware.com/vtk-pbr/)
1. PBR integration in Paraview [https://www.kitware.com/physically-based-rendering-improvements-in-paraview/](https://www.kitware.com/physically-based-rendering-improvements-in-paraview/) 
1. Related merge request for VTK [https://gitlab.kitware.com/vtk/vtk/-/merge_requests/5584](https://gitlab.kitware.com/vtk/vtk/-/merge_requests/5584)
