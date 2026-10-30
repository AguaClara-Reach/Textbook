.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/AIDE/Specifications.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>


.. _title_AguaClara_Specifications:

************************
AguaClara Specifications
************************

This document specifies the design goals, the raw water quality parameters, and the design and construction requirements for an AguaClara drinking water treatment plant. The plant will produce safe, potable drinking water from a source water that may be contaminated with particles, pathogens, and dissolved organics.

AguaClara Plant Design Goals |20-80Lpsplant|
============================================

AguaClara drinking water treatment technologies remove turbidity and pathogens from raw water and to deactivate remaining pathogens before distribution. AguaClara technologies are best suited for centralized water treatment in communities of at least 200 people. AguaClara technologies would not be appropriate for treatment of low-turbidity groundwater where the primary contamination issues are chemical, such as nitrate, fluoride, or heavy metals. AguaClara technologies are gravity-driven and do not require electricity. When required by the topography, pumps can raise the source water to the elevation necessary for water treatment and water distribution.

AguaClara treatment technologies include trash and grit removal, flow measurement, chemical dosing, rapid mix, flocculation, floc filter, sedimentation, filtration, and disinfection. The  :ref:`floc filter <title_Clarification_Intro>` is a fluidized suspension of flocs located in the bottom of the clarifier.  An AguaClara treatment plant may be designed with all of these processes, or if raw water turbidity is consistently less than about 3 NTU, the treatment plant may be designed without flocculation, floc filter, and sedimentation.


Water Quality Parameters
------------------------

The tables below summarize the raw water quality parameters for which AguaClara treatment technologies are appropriate.

.. _table_Water_Quality_Parameters:

.. csv-table:: Water Quality Parameters Treated by AguaClara Plants
   :header: "Water Quality Parameter", "Comments"
   :align: left

   Turbidity, "Raw water with turbidity less than 600 NTU can consistently be treated to less than 1 NTU. Treatment of higher turbidities may require a customized clarifier design."
   "Color/Dissolved Organic Matter (DOM)", "For raw water with high color or total organic matter content, pilot studies are recommended to confirm the efficacy of the coagulant and the ability of the flocs to settle."
   pH, "pH can be lowered to prevent calcium carbonate scaling in distribution piping or increased to reduce corrosion potential."
   Microbiological contamination, "The AguaClara treatment processes are designed to remove pathogens through particle removal and deactivate pathogens through disinfection."

AguaClara plants are designed to treat the water quality parameters listed above. Some other contaminants may also be removed, but that must be verified by jar and/or pilot scale testing. All other parameters should be within acceptable ranges in the raw water or should be treated by other means.

Before beginning construction of an AguaClara treatment plant, bench-scale jar testing should be performed to confirm that polyaluminum chloride, aluminum sulfate, or another proposed coagulant is able to successfully form flocs that settle.

Entrance Tank |EntranceTank|
============================

For more detailed information see :ref:`Entrance Tank Design <title_entrance_tank_design>`. The entrance tank (see :numref:`figure_spec_ET_Diagram_Labeled`) has multiple functions in a drinking water treatment plant.

#. Remove air bubbles to reduce splashing, turbulence, and unsteady motion of the chemical feed surface tracking lever system
#. Remove grit to prevent accumulation in the flocculator
#. Remove leaves and other debris to prevent clogging of the diffusers in the clarifier inlet
#. Dissipate kinetic energy to keep the water level steady for accurate flow measurement
#. Measure the incoming flow rate with the Linear Flow Orifice Meter (LFOM) so that operators can make adjustments and respond to changes in water demand
#. Inject the coagulant and any other amendments required for flocculation

.. _figure_spec_ET_Diagram_Labeled:

.. figure:: ../Images/ET_Diagram_Labeled.png
    :width: 900px
    :align: center
    :alt: entrance tank diagram

    Cross-section of an entrance tank. Chemical dosing system not shown.

Grit Removal
------------

A. The entrance tank shall be designed as a horizontal flow sedimentation tank for the removal of grit with a recommended capture velocity of less than 15 mm/s.

#. The bottom of the entrance tank shall be a series of grit hoppers that can easily be cleaned by temporarily removing the pipe stub that blocks the outlet of each hopper.

Trash Rack
----------

A. The trash rack shall have an opening size that is smaller than the diffusers in the clarifier and the orifices in the stacked rapid sand filter inlet branches.

#. The trash rack area shall be sufficient such that it can be at least 80% clogged before exceeding the available head loss in the entrance tank.

Linear Flow Orifice Meter (LFOM) or Equivalent |LFOM|
-----------------------------------------------------

A. The plant entrance tank shall be equipped with a device that will result in a linear relationship between the plant flow and the water level in the entrance chamber. The Linear Flow Orifice Meter (LFOM), which has a pattern of orifices through which flow exits the entrance tank, is described below. An equivalent device, such as a Sutro weir, can also be used if demonstrated to function equivalently.

#. The pattern of orifices shall be designed so that the water level in the entrance chamber (equal to the hydrostatic head pushing water through the offices) is linearly proportional to the total flow through the orifices (equal to the plant flow). An example of an LFOM is shown in :numref:`figure_spec_LFOM`. The orifices may be drilled in a flat plate or in the walls of a vertical pipe.

#. At a minimum, the LFOM shall be capable of measuring flow ranging from 25 percent to 100 percent of the maximum plant design flow. If needed the lowest flow rate measured can be further reduced.

