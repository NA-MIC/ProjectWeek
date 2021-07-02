import os
import numpy
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

#
# ExportFrameToPoints
#

class ExportFrameToPoints(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Export Frames To Points"  # TODO: make this more human readable by adding spaces
    self.parent.categories = ["RGB-D Tracking"]  # TODO: set categories (folders where the module shows up in the module selector)
    self.parent.dependencies = []  # TODO: add here list of module names that this module requires
    self.parent.contributors = ["Rebecca Hisey (Queen's University)"]  # TODO: replace with "Firstname Lastname (Organization)"
    # TODO: update with short description of the module and a link to online module documentation
    self.parent.helpText = """
This module allows for the conversion of depth images to point clouds
"""
    # TODO: replace with organization, grant and thanks
    self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc., Andras Lasso, PerkLab,
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
"""

#
# ExportFrameToPointsWidget
#

class ExportFrameToPointsWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent=None):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.__init__(self, parent)
    VTKObservationMixin.__init__(self)  # needed for parameter node observation
    self.logic = None
    self._parameterNode = None
    self._updatingGUIFromParameterNode = False

  def setup(self):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.setup(self)

    # Load widget from .ui file (created by Qt Designer).
    # Additional widgets can be instantiated manually and added to self.layout.
    uiWidget = slicer.util.loadUI(self.resourcePath('UI/ExportFrameToPoints.ui'))
    self.layout.addWidget(uiWidget)
    self.ui = slicer.util.childWidgetVariables(uiWidget)

    # Set scene in MRML widgets. Make sure that in Qt designer the top-level qMRMLWidget's
    # "mrmlSceneChanged(vtkMRMLScene*)" signal in is connected to each MRML widget's.
    # "setMRMLScene(vtkMRMLScene*)" slot.
    uiWidget.setMRMLScene(slicer.mrmlScene)

    # Create logic class. Logic implements all computations that should be possible to run
    # in batch mode, without a graphical user interface.
    self.logic = ExportFrameToPointsLogic()

    # Connections

    # These connections ensure that we update parameter node when scene is closed
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.StartCloseEvent, self.onSceneStartClose)
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.EndCloseEvent, self.onSceneEndClose)

    self.ui.depthNodeSelector.setMRMLScene(slicer.mrmlScene)

    # Buttons
    self.ui.thresholdSlider.connect('valueChanged(int)',self.onThresholdModified)
    self.ui.exportToPointsButton.connect('clicked(bool)', self.onApplyButton)

    # Make sure parameter node is initialized (needed for module reload)
    self.initializeParameterNode()

  def cleanup(self):
    """
    Called when the application closes and the module widget is destroyed.
    """
    self.removeObservers()

  def enter(self):
    """
    Called each time the user opens this module.
    """
    # Make sure parameter node exists and observed
    self.initializeParameterNode()

  def exit(self):
    """
    Called each time the user opens a different module.
    """
    # Do not react to parameter node changes (GUI wlil be updated when the user enters into the module)
    self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

  def onSceneStartClose(self, caller, event):
    """
    Called just before the scene is closed.
    """
    # Parameter node will be reset, do not use it anymore
    self.setParameterNode(None)

  def onSceneEndClose(self, caller, event):
    """
    Called just after the scene is closed.
    """
    # If this module is shown while the scene is closed then recreate a new parameter node immediately
    if self.parent.isEntered:
      self.initializeParameterNode()

  def initializeParameterNode(self):
    """
    Ensure parameter node exists and observed.
    """
    # Parameter node stores all user choices in parameter values, node selections, etc.
    # so that when the scene is saved and reloaded, these settings are restored.

    self.setParameterNode(self.logic.getParameterNode())

    # Select default input nodes if nothing is selected yet to save a few clicks for the user
    if not self._parameterNode.GetNodeReference("DepthImageNode"):
      firstVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
      if firstVolumeNode:
        self._parameterNode.SetNodeReferenceID("DepthImageNode", firstVolumeNode.GetID())

  def setParameterNode(self, inputParameterNode):
    """
    Set and observe parameter node.
    Observation is needed because when the parameter node is changed then the GUI must be updated immediately.
    """

    if inputParameterNode:
      self.logic.setDefaultParameters(inputParameterNode)

    # Unobserve previously selected parameter node and add an observer to the newly selected.
    # Changes of parameter node are observed so that whenever parameters are changed by a script or any other module
    # those are reflected immediately in the GUI.
    if self._parameterNode is not None:
      self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
    self._parameterNode = inputParameterNode
    if self._parameterNode is not None:
      self.addObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

    # Initial GUI update
    self.updateGUIFromParameterNode()

  def updateGUIFromParameterNode(self, caller=None, event=None):
    """
    This method is called whenever parameter node is changed.
    The module GUI is updated to show the current state of the parameter node.
    """

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    # Make sure GUI changes do not call updateParameterNodeFromGUI (it could cause infinite loop)
    self._updatingGUIFromParameterNode = True

    # All the GUI updates are done
    self._updatingGUIFromParameterNode = False

  def updateParameterNodeFromGUI(self, caller=None, event=None):
    """
    This method is called when the user makes any change in the GUI.
    The changes are saved into the parameter node (so that they are restored when the scene is saved and loaded).
    """

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    wasModified = self._parameterNode.StartModify()  # Modify all properties in a single batch

    self._parameterNode.EndModify(wasModified)

  def onThresholdModified(self):
    self.logic.setThresholdValue(self.ui.thresholdSlider.value)

  def onApplyButton(self):
    self.logic.exportDepthToPoints(self.ui.depthNodeSelector.currentNode().GetName(),self.ui.thresholdSlider.value)


#
# ExportFrameToPointsLogic
#

class ExportFrameToPointsLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self):
    """
    Called when the logic class is instantiated. Can be used for initializing member variables.
    """
    ScriptedLoadableModuleLogic.__init__(self)
    self.threshold = 25.0

  def setDefaultParameters(self, parameterNode):
    """
    Initialize parameter node with default settings.
    """
    pass

  def setThresholdValue(self,value):
    self.threshold = value

  def exportDepthToPoints(self,depthImageNode,threshold):
    self.threshold = threshold
    try:
      self.depthImageNode = slicer.mrmlScene.GetFirstNodeByName(depthImageNode)
      self.getDepthImageData()
      self.convertDepthToPoints()
    except slicer.util.MRMLNodeNotFoundException:
      logging.info("No depth image node selected")

  def removeColorizing(self):
    imdata = self.getVtkImageDataAsOpenCVMat()
    shape = imdata.shape
    self.depthImage = numpy.array([[self.convertRGBtoD(j) for j in imdata[i]] for i in range(shape[0])])

  def convertRGBtoD(self,pixel1):
    is_disparity = False
    min_depth = 0.16
    max_depth = 300.0
    min_disparity = 1.0 / max_depth
    max_disparity = 1.0 / min_depth
    r_value = float(pixel1[0])
    g_value = float(pixel1[1])
    b_value = float(pixel1[2])
    depthValue = 0
    if (b_value + g_value + r_value) < 255:
      hue_value = 0
    elif (r_value >= g_value and r_value >= b_value):
      if (g_value >= b_value):
        hue_value = g_value - b_value
      else:
        hue_value = (g_value - b_value) + 1529
    elif (g_value >= r_value and g_value >= b_value):
      hue_value = b_value - r_value + 510

    elif (b_value >= g_value and b_value >= r_value):
      hue_value = r_value - g_value + 1020

    if (hue_value > 0):
      if not is_disparity:
        z_value = ((min_depth + (max_depth - min_depth) * hue_value / 1529.0) + 0.5);
        depthValue = z_value
      else:
        disp_value = min_disparity + (max_disparity - min_disparity) * hue_value / 1529.0
        depthValue = ((1.0 / disp_value) / 1000 + 0.5)
    else:
      depthValue = 0
    return depthValue


  def getVtkImageDataAsOpenCVMat(self):
    cameraVolume = self.depthImageNode
    '''if cameraVolume.GetClassName() == "vtkMRMLStreamingVolumeNode":
      image = cameraVolume.GetFrameData()'''

    image = cameraVolume.GetImageData()
    shape = list(cameraVolume.GetImageData().GetDimensions())
    shape.reverse()
    components = image.GetNumberOfScalarComponents()
    if components > 1:
      shape.append(components)
      shape.remove(1)
    imageMat = vtk.util.numpy_support.vtk_to_numpy(image.GetPointData().GetScalars()).reshape(shape)
    return imageMat

  def getDepthImageData(self):
    imdata = self.getVtkImageDataAsOpenCVMat()
    shape = imdata.shape
    if len(shape) > 2:
      self.removeColorizing()
    else:
      self.depthImage = numpy.array([[j for j in imdata[i]] for i in range(shape[0])])


  def convertDepthToPoints(self):
    try:
      self.fiducialNode = slicer.util.getNode("depthFiducials")
      numFiducials = self.fiducialNode.GetNumberOfFiducials()
      for i in range(numFiducials,0,-1):
        self.fiducialNode.RemoveAllMarkups()
    except slicer.util.MRMLNodeNotFoundException:
      self.fiducialNode = slicer.vtkMRMLMarkupsFiducialNode()
      self.fiducialNode.SetName("depthFiducials")
      slicer.mrmlScene.AddNode(self.fiducialNode)
    max_depth = self.depthImage.max()
    imageShape = self.depthImage.shape
    fidAddedCount = 0
    for x in range(0,imageShape[0],10):
      for y in range(0,imageShape[1],10):
        depthValue = self.depthImage[x][y]
        if depthValue >= max_depth*(self.threshold/100.0):
          self.fiducialNode.AddFiducialFromArray(numpy.array([x,y,depthValue]))
          fidAddedCount += 1
    slicer.mrmlScene.Modified()






#
# ExportFrameToPointsTest
#

class ExportFrameToPointsTest(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear()

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
