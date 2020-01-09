Back to [Projects List](../../README.md#ProjectsList)

# Integration of Diabetic Foot Segmentation Algorithm based on Deep Learning

## Key Investigators

- Abián Hernández Guedes(University of Las Palmas de Gran Canaria, Spain)
- Alexandru Dorobanțiu (Lucian Blaga University of Sibiu, Romania)
- José-Carlos Ruiz-Luque (Instituto Astrofísico de Canarias, Spain)
- Natalia Arteaga-Marrero (Instituto Astrofísico de Canarias, Spain)
- Enrique Villa (Instituto Astrofísico de Canarias, Spain)
- Ignacio Sidrach-Cardona Martinez (Instituto Astrofísico de Canarias, Spain)
- Juan Ruiz-Alzola (University of Las Palmas de Gran Canaria, Spain)


# Project Description

This project is the follow-up of the development of a module to use InfraRed (IR) sensors in 3D Slicer for medical diagnosis, intended to use for monitoring of foot ulcers in diabetic patients, presented on the 28thPW NA-MIC. This project is proposed as a new stage in the diabetic foot assessment previously worked.

The aim is to integrate an algorithm, which is based on Deep Learning, for foot segmentation using multimodal images (visible and depth-map images). The resulting mask will be applied on thermal images in order to analyze the temperature pattern and detect possible foot ulcers.

## Objective

1. Update the "Diabetic Foot" extension created on the 28thPW NA-MIC.
1. Integrate the foot segmentation algorithm presented on the paper [1].

## Approach and Plan

1. Integrate TorchScript models, an intermediate representation of a PyTorch model
1. Include a point cloud processing library
1. Implementing the foot segmentation algorithm
1. *(Optional)* Visualization of point cloud using VTK

## Progress and Next Steps
TODO

# Illustrations
![Workflow](images/Workflow.png "Proposed workflow")
Proposed workflow for feet segmentation where the images are represented as squares
and the operations as rectangles.The network prediction is used to set the ROI on the depth
image, the point cloud, and then a second segmentation was applied to extract geometry models,
specifically planes.

# Background and References

[1] Hernández, A., Arteaga-Marrero, N., Villa, E., Fabelo, H., Callicó, G. M., & Ruiz-Alzola, J. (2019, September). Automatic Segmentation Based on Deep Learning Techniques for Diabetic Foot Monitoring Through Multimodal Images. In International Conference on Image Analysis and Processing (pp. 414-424). Springer, Cham. Avalible from: [https://link.springer.com/chapter/10.1007%2F978-3-030-30645-8_38](https://link.springer.com/chapter/10.1007%2F978-3-030-30645-8_38)