#. To ensure that plant flow is measured with adequate resolution the water level should change a minimum of 20 cm from no flow to the design flow rate. Larger water level changes can be used to enable use of smaller diameter LFOMs.

#. Depending on the plant flow, the LFOM may consist of orifices in one or multiple riser pipes or in a flat plate.

.. _figure_spec_LFOM:

.. figure:: ../Images/LFOM.png
    :width: 100px
    :align: center
    :alt: LFOM

    Example of a Linear Flow Orifice Meter


Chemical Dosing System
======================

For more detailed information see :ref:`Linear chemical dosing system <heading_linear_cdc>`.

Design Goals
------------

A. The system will be capable of dosing chemicals for the following purposes. All materials shall be compatible with the chemicals being dosed.

   1. Disinfectant (normally sodium or calcium hypochlorite)

   #. Coagulant (typically polyaluminum chloride [PACl], but other coagulants such as alum can be used if justification is provided. Bench-scale jar testing should be performed to confirm that the proposed coagulant is able to successfully form flocs.)

   #. pH adjustment (if necessary)

#. The chemical dosing system shall function by gravity and not depend on pumps or electrical power.

#. The chemical dosing shall be flow-paced, meaning that the rate of chemical application is automatically adjusted proportional to the flow rate of water moving through the plant.

#. The system shall be easily disassembled by the plant operator for cleaning, including with vinegar to remove calcium carbonate deposits.

#. The chemical dose (mass chemical per volume water passing through the plant) shall be easily adjustable by the plant operator.


Chemical Storage
----------------

A. For each chemical, the plant shall include two or more storage tanks. The tank and fitting materials shall be compatible with the chemical. Storage tanks can be plastic or concrete, as long as they are confirmed to be compatible with the chemical being stored.

#. The combined volume of all tanks used for a chemical shall allow for storage of sufficient chemical to supply the plant at maximum flow and maximum chemical dose for at least 48 hours.

Chemical Feed System
--------------------

The plant shall be equipped with a chemical feed system configured as shown in :numref:`figure_spec_chemDoseController`. Materials that will be in contact with chemicals must be compatible with the chemical and suitable for use with potable water.

.. _figure_spec_chemDoseController:

.. figure:: ../Images/CDC_derivation.png
    :width: 500px
    :align: center
    :alt: chemDoseController

    Gravity powered chemical feed system schematic.

A. Constant Level Tank

   1. From the chemical storage tanks, the chemical passes via gravity to a constant level tank (see :numref:`figure_spec_constantLevelTank`). The chemical enters the constant level tank via a float valve, which maintains a constant level of chemical, providing a constant head to drive the chemical through the doser.

   #. The chemical level in the constant level tank shall be level with the fulcrum of the dosing lever.

   #. The vertical distance from the constant level tank level to the end of the dosing hose at max flow and max dose shall be 20 cm.


.. _figure_spec_constantLevelTank:

.. figure:: ../Images/CLT.png
    :width: 600px
    :align: center
    :alt: Constant Level Tank

    Constant level tank module for coagulant and chlorine.

B. Dosing Tubes

   1. Chemical flows from the constant level tank into dosing tubes, which terminate in a free discharge at the dose slider on the doser lever.

   #. The diameter of the tubes shall be designed to provide laminar flow over the desired range of chemical flows. Given the laminar flow, the flowrate through the dosing tubes will be directly proportional to elevation difference between the chemical level in the constant level tank and the dose slider.

   #. The plant shall have a spare set of dosing tubes on hand for each chemical feed so that one set of tubes can be cleaned while the other set is in use.

   #. Head loss through all other tubes and fittings connecting the constant level tank to the free discharge at the dose slide shall be less than 5% of the head loss through the dosing tubes.

#. Chemical Dose Controller |Doser|

   1. One end of the chemical dose controller (see :numref:`figure_spec_doser`) is connected to a float in the plant entrance tank. The dose slider and thus the ends of the doser hoses are located on the other end of the chemical dose controller lever.

   #. The lever on the float side shall be at least two times as long as the LFOM change in water depth (typically 20 cm) to provide a reasonable maximum angle of the lever system.

.. _figure_spec_doser:

.. figure:: ../Images/doser.png
    :width: 500px
    :align: center
    :alt: Doser

    Chemical dose controller designed for two independent chemical feeds.


D. Function

   1. The doser is designed so that the operator can select a chemical dose (mass of chemical per volume of water) by moving the dose slider to a specific position along the lever. The lever, LFOM and constant level tank then work together to adjust the chemical flow proportional to the plant flow to maintain a constant chemical dose.

   #. When the plant flow is zero, the lever is horizontal and chemical flow is zero.

   #. When plant flow increases, the water level in the entrance tank increases (due additional head loss through the LFOM), causing one end of the doser lever to rise. This, in turn, causes the other end of the lever, and the dose slider, to fall, increasing the elevation difference between the chemical level in the constant level tank and the dose slider. The greater driving head increases the chemical flow through the doser.

   #. The water level in the entrance tank level is directly proportional to the plant flow rate (due to the LFOM). The dose slider elevation is directly proportional to the entrance tank water level. The chemical flow is directly proportional to the dose slider elevation. Therefore the chemical flow is directly proportional to the plant flow and changes in the slider position directly set the chemical dose.


Flocculator
===========

