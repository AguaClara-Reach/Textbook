.. _title_Chemical_Dosing:

*************************
Chemical Dosing
*************************

.. add design information from textbook where it exists 

General Chemical Dosing
-----------------------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^

The coagulation and disinfection processes require the precise dosage of coagulant to the plant influent and calcium hypochlorite to the plant effluent. To carry out this process without pumps, the AguaClara plant uses a hydraulic dosing system.

The main components of the system are:

* Tanks to store the coagulant, chlorine, and pH adjustment stock solutions
* An elevated platform to support the chemical storage tanks at the correct elevation for gravity powered dosing
* A flow measurement calibration column for each chemical
* A pair of constant level tanks (CLTs) with float valves that maintain a constant level for both chemical solutions
* Two dosing tube modules that provide the necessary relationship between pressure drop and chemical flow rates for each chemical
* A chemical doser (the balance) that connects the water level in the plant's entrance tank to the level at the outlet of the chemical dosing system

This system has the characteristic of maintaining a constant chemical **dosage** even as the flow rate through the plant varies. The plant operator can vary the chemical dosage directly, without doing any calculations, and without having to manipulate the system every time the flow rate in the plant changes. The AguaClara dosing system provides the added benefit of automatically turning off the chemical flow when there is no flow in the plant. This provides security against contamination with excess chemicals and chemical waste in the event that the plant is shut down inadvertently which may occur if the transmission line is damaged.

Chemical Flow Path
^^^^^^^^^^^^^^^^^^
The liquid chemical stock solutions are prepared and stored in the chemical stock tanks, on the chemical platform. Chemicals exit the stock tanks through a sloped tube settler (to prevent sediment from exiting the tank through the chemical supply tubing) and then continue on to the constant level tanks (CLT). The sediment in the chemical stock tanks is removed through the drain during tank cleaing. The CLT uses a float valve to provide a relatively constant chemical level. The chemicals exit the CLT and flow to a set of dosing tubes that serve as linear resistors with head loss proportional to the chemical flow rate. The chemicals continue to the dose controller where the operator can set the chemical dosages by adjusting the position of a slider. The chemicals leaving the dose controller are then routed to the chemical drip locations. The coagulant and chemicals used for pH adjustment are dripped into the LFOM and the chlorine is dripped into the filter exit tank.

Plant Specifications
^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Chemical Dosing General Specifications
   :header: "Parameter", "Value"
   :align: left
   :widths: 50 50
   :class: wraptable

   Required chemicals, "Coagulant, Chlorine, and pH Adjustment"
   Plant maximum flow rate,  :sub:`($..et.lfom.Qm_max) no-sub`
   Maximum head loss thru doser tubes, :sub:`($..doserTubes.HL_max) no-sub`
   Coagulant stock concentration, :sub:`($..chemPipes.coagStockC) no-sub`
   Coagulant maximum dose, :sub:`($..chemPipes.coagDoseCm_max) no-sub`
   Coagulant maximum flow rate, :sub:`($..chemPipes.coagQu_max) no-sub`
   Chlorine stock concentration, :sub:`($..chemPipes.chlorineStockC) no-sub`
   Chlorine maximum dose, :sub:`($..chemPipes.chlorineDoseCm_max) no-sub`
   Chlorine maximum flow rate, :sub:`($..chemPipes.chlorineQu_max) no-sub`

Chemical Stock Tanks
--------------------
Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The chemical stock tanks are used to store the following chemicals: coagulant, chlorine, and chemicals used for pH adjustment. There are two storage tanks for each chemical.

.. TOCHANGE, image for non pH for replacement

.. _figure_chemical_stock_tanks_overview_pH:
.. figure:: Images/chem_stock_tanks_overview_pH.png
    :width: 600px
    :align: center
    :alt: chemical stock tank overview

    Overview of the chemical platform

.. csv-table:: Chemical Platform Overview Figure Key for :numref:`figure_chemical_stock_tanks_overview_pH`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Chemical stock platform"
   "2", "Coagulant stock tanks"
   "3", "Chlorine stock tanks"
   "4", "pH adjustment stock tanks"

