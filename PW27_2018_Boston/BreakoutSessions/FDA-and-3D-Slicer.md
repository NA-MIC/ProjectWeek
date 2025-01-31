Back to [Breakout Sessions List](../README.md#BreakoutSessions)

# FDA and 3D Slicer

## Agenda

* Slicer License
* 510(k)
* Documentation Requirements
* Shared Experiences


## Presenter

- Nicole Aucoin (Harmonus Inc.)

## FDA and 3D Slicer

### Slicer License

The Slicer license allows commerial use:

> The license does not impose restrictions on the use of the software.
> 3D Slicer is NOT FDA approved. It is the users responsibility to ensure compliance with applicable rules and regulations.

Open source software can be included in the package being registered, it's helpful to isolate modules/classes that are used. Testing has to incorporate verifying the functionality of that software.

### 510(k)

> Each person who wants to market in the U.S., a Class I, II, and III device intended for human use, for which a Premarket Approval application (PMA) is not required, must submit a 510(k) to FDA unless the device is exempt from 510(k) requirements of the Federal Food, Drug, and Cosmetic Act (the FD&C Act) and does not exceed the limitations of exemptions in .9 of the device classification regulation chapters


The FDA provides Guidance documents online. These are guidelines to help you prepare your application. A regulatory consultant is very helpful in preparing your application.

#### Predicate Devices

> A 510(k) requires demonstration of substantial equivalence to another legally U.S. marketed device. Substantial equivalence means that the new device is at least as safe and effective as the predicate.


### Documentation Requirements

A quality system needs to be in place that includes a software standard operating procedure document. It will detail your software release procedures that will have to be followed to release a version for the application.

In the Software section of the 510(k) application you have to provide:
* Risk Analysis
* Requirements Specification: developed from Clinical User Needs and Design Input
* Software Design Document
  * Includes module level descriptions for the software
  * Includes third party libraries:

| Name    | Description | How Used in the Software |
| ------- | ----------- | ------------------------ |
| 3D Slicer 4.6.2 | url, description from web page | ... uses the visualization and data structure of 3D Slicer. ... uses the following modules from 3D Slicer: DICOM database, 2D and 3D image data structures, loading, and visualization modules( list). It also contains the VTK, ITK and Slicer Execution Model libraries that are used. |
| CTK # | |
| Qt # | |
| etc | |

* Verification and Validation: user level testing
* Unit Testing: module level testing

Bench testing has to be provided to prove substantial equivalence to a predicate device.

### Shared Experiences

* Writing good requirements leads to writing good tests.
* Slicer's self tests are very helpful to incorporate as unit tests.
* Collect testing data sets.
* Keep your release requirements as simple as possible.

## Background and References

- [Community discussion](https://discourse.slicer.org/t/clinical-use-of-slicer-extensions/1630)
- [Slicer License](https://www.slicer.org/wiki/CommercialUse)
- [510(k)](https://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/PremarketSubmissions/PremarketNotification510k/)