For more detailed information see :ref:`Flocculation Design <title_Flocculation_Design>`. AguaClara flocculators have three potential flow patterns (see :numref:`figure_spec_flocculator_Geometry`) depending on the flow rate, plant layout, and velocity gradient. There is overlap between the different flow geometries and ongoing work to assess how to select the best type of flocculator given a flow that could be handled by two different types.

The flocculator geometries are specified by two flow directions. The first direction is the flow direction in a channel from the channel inlet to the channel outlet. The second direction is the flow direction around a baffle.

#. |FlocculatorVH| Vertical - Horizontal: Plant design flows between about 0.5 L/s and 20 L/s. See :numref:`figure_VHflocculator`.

#. |FlocculatorHV| Horizontal - Vertical: Plant design flows between about 3 and 200 L/s. See :numref:`figure_HVflocculator`. This geometry is also referred to as over-under.

#. |FlocculatorHH| Horizontal - Horizontal: Plant design flows above about 100 L/s. See :numref:`figure_HHflocculator`. This geometry is also referred to as around-the-end.

.. _figure_spec_flocculator_Geometry:

.. figure:: ../Images/flocculator_Geometry.png
  :align: center
  :width: 500px
  :alt:  3 flocculator geometries

  The optimal flocculator geometry transitions as the flow rate increases. Note that each of these flocculators has approximately the same depth.

Design Goals
------------

The AguaClara flocculator is designed with the following goals:

A. Provide a velocity gradient and residence time allowing aggregation of individual particles and small flocs into flocs large enough to settle out in the clarifier. The product of velocity gradient (G) and residence time (ϴ) is a dimensionless number known as collision potential or Gϴ.

#. Set the retention time to reach a design Gϴ of approximately 35,000. This determines the minimum total volume of the flocculator. The design volume of the flocculator may be larger due to construction constraints, such as making the length of the flocculator the same as the length of the clarifier bays or keeping the flocculator channels wide enough to fit a human body for ease of cleaning and maintenance. 

#. Minimize “dead zones” in the flocculator and reduce the opportunity for short circuiting of the flocculator.

#. Facilitate the draining of sludge and maintenance manually by one person

Flow Paths
----------

A. The length of the flocculator channels is typically determined by the length of the clarifier to create a compact plant layout.

#. The width of each flocculation channel is determined by material constraints and to facilitate cleaning and maintenance. The flocculator baffles are made of polycarbonate sheets, so the width of the channel should be no larger than the width of a polycarbonate sheet. The width of the channel should be no smaller than 50 cm so an operator can safely enter the tank. Large plants treating more than about 200 L/s may be designed with horizontal flocculation channels and may use ferrocement baffles.

#. The depth of the flocculation channels is determined by construction constraints and to minimize the plan view area of the flocculators and thus the plant. Typically the flocculator and clarifier share the same slab.

#. The overall volume of the flocculator is determined by the individual constraints on each dimension of the flocculator, but the collision potential, Gϴ, of the flocculator must be at least 35,000 at the plant design flow.

#. The spacing between baffles is designed to achieve the target velocity gradient, G, at the design flow rate.

#. The ports between flocculator channels (see :numref:`figure_flocChannelPort` should be designed with the same flow area as the space between the baffles so that the port improves flocculation without breaking flocs. The width of the port is equal to the spacing between baffles and the height of the port is equal to the channel width.

.. _figure_flocChannelPort:

.. figure:: ../Images/flocChannelPort.png
  :align: center
  :width: 500px
  :alt:  ports

  Flocculator with end and side walls removed to show the port between channels. Water flows between flocculator channels through a port that has the same flow dimensions as the space between baffles.

Channel Construction
--------------------

A. The walls of the flocculation channels should be vertical, maintaining the channel width along both the length and height of each flocculator channel.

#. The drain pipes are activated by removing a vertical pipe stub. The drain pipes must be large enough to empty the flocculation channels in 20 minutes. The drains are placed near a port between channels so that each drain can serve two channels.

#. The flocculator should have sufficient lighting for the operator to observe floc formation. The operator should also have a flashlight to observe floc formation during power outages.

Baffles
-------

A. The flocculation baffles must be constructed to be removable. A baffle module (see :numref:`figure_spec_baffleModule`) should be raisable by one operator working alone so that water can flow beneath the baffle and drain from the flocculator channel. Large flocculators may have baffle modules that require more than one person to completely remove from the flocculator channel.

#. The flocculation baffles should be constructed from polycarbonate sheets, and the frame for holding together baffle modules should be made from PVC pipe. Other materials may be used if justification is provided, including the use of ferrocement baffles for horizontal flocculators in large plants.

#. The width of each baffle should be approximately 5 millimeters wider than the channel width so they deform slightly and created a tighter seal with the channel wall.


.. _figure_spec_baffleModule:

.. figure:: ../Images/baffleModule.png
  :align: center
  :width: 500px
  :alt:  Baffle Module

  The baffle modules transfer the force of the water to the downstream wall through the PVC pipe frame. Each flocculator channels holds one baffle module.


Clarifier |Clarifier|
=====================

For more detailed information see :ref:`Clarifier Design <title_Clarifier_Design>`. The clarifier (see :numref:`figure_spec_clarifierElevation`) contains three separate processes: filtration in the floc filter, sedimentation in the plate settlers, and consolidation in the floc hopper.

