.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/AIDE/AIDE.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_AguaClara_Infrastructure_Design_Engine:


.. list-table::
   :widths: 150 30
   :header-rows: 0

   * - |ACRlogowithname|
     - |donate|

**************************************
AguaClara Infrastructure Design Engine
**************************************

.. toctree::
  :caption: About
  :maxdepth: 1

  About/Clarifier.rst
  About/Doser.rst
  About/ET.rst
  About/FlocHH.rst
  About/FlocHV.rst
  About/FlocVH.rst
  About/LFOM.rst
  About/OStaRS.rst
  About/Plant20-80.rst

The AguaClara Infrastructure Design Engine (AIDE) is created and continuously improved by AguaClara Reach using the |Onshape| platform.  AIDE is a long term effort that began in 2005 and represents the contributions of thousands of individuals. AguaClara Reach is providing open access to this beta release of AIDE configurable components for educational purposes and so AguaClara implementation partners can explore our technologies (see our :ref:`Disclaimer <heading_Disclaimer>`).

We rely on donor support to develop AIDE and to create this textbook. Please |donate| to support our mission of developing and providing the next generation of drinking water treatment plants so that many more communities can have safe water on tap.

In the :ref:`table below <table_AIDE_configurable_components>` are links to configurable component models. Information on how to :ref:`access and modify the models is given below the table <heading_Using_AIDE>`. We welcome `your feedback on the AIDE models <https://docs.google.com/forms/d/e/1FAIpQLSdYHVinzW-xZskW74rpZ_7prHAqjLQDwadCNiRP39nyu7NHMw/viewform?>`_. If you are interested in AguaClara technologies to produce safe water on tap please fill out our `survey for potential implementation partners <https://docs.google.com/forms/d/e/1FAIpQLSdU7ZrWlnugDqEutdELWLoj5jq8JW6yzOeUg3Al4R7LUSYzRA/viewform?>`_.

.. raw:: html

    <embed>
       <div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/272ed6d0570a4b489ca630a10aa5a65d" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    </embed>


.. _table_AIDE_configurable_components:

.. csv-table:: AIDE configurable components.
   :header: "Link to Onshape", "Description", "Approximate time to generate model component (s)"
   :align: left
   :widths: 30 60 15

   |20-80Lpsplant|, "20-80 L/s plant: Integrated plant for flows between 20 and 80 L/s (see `AIDE: Introductory Video <https://www.loom.com/share/272ed6d0570a4b489ca630a10aa5a65d>`_)", 180
   |LFOM|, "Linear Flow Orifice Meter (see `AIDE: Linear Flow Orifice Meter <https://www.loom.com/share/59c642e57000459290eeeaf4eae794c2>`_)", 5
   |Doser|, "Chemical Dose Controller", 5
   |EntranceTank|,  "Entrance Tank: trash racks, grit removal, chemical dose controller, and linear flow orifice meter", 20
   |FlocculatorVH|, "Flocculator VH: Vertical-Horizontal Flocculator for flows below about 20 L/s", 15
   |FlocculatorHV|, "Flocculator HV: Horizontal-Vertical Flocculator for flows between about 10 and 100 L/s", 15
   |FlocculatorHH|, "Flocculator HH: Horizontal-Horizontal Flocculator for flows above about 100 L/s", 5
   |Clarifier|, "Clarifier: floc filter, plate settlers, and floc hopper", 32
   |OStaRS|, "OStaRS: Open Stacked Rapid Sand Filter", 25

The AIDE components will be updated as we continue to improve the designs and we will be adding new components as we extend our designs to a wide range of flow rates.

.. _heading_Disclaimer:

Disclaimer
==========

The configurable components created by AIDE are not engineering designs. The configurable components are provided for educational purposes. The configurable components create models that have not been reviewed and are likely NOT suitable for any particular application.

**In no event shall AguaClara Reach, or their employees be liable to any party for direct, indirect, special, incidental, or consequential damages, including lost profits, arising out of the use of AIDE, even if AguaClara Reach may have been advised of the possibility of such damage.**


Introduction to AIDE
====================

