Back to [Projects List](../../README.md#ProjectsList)

# SlicerWGPU

## Key Investigators

- Steve Pieper, Isomics, Cambridge MA, USA
- others interested?

# Project Description

Explore the utility of using WebGPU from python in Slicer.

A working prototype already exists here: https://github.com/pieper/SlicerWGPU

## Objective

1. Bounce the idea off people as a sanity check
2. Collect ideas for possible use cases
3. See if anyone wants to try implementing something practical

## Progress and Next Steps

# Illustrations

![image](https://user-images.githubusercontent.com/126077/175835561-de9e3e40-0e58-462a-abc7-ef87e9d1bcee.png)
Figure 1: [Simple compute shader example](https://github.com/pieper/SlicerWGPU/blob/main/Experiments/slicer-compute.py) that inverts the values of a volume.
```
@group(0) @binding(0)
var<storage,read> data1: array<i32>;
@group(0) @binding(1)
var<storage,read_write> data2: array<i32>;
@stage(compute)
@workgroup_size(1)
fn main(@builtin(global_invocation_id) index: vec3<u32>) {
    let i: u32 = index.x * @@SLICE_SIZE@@ + index.y * @@ROW_SIZE@@ + index.z;
    data2[i] = -1 * data1[i];
}
```
Figure 2: Example WGSL compute shader code.

![image](https://user-images.githubusercontent.com/126077/175835635-6df93864-b709-450a-99d3-4ae8b02fdf8d.png)
Figure 3: [Off-screen GPU render example](https://github.com/pieper/SlicerWGPU/blob/main/Experiments/slicer-render.py).

# Background and References
See [the README](https://github.com/pieper/SlicerWGPU) for links and background.