.. _figure_chem_platform_bottom_pH:

.. figure:: Images/chem_platform_bottom_pH.png
   :width: 700px
   :align: center
   :alt: chemical stock tank bottom

   Bottom view of the chemical stock tanks


.. csv-table:: Chemical Platform Bottom View Figure Key for :numref:`figure_chem_platform_bottom_pH`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "5", "Chemical pipes - tank to CLT"
   "6", "Chemical drain pipes"

.. _figure_chem_platform_cutout_pH:
.. figure:: Images/chem_platform_cutout_pH.png
   :width: 700px
   :align: center
   :alt: chemical stock tank bottom
   
   Detail view of the chemical stock tanks valves

Valves with orange handles are compatible with chlorine and other chemicals, and have chemical-resistant o'rings.

.. csv-table:: Chemical Platform - Bottom View Cut-Out Figure Key for :numref:`figure_chem_platform_cutout_pH`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable
   
   "7", "Pipe clamping hangers"
   "8", "Union to connect chemical piping to CLT"
   "9", "Valve for chemical drainage"

.. _figure_chem_stock_tank_section:

.. figure:: Images/chem_stock_tank_section.png
   :width: 600px
   :align: center
   :alt: chemical stock tank section

   Section view of the chemical stock tank


.. csv-table:: Chemical Platform Section View Figure Key for :numref:`figure_chem_stock_tank_section`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "10", "Through-wall adaptor for chemical tank to CLT piping"
   "11", "Tube settler"
   "12", "Through-wall adaptor for chemical tank to drain piping"

Plant Specifications
^^^^^^^^^^^^^^^^^^^^^
.. csv-table:: Chemical Platform Specifications for :numref:`figure_chemical_stock_tanks_overview`-:numref:`figure_chem_stock_tank_section`
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 80 20
   :class: wraptable

   "1", "Chemical stock platform", ""
   " ", "Width", :sub:`($..chemPlatform.OW) no-sub`
   " ", "Length", :sub:`($..chemPlatform.OL) no-sub`
   " ", "Distance between top of plant floor and top of platform floor", :sub:`($..chemPlatform.H) no-sub`
   "2", "Coagulant tank", ""
   " ", "Volume", :sub:`($..chemPlatform.chemBase.coagTank.VOLm) no-sub`
   " ", "Height", :sub:`($..chemPlatform.chemBase.coagTank.H) no-sub`
   " ", "Bottom Diameter", :sub:`($..chemPlatform.chemBase.coagTank.botD) no-sub`
   "3", "Chlorine tank", ""
   " ", "Volume", :sub:`($..chemPlatform.chemBase.chlorineTank.VOLm) no-sub`
   " ", "Height", :sub:`($..chemPlatform.chemBase.chlorineTank.H) no-sub`
   " ", "Bottom Diameter", :sub:`($..chemPlatform.chemBase.chlorineTank.botD) no-sub`
   "4", "Soda ash tank", ""
   " ", "Volume", :sub:`($..chemPlatform.chemBase.sodiumCarbonateTank.VOLm) not applicable`
   " ", "Height", :sub:`($..chemPlatform.chemBase.sodiumCarbonateTank.H) not applicable`
   " ", "Bottom Diameter", :sub:`($..chemPlatform.chemBase.sodiumCarbonateTank.botD) not applicable`
   "5-11", "Dose and drain plumbing nominal diameter", :sub:`($..chemPipes.dosing.ND) no-sub` inch
   " ", "Height of stock tanks above constant head tanks", :sub:`($..chemPlatform.platformCltHW_delta) no-sub`
   " ", "Maximum head loss through the float valve orifice", :sub:`($..chemPlatform.chemBase.clt.floatValve.HL_max) no-sub`

.. add weight to the tank dimensions (based on chemical densities)

All of the chemical feed and drain piping uses a nominal diameter of  :sub:`($..chemPipes.dosing.ND) no-sub` inch.