AIDE is based on parametric design. The vast majority of the dimensions are calculated from hydraulic constraints. Pipe diameters are sometimes based on a head loss constraint, sometimes are designed to not break up flocs, and in the chemical doser are designed to ensure laminar flow. Wall thicknesses are based on the construction methods used by the implementation partner and vary based on the depth of water in the tank. Thus the filter has thicker walls than the clarifier.

AIDE is built from many modular components that are all connected so they can share design information. The entire water treatment plant is an example of a top level component, a trunk, that has an entrance tank, flocculator, clarifier, and filter as branches. Each of the branches also has its own twigs. We call the connections between trunk, branch, and twigs a part studio tree. The part studio tree is assembled level by level in a way that allows the trunk to know everything about all of the branches and their twigs. This sharing of design parameters between components enables an integrated design and an optimized plant layout.

All of the parts used to assemble the design originate in a parts database.  The database can be customized for different implementation partners so that the part dimensions and costs match their requirements.  The database approach to design ensures that when an alternative part is selected that all plant dimensions update to accommodate the new part dimensions.

The AIDE configurable components are not engineering designs. AguaClara Reach uses AIDE configurable components, expertise in drinking water treatment, and site specific conditions detailed by AguaClara Implementation Partners to develop customized designs for community-scale water treatment plants.

Most of the configurable component models have two or more check boxes that provide increasing level of model detail. A few models have more options to turn on computationally intensive parts of the design.

  #. *Add plastic components* - Enables the modeling of pipes, baffles, and other plastic components and creates a complete bill of materials. For some of the components it will only show an example rather than fully replicating all of the parts.

  #. *Replicate all parts* - Fully replicates all parts and may significantly extend the time required to generate a new model. Note that the Bill of Materials includes the correct quantity of each of the parts even if the parts are not all replicated.

  #. *Print parameter map* - Prints a full map in the FeatureScript notices of all of the model inputs. Only a small fraction of the available inputs are exposed in the model configuration parameters. Click on show FeatureScript Notices |showFSNotices| to open a new pane at the bottom of the browser window where the full parameter map will be displayed.

The full plant can take up to several minutes to generate a new model that shows internal components fully replicated (see the column of *time to generate model component* in :numref:`table_AIDE_configurable_components` for estimates of the time required for regenerating a fully detailed model). If you are interested in exploring the overall size or layout of the components the time to generate a new model can be substantially reduced by not replicating all parts and not showing internal components.

If you would like to explore possible configurations, change the values to generate new models. The configurations have minimum and maximum values. This does not imply that the models created in that range are viable designs. The intent of providing the configuration options is to allow exploration to see how the models change when the input configurations are changed. If a configuration input is red, it is out of range.



.. _heading_Using_AIDE:

Using AIDE to Explore AguaClara Technologies
============================================

If you do not yet have an |Onshape| account, then you will be able to make changes to the component configuration by using the `view only toolbar <https://cad.onshape.com/help/Content/viewonlytoolbar.htm>`_. You can sign up for a `free public Onshape account <https://www.onshape.com/en/products/free>`_ that will enable you to access the parts lists and *estimated* materials cost for each of the AIDE configurable components. The AIDE videos (see :numref:`table_AIDE_videos`) introduce the core AIDE features.

.. _table_AIDE_videos:

.. csv-table:: AIDE play list of videos.
   :header: "Link to video", "Description"
   :align: left
   :widths: 50 50
   :width: 100

   |AIDEIntroduction|, "AIDE | Introduction"
   |AIDEConfigurations| , "AIDE | Configurations"
   |AIDEBOM|, "AIDE | Bill of Materials"
   |AIDEconfigurableComponent|, "AIDE | Configurable component example"


How AguaClara Reach Uses AIDE
=============================

AguaClara Reach (ACR) uses AIDE to provide Implementation Partners (IPs) with customized hydraulic designs. AguaClara Reach works with IPs to customize the AIDE parts database so that the design reflects construction practices and part availability in the IP's region. This includes pipes and fittings from preferred vendors and custom dimensions used for the civil work based on the construction methods used by each Implementation Partner. The designs are customized based on water quality. ACR also provides training and technical support to IPs.

There are approximately 300 input parameters required to design a full AguaClara water treatment plant. In addition there are many hundreds of parts in the parts database that each require dimensions. AIDE makes it possible to modify both the parts database and the input parameters for each IP.

