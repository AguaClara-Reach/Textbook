.. _title_Entrance_Tank:

.. maybe the flow path for general should go through each specific section!
.. will need to connect to textbook chapters

*************
Entrance Tank
*************

Design information for the AguaClara entrance tank is available in `the Entrance Tank Design chapter of The Physics of Water Treatment Design <https://aguaclara.github.io/Textbook/Flow_Control_and_Measurement/ET_Design.html>`_.

General
-------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^

The entrance tank (see :numref:`figure_spec_ET_Diagram_Labeled`) has multiple functions in a drinking water treatment plant:

A. Remove air bubbles to reduce splashing, turbulence, and unsteady motion of the chemical feed surface tracking lever system
B. Remove grit to prevent accumulation in the flocculator
C. Remove leaves and other debris to prevent clogging of the diffusers in the clarifier inlet
D. Dissipate kinetic energy to keep the water level steady for accurate flow measurement
E. Measure the incoming flow rate with the Linear Flow Orifice Meter (LFOM) so that operators can make adjustments and respond to changes in water demand
F. Provide a water surface elevation that is proportional to the plant flow rate that is used to automatically ensure the chemical dosages remain constant even as the plant flow rate varies
G. Inject the coagulant and any other amendments required for flocculation

.. _figure_spec_ET_Diagram_Labeled:

.. figure:: Images/et_overview.png
    :width: 900px
    :align: center
    :alt: entrance tank diagram

    Section overview of an entrance tank

.. csv-table:: Entrance Tank Overview Figure Key for :numref:`figure_spec_ET_Diagram_Labeled`
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

    "1", "Chemical doser" 
    "2", "Float that tracks the water level set by the LFOM"
    "3", "Bypass"
    "4", "LFOM"
    "5", "Sediment drain pipe stub"
    "6", "Sediment hopper"
    "7", "Maximum water level set by the LFOM"
    "8", "Trash rack"
    "9", "Overflow"
    "10", "Raw water inlet"
    "11", "Maximum water level upstream of the trash rack"
    "12", "Drain channel that connects to the main plant drain channel"
    "13", "Pipe leading to the flocculator"

Flow Path
^^^^^^^^^

Raw water enters the the entrance tank as shown in :numref:`figure_spec_ET_Diagram_Labeled` and flows across the hoppers at the bottom of the tank. The first hopper contains an overflow pipe to waste any water entering the plant in excess of th design maximum plant flow rate. The overflow pipe is sized to handle the total maximum design plant flow rate. A removable drain pipe stub is installed in each hopper, allowing the operator to discharge accumulated sediment from the hoppers while the plant is in operation.  


Plant Specifications
^^^^^^^^^^^^^^^^^^^^^
.. _table_Entrance_Tank_Specifications:

.. csv-table:: Entrance Tank Specifications for :numref:`figure_spec_ET_Diagram_Labeled`
   :header: "Parameter", "Value"
   :align: left
   :widths: 20 50 50
   :class: wraptable

   "", Capture velocity, :sub:`($..et.captureVm) no-sub`
   "", Entrance tank internal width, :sub:`($..et.W) no-sub`
   "", Entrance tank internal length, :sub:`($..et.L) no-sub`
   "5", Removable drain pipe stub nominal diameter, :sub:`($..et.etHopper.drainND) no-sub` inches
   "6", **Hoppers**, ""
   "", Number of hoppers, :sub:`($..et.etHopper.N) no-sub`
   "", Hopper angle,  :sub:`($..et.etHopper.AN) no-sub`
   "7", Maximum depth of water at the LFOM,  :sub:`($..et.lfomHW) no-sub`
   "9", Overflow pipe nominal diameter, :sub:`($..et.overflow.ND) no-sub` inches


Trash Rack
----------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The trash racks are designed to remove any debris that would be large enough to obstruct downstream processes.

Flow Path
^^^^^^^^^
As the raw water flows from the first hopper to the subsequent ones, it must pass through two trash racks, preventing large debris from entering the treatment process. Having two trash racks allows the operator to remove one of the trash racks for cleaning. 

Plant Specifications
^^^^^^^^^^^^^^^^^^^^^
The smallest flow dimensions are the diffusers in the clarifier and the orifices in the stacked rapid sand filter inlet branches. The trash rack string spacing defined is the maximum allowable spacing of these strings.

.. _table_Trash_Rack_Specifications:

.. csv-table:: Trash Rack Specifications
   :header: "Parameter", "value"
   :align: left
   :widths: 50 50
   :class: wraptable

   Channel width, :sub:`($..trashRack.W) no-sub`
   Trash rack height, :sub:`($..et.trashRack.L) no-sub`
   Fractional open area, :sub:`($..et.trashRack.PO) no-sub`
   Downstream water depth, :sub:`($..et.trashRack.downstreamHW) no-sub`
   Clean head loss, :sub:`($..et.trashRack.HL_min) no-sub`
   Maximum fractional clogging, :sub:`($..et.trashRack.PO_pi) no-sub`
   Maximum head loss, :sub:`($..et.trashRack.HL_max) no-sub`
   String diameter, :sub:`($..et.trashRack.Dm) no-sub`
   Open space between strings, :sub:`($..et.trashRack.Sm) no-sub`
   Diffuser flow width, :sub:`($..inletManifold.diffuser.slotW) no-sub`
   StaRS inlet branch orifice diameter, :sub:`($..filter.fiPipes.branch.inlet.portD) no-sub`


Sediment and Grit Removal
-------------------------

The entrance tank has a capture velocity of :sub:`($..et.captureVm) no-sub` to remove particules that would otherwise settle in the bottom of the flocculator. Large particulates settle out in the hoppers, and collect near the drains at the bottom. 

The entrance tank length of :sub:`($..et.L) no-sub` corresponds to the clarifier tank length. The width, :sub:`($..et.W) no-sub`, ensures the minimum desired capture velocity is met while still allowing enough space for a person to fit inside and construct the tank.

The :sub:`($..et.etHopper.N) no-sub` hoppers collect sand and grit that then settles to the bottom where the :sub:`($..et.etHopper.drain.ND) no-sub` inch nominal diameter drains are located. When too much sediment has accumulated, the drain pipes must be removed until the sludge is flushed out. Directly below the entrance tank, there is a drain channel that transfers the waste to the main plant drain channel.



Linear Flow Orifice Meter
-------------------------
Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The Linear Flow Orifice Meter (LFOM) is a weir shape cut into a pipe with rows of holes, or orifices, drilled into it. The LFOM creates a linear relationship between water level in the entrance tank and the flow out of the entrance tank. It does not control the flow through the plant. The flow rate is controlled by inlet valve where raw water is entering the entrance tank.


This serves two purposes:

#. Allows the operator to measure the flow through the plant quickly and easily.
#. Allows for the Linear Chemical Dose Controller to automatically adjust the flow of coagulant and chlorine into the plant as the plant flow rate changes. This means the operators only need to adjust the coagulant when there is a need to change the **dose** due to a change in turbidity or organic matter concentration.


.. _figure_lfom_overview:

.. figure:: Images/lfom_overview.png
    :width: 150px
    :align: center
    :alt: An LFOM

    An AguaClara LFOM showing the flow rate in L/s.

.. csv-table:: LFOM Overview Figure Key
   :header: "Key", "Description"
   :align: center
   :widths: 20 80
   :class: wraptable

    "1", "Maximum flow rate in L/s and maximum water level"
    "2", "Zero flow and minimum water level"
    "3", "Pipe stub that can be removed"
    "4", "Invert of entrance tank"
    "5", "Pipe coupling that is embedded in concrete"


Flow Path
^^^^^^^^^
Water in the entrance tank flows into and down the LFOM, towards the rapid mix orifice and flocculator. 

Plant Specifications
^^^^^^^^^^^^^^^^^^^^^
.. _table_LFOM_Specifications:

.. csv-table:: LFOM Specifications
   :header: "Parameter", "Value"
   :align: center
   :widths: 40 60
   :class: wraptable

   LFOM nominal diameter, :sub:`($..et.lfom.ND) no-sub` inch
   Number of rows of orifices, :sub:`($..et.lfom.rowN) no-sub`
   Max flow rate, :sub:`($..et.lfom.Qm_max) no-sub`
   Head loss at max flow, :sub:`($..et.lfom.HL_max) no-sub`
   Diameter of orifices, :sub:`($..et.lfom.orificeD) no-sub`
   Space between orifices measured on the outside of the pipe,  :sub:`($..et.lfom.orificeS) no-sub`
   Number of orifices in each row starting from bottom row, :sub:`($..et.lfom.rowOrificeN_VEC) no-sub`
   Elevation of each row from zero flow datum, :sub:`($..et.lfom.rowOrificeH_VEC) no-sub`