Constant Level Tanks
--------------------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The constant level tank (CLT) system provides convenient central controls for selection of stock tank, flow calibration, purging sediment, and selection of which of the redundant chemical feed systems to use. The redundant systems facilitate cleaning and maintenance. The dosing system controls are centralized around the constant level tanks (see :numref:`figure_clt_overview`).

.. _figure_clt_overview_pH:
.. figure:: Images/clt_overview_pH.png
   :width: 400px
   :align: center
   :alt: constant level tank overview

   Overview of the constant level tank module mounted on the side of the chemical stock tank platform.

.. csv-table:: CLT Overview Figure Key for :numref:`figure_clt_overview_pH`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Chemical stock tank volume and flow calibration column sight tube"
   "2", "Constant level tank"
   "3", "Dosing tube module"

The constant level tanks prevent the changing chemical levels in the stock tanks from influencing the flow rate through the dosing system. Float valves maintain a relatively constant level of chlorine and coagulant. The float valves are sized to provide up to the maximum chemical flow rate of :sub:`($..chemPipes.chemQu_max) no-sub` given the minimum head provided by stock tanks (:sub:`($..floatvalveHL_bod) no-sub`).

.. _figure_clt_details_pH:
.. figure:: Images/clt_details_pH.png
   :width: 300px
   :align: center
   :alt: constant level tank details

   Constant level tank with associated valves and dosing tubes. The valves with orange handles are compatible with chlorine and other chemicals and have chemical resistant o'rings.

.. csv-table:: CLT Details Figure Key for :numref:`figure_clt_details_pH`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Coagulant stock tank volume and flow calibration column sight tube"
   "2", "Constant level tank"
   "3", "Dosing tubes to provide linear relationship between chemical flow rate and head loss"
   "4", "Valve to select constant level tank and dosing tube set"
   "5", "Float valve to provide constant level of coagulant"
   "6", "Air vent to discharge bubbles from dosing tubes"
   "7", "Valve to select which stock tank to use"
   "8", "Valve to drain constant level tank (for cleaning with vinegar)"
   "9", "Sediment trap to capture particles from the stock tank"
   "10", "Valve to purge the sediment trap"
   "11", "Connection to feed line to the doser"
   "12", "Valve to drain the line going to the doser (for cleaning with vinegar)"

There is a pair of constant level tanks for each chemical feed. The specifications for each tank is given below.

Plant Specifications
^^^^^^^^^^^^^^^^^^^^^
.. _table_Constant_Level_Tank_Specifications:

.. csv-table:: Constant Level Tank Specifications for :numref:`figure_clt_overview`-:numref:`figure_clt_details_pH`
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 50 30
   :class: wraptable

   "", Minimum head provided by stock tanks,  :sub:`($..floatvalveHL_bod) no-sub`
   5, **Float Valve**, ""
   "", Maximum head loss through the float valve orifice,  :sub:`($..floatValve.HL_max) no-sub`
   "", Float valve orifice diameter, :sub:`($..floatValve.orificeD) no-sub`
   2, **Constant level tank**, ""
   "", Tank inner length, :sub:`($..clt.tankL) no-sub`
   "", Tank inner width, :sub:`($..clt.tankW) no-sub`
   "", Tank depth, :sub:`($..clt.tankH) no-sub`
   "", Tank fluid depth, :sub:`($..clt.tankHW) no-sub`


Dosing Tubes
------------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
Dosing tubes use laminar flow in a long straight small diameter tube to establish a linear relationship between head loss and flow rate. The velocity in the tubes is limited to ensure that minor losses that scale with velocity squared remain less than :sub:`($..doserTubes.minorHL_pi) no-sub` of the maximum head loss, :sub:`($..doserTubes.HL_max) no-sub`, is from minor losses. 

The number of dosing tubes is increased as needed to ensure that the maximum allowable tube velocity is not exceeded. The dosing tubes are mounted in a module to facilitate cleaning and replacement.

.. _figure_dosing_tube_module:

.. figure:: Images/dosing_tube_module.png
   :width: 300px
   :align: center
   :alt: constant level tank details

   Dosing tube module