The clarifier must be designed based on the coldest water temperature and based on the lowest density primary particles that will need to be captured. Surface waters with high concentrations of dissolved organic matter and low concentrations of suspended solids produce low density flocs and thus the velocity gradient in the inlet manifold and jet reverser must be reduced. In some cases it may also be necessary to reduce the floc filter upflow velocity and plate settler capture velocity by increasing the clarifier plan view area.

.. _figure_spec_clarifierElevation:

.. figure:: ../Images/clarifierElevation.png
  :align: center
  :width: 500px
  :alt:  Clarifier Elevation view

  Elevation view of a clarifier bay showing location of the floc filter, plate settlers, and floc hopper.

The clarifier may have multiple bays (see :numref:`figure_clarifier_with_4_bays`) that work in parallel to treat the required plant flow.


.. _figure_clarifier_with_4_bays:

.. figure:: ../Images/clarifier_with_4_bays.png
  :align: center
  :width: 500px
  :alt:  Clarifier showing 4 bays

  Clarifier with four bays. Each bay has its own inlet, outlet, floc filter, plate settlers, and floc hopper so that a bay can be taken offline while the other bays continue to operate.

Design Goals
------------

The high-rate, vertical flow clarifier is designed with the following goals:

A. To deliver flocs to the clarifier bay without breaking them into pieces with terminal velocities below the capture velocity of the plate settlers. This sets the maximum velocity gradient for the transfer of the flocs from the flocculator to the floc filter in the clarifier bay. The maximum velocity gradient shall be less than 250 Hz. Lower values will be required for raw waters with high concentrations of dissolved organic matter.

#. To provide a mechanism for the operator to dump poorly flocculated water before it enters the clarifier. This is important to reduce the recovery time when there is a flocculation failure.

#. To produce a stable floc filter (fluidized suspension of flocs) that reduces the clarified water turbidity.

#. To provide evenly distributed low-velocity flow through the plate settlers.

#. To prevent accumulation of sludge that would tend to become anaerobic and release both dissolved organics (taste and odor issues) and methane bubbles that would carry flocs to the top of the clarifier.

#. To remove the solids without requiring power or moving mechanical parts.

#. To ensure easy operation and maintenance.

#. To be able to take any clarifier bay offline for maintenance while the other clarifier bays continue to operate.

#. To be able to refill a clarifier bay with clarified water for rapid return to service.


Inlet Channel
-------------

The inlet channel (see :numref:`figure_spec_ClarifierInletOutletHydraulics`) is designed to have a velocity head that is very small compared with the head loss in the outlet manifold orifices to achieve uniform flow distribution between clarifier bays. The inlet channel is sloped up in the direction of flow to maintain relatively uniform velocity for improved flow distribution and to reduce floc deposition in the channel.

.. _figure_spec_ClarifierInletOutletHydraulics:

.. figure:: ../Images/ClarifierInletOutletHydraulics.png
  :align: center
  :width: 500px
  :alt:  Clarifier Inlet Outlet Hydraulics

  Flocculated water flows from the inlet channel to the inlet manifold and then through the diffusers, jet reverser, floc filter, and plate settlers. Clarified water flows into the outlet manifold, the collector channel, across the outlet weir, and into the outlet channel.

Inlet Manifold
--------------

Flocculated water enters a pipe in the bottom of the inlet channel. Water flows down the pipe, through a 90-degree elbow, into the inlet manifold. Water exits the inlet manifold through a series of orifices and diffusers in the bottom of the pipe. The end of the inlet manifold is capped. The minimum diameter of the inlet manifold is set by the velocity gradient downstream of the 90-degree elbow (see Equation :eq:`D_pipe_min_of_K_and_jet_G_max`).

Achieving reasonable flow distribution between diffusers may require a flow equalization chamber inside the inlet manifold (see :numref:`figure_2stageInletManifold`).

Diffusers
---------

The orifices and diffusers point down to the bottom of the clarifier bay and extend along the length of the pipe at regular intervals to ensure that water is evenly distributed within the bay. Diffusers are designed to ensure that the jet exiting the jet reverser has a maximum velocity gradient that is less than the design constraint to prevent excessive floc breakup (see Equation :eq:`planejet_v_max_of_q`).

Diffusers are shaped so that one end is molded to be a reduced diameter that fits into the influent manifold port, and the other end is deformed to the shape of a rectangle (:numref:`figure_spec_diffuser_dimensions`). This deformation is done to create a line jet entering the jet reverser in the bottom of the clarifier bay and to enhance flow distribution by maximizing the jet velocity given the constraints of Equation :eq:`planejet_v_max_of_q`.

.. _figure_spec_diffuser_dimensions:

.. figure:: ../Images/diffuser_dimensions.png
   :width: 500px
   :align: center
   :alt: Diffuser dimension definition

   Dimensions and geometry of a diffuser. The first image at the left shows a view of a diffuser from the end of a clarifier bay. The second image shows a view of a diffuser from the side of a clarifier bay.

Jet Reverser
------------

The jet reverser consists of a longitudinally-cut half-pipe that is laid in the bottom of the bay (see :numref:`figure_spec_clarifierEndView`). It functions as a way to keep flocs suspended in the clarifier by ensuring that any sludge that settles will be propelled back up by the force of the diffuser jet.

The diffusers are offset from the jet reverser centerline. This is intentionally done to promote the resuspension of flocs, which form a floc filter for primary filtration.

.. _figure_spec_clarifierEndView:

.. figure:: ../Images/clarifierEndView.png
   :width: 500px
   :align: center
   :alt: Clarifier showing jet reverser

   End view of a clarifier bay showing the sloped bottom, inlet manifold, diffusers, and jet reverser. The diffusers direct a jet of water into one side of the jet reverser.

Floc Filter (Floc Blanket)
--------------------------

Floc filters significantly improve the performance of a clarifier and reduce the clarified water turbidity.

A. The line jet from the diffusers enters the jet reverser to force flow up through the clarifier bay. The vertical upward jet momentum is used to resuspend flocs that have settled to the bottom of the clarifier bay. The resuspended flocs form a fluidized bed which is a floc filter. Small particles are captured by the flocs in the floc filter as the small particles flow into a floc.  The bed is fluidized because flocs are kept in suspension by the upflowing water.

#. Clarifiers use an upflow velocity of 1 mm/s in the floc filter. This velocity is measured above the sloped bottom in the section of the clarifier bay with vertical walls.

#. For a floc filter to form, a clarifier requires that:

   1. The plate settlers capture small flocs and cause them to aggregate into larger flocs as they avalanche back into the floc filter zone. The increased terminal velocity of the larger flocs enables them to create a stable floc filter.

   #. All settled flocs are resuspended by the vertical jet of water exiting the jet reverser.

Sloped Bottom Geometry
----------------------

The clarifier bottom geometry (see :numref:`figure_spec_clarifierEndView`) prevents sludge accumulation while also ensuring good flow distribution. The slope on either side of the diffusers is at a 50 degree angle above horizontal. The bottom geometry allows for smooth flow expansion to the entire plan view area of the bay, and ensures that all flocs that settle are transported to the jet reverser. The diffusers do not touch the bottom of the tank so that flocs on both sides of the diffuser can return to the jet reverser for resuspension. Thus, there is no accumulation of settled flocs in the main clarifier bays.

Floc Hopper
-----------

The floc hopper (:numref:`figure_spec_flocHopper`) provides an opportunity for floc consolidation. The floc weir controls the depth of the floc filter because as the floc filter grows, it will eventually reach the top of the floc weir. Because flocs are more dense than water, the flocs “spill” over the edge of the floc weir which allows the floc filter to stay a constant height while sludge accumulates and consolidates in the floc hopper. Operators can use a flashlight to observe the floc filter moving into the lower end of the plate settlers indicating that the floc hopper is full. The sludge is drained from the floc hopper by opening a valve. The operator can observe that the sludge has completely drained from the floc hopper by the clarity of the water exiting from the drain valve.

The floc hopper allows for a self-cleaning clarifier. Operators only have to clean the clarifier once every three to six months because there is no stagnant accumulation of anoxic sludge.

.. _figure_spec_flocHopper:

.. figure:: ../Images/flocHopper.png
   :width: 400px
   :align: center
   :alt: Floc Hopper

   The floc hopper is located beneath the inlet and outlet channels. Flocs enter the hopper by flowing over the floc weir. Sludge is drained from the bottom of the hopper.

Plate Settlers
--------------

After flowing through the floc filter, flocs reach the plate settlers. Plate settlers are sloped surfaces that provide additional settling area for flocs, thereby increasing the effective settling area of the clarifier without increasing the plan view area. AguaClara plate settlers are sloped at 60 degrees. The spacing between plates is 2.5 cm.

The plate settlers are made from clear polycarbonate sheets. The sheets are assembled in modules (see :numref:`figure_spec_plateSettlerModule`). The modules are light enough to be removed from the clarifier by hand. The plate settler modules are supported by ledges along the clarifier bay walls and by a PVC pipe frame.

.. _figure_spec_plateSettlerModule:

.. figure:: ../Images/plateSettlerModule.png
   :width: 300px
   :align: center
   :alt: Plate settler module

   Plate settler module assembled from polycarbonate sheets and PVC piping. 


.. _table_Plate_Settler:

.. csv-table:: Plate Settler Design Parameters
   :header: Parameter, Determined by:, Determines , Value
   :align: left

   Upflow velocity, Floc blanket,Plan view area of tank, 1 mm/s maximum value
   Capture velocity, Target turbidity, Particle size distribution, 0.12 mm/s maximum value
   Plate angle, Self-cleaning requirement, Plate settler length, 60 deg
   Plate spacing, Clogging and floc rollup constraints, Plate settler length, 2.5 cm
   Plate settler length, "Upflow velocity, Capture velocity, Plate angle, Plate spacing ", Tank depth, Calculated for each plant


Submerged Outlet Manifold
---------------------------

The submerged outlet manifold, sometimes called a launder, collects clarified water from the top of the clarifier. It is a horizontal pipe that extends along the length of the clarifier bay and is located above the plate settlers but below the surface of the water. The submerged pipe has orifices drilled into its top; water enters the pipe through the orifices and the pipe leads out of the clarifier bay.

The outlet manifold is designed to generate 5 cm of head loss to ensure uniform flow distribution between clarifier bays and to have the majority of the head loss through the orifices to obtain uniform flow distribution between the orifices.

Outlet Weir
-----------

The submerged outlet manifold transports water from the clarifier bay to a collector channel that runs perpendicular to the clarifier bays (see :numref:`figure_spec_diffuser_dimensions`). All of the clarifier bay outlet manifolds deliver the clarified water to the collector channel. Water leaves the collector channel by flowing over the outlet weir. The elevation of the outlet weir controls the water levels in the clarifier and in the flocculator. The outlet weir does not need to be adjustable and small elevation errors are accommodated because water can flow in the collector channel with less head loss than the orifice head loss.

