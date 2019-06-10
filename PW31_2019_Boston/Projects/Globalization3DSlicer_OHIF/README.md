Back to [Projects List](../../README.md#ProjectsList)

# Globalization in 3D Slicer and OHIF

## Key Investigators

- José-Carlos Ruiz-Luque (ULPGC - GTMA-IUIBS - MACbioIDi)
- Jean-Christophe Fillion-Robin (Kitware)
- Erik Ziegler (Radical Imaging / Open Health Imaging Foundation)

## Project Description

The software globalization is the translation process of software from a source language into a target language. The process is divided into two steps: software internationalization (i18n) and software localization (L10n). The former is the task of designing software without a specific location i.e. building it independent of any specific language or culture. The latter is the process of adapting a software for a specific location. 

The aim of this project is to develop/improve the 3D Slicer internationalization (i18n) and localization (l10n) support. This project is a next step in the [one](https://github.com/NA-MIC/ProjectWeek/blob/master/PW30_2019_GranCanaria/Projects/UltrasoundSimulatorTraining/README.md) presented during 30th PW NA-MIC.  

Also, we will discuss about the globalization in OHIF.

## Objectives

1. Improving the I18n support in the 3d Slicer core.
1. Supporting the I18n in scripted module.
1. Discussing the number and date formats in the dependence libraries and 3D Slicer core.
1. Defining the step for translation of a module.


## Approach and Plan

1. Enhancing the contexts for the text displayed in GUI for the translation files (ts).
    1. Removing the *QObject::tr* and *q->tr*
    1. Removing the lupdate warnings: 
        1. *Cannot invoke tr() like this*.
        1. *Class MyClass lacks Q_OBJECT macro*.
1. Designing a WEB page so as to store the language files. 
1. Developing the i18n support for scripted module.

## Progress and Next Steps

## Illustrations


# Background and References
- [3D Slicer I18n support](https://www.slicer.org/wiki/Documentation/Labs/I18N)
- [Enabling I18n support ](https://discourse.slicer.org/t/slicer-internationalization/579)  
- [Globalization source code](https://github.com/mt4sd/Slicer/tree/support_i18n_l10n)
- [Forgot tr](https://doc.qt.io/archives/qq/qq03-swedish-chef.html)
- [Qt internationalization](https://doc.qt.io/qt-5/internationalization.html)