ACR developed AIDE to reduce the time required to customize the designs and to make it possible to provide detailed designs quickly. With AIDE ACR can provide an IP with a quick bill of materials so they can see if the parts are available in country and a quick **estimate** of material cost. AIDE has the additional benefit of enabling ACR to upgrade the design algorithms as new insights come in from both IPs and the AguaClara academic partners. New design algorithms can be deployed across the entire suite of AIDE components and updated designs can be provided to IPs when they are ready to adopt the new features.

Next Steps for Potential Implementation Partners
================================================

AguaClara Reach is ready to develop partnerships with both non-profit organizations and engineering firms. Our partners use the AguaClara technologies to provide sustainable safe water on tap to cities, towns, and villages. The :ref:`title_AguaClara_Specifications` are available for IP reference.


.. |LFOM| image:: https://cad.onshape.com/api/thumbnails/d/49035a16b895fd8095d17a02/w/b76e9410efc3d9f5861e9516/s/300x170
  :width: 200
  :target: https://cad.onshape.com/documents/49035a16b895fd8095d17a02/w/b76e9410efc3d9f5861e9516/e/c063acb14de8f1f558b02d2d?configuration=HL_min%3D0.2%2Bmeter%3BND_max%3D12.0%3BQm_max%3D5.0%3BTEMP_min%3D10.0%3BdrillD_max%3D0.1%2Bmeter%3BprintParams%3Dfalse&renderMode=0&uiState=626fea458d39dd1e3b6106e1

.. |Doser| image:: https://cad.onshape.com/api/thumbnails/d/e71bb0c05d9e7241822776b7/w/533d9612b07de271291829dc/s/300x170
  :width: 200
  :target: https://cad.onshape.com/documents/e71bb0c05d9e7241822776b7/w/533d9612b07de271291829dc/e/20f111b627e4c6d59c3f0ff9?configuration=HL_max%3D0.2%2Bmeter%3BQ_pi%3D1.0%3BchlorineC_pi%3D0.6%3BcoagC_pi%3D0.5%3BprintParams%3Dfalse%3Brep%3Dtrue%3BtankOW%3D1.0%2Bmeter&renderMode=0&uiState=6273e0ecd685467dff5c17c4

.. |EntranceTank| image:: https://cad.onshape.com/api/thumbnails/d/4c47a124da3abec33e0ce813/w/3955cd0d266daedd3eabf165/s/300x170
  :width: 200
  :target: https://cad.onshape.com/documents/4c47a124da3abec33e0ce813/w/3955cd0d266daedd3eabf165/e/bcf152c5be02d9ab5b2b5285?configuration=L%3D8.0%2Bmeter%3BQm_max%3D40.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D10.0%3BcaptureVm%3D20.0%3BflocUpstreamHW%3D2.0%2Bmeter%3BprintParams%3Dfalse%3Brep%3Dtrue&renderMode=0&uiState=626fea87ee1eae4ff2291321


.. |FlocculatorVH| image:: https://cad.onshape.com/api/thumbnails/d/673077f4fa843a817d4cd55d/w/8bd189f4769c2a64aa07a8c0/s/300x170
  :width: 200
  :target: https://cad.onshape.com/documents/673077f4fa843a817d4cd55d/w/8bd189f4769c2a64aa07a8c0/e/cdc0c6cfa0e8b64f179ced51?configuration=GT_min%3D35000.0%3BG_bod%3D50.0%3BQm_max%3D1.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D5.0%3BoutletHW%3D1.7%2Bmeter%3BprintParams%3Dfalse%3Brep%3Dtrue&renderMode=0&uiState=626feb5ffb767608344ad1ad

.. |FlocculatorHV| image:: https://cad.onshape.com/api/thumbnails/d/9742e8c019b742df4ae4db85/w/cbe4d0f58d318c45281687ae/s/300x170
  :width: 200
  :target: https://cad.onshape.com/documents/9742e8c019b742df4ae4db85/w/cbe4d0f58d318c45281687ae/e/05162587e7127122572d3a10?configuration=GT_min%3D35000.0%3BG_bod%3D50.0%3BL%3D6.0%2Bmeter%3BQm_max%3D30.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D25.0%3BoutletHW%3D2.0%2Bmeter%3BprintParams%3Dfalse%3Brep%3Dtrue&renderMode=0&uiState=626feb168bd195153bbbe9af