.. csv-table:: Dosing Tubes Figure Key for :numref:`figure_dosing_tube_module`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Reducer"
   "2", "Union"
   "3", "Part of union that is glued to the pipe shield and disk"
   "4", "Dosing tubes"
   "5", "Pipe shield that maintains the dosing tubes in tension"
   "6", "PVC disk that is glued to the union and that has slightly undersized holes for the dosing tubes"
   "7", "Isometric view of the union showing that the dosing tubes are visible above the disk"

Plant Specifications
^^^^^^^^^^^^^^^^^^^^^
The coagulant dosing tube specifications are given below.

.. _table_Coagulant_Dosing_Tube_Specifications:

.. csv-table:: Coagulant dosing tube specifications for :numref:`figure_dosing_tube_module`
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 50 30
   :class: wraptable

   4, **Dosing tubes**, ""
   "", Number of tubes per module,  :sub:`($..coagDoserTube.N) no-sub`
   "", Tube inner diameter, :sub:`($..coagDoserTube.tube.ID) no-sub`
   "", Tube outer diameter, :sub:`($..coagDoserTube.tube.OD) no-sub`
   "", Tube length, :sub:`($..coagDoserTube.tube.L) no-sub`
   5, **Pipe guard**, ""
   "", Pipe guard length, :sub:`($..coagDoserTube.shell.pipe.L) no-sub`
  
The chlorine dosing tube specifications are given below.

.. _table_Chlorine_Dosing_Tube_Specifications:

.. csv-table:: Chlorine dosing tube specifications for :numref:`figure_dosing_tube_module`
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 50 30
   :class: wraptable

   4, **Dosing tubes**, ""
   "", Number of tubes per module,  :sub:`($..chlorineDoserTube.N) no-sub`
   "", Tube inner diameter, :sub:`($..chlorineDoserTube.tube.ID) no-sub`
   "", Tube outer diameter, :sub:`($..chlorineDoserTube.tube.OD) no-sub`
   "", Tube length, :sub:`($..chlorineDoserTube.tube.L) no-sub`
   5, **Pipe guard**, ""
   "", Pipe guard length, :sub:`($..chlorineDoserTube.shell.pipe.L) no-sub`
   "", Pipe guard nominal diameter, :sub:`($..chlorineDoserTube.shell.ND) no-sub` inch
  
The pH adjustment tube dosing tube specifications are given below.

.. _table_pH_Dosing_Tube_Specifications:

.. csv-table:: pH adjustment dosing tube specifications for :numref:`figure_dosing_tube_module`
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 50 30
   :class: wraptable

   4, **Dosing tubes**, ""
   "", Number of tubes per module,  :sub:`($..coagDoserTube.N) no-sub`
   "", Tube inner diameter, :sub:`($..coagDoserTube.tube.ID) no-sub`
   "", Tube outer diameter, :sub:`($..coagDoserTube.tube.OD) no-sub`
   "", Tube length, :sub:`($..coagDoserTube.tube.L) no-sub`
   5, **Pipe guard**, ""
   "", Pipe guard length, :sub:`($..coagDoserTube.shell.pipe.L) no-sub`

Chemical Dose Controller
-------------------------
Design information for the AguaClara chemical dose controller is available in `the Flow Control chapter of The Physics of Water Treatment Design <https://aguaclara.github.io/Textbook/Flow_Control_and_Measurement/FCM_Design.html#linear-chemical-dose-controller-cdc>`_.


Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The chemical dose controller makes it easy and accurate to dose chemicals. The flow of chemicals automatically adjusts to changes in the plant flow rate to keep a constant dose, set by the operator. When a turbidity event occurs, the operator can change the dose of coagulant by moving the coagulant slider lower on the lever to increase the dose. The slider has labelled marks so the operator can record the dose accurately.

.. _figure_doser_overview_pH:
.. figure:: Images/doser_overview_pH.png
   :width: 500px
   :align: center
   :alt: Chemical doser controller overview

   Overview of the chemical dose controller


