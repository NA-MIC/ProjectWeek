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

<img width="1298" alt="image" src="https://user-images.githubusercontent.com/126077/175835831-a052d131-bdc3-4cb6-90b6-de5c2d0d0659.png">

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

<img width="1293" alt="image" src="https://user-images.githubusercontent.com/126077/175835810-0bb72ccf-91b7-4b0f-87ee-207ea01fff41.png">

Figure 3: [Off-screen GPU render example](https://github.com/pieper/SlicerWGPU/blob/main/Experiments/slicer-render.py).

# Background and References
See [the README](https://github.com/pieper/SlicerWGPU) for links and background.