.. |FlocculatorHH| image:: https://cad.onshape.com/api/thumbnails/d/84c4c94f9773b67506cd35bb/w/58a1f53fe5ebbbbc808a3541/s/300x170
  :width: 200
  :target: https://cad.onshape.com/documents/84c4c94f9773b67506cd35bb/w/58a1f53fe5ebbbbc808a3541/e/aa5906755ba02b0a3925ec10?configuration=GT_min%3D35000.0%3BG_bod%3D50.0%3BQm_max%3D200.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D0.0%3BoutletHW%3D3.0%2Bmeter%3BprintParams%3Dfalse%3Brep%3Dtrue&renderMode=0&uiState=626fead687c54745ef4c039f

.. |Clarifier| image:: https://cad.onshape.com/api/thumbnails/d/e05915c533ee7568c402981a/w/56de4202f426e6443151ca07/s/300x170
  :width: 200
  :target: https://cad.onshape.com/documents/e05915c533ee7568c402981a/w/56de4202f426e6443151ca07/e/3f94eabd115787bc33ae755d?configuration=G_max%3D140.0%3BQm_max%3D20.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D10.0%3BcaptureVm%3D0.12%3BprintParams%3Dfalse%3Brep%3Dtrue%3BrepBayInternals%3Dfalse%3BupVm%3D1.0&renderMode=0&uiState=627688ef04309300574a09f6

.. |OStaRS| image:: https://cad.onshape.com/api/thumbnails/d/8a1a990f01575e6e5eed1922/w/3811cfb89da77b076395fdc0/s/300x170
  :width: 200
  :target: https://cad.onshape.com/documents/8a1a990f01575e6e5eed1922/w/3811cfb89da77b076395fdc0/e/fd576f076cd3757b426c7f20?configuration=Qm_max%3D20.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D10.0%3BfilterHL_pi%3D0.5%3BfilterMode%3Dfalse%3BprintParams%3Dfalse%3Brep%3Dtrue%3BrepBayInternals%3Dfalse%3BrepInternalPiping%3Dfalse%3BspareFilter%3Dfalse&renderMode=0&uiState=6276885764a43e34bd8c13b9

.. |20-80Lpsplant| image:: https://cad.onshape.com/api/thumbnails/d/0e9ede93e11e5a54f68f8606/w/2744164cc6e56e3693a3190f/s/300x170
  :width: 200
  :target: https://cad.onshape.com/documents/0e9ede93e11e5a54f68f8606/w/2744164cc6e56e3693a3190f/e/723e9e9d93f3008c9815e2d6?configuration=Qm_max%3D40.0%3BShow_Internal_Components%3Dfalse%3BTEMP_min%3D10.0%3BprintParams%3Dfalse%3Brep%3Dfalse&renderMode=0&uiState=626fedaca473381cd632eede

.. |ACRlogowithname| image:: /Images/ACRlogowithname.png
  :target: https://www.aguaclarareach.org/
  :height: 50

.. |Onshape| image:: /Images/Onshape.png
  :target: https://cad.onshape.com/
  :height: 18

.. |donate| image:: /Images/donate.png
  :target: https://www.aguaclarareach.org/donate-now
  :height: 30

.. |showFSNotices| image:: /Images/showFeatureScriptNotices.png
  :height: 30


.. |AIDEIntroduction| image:: /Images/AIDEIntroductionThumbnail.png
  :width: 200
  :target: https://www.loom.com/share/272ed6d0570a4b489ca630a10aa5a65d


.. |AIDEConfigurations| image:: /Images/AIDEconfigurationsThumbnail.png
  :width: 200
  :target: https://www.loom.com/share/50cfe59aef434cc8a421af959aef5b61


.. |AIDEBOM| image:: /Images/AIDEBOMthumbnail.png
  :width: 200
  :target: https://www.loom.com/share/b501b6205ac84776980953c4368efec8

.. |AIDEconfigurableComponent| image:: /Images/AIDEConfigComponentThumbnail.png
  :width: 200
  :target: https://www.loom.com/share/59c642e57000459290eeeaf4eae794c2
