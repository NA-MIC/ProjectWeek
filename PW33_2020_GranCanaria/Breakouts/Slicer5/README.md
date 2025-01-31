Back to [Project Week](../../README.md)

# Slicer 5

## Organizers

- Sam Horvath (Kitware Inc.)

## Attendees

- Adam Rankin (Robarts Research Institute)
- Andras Lasso (Queen's University)
- Csaba Pinter (Ebatin S.L)
- Jean-Christophe Fillion-Robin (Kitware Inc.)
- Kyle Sunderland (Queen's University)
- Steve Pieper (Isomics Inc.)
- Sonia Pujol (Brigham and Women’s Hospital and Harvard Medical School)

# Breakout Description

This breakout aims to plan the next major version of Slicer and assigns action items.

## Agenda

<!-- Describe topics and schedule. -->

1. Review roadmap and identify remaining tasks


# Background and References

* https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap


# Results of Discussion

<!-- To be filled out after the event. -->

###  Release planning

Action items (Jc):
* Review list of issues and re-target them to 5.1
* Add missing issues
* Update Slicer [roadmap page](https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap).

### Coordinate System in Files: RAS to LPS

Notes:
* All medical tools uses LPS
* Andras already has a branch: ??

Action items (Andras):
  * Test and integrate changes

Ideas:
* We could probably switch Slicer to internally use LPS. Challenge is to know if we need to switch the normal and displacement field

References:
* https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap#Coordinate_system_in_files
* https://issues.slicer.org/view.php?id=4445

### Legacy Modules

Notes:
* Move all legacy module into a Slicer extension
* There is already a repository https://github.com/Slicer/SlicerLegacyModules

Action items (Jc):
* Add Editor, ResampleScalarVolume, ExpertAutomatedRegistration
* Create corresponding Slicer extension

### GitHub transition

Notes:
* release more often -> release number picked during core team meeting

Action Items (Jc):
* Rename Slicer -> SlicerGitSVNArchive
* Publish updated history as SlicerGit
  * when ready to switch: Rename SlicerGit to Slicer
* Transition scripts
  * Update commit message to change link from https://github.com/Slicer/Slicer/pull/N  to https://github.com/Slicer/SlicerGitSVNArchive/pull/N
  * Add new trailer called: `svn-url: http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&revision=REV`
* Create FAQ document to explain how and why to re-fork, etc ...
* Extract list of all contributors and ask on discourse which emails is preferred
* Mantis:
  * Create redirect from mantisarchive.slicer.org/view.php?id=4681 to https://issues.slicer.org/view.php?id=4681

Post-release Action items:
* Mantis:
  * Create static website with archived mantis issues
  * Ensure mantisarchive.slicer.org/view.php?id=4681 redirects to that website
* SVN:
  * Question: Should we create a static website for http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&revision=28742 or have redirect to the corresponding commit on GitHub

### web: Landing page for slicer.org

Notes:
* we would like consistency between landing page and download page
* design similar to what is done on https://salt.slicer.org/ or https://jupyter.org would be ideal

Action items (Jc):
* Setup an other meeting to evaluate which information we want to highlight

### download.slicer.org

Notes:
* webserver and backend processing need to be on the same machine
* list of packages is generated from a template file -> website is not fully static

Action items (Mike Halle):
* Coordindate with Greg to relocate server from BWH to Digital Ocean
* Sync deployment from https://github.com/Slicer/download.slicer.org/

### Slicer documentation

Notes:
* after Github migration, we will transition to readthedocs and markdown

Action items (Andras, Jc):
* integrate https://github.com/Slicer/Slicer/pull/686

### Slicer Training and Tutorials

Notes:
* readthedocs/markdown/... could contain the training so that it is versionned
* Powerpoint slides have the advantage of allowing easy copy/paste
* two use cases for tutorials
  * at home: website works well. For example, https://lassoan.github.io/SlicerSegmentationRecipes/
  * teaching: slides works well

Ideas:
* every tutorial could have a discourse thread to post comment but on youtube video there is a comment section but there are no comments
* generation of PDF from PPT slides could be automated

Action items:
* create shared Google drive to collect all powerpoints (Jc): **DONE**
  * Shared Drive: While non-kitware member can be added, the team drive can not be publicly visible. See https://support.google.com/a/thread/13540273?hl=en
  * Shared Folder: This can be visible by anyone with the link and non-kitware member can be added. Click [here](https://drive.google.com/drive/folders/1aU77cEqkEBl8764-IL-hdX067YYjZUE1?usp=sharing) to access the folder
* update power point slides into shared folder. Create one folder per Slicer version (e.g 3.6, 4.0, 4.1, ...) (Sonia)


### Default Theme

Notes:
* Dark theme could be the default for Slicer
* This would make the Slicer 5 transition obvious

Action items (Andras, Jc):
* Confirm and update default

### Integrate Sequences module into core

Notes:
* Sequences module is now a very useful module and should be integrated into the code

Questions:
* Should the module be integrated as a [Slicer Remote module](https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_system/Remote_Module) or do we want to cherry pick the complete history ?

Action items (Andras, 2 to 3 weeks):
* Revisit MRML Copy API
* Integrate Sequences

### Extension description file

Notes:
* s4ext -> <extension_name>.slicer.extension.json
* Two steps:
  * (1) Update extension index changing format and extension. For now, keep backend working with s4ext
  * (2) de-duplication of metadata in CMakeLists.txt vs description file. Metadata will be extracted from the json file using CMake function

Action items (Jc, Sam):
* Implement step 1
