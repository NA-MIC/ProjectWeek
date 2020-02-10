Back to [Projects List](../../README.md#ProjectsList)

# Secure Interface between KHEOPS and OHIF

## Key Investigators

- [Joël Spaltenstein][spalte] ([OsiriX Foundation][OsiriXFoundation] / [Swiss Institute of Bioinformatics][sib])
- [Nicolas van Dooren][nicolas] ([OsiriX Foundation][OsiriXFoundation] / [University of Geneva][unige])
- [Erik Ziegler][erik] ([Radical Imaging][radical])
- [James A Petts][james] ([Radical Imaging][radical], [Ovela Solutions LTD][OvelaSolutions])

# Project Description

The [KHEOPS](https://www.kheops.online) image sharing platform needs to be able to be able to open the OHIF viewer in a secure
fashion.

Currently KHEOPS launches OHIF by passing a [capability URL](https://www.w3.org/TR/capability-urls/) from which OHIF can
obtain the list of DICOM objects that need to be downloaded. In order to be able to take full advantage of OHIF, and in
particular the newer annotation functionallity being added to OHIF, it would be beneficial if OHIF could be granted read/write
access directly using a DICOMweb interface to the study data.

KHEOPS has a built-in mechanism called [Report Providers](https://github.com/OsiriX-Foundation/KheopsAuthorization/wiki/Report-Providers-API)
that works in a way that is similar to OAuth 2.0 to give an external website read/write access to a DICOM study. We plan on
implementing functionality analogous to the [OIDC Hybrid Flow](https://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth)
to make it possible to securly launch OHIF from KHEOPS using the Report Provider API.

<!-- Add a short paragraph describing the project. -->

## Objective



<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Provide the DICOMweb URL to OHIF on launch along with an Authorization Code.
2. Have OHIF use the KHEOPS token endpoint to exchange the authorization code for an Access Token.
3. Have OHIF use the Access Token for all futher DICOMweb access to the KHEOPS DICOMweb URL.

## Approach and Plan

We will take a two step approach. The frist step will provide the minimal functionality required to give users good experience and an acceptable risks from a security point of view. The desired user experience is to have the user taken to OHIF when a thumbnail of a series is clicked in the KHEOPS UI. OHIF will open the relevant study, and display the clicked-on series. We would then like to make sure that the novel advanced OHIF functionality (3D MIP, annotations) function seamlessly.

1. Implement using the dynamic configuration loading existing in OHIF. This approach has the drawback of forcing OAuth2.0 Access Token be passed in the URL used to lauch OHIF. This security issue is considered acceptable since the Viewer Token capabilities of KHEOPS are used. A Viewer Token is an Access Token which grants the bearer access only to a specific DICOM study and for only a very limited durration. Unfortunaly, this approach does not provide any means of renewing the provided token, which can lead to the Access Token expiring while the user is actively using OHIF. This could be catastrophic for the user if the user invested a significant amount of time marking manual annotations only to discover that the annotations can not be saved because the token has expired.

2. Implement an Authorization Code, and token refreshing token system in OHIF.

We hope to implement the first solution durring project week, and have enough time to divise a good stratagy to develop the second solution at a later date.

## Progress and Next Steps

Step 1 mentioned above was implemented and presented at the end of the week. The extensive use of the dynamic configuration loading functionality present in OHIF revieled a number of OHIF bugs. The presence of OHIF developers allowed for the bugs to be immediately taken care of and for work to progress very quickly.

Through discussions with OHIF developers, we were able to have a better understanding of the extent of the [OpenID Connect](https://openid.net/connect/) functionaly currently present in OHIF. Over the course of the Project Week we realized that is was possible to integrate KHEOPS with OHIF by making some modifications to the KHEOPS [Report Provider API](https://github.com/OsiriX-Foundation/KheopsAuthorization/wiki/Report-Providers-API) that would allow KHEOPS to launch OHIF using a pure OpenID Connect API. This will provide security that fully conforms to all the current best practices. In addition, this will allow KHEOPS to integrate with any third party software that implements OpenID Connect.

In order to test this strategy, we built a KHEOPS Report provider that provides a bridge between the Report Provider API and a pure OpenID Connect API. The flow we defined depended on OHIF implementing the OpenID Connect [Third Party Login Initiation](https://openid.net/specs/openid-connect-core-1_0.html#ThirdPartyInitiatedLogin) endpoint. This endpoint was implemented and has been merged into the main OHIF codebase. Using this new functionality we were able to launch a master-branch version of OHIF and have it open a study, without every passing an Access Token in the URL, have OHIF issue refresh requests for new Access Tokens, and have full bidirectional communication between OHIF and KHEOPS. Following this proof of concept, we will make the necessary modifications to KHEOPS to directly configure OHIF as a Report Provider.

[Project Week Demo](https://demo.kheops.online/view/Ez4otjNCUgcgSIyMaeGlLs)

[radical]: http://radicalimaging.com/
[erik]: https://github.com/swederik
[james]: https://github.com/jamesapetts
[OvelaSolutions]: https://www.ovelasolutions.com
[spalte]: https://github.com/spalte
[nicolas]: https://github.com/nicolasvandooren
[OsiriXFoundation]: https://github.com/OsiriX-Foundation
[sib]: https://www.sib.swiss
[unige]: https://www.unige.ch
