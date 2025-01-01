.. _title_Entrance_Tank:

*************
Entrance Tank
*************

Design information for the AguaClara flocculator is available in `the Entrance Tank Design chapter of The Physics of Water Treatment Design <https://aguaclara.github.io/Textbook/Flow_Control_and_Measurement/ET_Design.html>`_


Purpose and Description
=======================


The entrance tank (see :numref:`figure_spec_ET_Diagram_Labeled`) has multiple functions in a drinking water treatment plant.

#. Remove air bubbles to reduce splashing, turbulence, and unsteady motion of the chemical feed surface tracking lever system
#. Remove grit to prevent accumulation in the flocculator
#. Remove leaves and other debris to prevent clogging of the diffusers in the clarifier inlet
#. Dissipate kinetic energy to keep the water level steady for accurate flow measurement
#. Measure the incoming flow rate with the Linear Flow Orifice Meter (LFOM) so that operators can make adjustments and respond to changes in water demand
#. Provide a water surface elevation that is proportional to the plant flow rate that is used to automatically ensure the chemical dosages remain constant even as the plant flow rate varies
#. Inject the coagulant and any other amendments required for flocculation

.. _figure_spec_ET_Diagram_Labeled:

.. figure:: Images/et_overview.png
    :width: 900px
    :align: center
    :alt: entrance tank diagram

    Overview of an entrance tank.

    ===  ============
    Key  Description
    ===  ============
     1   chemical doser 
     2   float that tracks the water level created by the LFOM
     3   bypass
     4   LFOM
     5   sediment drain pipe stub
     6   sediment hopper
     7   maximum water level created by the lfom
     8   trash rack
     9   overflow
     10  raw water inlet
     11  maximum water level upstream of the trash rack
     12  drain channel that connects to the main plant drain channel
     13  pipe leading to the flocculator
    ===  ============

Raw water enters the the entrance tank as shown in :numref:`figure_spec_ET_Diagram_Labeled` and flows across the hoppers at the bottom of the tank. The first hopper contains an overflow pipe to waste any water entering the plant in excess of the plant flow rate. The overflow pipe has a nominal diameter of :sub:`($..et.overflow.ND) no-sub` inches, sized to handle the total plant flow rate. A :sub:`($..et.etHopper.drainND) no-sub` inch nominal diameter removable drain pipe stub is installed in each hopper, allowing the operator to discharge accumulated sediment from the hoppers while the plant is in operation.  

Design Data
===========

.. _table_Entrance_Tank_Specifications:

.. csv-table:: Entrance Tank Specifications.
   :header: "Parameter", "value"
   :align: left
   :widths: 50 50
   :class: wraptable

   Entrance tank internal width, :sub:`($..et.W) no-sub`
   Entrance tank internal length, :sub:`($..et.L) no-sub`
   Maximum depth of water at the LFOM,  :sub:`($..et.lfomHW) no-sub`
   Number of hoppers, :sub:`($..et.etHopper.N) no-sub`
   Hopper angle,  :sub:`($..et.etHopper.AN) no-sub`
   Drain diameter,  :sub:`($..et.etHopper.drain.ND) no-sub`


Trash Rack
==========

As the raw water flows from the first hopper to the subsequent ones, it must pass through two trash racks, preventing large debris from entering the treatment process. Having two trash racks allows the operator to remove one of the trash racks for cleaning. The trash racks are made of a frame and fishing line or other suitable material. The trash racks are designed to remove any particles that would be large enough to obstruct downstream processes. The smallest flow dimensions are the diffusers in the clarifier with a width of :sub:`($..inletManifold.diffuser.slotW) no-sub` and the orifices in the stacked rapid sand filter inlet branches with a diameter of :sub:`($..filter.fiPipes.branch.inlet.portD) no-sub`. The maximum spacing between the trashrack strings is :sub:`($..trashRack.Sm) no-sub`.

The trash rack area is sufficient such that the fractional clogging can be as high as :sub:`($..et.trashRack.PO_pi) no-sub` before exceeding the maximum available head loss of :sub:`($..et.trashRack.HL_max) no-sub` in the entrance tank.

.. _table_Trash_Rack_Specifications:

.. csv-table:: Trash Rack Specifications.
   :header: "Parameter", "value"
   :align: left
   :widths: 50 50
   :class: wraptable

   Channel width, :sub:`($..trashRack.W) no-sub`
   Trash rack height, :sub:`($..et.trashRack.L) no-sub`
   Fractional open area, :sub:`($..et.trashRack.PO) no-sub`
   Downstream water depth, :sub:`($..et.trashRack.downstreamHW) no-sub`
   Clean head loss, :sub:`($..et.trashRack.HL_min) no-sub`
   Maximum head loss, :sub:`($..et.trashRack.HL_max) no-sub`
   String diameter, :sub:`($..et.trashRack.Dm) no-sub`
   Open space between strings, :sub:`($..et.trashRack.Sm) no-sub`


Sediment and Grit Removal
=========================

The entrance tank has a capture velocity of :sub:`($..et.captureVm) no-sub` to remove particules that would otherwise settle in the bottom of the flocculator. Large particulates settle out in the hoppers, and collect near the drains at the bottom. 

The entrance tank length of :sub:`($..et.L) no-sub` corresponds to the clarifier tank length. The width, :sub:`($..et.W) no-sub`, ensurse the minimum desired capture velocity is met while still allowing enough space for a person to fit inside and construct the tank.

The :sub:`($..et.etHopper.N) no-sub` hoppers collect sand and grit that then slides to the bottom where the :sub:`($..et.etHopper.drain.ND) no-sub` inch nominal diameter drains are located. When too much sediment has accumulated, the drain pipes must be removed until the sludge is flushed out. Directly below the entrance tank, there is a drain channel that transfers the waste to the main plant drain channel.


.. include:: lfom.rst