The outlet weir makes it possible to refill and empty individual clarifier bays with clarified water to ensure that after returning a clarifier bay to service the first water is of high quality.

Outlet Channel
--------------

After the water flows over the outlet weir, it is collected in the outlet channel. The water can be transported from the clarifier outlet channel to the filter inlet channel by pipes or by a channel.

Stacked Rapid Sand Filter |OStaRS|
==================================

For more detailed information see :ref:`Filtration Design <title_Filtration_Design>`. Stacked Rapid Sand, StaRS, filters (see :numref:`figure_spec_OStaRSoverview`) were invented in 2010 by the AguaClara Cornell program in response to the need for a new technology that would both eliminate the need for backwash pumps and not require the construction of 6 filters for small towns. As shown in :numref:`figure_spec_OStaRSfilterMode`, StaRS filters use six 20 cm deep layers of sand with the layers stacked vertically. The six layers give a total active sand depth of 1.2 m.

.. _figure_spec_OStaRSoverview:

.. figure:: ../Images/OStaRSoverview.png
   :width: 500px
   :align: center
   :alt: Floc Hopper

   The open stacked rapid sand filters include advanced hydraulic controls to ensure stable operation during both filtration and backwash modes.

Operation
---------

A. The filter operates with the same design flow rate for both filtration (see :numref:`figure_spec_OStaRSfilterMode`) and backwash (see :numref:`figure_spec_OStaRSbackwashMode`) modes and uses clarified water for backwash. This eliminates the need for backwash pumps and ensures that the filters can be backwashed as long as clarified water is available.

.. _figure_spec_OStaRSfilterMode:

.. figure:: ../Images/OStaRSfilterMode.png
   :width: 500px
   :align: center
   :alt: OStaRS filtration mode

   In filtration mode the flow divides between the six sand layers. The six sand layers operate in parallel during filtration.


.. _figure_spec_OStaRSbackwashMode:

.. figure:: ../Images/OStaRSbackwashMode.png
   :width: 500px
   :align: center
   :alt: OStaRS backwash mode

   In backwash mode all of the flow enters at the bottom of the filter box and flows up through the six sand layers. The six sand layers operate in series during backwash.


Design Goals
------------

A. Stacked Rapid Sand (StaRS) filters were developed to eliminate the need for backwash pumps and minimize the plan area required.

#. The filters should be designed so that the process of emptying the sand from the filter, removing the modules, cleaning the modules, replacing the modules, and replacing the sand is as easy as possible.

#. During backwash, all outlets and all inlets besides the bottom most inlet must be hydraulically isolated so all flow enters through the bottom inlet and flows out through the backwash siphon pipe.

#. The plant shall have a minimum of two StaRS filters so that one of the StaRS filters can be in operation while the other is offline for maintenance or repairs.

Configurations
--------------

A. Open StaRS (OStaRS) with 6 filter layers - used for flow rates greater than about 20 L/s. The minimum OStaRS flow rate is set by the minimum dimensions of the filter box that can be constructed and that enable filter maintenance.

#. Open StaRS (OStaRS) with 2 filter layers - used for flow between about 3 and 12 L/s. This technology is under development.

#. Enclosed StaRS (EStaRS) filters - used for lower flow rates. This technology is under development

   1. Can be located on the same slab as the clarifier and flocculator because the EStaRS is operated under vacuum in backwash mode to achieve the necessary head for fluidizing the sand.
   #. Assembled using PVC pipe as the body of the filter
   #. Inner plumbing accessed through openings in the top and bottom of the main filter body

Sand Specification
------------------

StaRS filters use (6) six 20 cm deep layers of silica sand (no dual-media required) with the layers stacked vertically. The six layers give an active sand depth of 1.2 m. The grain size is 0.45 to 0.55 mm.

Filter Modules
--------------

The sand layers are contiguous and the only distinction between layers is the direction of flow during filtration. Each layer of sand sits in between an inlet and outlet filter module. Each module consists of a large diameter trunk inlet/outlet pipe, which connects to a row of smaller branch pipes. The branch pipes are supported along the filter walls by receptor pipes.

The filter modules are anchored to the concrete slab to prevent uplift at the transition to backwash. The uplift forces are considerable and are detailed in :ref:`Backwash Initiation Forces <heading_StaRS_Backwash_Forces>`.

A. Inlet Filter Module

   1. Small holes (orifices) are drilled into the inlet branches (see :numref:`figure_spec_OStaRSinletBranches`). The orifice diameter is selected based on constructability and not being too small to risk clogging (between 4 and 10 mm).

   #. During filtration mode, water flows into the inlet filter modules through the inlet trunk and into the branches. Water flows out of the branches through small holes, into the space created by the wing, and then into the sand.

   #. During the transition from the backwash to filtration modes, a small volume of water flows back into the inlet pipes. The “wings,” PVC pipes cut longitudinally, are affixed to the inlet branches to prevent sand from flowing into the inlet pipe. Wings are only included on the inlet filter modules.

#. Outlet Filter Module

   1. The slots in the outlet branches (see :numref:`figure_spec_OStaRSoutletBranches`) are small enough to prevent sand from passing through. The filter modules shall be adequately supported to limit deflection of any of the module pipes to 2 millimeters or less to prevent significant opening or closing of the slots.

   #. During filtration mode, water flows from the filter media into the slots and then through the branches and into the trunk pipes.

   #. During backwash mode, the outlet trunks are closed or isolated and water does not flow through the outlet modules.

