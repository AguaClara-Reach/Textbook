.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Fluids_and_Hydraulics/Manifold_Hydraulics.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_plant_hydraulics:

****************
Plant Hydraulics
****************

Pipes that carry the plant flow rate are used for:

 * source water from the surface water
 * linear flow orifice meter and connecting pipe from the entrance tank to the flocculator
 * bypass the plant taking the water from the entrance tank (by moving the linear flow orifice meter to the bypass socket) to the filter outlet tank where it is chlorinated
 * clarified water to filters
 * recycle backwash water to the entrance tank
 * filtered water to distribution tank

Minor losses dominate the head loss in most pipes in a water treatment plant. An exception is the dosing tubes that are specifically designed to have major losses dominate. We can solve the minor loss Equation, :eq:`minor_loss` for the maximum velocity in a pipe given a constraint of head loss and the sum of the minor loss coefficients.

.. math::
  :label: v_max_minor_losses

  \bar v_{max}^2 = \sqrt{\frac{2gh_{e_{max}}}{K_e}}

This calculations for the maximum velocities for different sections of the plant piping are in the `PipeMap Onshape document <https://cad.onshape.com/documents/feb8f8b15585d57ecb0091f2/w/11145594f45115d4e255d7ae/e/b3519c65bc0794966e96cb8e>`_.

Kawamura :cite:`plantHydraulics-kawamura2000integrated` recommends maximum velocities of about 2 m/s except where floc breakup is a concern. He also recommends that the plant hydraulics be designed to handle 1.2 to 1.5 of the plant design flow rate. If we use the less conservative factor we obtain a maximum plant pipe velocity of 1.7 m/s.

The bypass line requires a careful design because the elevation difference is slightly greater than 1 m and contains an entrance (K = 0.5), 6 elbows (K = 0.9), and an exit (K = 1). The minor loss equation gives a maximum velocity of 1.7 m/s without any additional safety factor.

The linear flow orifice (LFOM) is sized based on a maximum velocity of Equation :eq:`LFOM_V_max`. For the AguaClara standard LFOM head loss of 20 cm the maximum velocity is 0.84 m/s. With a safety factor of 1.2 this results in a maximum velocity of 0.7 m/s. Thus the LFOM requires a larger diameter pipe than the plant bypass line. Given the high cost of switching to larger pipes and fittings it is worth designing for the precise bypass line requirements rather than simple using the LFOM diameter for other pipes.

The plant bypass line, backwash recycle line and source water pipes will all be designed using the bypass line nominal diameter. The bypass line will be designed based on the minor losses of the entrance, elbows, and exit as well as the total elevation difference between the entrance tank and the filter outlet tank.

Pipes used to connect the clarifier to the filter need to be designed in context because the head loss directly influences the overall plant head loss and hence the height of the building. In that case the head loss should be limited to about 0.1 m. The velocity will be limited based on the number of elbows required. As plant flow rates increase the clarified pipe will quickly reach the maximum pipe diameter that the implementation partner is willing to install. In that case the options are to use multiple pipes or switch to open channel flow.

The chemical pipes have three sections with different constraints.

.. _table_chemical_pipes:

.. csv-table:: Design constraints for the chemical feed piping.
   :header: "Location", "Constraint", "maximum velocity"
   :align: left

   stock tanks to float valves, low head loss so that chem platform doesn't need to be raised significantly,
   constant level tank through dosing tubes and to doser, low head loss compared with dosing tube head loss,
   drop tube to flexible tubing, tube must contain air to the elevation where full pipe flow begins,
   flexible tubing, small head loss compared with the hydraulic safety factor (10 cm),
   flexible tubing to injection point (coagulant), small head loss compared with the hydraulic safety factor (10 cm),
   flexible tubing to drip point (chlorine), small head loss compared with the hydraulic safety factor (10 cm),


Stock tanks to float valves
============================



Constant level tank through dosing tubes and to the doser
=========================================================

Any loses that scale with the velocity squared must be minimized in this section of tubing. The minor losses should be less than about 5% of the 20 cm doser tube head loss (1 cm of head loss). There are about 6 elbows in this trajectory and this sets the maximum velocity in this section of piping to 0.14 m/s.

Drop tube to flexible tubing
============================

The flow transitions from full pipe flow to open channel flow in the horizontal pipe leading to the drop tube. The vertical (or almost vertical) drop tube has supercritical open channel flow. In supercritical flow downstream conditions have no influence on the flow. An example of supercritical flow is flow down a spillway from a dam. The supercritical flow prevents the water level at the injection point for the coagulant from having any influence on the coagulant flow rate that is controlled by the head loss through the dosing tubes. The chemical will have the lowest vertical velocity at the point where it transitions from horizontal to vertical flow. The open channel flow condition must begin at the end of the horizontal section.

We can specify that the chemical depth at the end of the horizontal section should not exceed 50% of the pipe diameter. The flow at the transition from the horizontal to vertical pipe is critical flow. The equation for critical flow for an arbitrary channel cross section is given by:

.. math::
  :label: FroudeNumber

  Fr^2 = \frac{Q^2 T}{gA^3}

where Fr is the Froude number, Q is the flow rate, T is the top width of the fluid surface, g is the acceleration due to gravity, and A is the cross sectional area of the flow. The Froude number has a value of 1 for critical flow. We can apply the constraint that the horizontal pipe be half full at the transition to the vertical pipe and replace the flow rate with velocity times area to obtain:

.. math::
  :label: criticalFlow1

  1 = \frac{V^2 A^2 D}{g A^3}

The area, A, in Equation :eq:`criticalFlow1` is half of the pipe cross sectional area, :math:`\frac{\pi D^2}{8}`.

.. math::
  :label: criticalFlow2

  1 = \frac{8 V^2 D}{g \pi D^2}

Equation :eq:`criticalFlow2` can be solved for the maximum fluid velocity in half full pipe.

.. math::
  :label: V_max_halfPipe

  V_{max_{halfPipe}} = \frac{\sqrt{2\pi g D}}{4}

For design purposes we want a constraint on the maximum velocity over the entire pipe. The entire pipe has twice the area and thus the maximum velocity over the entire pipe is half of the value in Equation :eq:`V_max_halfPipe`.

.. math::
  :label: V_max_dropTube

  V_{max_{dropTube}} =  \frac{\sqrt{2\pi g D}}{8}


Try again using flow as the parameter. The flow area, A, is 1/2 of the pipe cross sectional area when T is the diameter.

.. math::
  :label: criticalFlow3

  1 = \frac{Q^2 D}{g\left(\frac{\pi D^2}{8}\right)^3}

Now solve for D.

.. math::
  :label: DforCriticalFlow

  D = \left[\frac{Q^2}{g }\left(\frac{8}{\pi}\right)^3\right]^\frac{1}{5}

The critical flow constraint is less severe than the constant level tank to the doser. To minimize the number of different sizes of piping that are used the drop tube will have the same diameter as the pipes leaving the constant level tank.

Flexible tubing
===============
All designed to have less than 1 cm of minor losses so the same tubing can be used both entering and exiting the doser.

Doser to injection point (coagulant)
====================================

Doser to drip point (chlorine)
==============================


.. bibliography:: /references.bib
   :cited:
   :keyprefix: plantHydraulics-
