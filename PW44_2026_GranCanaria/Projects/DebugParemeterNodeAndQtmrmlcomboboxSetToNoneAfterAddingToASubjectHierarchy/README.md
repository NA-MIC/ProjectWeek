---
layout: pw44-project

permalink: /:path/

project_title: Subject hierarchy combobox selection bug
category: Infrastructure
presenter_location: 

key_investigators:

- name: Chi Zhang
  affiliation: Texas A&M University College of Dentistry
  country: USA

- name: Csaba Pintér
  affiliation: Ebatinca SL
  country: Spain

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Bug description:
1. Sync a parameter node to a qtMRLComboBox node.
2. Add the parameter node to a subjectHierarchy folder. Both the parameter Node and the qtMRMLComboBox node set to 'None'.

 [Slicer Discourse thread](https://discourse.slicer.org/t/slicer-5-10-qmrmlsubjecthierarchycombobox-turned-to-none-but-no-issue-with-5-8-1/45203/5)



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Fix the bug




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


Here is a sample script that connect a qtMRMLComboBox node to a parameter node, and creating a subjectHierarchy folder to add the parameter node to it. Both will be set to 'None'

```
import slicer, qt

dialog = qt.QDialog(slicer.util.mainWindow())
layout = qt.QVBoxLayout(dialog)

shComboBox = slicer.qMRMLSubjectHierarchyComboBox()
shComboBox.nodeTypes = ["vtkMRMLMarkupsFiducialNode"]
shComboBox.noneEnabled = True
shComboBox.setMRMLScene(slicer.mrmlScene)

layout.addWidget(qt.QLabel("Select a fiducial (SubjectHierarchyComboBox):"))
layout.addWidget(shComboBox)

runButton = qt.QPushButton("Move selected node into folder (triggers reset)")
layout.addWidget(runButton)

shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

def printState(tag):
    print(f"\n[{tag}]")
    print("  shComboBox.currentItem():", shComboBox.currentItem())
    print("  shComboBox.currentNode():", repr(shComboBox.currentNode()))  

# Add the parameter node to a folder
def onRun():
    currentItemID = shComboBox.currentItem()
    if currentItemID == 0:
        print("No selection (currentItemID==0)")
        return

    printState("BEFORE MOVE")

    folderItemID = shNode.CreateFolderItem(shNode.GetSceneItemID(), "SHCombo_TestFolder")
    shNode.SetItemParent(currentItemID, folderItemID)

    printState("AFTER MOVE (post SetItemParent)")

runButton.clicked.connect(onRun)

dialog.show()
```

![](https://github.com/user-attachments/assets/fb1dc7c1-f782-49a3-9688-9da18e58a1c1)

```
[AFTER MOVE (post SetItemParent)]
shComboBox.currentItem(): 0
shComboBox.currentNode(): None
parameter.selectedFiducial: None
```

If qt combobox signal is blocked using `qt.QSignalBlocker`, then parameter node will not be set to 'None'



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. First finding is that the bug is simpler than seemed originally, and the parameter node is not needed, self-contained test script simplified
2. Actual bug confirmed: when an SH item is reparented in the logic that is selected in a view (tree view or combobox), then that selection is cleared. The reason is that when reparenting, the item is first removed then re-inserted under the new parent
3. [PR](https://github.com/Slicer/Slicer/pull/9009) opened about possible solution - behavior turns out to be wrong in a different way
4. Proper reparenting seems to involve wrapping the steps between `beginMoveRows` and `endMoveRows`. This will probably be the correct solution if we can me it work (first attempt is not robust, something is missing)



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_