.. _figure_spec_OStaRSinternalPiping:

.. figure:: ../Images/OStaRSinternalPiping.png
   :width: 500px
   :align: center
   :alt: OStaRS internal piping

   The seven filter modules stack inside the filter box. Each module is held together using band clamps. The only pipe connections that are glued in the filter modules are the end caps on the trunks and receptors.

.. _figure_spec_OStaRSinletBranches:

.. figure:: ../Images/OStaRSinletBranches.png
   :width: 500px
   :align: center
   :alt: OStaRS inlet branch

   The inlet branches use orifices to obtain uniform flow distribution and a wing system to prevent sand from entering into the branches during backwash and filter mode transitions.

.. _figure_spec_OStaRSoutletBranches:

.. figure:: ../Images/OStaRSoutletBranches.png
   :width: 500px
   :align: center
   :alt: OStaRS outlet branch

   The outlet branches use 0.2 mm slots to keep the sand in the filter bed.


Backwash Siphon
---------------

The siphon should be designed so the airlock can hold the water in the filter box at least until the filter reaches the design maximum head loss. Backwash is initiated when the operator briefly opens a small diameter air release valve to remove the trapped air from the siphon pipe. The siphon diameter must be sufficient to lower the water in the filter at an average velocity that is equal to or exceeds the backwash velocity.

Backwash Flow Control Weirs
---------------------------

A. The backwash gate (see :numref:`figure_spec_OStaRShydraulicControls`) ensures there is adequate flow to backwash one filter as long as there is at least that much flow entering the plant. This is important because many water treatment plants operate under reduced flow during the dry season.

#. Removing the backwash gate in front of the desired backwash filter will create the desired backwash flow rate for the filter, while evenly distributing the remaining flow rate to the other filters. By removing the backwash gate the flow control for that filter is shifted from the wide weir to the slot weir.

#. The slot weir sets the backwash flow rate and ensures that the backwash flow doesn't cause sand loss by expanding the sand bed excessively. The slot weir can be partially filled at plant commissioning to reduce the maximum backwash flow if needed.

.. _figure_spec_OStaRShydraulicControls:

.. figure:: ../Images/OStaRShydraulicControls.png
   :width: 500px
   :align: center
   :alt: OStaRS hydraulic controls

   The hydraulic controls give the operator full control of filter operation while ensuring that the flow is distributed evenly between filters in filtration mode and that a filter in backwash mode receives the correct backwash flow rate.


Sand Dump
---------

The sand dump is critical for StaRS filters because the filter bed piping would make manual removal very difficult.

A. A sand dump pipe shall be installed in the filter box to allow for the filter media to be removed when the filter is in backwash mode and the sand bed is fluidized.

#. The sand dump pipe must be designed so that the sand doesn’t collect at one location in the pipe and cause a clog when the flow of the sand slurry is stopped. This requirement is met by using a single straight pipe with a slope less than the angle of repose of sand in water.

#. The sand dump velocity shall be at least 3 m/s to prevent the sand from settling in the sand dump pipe during operation.

#. The sand dump is activated by removing a clamp on connector and cap assembly from the end of the pipe.



.. _figure_spec_OStaRSsandDump:

.. figure:: ../Images/OStaRSsandDump.png
   :width: 500px
   :align: center
   :alt: OStaRS sand dump

   The sand dump is straight to prevent sand blockages and to minimize head loss.

Backwash Recycle
----------------

Backwash recycle is recommended for all communities where low flow conditions are likely to require water rationing. The backwash water storage tank is designed to hold the flow from one backwash event. A centrifugal pump can then be used to meter the water back to the entrance tank at a flow rate that empties the backwash water storage tank before the next filter needs to be backwashed.

In the event of a power failure the backwash recycle system will instead use backwash to waste to dispose of the spent backwash filter water.

Disinfection
============

Sodium or calcium hypochlorite is metered into the filtered water as it exits the filter hydraulic controls and enters the pipe that carries the water to a chlorine contact tank or directly to the community distribution tank. The chlorine is added after the previous treatment processes to reduce the production of disinfection byproducts and to enable biofiltration. The chlorine concentration is set by adjusting the position of the slider on the doser (see :numref:`figure_spec_doser`).


.. |LFOM| image:: https://cad.onshape.com/api/thumbnails/d/49035a16b895fd8095d17a02/w/b76e9410efc3d9f5861e9516/s/300x170
  :width: 100
  :target: https://cad.onshape.com/documents/49035a16b895fd8095d17a02/w/b76e9410efc3d9f5861e9516/e/c063acb14de8f1f558b02d2d?configuration=HL_min%3D0.2%2Bmeter%3BND_max%3D12.0%3BQm_max%3D5.0%3BTEMP_min%3D10.0%3BdrillD_max%3D0.1%2Bmeter%3BprintParams%3Dfalse&renderMode=0&uiState=626fea458d39dd1e3b6106e1

.. |Doser| image:: https://cad.onshape.com/api/thumbnails/d/e71bb0c05d9e7241822776b7/w/533d9612b07de271291829dc/s/300x170
  :width: 100
  :target: https://cad.onshape.com/documents/e71bb0c05d9e7241822776b7/w/533d9612b07de271291829dc/e/20f111b627e4c6d59c3f0ff9?configuration=HL_max%3D0.2%2Bmeter%3BQ_pi%3D1.0%3BchlorineC_pi%3D0.6%3BcoagC_pi%3D0.5%3BprintParams%3Dfalse%3Brep%3Dtrue%3BtankOW%3D1.0%2Bmeter&renderMode=0&uiState=6273e0ecd685467dff5c17c4

