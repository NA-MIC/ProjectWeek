# Live discourse

NA-MIC Project Week 2020-12-16, 12-2pm EST

## User questions/suggestions:

* I could never fully understand those functions that can be edited in the Volume Rendering module (Advanced/Volume properties). Can you explain what they mean?
* Can Slicer be connected to a DICOMweb server to retrieve and store images there?
    * See [SlicerDICOMwebBrowser](https://www.google.com/url?q=https://github.com/lassoan/SlicerDICOMwebBrowser&sa=D&ust=1608152866180000&usg=AOvVaw1wBAAMArS0JsnfJ9dpqhom) extension
    * "Dropbox" for medical images. See [https://demo.kheops.online/](https://www.google.com/url?q=https://demo.kheops.online/&sa=D&ust=1608152866180000&usg=AOvVaw1FFfzhwsnKlrynrNWQfHhc) 
        * Create Album -> create a link -> then use in Slicer dicom web client
* Are SampleData free for reuse ?
    * Yes. except the Panoramix dataset that we are currently removing (see [PR Slicer#5311](https://www.google.com/url?q=https://github.com/Slicer/Slicer/pull/5311&sa=D&ust=1608152866181000&usg=AOvVaw2ugr46Icc7huRkWOSFJBKh))
    * If you need paperwork (e.g in context of IRB), getting data from [TCIA](https://www.google.com/url?q=https://www.cancerimagingarchive.net/collections/&sa=D&ust=1608152866181000&usg=AOvVaw1iEQDE9Bksz4jUfpqKBuTs) is recommended.
* What is the suggested "best practice" to learn slicer?
    * A good starting point is to download the tutorials and pre-computed datasets on the [Slicer Training Compendium](https://www.google.com/url?q=https://www.slicer.org/wiki/Documentation/Nightly/Training&sa=D&ust=1608152866181000&usg=AOvVaw26T6zx2JlfCRYQngyhzsCe). (be sure to be aware of the version of Slicer you are using vs the version mentioned in the tutorial).
    * Additional questions:
        * How can I get help without feeling like I'm asking for too much?
            * We are always happy to help either on the Slicer Discourse Forum or directly by email.  
            * Try to pose your questions thoughtfully ([http://sscce.org](https://www.google.com/url?q=http://sscce.org&sa=D&ust=1608152866182000&usg=AOvVaw2X0yT_eoIk3OccuwxT-Qtm)/)
            * A good practice is to check if your Slicer question has already been answered on the Slicer Forum before posting it.
            * What about adding a category in the discourse for "Beginner/New User Questions?"
        * Is there a way to get help if I don't speak English well?
            * Many Slicer team members are non-native English speakers, just mention what your native language is and we’ll try to find someone who could help out
            * There are some [Chinese resources](https://www.google.com/url?q=https://spujol.github.io/SlicerTutorialsInChinese/&sa=D&ust=1608152866182000&usg=AOvVaw09IFKcwb2Dn_B5lvluSjNg) for example
            * (Sonia Pujol spujol@bwh.harvard.edu) I am always happy to help with Slicer questions in French
            * (Andrey, @fedorov in Discourse) I am a native Russian speaker, and fluent in Ukrainian - happy to help
* Volume rendering seems to delineate structures quite nicely. Can I use it for quantification?
    * Short answer: No. You would need to perform a segmentation or place markups fiducials on the visible surface to measure.
    * Longer answer: placing fiducials on volume rendering is possible, also segmentation based on opacity could possibly be done. Fiducials are placed at 50% opacity.
    * Follow up questions:
        * Which picker is used ?
            Software picker is used to place markups. In the future, we could re-evaluate to make picking faster.
        * Can we adjust the 50% threshold ?
            Adjusting the transfer function may be an alternative approach.
    * Comments / suggestions:
        * Add presets for CBCT
        * MicroCT does volume render but it’s tricky to adjust depending if 8-bit or 16-bit
* Documentation is quite fragmented ([ReadTheDocs](https://www.google.com/url?q=https://slicer.readthedocs.io/en/latest/&sa=D&ust=1608152866183000&usg=AOvVaw1qaL9prP4aEkFKp6l-XXV0), [wiki](https://www.google.com/url?q=https://www.slicer.org/wiki/Documentation/Nightly&sa=D&ust=1608152866183000&usg=AOvVaw0viYLr3r0tTLETqJzzR7pt)). Can I do something to help?
    * (Jc) We currently focus on moving documentation to readthedocs and updating the wiki to add links “redirecting” to the readthedocs. We would greatly benefit from help to:
        (a) move documentation of module to readthedocs,
        (b) review the description of existing modules and update them.
        (c) mark deprecated content on the wiki as “historical”. This is done by using the [historical](https://www.google.com/url?q=https://www.slicer.org/wiki/Template:Historical&sa=D&ust=1608152866184000&usg=AOvVaw1-MGgsjSNbcYn4-EZNrKKv)template. For an example of use, see [this page](https://www.google.com/url?q=https://www.slicer.org/wiki/Slicer:git-svn&sa=D&ust=1608152866184000&usg=AOvVaw1IOdB6qBUnLBDbKoHbYcoM),
        (d) improve the extension wizard to to include template for documentation (we would need to discuss this during the weekly hangout)
    * Comments / Suggestions:
        * Ron: Add last modified timestamp to documentation page
            * Jc: Looking into enabling [https://pypi.org/project/sphinx-gitstamp/](https://www.google.com/url?q=https://pypi.org/project/sphinx-gitstamp/&sa=D&ust=1608152866184000&usg=AOvVaw3-7jkad2dwZtWvgTkg6FdT) 
        * Andras: Discourse tag “[feature-requests](https://www.google.com/url?q=https://discourse.slicer.org/c/support/feature-requests/9&sa=D&ust=1608152866185000&usg=AOvVaw3e-VRli8zjjlwOH8jcFLmg)” can be “followed” to be notified
* Slicer’s Segmentation Editor is very powerful.  Please review where to find the best tutorials and materials for learning it to segment data in the wild.
    * [https://lassoan.github.io/SlicerSegmentationRecipes/](https://www.google.com/url?q=https://lassoan.github.io/SlicerSegmentationRecipes/&sa=D&ust=1608152866185000&usg=AOvVaw1S7uBrYJ_gxlTN4nPU-xkA)
    * Also many tutorials in Slicer’s tutorial documentation
    * How to store tutorials: github pages, google slides, powerpoint
* Why estimation of MeanDiffusivity is not possible?
    * should be available in SlicerDMRI[ (see this paper](https://www.google.com/url?q=https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5679308/&sa=D&ust=1608152866186000&usg=AOvVaw0KhmgS5oL5KEu69IBgYcDJ) for features)
* With the addition of more model editing tools, are there any plans to add a Sketchfab exporter?
    * With the [OpenAnatomy extension](https://www.google.com/url?q=https://github.com/PerkLab/SlicerOpenAnatomy&sa=D&ust=1608152866186000&usg=AOvVaw2G9tYpcT4y8VzlCyS1275d) you can export glTF which should be easy to put in Sketchfab
    * MorphoSource does not support interactive visualization
    * Sketchfab can show models without making it easy to download, and download link is provided to MorphoSource (where access control and downloads are counted)
    * From Stephen: Video explaining how to load data using vtk based javascript viewer: [https://vimeo.com/413597904](https://www.google.com/url?q=https://vimeo.com/413597904&sa=D&ust=1608152866186000&usg=AOvVaw2fD6Jj-5_ot6fAikgOseJy) 
* Is there a recommended way of removing noise from CT scans ? especially metal artifacts from dental work and titanium plates without affecting the quality very much ?  It was recommended to do anisotropic diffusion filter but i get the error “Pixel type: 16-bit signed integer is not supported in 3D by N3itk6simple40CurvatureAnisotropicDiffusionImageFilterE.”
    * You can use the Cast Scalar Volume modul to create a different data type.  Probably Float is the best.
* Is there a way to do non-binary segmentations, where you could have a label and a probability associated with each volume sample? Or multiple labels and multiple probabilities associated with each volume sample?
    * There is a representation called Fractional labelmap just for this, but it’s not used by the majority of the segmentation methods
    * Thanks -- can it be displayed as a “LabelMap Volume” in the Slicer application?
    * LabelMap Volume is strictly binary. In modern Slicer segmentations should be Segmentation nodes. The infrastructure of Fractional labelmaps and its visualization is in place, but it seems (in the latest nightly) that it’s not enabled
        * OK, could I render it as one of the two volume images or do I have to convert it to a grey-scale volume first?
        * I suggest reading [this page](https://www.google.com/url?q=https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html&sa=D&ust=1608152866187000&usg=AOvVaw13NVCNZ_TinUiWaTud7nwp) to understand difference btw volume and segmentation
    * In almost all cases supersampling the labelmap in comparison to the source data is better use of memory than a fractional volume would be.  E.g. 8 bits per pixel could be fractional but could also be a 2x2x2 supersample.
* Probably a small thing, but in Mimics I’m used to having a circle, square and lasso when editing segmentations, would it be difficult to add the option to edit with a square that is 1 voxel and scalable? Sometimes 1 voxel can cause a spike or hole, but you don’t need to smooth a large area.
    * We can add this if there is a compelling use case.
* I saw the feature that allows you to adjust contours with control points that you showed in your SlicerHeart demo - where does that live?
    * Markups module: closed/open curves
* Can triangle models/surface models be edited on the fly? If yes, could you point us to an example where this is done?
    * Segment Editor: for closed surfaces only, uses binary labelmap representation
    * Dynamic modeler: for any models, but has limited editing features

## Developer questions/suggestions

* How 3D Slicer development is funded? How can I become a full-time 3D Slicer developer?
    * The typical scenario these days is that Slicer support comes as a by-product of other funded efforts that rely on it.  For example, several commercial and academic projects that employ the core slicer developers and agree that it's in their best interest to have a robust platform to work from.
    * [Commercial partners](https://www.google.com/url?q=https://www.slicer.org/wiki/CommercialUse&sa=D&ust=1608152866188000&usg=AOvVaw3XnLkseHXVCKjr2nh_04q3)are hiring (see also [Kitware](https://www.google.com/url?q=https://jobs.lever.co/kitware?location%3DCarrboro%252C%2520North%2520Carolina&sa=D&ust=1608152866188000&usg=AOvVaw1ocz2l_o5-b8_br4tvr645))
    * What about creating a Slicer Developer job board?
        * We usually post these in the “Jobs” category on discourse: [https://discourse.slicer.org/c/announcements/events/27](https://www.google.com/url?q=https://discourse.slicer.org/c/announcements/events/27&sa=D&ust=1608152866189000&usg=AOvVaw2vhsUGOEcUt188Qar3oDME) 
* How do I figure out how to automate something that I know how to do in the GUI?
    * The [Python script repo](https://www.google.com/url?q=https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository&sa=D&ust=1608152866189000&usg=AOvVaw3ZmLPg1utOtnVL2SB1h_s6) is the best starting point for automating Slicer using Python
* How can I make auto-complete work in my Python IDE (Visual Studio Code, PyCharm)?
    * Setting up PythonSlicer as Python interpreter can help
    * ITK Python wrapping: interface file pyi, works for PyCharm
    * See [https://www.python.org/dev/peps/pep-0484/#stub-files](https://www.google.com/url?q=https://www.python.org/dev/peps/pep-0484/%23stub-files&sa=D&ust=1608152866190000&usg=AOvVaw28FSoHWgcI-SELwqGQ_LAT) 
* Where can I upload sample data for my own extension?
    * (Large data sets can be store in Github repositories as release assets - for example [https://github.com/lassoan/SlicerOrthodonticAnalysis/releases/tag/TestingData](https://www.google.com/url?q=https://github.com/lassoan/SlicerOrthodonticAnalysis/releases/tag/TestingData&sa=D&ust=1608152866190000&usg=AOvVaw0mZGiuL-OLOoQxVrTFUsaO))
    * Scripts for Automatic content-based addressing: <span class="c0 c6">[https://github.com/Slicer/SlicerTestingData/releases](https://www.google.com/url?q=https://github.com/Slicer/SlicerTestingData/releases&sa=D&ust=1608152866190000&usg=AOvVaw3qq5s-BBsABhHGhtpM9roY)
* How to import and use python modules inside Slicer python or extension modules?(what about other modules?)
    * slicer.util.pip_install() in the python interactor or in python code to pip install packages
    * For custom applications: Python packages can be added as additional dependencies
* How does the continuous integration for extensions work? If I start a new extension, can I use the CI from the beginning?
    * In order for the extension to be built by the CI, it needs to be submitted to the [ExtensionIndex](https://www.google.com/url?q=https://github.com/Slicer/ExtensionsIndex&sa=D&ust=1608152866191000&usg=AOvVaw0ZlrDq71HMxPkFbyIuav2S)
    * We generally require that extensions be basically functional before approving a submission to the index,
* My 2 cents: maybe it could be useful to highlight/remind participants that some Slicer algorithms can be run via command line, without GUI. Maybe someone is interested in adding some slicer stuff to his/her processing script that runs automatically without user interaction.
* What's the best way to share a module to others without going through extension manager? (for under development modules to share with people to test functionality)
    * extension can be installed from file
    * manually downloaded, non-packaged modules can be added to Slicer by using Application settings / Modules / Additional module paths
    * for functions that do not depend on Slicer, creating a regular python package can be an option
