Back to [Projects List](../../README.md#ProjectsList)

# Parameter Node Wrapper

## Key Investigators

- Connor Bowley (Kitware, USA)
- Sam Horvath (Kitware, USA)
- David Allemang (Kitware, USA)

# Project Description

Best practice when writing new ScriptedLoadableModules is to use a "parameter node" to store state (most commonly the state of the GUI). However, the existing parameter node system was in essence a string to string map (which some exceptions regarding storing MRML node references), while many times the state should not logically be a string.

A wrapper system was created, the `parameterNodeWrapper`, to allow better typed access to parameter nodes. This system allows using many Python built-ins by default, and is extensible for custom classes.

Because the `parameterNodeWrapper` uses type annotations, automatic connections can also be made to GUI components.

Example:

```py
import enum
from slicer.parameterNodeWrapper import parameterNodeWrapper

class ConversionMethods(enum.Enum):
    LUMINANCE = 1
    AVERAGE = 2
    SINGLE_COMPONENT = 3


@parameterNodeWrapper
class VectorToScalarVolumeParameterNode:
    InputVolume: slicer.vtkMRMLVectorVolumeNode
    OutputVolume: slicer.vtkMRMLScalarVolumeNode
    ConversionMethod: ConversionMethods
    ComponentToExtract: int


class VectorToScalarVolumeWidget(ScriptedLoadableModuleWidget):
  def setup(self):
    self._parameterNode = VectorToScalarVolumeParameterNode(self.logic.getParameterNode())
    
  def updateParameterNodeFromGUI(self, caller=None, event=None):
    # Modify all properties in a single batch
    with slicer.util.NodeModify(self._parameterNode):
      self._parameterNode.InputVolume = self.ui.inputSelector.currentNode()
      self._parameterNode.OutputVolume = self.ui.outputSelector.currentNode()
      self._parameterNode.ConversionMethod = self.ui.methodSelectorComboBox.currentData
      self._parameterNode.ComponentToExtract = self.ui.componentsSpinBox.value
    
  def onApplyButton(self):
    self.logic.run(self._parameterNode.InputVolume,
                   self._parameterNode.OutputVolume,
                   self._parameterNode.ConversionMethod,
                   self._parameterNode.ComponentToExtract)
```

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Work on automatic GUI creation from a `parameterNodeWrapper`.
2. Create examples/templates/documentation on how to use the `parameterNodeWrapper` functionality.
3. Determine new features.
4. Implement new features as able.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Describe specific steps of **what you plan to do** to achieve the above described objectives.
1. ...
1. ...

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Added ability to use the `typing.Any` annotation in the parameter node wrapper, with some limitations.
2. Added automatic gui generation for the parameterNodeWrapper (PR coming soon).
3. Bug fixes.
4. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- [Parameter node wrapper documentation](https://slicer.readthedocs.io/en/latest/developer_guide/parameter_nodes.html)
