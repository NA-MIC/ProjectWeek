---
layout: pw41-project

permalink: /:path/

project_title: Integrate CPU friendly auto segmentation and CT utility models into mhub
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Suraj Pai
  affiliation: Brigham and Women's Hospital
  country: Boston

- name: Leonard Nürnberg
  affiliation: Brigham and Women's Hospital
  country: Boston

- name: Andriy Fedorov
  affiliation: Brigham and Women's Hospital
  country: Boston

- name: Hugo Aerts
  affiliation: Brigham and Women's Hospital
  country: Boston

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project will aim to integrate two categories of models into [mhub.ai](mhub.ai)

**1. CPU friendly (whole-body) auto-segmentation models**

**2. CT utility model for image QA**



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Working example of a CPU-friendly (whole-body) auto-segmentation model through the `mhub.ai` platform
2. Working example of a QA pipeline using CT utility tools through `mhub.ai` platform




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


**CPU-friendly auto-seg**
Several auto-segmentation models have been integrated into slicer recently through [https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults](https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults)

While the quick version of these models run fast on CPU, the slower versions take a couple of mins. It would be interesting to explore if CPU related optimizations would work to increase the speed and reduce memory of the full resolution versions while making the quick versions even faster. 

Some initial thoughts on optimization techniques could include,
1. Converting models to OpenVINO format for optimized inference on CPU ([https://docs.openvino.ai/2024/home.html](https://docs.openvino.ai/2024/home.html), [https://docs.openvino.ai/2024/omz_demos_3d_segmentation_demo_python.html](https://docs.openvino.ai/2024/omz_demos_3d_segmentation_demo_python.html)). This could provide faster inference and make models more lightweight offering a better user experience as well. 

2. For a majority of these auto-seg models, sliding window inferer implementation results in major differences in memory (with higher batch-size) and inference time (with larger overlap ratios). Is there an optimal configuration to save memory and increase speed? 
3. Another ticket item is that the the memory consumption largely increases when predicting more output classes in the softmax, is there a way to efficienlty address this issue as well. Perhaps a more restrictive implementation of the sliding window inferer with a accuracy-efficiency trade-off?
4. Distilling models to smaller ones that run faster (might be something that takes longer than PW): [https://github.com/VaticanCameos99/knowledge-distillation-for-unet](https://github.com/VaticanCameos99/knowledge-distillation-for-unet)


**CT utility models**
Implementing CT image inspection utility models, namely, body part regression - [https://github.com/MIC-DKFZ/BodyPartRegression](https://github.com/MIC-DKFZ/BodyPartRegression). This model allows determining the body part examined and if there are anomalies in certain slices in the processed image (nifti). 


Integrating this into Mhub would allow users to perform this QA by providing DICOM inputs directly




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Tested out an implementation of Pytorch CPU inference (similar to implementation in SlicerMONAIAuto3DSeg) against OpenVINO optimized implementation. 

```python

model = SegResNet(out_channels=1)
model.to("cpu")

# Initialize variables for benchmarking
total_time = 0
num_runs = 500

# Set the model to evaluation mode
model.eval()

with torch.no_grad():
    with autocast(enabled=True):
        for _ in range(num_runs):
            # Generate random input tensor
            torch_input = torch.randn(1, 1, 64, 128, 128)
            
            # Measure inference time
            start_time = time.time()
            model(torch_input)
            end_time = time.time()
            
            # Accumulate total inference time
            total_time += end_time - start_time

        # Calculate average inference time
        avg_time = total_time / num_runs

# Print the average execution time
print(f"Average execution time over {num_runs} runs: {avg_time:.5f} seconds")

```

Result:
`Average execution time over 100 runs: 0.24193 seconds`


```python
# Initialize OpenVINO core and read the model
core = ov.Core()
model = core.read_model("segresnet.xml")
compiled_model = core.compile_model(model, "CPU")

# Create an infer request
infer_request = compiled_model.create_infer_request()

# Number of iterations for benchmarking
num_iterations = 500
execution_times = []

# Generate random input tensor with the correct shape
input_shape = (1, 1, 64, 128, 128)

for i in range(num_iterations):
    # Create tensor from external memory
    torch_input = torch.randn(*input_shape)
    input_tensor = ov.Tensor(array=torch_input.numpy(), shared_memory=True)
    
    # Measure inference time
    start_time = time.time()
    
    # Set input tensor for model with one input
    infer_request.set_input_tensor(input_tensor)
    infer_request.start_async()
    infer_request.wait()
    
    # Get output tensor for model with one output
    output = infer_request.get_output_tensor()
    output_buffer = output.data
    
    end_time = time.time()
    execution_times.append(end_time - start_time)

# Calculate average execution time
avg_execution_time = sum(execution_times) / num_iterations
print(f"Average execution time over {num_iterations} iterations: {avg_execution_time:.5f} seconds")
```

Result:
`Average execution time over 100 iterations: 0.19558 seconds`

There seems to be speed up with OV. More investigation needed for the exact patch-size that AutoSeg3D uses + for sliding window inference setting.

2. Test out accuracy-speed trade-off for different configurations of sliding window inferer on TotalSegmentator test set. 
3. Design an "optimal" sliding window inferer for CPU/GPU. For example, an overlap of 0.625 seems very high and might not impact results as much. 
4. Implement a sandboxed environment for this inference.
5. Implement sandboxed environment for Body Part Regression. 
6. Run and test sandboxed environments on IDC data
7. Package sandboxed environment in Mhub.ai templates



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->



BPREG:

![image](https://github.com/NA-MIC/ProjectWeek/assets/10467804/db57f0d3-6e36-4bb1-85a8-93089f158f68)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. [https://github.com/lassoan/SlicerMONAIAuto3DSeg](https://github.com/lassoan/SlicerMONAIAuto3DSeg)
2. [https://docs.openvino.ai/2024/home.html](https://docs.openvino.ai/2024/home.html)
3. [https://github.com/MIC-DKFZ/BodyPartRegression](https://github.com/MIC-DKFZ/BodyPartRegression)
4. [https://mhub.ai](https://mhub.ai)

