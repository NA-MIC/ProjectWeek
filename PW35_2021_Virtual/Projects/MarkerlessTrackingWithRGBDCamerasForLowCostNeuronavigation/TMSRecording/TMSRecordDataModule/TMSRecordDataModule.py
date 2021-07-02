import os
import unittest
import logging
import time
import subprocess
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

#
# RecordHerniaData
#

class TMSRecordDataModule(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Record TMS Data"
    self.parent.categories = ["Training"]
    self.parent.dependencies = []
    self.parent.contributors = ["Rebecca Hisey (Queen's University)"]
    self.parent.helpText = """
This module is used to record RGB and depth video for Inguinal Hernia Repair using 2 Intel Realsense cameras.
"""
    # TODO: replace with organization, grant and thanks
    self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc., Andras Lasso, PerkLab,
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
"""

    # Additional initialization step after application startup is complete
    #slicer.app.connect("startupCompleted()", registerSampleData)

#
# RecordHerniaDataWidget
#

class TMSRecordDataModuleWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """
  '''
  def __init__(self, parent=None):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.__init__(self, parent)
    VTKObservationMixin.__init__(self)  # needed for parameter node observation
    self.logic = RecordHerniaDataLogic()
    self._parameterNode = None
    self._updatingGUIFromParameterNode = False'''

  def setup(self):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.setup(self)

    # Load widget from .ui file (created by Qt Designer).
    # Additional widgets can be instantiated manually and added to self.layout.
    uiWidget = slicer.util.loadUI(self.resourcePath('UI/RecordHerniaData.ui'))
    self.layout.addWidget(uiWidget)
    self.ui = slicer.util.childWidgetVariables(uiWidget)

    # Set scene in MRML widgets. Make sure that in Qt designer the top-level qMRMLWidget's
    # "mrmlSceneChanged(vtkMRMLScene*)" signal in is connected to each MRML widget's.
    # "setMRMLScene(vtkMRMLScene*)" slot.
    uiWidget.setMRMLScene(slicer.mrmlScene)

    # Create logic class. Logic implements all computations that should be possible to run
    # in batch mode, without a graphical user interface.
    self.logic = TMSRecordDataModuleLogic()
    self.recordingStarted = False
    self.camerasStarted = False
    self.moduleDir = os.path.dirname(slicer.modules.tmsrecorddatamodule.path)
    self.logic.setupScene()

    # Buttons
    self.ui.StartStopRecordingButton.connect('clicked(bool)', self.onStartStopRecordingClicked)
    self.ui.startCamerasButton.connect('clicked(bool)',self.onStartStopCamerasClicked)

  def cleanup(self):
    """
    Called when the application closes and the module widget is destroyed.
    """
    #self.removeObservers()
    pass

  def onStartStopRecordingClicked(self):
    """
    Run processing when user clicks "Apply" button.
    """
    try:

      if not self.recordingStarted:
        self.ui.StartStopRecordingButton.setText("Stop Recording")
        self.logic.StartRecording(self.ui.userIDLineEdit.text)
        self.recordingStarted = True
      else:
        self.logic.StopRecording()
        self.recordingStarted = False
        self.ui.StartStopRecordingButton.setText("Start Recording")

    except ValueError:
      logging.info("Ports must have numeric values")

  def onStartStopCamerasClicked(self):
    if not self.camerasStarted:
      rgbPort = int(self.ui.rGBPortLineEdit.text)
      depthPort = int(self.ui.depthPortLineEdit.text)
      self.logic.setupOpenIGTLinkConnectors(rgbPort,depthPort)
      cmd = str(self.moduleDir+"\Scripts\StartPlusServer.bat")
      print(cmd)
      startupEnv = slicer.util.startupEnvironment()
      p = subprocess.Popen(cmd, env=startupEnv)
      self.ui.startCamerasButton.text = "Stop Cameras"
      self.camerasStarted = True
    else:
      cmd = str(self.moduleDir + "\Scripts\StopPlus.bat")
      startupEnv = slicer.util.startupEnvironment()
      p = subprocess.Popen(cmd, env=startupEnv)
      self.ui.startCamerasButton.text="Start Cameras"
      self.camerasStarted = False



#
# RecordHerniaDataLogic
#

class TMSRecordDataModuleLogic(ScriptedLoadableModuleLogic):
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
    self.rgbport = 18944
    self.depthPort = 18945



  def setupOpenIGTLinkConnectors(self, rgbPort,depthPort):
    try:
      self.rgbConnectorNode = slicer.util.getNode('RGBConnector')
      self.rgbConnectorNode.SetTypeClient('localhost',int(rgbPort))
    except slicer.util.MRMLNodeNotFoundException:
      self.rgbConnectorNode = slicer.vtkMRMLIGTLConnectorNode()
      self.rgbConnectorNode.SetName('RGBConnector')
      slicer.mrmlScene.AddNode(self.rgbConnectorNode)
      self.rgbConnectorNode.SetTypeClient('localhost',int(rgbPort))
      logging.debug('RGB Connector Created')
    self.rgbConnectorNode.Start()

    try:
      self.depthConnectorNode = slicer.util.getNode('DepthConnector')
      self.depthConnectorNode.SetTypeClient('localhost',int(depthPort))
    except slicer.util.MRMLNodeNotFoundException:
      self.depthConnectorNode = slicer.vtkMRMLIGTLConnectorNode()
      self.depthConnectorNode.SetName('DepthConnector')
      slicer.mrmlScene.AddNode(self.depthConnectorNode)
      self.depthConnectorNode.SetTypeClient('localhost',int(depthPort))
      logging.debug('Depth Connector Created')
    self.depthConnectorNode.Start()

  def setupScene(self):
    self.saveScenesDirectory = os.path.join(os.path.dirname(slicer.modules.tmsrecorddatamodule.path), "Resources\SavedScenes")
    self.setupOpenIGTLinkConnectors(18944,18945)


    try:
      self.rgbCamera1 = slicer.util.getNode("ImageRGB")
    except slicer.util.MRMLNodeNotFoundException:
      self.rgbCamera1 = slicer.vtkMRMLStreamingVolumeNode()
      self.rgbCamera1.SetName("ImageRGB_ImageRGB")
      slicer.mrmlScene.AddNode(self.rgbCamera1)
    self.setupVolumeResliceDriver(self.rgbCamera1,"Red")

    try:
      self.depthCamera1 = slicer.util.getNode("ImageDEPTH")
    except slicer.util.MRMLNodeNotFoundException:
      self.depthCamera1 = slicer.vtkMRMLStreamingVolumeNode()
      self.depthCamera1.SetName("ImageDEPTH_ImageDEPT")
      slicer.mrmlScene.AddNode(self.depthCamera1)
    self.setupVolumeResliceDriver(self.depthCamera1, "Yellow")

  def setupVolumeResliceDriver(self,cameraNode,sliceColor):

    layoutManager = slicer.app.layoutManager()
    slice = layoutManager.sliceWidget(sliceColor)
    sliceLogic = slice.sliceLogic()
    sliceLogic.GetSliceCompositeNode().SetBackgroundVolumeID(cameraNode.GetID())

    resliceLogic = slicer.modules.volumereslicedriver.logic()
    if resliceLogic:
      sliceNode = slicer.util.getNode('vtkMRMLSliceNode'+sliceColor)
      sliceNode.SetSliceResolutionMode(slicer.vtkMRMLSliceNode.SliceResolutionMatchVolumes)
      resliceLogic.SetDriverForSlice(cameraNode.GetID(), sliceNode)
      resliceLogic.SetModeForSlice(6, sliceNode)
      resliceLogic.SetFlipForSlice(False, sliceNode)
      # resliceLogic.SetRotationForSlice(180, yellowNode)
      #sliceLogic.FitSliceToAll()

  def StartRecording(self,fileName):
    self.fileName = fileName + "-" + time.strftime("%Y%m%d-%H%M%S")
    self.recordingStartTime = vtk.vtkTimerLog.GetUniversalTime()
    self.herniaSequenceBrowserNode = slicer.vtkMRMLSequenceBrowserNode()
    self.startSequenceBrowserRecording(self.herniaSequenceBrowserNode)

  def StopRecording(self):
    self.stopSequenceBrowserRecording(self.herniaSequenceBrowserNode)
    self.saveRecording()
    #self.removeRecordingFromScene()

  def startSequenceBrowserRecording(self, browserNode):
    if (browserNode is None):
      return

    # Indicate that this node was recorded, not loaded from file
    browserNode.SetName(slicer.mrmlScene.GetUniqueNameByString("Recording"))
    browserNode.SetAttribute("Recorded", "True")
    # Create and populate a sequence browser node if the recording started
    browserNode.SetScene(slicer.mrmlScene)
    slicer.mrmlScene.AddNode(browserNode)
    sequenceBrowserLogic = slicer.modules.sequences.logic()


    modifiedFlag = browserNode.StartModify()
    sequenceBrowserLogic.AddSynchronizedNode(None, self.rgbCamera1, browserNode)
    sequenceBrowserLogic.AddSynchronizedNode(None, self.depthCamera1, browserNode)

    # Stop overwriting and saving changes to all nodes
    browserNode.SetRecording(None, True)
    browserNode.SetOverwriteProxyName(None, False)
    browserNode.SetSaveChanges(None, False)
    browserNode.EndModify(modifiedFlag)

    browserNode.SetRecordingActive(True)

    #self.StartRecordingSeekWidget.setMRMLSequenceBrowserNode(browserNode)
  def stopSequenceBrowserRecording(self, browserNode):
    if (browserNode is None):
      return
    browserNode.SetRecordingActive(False)
    browserNode.SetRecording( None, False )

  def saveRecording(self):
    savedScenesDirectory = self.saveScenesDirectory
   

    recordingCollection = slicer.mrmlScene.GetNodesByClass( "vtkMRMLSequenceBrowserNode" )
    for nodeNumber in range( recordingCollection.GetNumberOfItems() ):
      browserNode = recordingCollection.GetItemAsObject( nodeNumber )
      dataNodeNames = ["ImageRGB_ImageRGB","ImageDEPTH_ImageDEPT"]
      for dataNode in dataNodeNames:
        proxyNode = slicer.util.getNode(dataNode)
        sequenceNode = browserNode.GetSequenceNode(proxyNode)
        if not sequenceNode.GetStorageNode() or not sequenceNode.GetStorageNode().IsA("vtkMRMLStreamingVolumeSequenceStorageNode"):
          sequenceStorageNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLStreamingVolumeSequenceStorageNode")
          sequenceNode.SetAndObserveStorageNodeID(sequenceStorageNode.GetID())
      filename = self.fileName + os.extsep + "sqbr"
      filename = os.path.join( savedScenesDirectory, filename )
      slicer.util.saveNode(browserNode, filename)
      

  def removeRecordingFromScene(self):
    slicer.mrmlScene.Clear()



#
# RecordHerniaDataTest
#

class TMSRecordDataModuleTest(ScriptedLoadableModuleTest):
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