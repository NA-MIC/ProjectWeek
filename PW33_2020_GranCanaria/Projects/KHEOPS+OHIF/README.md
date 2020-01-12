Back to [Projects List](../../README.md#ProjectsList)

# Secure Interface between KHEOPS and OHIF

## Key Investigators

- Joël Spaltenstein (OsiriX Foundation / Swiss Institute of Bioinformatics)
- Nicolas van Dooren (OsiriX Foundation / University of Geneva)

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

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

# Illustrations

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