.. |EntranceTank| image:: https://cad.onshape.com/api/thumbnails/d/4c47a124da3abec33e0ce813/w/3955cd0d266daedd3eabf165/s/300x170
  :width: 100
  :target: https://cad.onshape.com/documents/4c47a124da3abec33e0ce813/w/3955cd0d266daedd3eabf165/e/bcf152c5be02d9ab5b2b5285?configuration=L%3D8.0%2Bmeter%3BQm_max%3D40.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D10.0%3BcaptureVm%3D20.0%3BflocUpstreamHW%3D2.0%2Bmeter%3BprintParams%3Dfalse%3Brep%3Dtrue&renderMode=0&uiState=626fea87ee1eae4ff2291321


.. |FlocculatorVH| image:: https://cad.onshape.com/api/thumbnails/d/673077f4fa843a817d4cd55d/w/8bd189f4769c2a64aa07a8c0/s/300x170
  :width: 100
  :target: https://cad.onshape.com/documents/673077f4fa843a817d4cd55d/w/8bd189f4769c2a64aa07a8c0/e/cdc0c6cfa0e8b64f179ced51?configuration=GT_min%3D35000.0%3BG_bod%3D50.0%3BQm_max%3D1.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D5.0%3BoutletHW%3D1.7%2Bmeter%3BprintParams%3Dfalse%3Brep%3Dtrue&renderMode=0&uiState=626feb5ffb767608344ad1ad

.. |FlocculatorHV| image:: https://cad.onshape.com/api/thumbnails/d/9742e8c019b742df4ae4db85/w/cbe4d0f58d318c45281687ae/s/300x170
  :width: 100
  :target: https://cad.onshape.com/documents/9742e8c019b742df4ae4db85/w/cbe4d0f58d318c45281687ae/e/05162587e7127122572d3a10?configuration=GT_min%3D35000.0%3BG_bod%3D50.0%3BL%3D6.0%2Bmeter%3BQm_max%3D30.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D25.0%3BoutletHW%3D2.0%2Bmeter%3BprintParams%3Dfalse%3Brep%3Dtrue&renderMode=0&uiState=626feb168bd195153bbbe9af

.. |FlocculatorHH| image:: https://cad.onshape.com/api/thumbnails/d/84c4c94f9773b67506cd35bb/w/58a1f53fe5ebbbbc808a3541/s/300x170
  :width: 100
  :target: https://cad.onshape.com/documents/84c4c94f9773b67506cd35bb/w/58a1f53fe5ebbbbc808a3541/e/aa5906755ba02b0a3925ec10?configuration=GT_min%3D35000.0%3BG_bod%3D50.0%3BQm_max%3D200.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D0.0%3BoutletHW%3D3.0%2Bmeter%3BprintParams%3Dfalse%3Brep%3Dtrue&renderMode=0&uiState=626fead687c54745ef4c039f

.. |Clarifier| image:: https://cad.onshape.com/api/thumbnails/d/e05915c533ee7568c402981a/w/56de4202f426e6443151ca07/s/300x170
  :width: 100
  :target: https://cad.onshape.com/documents/e05915c533ee7568c402981a/w/56de4202f426e6443151ca07/e/3f94eabd115787bc33ae755d?configuration=G_max%3D140.0%3BQm_max%3D20.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D10.0%3BcaptureVm%3D0.12%3BprintParams%3Dfalse%3Brep%3Dtrue%3BrepBayInternals%3Dfalse%3BupVm%3D1.0&renderMode=0&uiState=627688ef04309300574a09f6

.. |OStaRS| image:: https://cad.onshape.com/api/thumbnails/d/8a1a990f01575e6e5eed1922/w/3811cfb89da77b076395fdc0/s/300x170
  :width: 100
  :target: https://cad.onshape.com/documents/8a1a990f01575e6e5eed1922/w/3811cfb89da77b076395fdc0/e/fd576f076cd3757b426c7f20?configuration=Qm_max%3D20.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D10.0%3BfilterHL_pi%3D0.5%3BfilterMode%3Dfalse%3BprintParams%3Dfalse%3Brep%3Dtrue%3BrepBayInternals%3Dfalse%3BrepInternalPiping%3Dfalse%3BspareFilter%3Dfalse&renderMode=0&uiState=6276885764a43e34bd8c13b9

.. |20-80Lpsplant| image:: https://cad.onshape.com/api/thumbnails/d/0e9ede93e11e5a54f68f8606/w/2744164cc6e56e3693a3190f/s/300x170
  :width: 100
  :target: https://cad.onshape.com/documents/0e9ede93e11e5a54f68f8606/w/2744164cc6e56e3693a3190f/e/723e9e9d93f3008c9815e2d6?configuration=Qm_max%3D40.0%3BShow_Internal_Components%3Dfalse%3BTEMP_min%3D10.0%3BprintParams%3Dfalse%3Brep%3Dfalse&renderMode=0&uiState=626fedaca473381cd632eede

.. |ACRlogowithname| image:: ../Images/ACRlogowithname.png
  :target: https://www.aguaclarareach.org/
  :height: 50