.. csv-table:: Chemical Dose Controller Figure Key for :numref:`figure_doser_overview_pH`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Doser slider"
   "2", "Lever"
   "3", "Float"
   "4", "Counterweight"
   "5", "Chemical pipes from CLT"
   "6", "Clamping hangers for chemical pipes from CLT"
   "7", "Tubes from CLT piping to doser"
   "8", "Tee connector between dosing and injection tubes"
   "9", "Tubes from doser to injection plumbing/points"

Plant Specifications
^^^^^^^^^^^^^^^^^^^^^
.. csv-table:: Chemical Dose Controller Specifications for :numref:`figure_doser_overview_pH`
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 80 20
   :class: wraptable

   "5-6", "CLT to doser pipes plumbing nominal diameter", :sub:`($..chemPipes.dosing.ND) no-sub` inch
   "7-9", "Chemical tube nominal diameter", :sub:`($..chemPipes.flex.ND) no-sub` inch


Injection Points
-----------------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The chemical must be injected into the flow of water within the plant. 

* Coagulant: The coagulant is dripped into the top of the LFOM in the entrance tank.
* Chlorine: The chlorine is dripped into the water exiting the filter on its way to the community water storage tank.
* pH adjustment: The chemical for pH adjustment is dripped into the LFOM with the coagulant.
 

 .. TOCHANGE, update to remove pH adjustment section

.. _figure_injection_point_entrance_tank_pH:
.. figure:: Images/injection_point_entrance_tank_pH.png
   :width: 600px
   :align: center
   :alt: Entrance tank injection point

   Entrance tank injection point

Additional doser arm and injection points are added for pH adjustment.

.. csv-table:: Coagulant Injection Point Figure Key for :numref:`figure_injection_point_entrance_tank_pH`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Linear dose controller"
   "2", "Coagulant and pH adjustment injection tubes"
   "3", "LFOM"

.. figure:: Images/injection_point_chlorine_plantview_pH.png
   :width: 600px
   :align: center
   :alt: Chlorine injection point path (plant view)

   Chlorine injection point path along wall, plant view

.. _figure_injection_point_chlorine:
.. figure:: Images/injection_point_chlorine.png
   :width: 400px
   :align: center
   :alt: Chlorine injection point path (zoomed in)

   Chlorine injection point path along wall, zoomed in

.. csv-table:: Chlorine Injection Point at Wall Figure Key for :numref:`figure_injection_point_chlorine`    
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "4", "Tube from linear dose controller"
   "5", "Reducing adaptor"
   "6", "Piping to injection point"
   "7", "Drain channel"
   "8", "Clamping hangers"
   
.. _figure_injection_point_chlorine_filter:
.. figure:: Images/injection_point_chlorine_filter.png
   :width: 500px
   :align: center
   :alt: Chlorine injection point in filter

   Chlorine injection point in filter

.. csv-table:: Chlorine Injection Point at Filter Figure Key for :numref:`figure_injection_point_chlorine_filter`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "9", "Union connector"
   "10", "PVC disc with hole for tube"
   "11", "Injection tube"
   "12", "In-filter straight connector for pipe encasing injection tube"
   "13", "Piping encasing injection tube"
   "14", "Exit pipe"
   "15", "Filter exit box"

Plant Specifications
^^^^^^^^^^^^^^^^^^^^^
.. csv-table:: Injection Point Specifications for :numref:`figure_injection_point_entrance_tank_pH`-:numref:`figure_injection_point_chlorine_filter`
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 80 20
   :class: wraptable

   "2", "Coagulant injection tube nominal diameter", :sub:`($..chemPipes.flex.ND) no-sub` inch
   "4 & 11", "Chlorine injection tube nominal diameter", :sub:`($..chemPipes.flex.ND) no-sub` inch
   "6", "Plumbing to chlorine injection point nominal diameter", :sub:`($..chemPipes.inject.ND) no-sub` inch
   "12", "Piping encasing injection tube nominal diameter", :sub:`($..filter.ioControls.chlorineConduit.ND) no-sub` inch