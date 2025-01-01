.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Clarification/Clarifier_Examples.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Clarification_Examples:

***************************************
Clarification Examples
***************************************

These are a few short examples of calculations required for clarifier design.

`Be sure to run this code prior to trying any examples <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=FMhBN6N6xAPe&line=10&uniqifier=1>`_

Tube Settler Design
===============================

Design a tube settler for a laboratory scale clarifier. The vertical section of the clarifier, :math:`v_{z_{ff}}`, has a net upflow velocity of 3 mm/s. This velocity is maintained in the tube settler, :math:`v_{\alpha}`. The target capture velocity is 0.2 mm/s. The tube settler diameter is 2.54 cm.

.. math:: \frac{\bar v_{z_{ff}}}{\bar v_c} = \frac{L}{D} \cos \alpha \sin \alpha + \sin ^2 \alpha

.. math:: \bar v_{z_{ff}} = \bar v_\alpha\sin \alpha

`Solve for the length of the tube settler. <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=qxeWciqaZnPZ&line=4&uniqifier=1>`_

.. math:: L = \frac{D}{\cos \alpha}\left(\frac{\bar v_\alpha}{\bar v_c} - \sin \alpha\right)


The tube settler above the floc hopper needs to be 72 cm long. The tube settler should provide a capture velocity of at least 1 mm/s prior to the floc hopper. Thus there should be 11 cm below the floc hopper.

.. _heading_flow_thru_diffuser:

Determining flow through a diffuser
====================================

What is the flow rate of a single diffuser in the bottom of the clarifier? Consider a clarifier that is 6 m long, 1 m wide and 2 m deep, with an upflow velocity of 1 mm/s and a diffuser spacing of 5 cm.

What is this question really asking? This question is asking us to understand that each diffuser "serves" a specific cross-sectional area of the clarifier; all of the diffusers together serve the entire area of the clarifier. So, let's imagine a single diffuser serving a slice of a clarifier. With this in mind, we can easily solve this using :math:`Q = \bar vA`. The area, :math:`A`, is the slice of the clarifier that we are serving. We are told that the tank is 1 m wide, so :math:`W_{tank} = 1` m. The length of the slice is dictated by the spacing of the diffusers, :math:`B_{diff}`, so :math:`B_{diff} = 5` cm.

.. math:: A = B_{diff}W_{tank}

.. math:: A = 5 cm * 1 m

.. math:: A = 50,000 mm^2

The problem statement includes that :math:`\bar v_{z_{ff}} = 1` mm/s. Plugging into our flow equation,

.. math:: Q_{diff} = \bar v_{z_{ff}}A

.. math:: Q_{diff} = (1 \frac{mm}{s})(50,000mm^2)

.. math:: Q_{diff} = 50,000 \frac{mm^3}{s}

.. math:: Q_{diff} = 50 \frac{mL}{s}

The flow rate of each diffuser is :math:`50 \frac{mL}{s}`.

Identify Failure Modes from Old Design
==================================================

Look at a proposed design for the bottom of the clarifier, shown in :numref:`figure_failure_mode_example`. This design has an influent manifold at the bottom of the tank. Water flows upwards from the influent manifold. At one end of the influent manifold, there is a drain port. Above the influent manifold, there is a single slot that extends the length of the clarifier. There are no diffusers in this design.

.. _figure_failure_mode_example:

.. figure:: /Images/failure_mode_example.png
    :height: 300px
    :align: center
    :alt: Proposed clarifier design.

    Proposed clarifier design.

What are the failure modes for this design?

Some issues are:

- Flocs can settle in the influent manifold, specifically at the end of the influent manifold pipe
- The upflow line jet may be impacted and bent by settling flocs, allowing for floc settling on one side of the tank
- Without diffusers, there may not be uniform flow distribution from one end of the clarifier to the other
- Without diffusers, there will be large flow circulations inside the clarifier

This design has never been built and never will be. Understanding what the problems are with this design will help us design better in the future.

Diffuser and Jet Reverser Design
================================

1. `Calculate the maximum velocity of water leaving the diffuser based on the maximum head loss. <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=kmMZMexEak6->`_ Assume that the majority of head loss is the kinetic energy of the flow exiting the diffuser slot (this assumption will be checked later). Assume K=1.

`Use these given parameters <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=VE_1JE-pasAm&line=6&uniqifier=1>`_

To find the maximum velocity based on maximum headloss we will use the minor loss equation.

.. math:: h_{e,inlet} = K \frac{\bar v_{jet}^2}{2g}

To find the minimum width based on the maximum velocity through the diffuser, we will use conservation of mass. Since it is an incompressible fluid the flow rate entering from the diffuser line jet must be equal to the flow rate up through the clarifier.

.. math:: \bar v_{jet}W_{diff} L_{sed} = \bar v_{z_{ff}}W_{sed}L_{sed}

`Colab worksheet with diffuser design <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=VE_1JE-pasAm&line=2&uniqifier=1>`_

**Answer:** The maximum velocity of the clarifier diffusers is 0.4429 meters / second.
The minimum width of the clarifier diffusers is 2.409 millimeter.

2. `Calculate the minimum inner width of the diffuser. <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=f80nuueca2Hg&line=3&uniqifier=1>`_ Assume that the diffuser slot is continuous over the entire length of the clarifier to get an initial estimate (it isn't actually continuous because it is made from many flattened diffuser pipes).

Diffusers are made by deforming PVC pipe. Softened PVC pipe is forced onto a mold that shapes it into the rectangular shape of the diffuser. (link to clarifier chapter)

`What metal plate thickness should be used to make the mold for the diffusers? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=ycOd0J-tbABh&line=3&uniqifier=1>`_ This value will be the minimum diffuser width. Metal plates are available in 1/16" increments of thickness. The minimum thickness of plate that is strong enough for a mold is 1/16".
The `ceil_nearest` function defined in utility.py can take in a parameter and an array and it will find the closest value in the array that is at least as big and the parameter. For our problem we will use this to find the plate size that is available and at least as big as the minimum width defined above.


**Answer:** The width of clarifier diffuser is 0.3175 centimeter

The PVC pipe that forms the diffusers changes in shape and wall thickness during the molding process. The inner width of the rectangle is created by forcing the pipe over a rectangular wedge that is the thickness you calculated above. During the molding process, PVC pipe wall cross-sectional area is conserved. The pipe wall is stretched in total length approximately 20%. Another way to think about this is that the thickness of the wall is reduced by a factor of 1/1.2 because the mass of PVC is conserved and the density is unchanged. Thus, volume and cross-sectional area are conserved.


Area is given using the following Equation :math:`A_{PVC}=2\left (B_{diffuser}+W_{diffuser} \right)T_{diff}`

3. Use the equation for :math:`A_{PVC}` to `calculate the following: <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=aHNyi1V9bJGA&line=7&uniqifier=1>`_

- the outer length of the rectangular diffuser slot, :math:`B_{diffuser}`.
- the inner length of the rectangular diffuser slot, :math:`W_{diffuser}`.

**Answer:** The clarifier diffuser outer length: 5.736 centimeter

Clarification diffuser inner length: 5.522 centimeter

Each diffuser serves a certain width and length of the clarifier. Assume that the diffusers are installed so that they touch each other.

4. `Determine the flow and velocity through each diffuser. <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=CKVZRhHPbUfK&line=2&uniqifier=1>`_
:math:`Q_{max,diff} = \bar v_{z_{ff}} A`

:math:`A = W_{sed}  B_{diff}`

:math:`\bar v_{diff} = \frac{Q_{max,diff}}{W_{diff} * S_{diff}}`


**Answer:** The flow of water leaving a clarifier diffuser is 61.19 milliliter / second
The velocity of water leaving the clarifier diffuser is 0.349 meter / second

5. `What is the Reynolds number of the jet exiting the diffusers at the design temperature of 15 degrees Celsius? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=lwy3sEdObZar&line=2&uniqifier=1>`_

Recall the formula for Reynold's number:

:math:`Re = \frac{\bar v D}{\nu}` The D is actually just representative of the length scale so we can replace this with the width of the diffuser.
:math:`Re = \frac{\bar v_{diff}*W_{diff}}{\nu}`

**Answer:** The Reynolds number for this jet is 974.6 dimensionless

6. `What is the Reynolds number of the vertical flow up through the top of the floc filter? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=kvLaS4AEbhvR&line=2&uniqifier=1>`_

The same principle as above can be applied to this question except the length scale is the width of the clarifier and the velocity is the upwards velocity in the tank.

:math:`Re = \frac{\bar v_{z_{ff}} W_{sed}}{\nu}`

**Answer:** Reynolds number through floc is 938.2 dimensionless. These two Reynold's numbers are similar because conservation of mass requires for a constant length that :math:`\bar v_{1}*W_{1} = \bar v_{2}*W_{2}`. The slight difference in the numbers is due to that fact that diffusers are not a continuous line jet but rather broken up by two times the thickness of the pipe wall between the diffusers.

Next, we want to determine the energy dissipation rate for the flow leaving the jet reverser. For this process, you can assume that the jet remains laminar. The flow spreads to fill the gaps created by the walls of the diffuser tubes by the time it traverses the jet reverser. Jet velocity and flow rate are conserved as the jet changes direction in the jet reverser.

7. Calculate the thickness of the jet after it does the 180 degree bend of the jet reverser. < The change in thickness of the jet after the 180 degree bend is due to the flow spreading out to fill in the gaps created by the diffuser pipe walls.
:math:`W_{jet} * \bar v_{diff} = W_{sed} * \bar v_{z_{ff}}`

8. `Calculate the maximum energy dissipation rate* for the flow leaving the jet reverser. <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=8vvPOw1RbsK2&line=1&uniqifier=1>`_ See Equation :eq:`planejet_EDR` for the maximum energy dissipation rate in a plane jet and see :numref:`table_EDR_G_equations` for the value of :math:`\Pi_{JetPlane}`.

The energy dissipation rate for inlet jet is 158.5 milliwatt / kilogram

In designing AguaClara plants, it is critical to account for all forms of significant head loss. In the clarifier, effluent launders provide about 4 cm of head loss. We want to calculate the exit head loss for water leaving the diffusers to determine whether it is a significant addition to the total head loss through the clarifier.

9. Calculate the diffuser exit head loss in two ways.

First, calculate the head loss making sure to account for the upflow velocity in the clarifier.

:math:`h_e = \frac{\left( {{\bar v_{diff}} - {\bar v_{z_{ff}}}} \right)^2}{2g}`

Second, calculate the head loss but assume that the upflow velocity is negligible.

:math:`h_e = \frac{\ {\bar v_{diff}}^2}{2g}`

10. `Is it reasonable to neglect the upflow velocity in the clarifier when calculating this head loss? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=mT6cY0pGbzKt&line=1&uniqifier=1>`_

**Answer:** The best estimate of the exit head loss for the diffuser is 0.6176 centimeter. The 2nd estimate of the exit head loss for the diffuser ignoring the upflow velocity is 0.6211 centimeter. It is reasonable to neglect the effect of the upflow velocity. The error is 0.005755 dimensionless

Manifolds and Launders
=======================
Flow distribution between and within clarifiers is an important design component to ensure good clarifier performance. We need to distribute flow uniformly between clarifiers and also between diffusers on the inlet manifolds.

The following variable definitions and equations will be useful in answering later questions.

1. Determine the relationship between diffuser exit velocity and the head loss in the parallel paths.

:math:`{h}_{L,ParallelPath}` is the head loss (flow resistance) in the parallel paths leaving the manifold. The head loss in the parallel path is the total head loss from where the flow leaves the manifold to the point where the parallel flows reunite.

:math:`\Delta{H}_{Manifold}` is the variability in piezometric head in the manifold that is driving the flow through the parallel paths.

The ratio of minimum (first diffuser port) to maximum (last diffuser port) flow is given by:

.. math:: \Pi_{DiffuserFlow} = \sqrt{\frac{h_{L,parallelpath} - \frac{\Delta{H}_{Manifold}}{2}}{h_{L,parallelpath} + \frac{\Delta{H}_{Manifold}}{2}}}

The change in piezometric head is given by: :math:`\Delta{H}_{Manifold} = \frac{{v_{manifold}}^{2}}{2g}`

The maximum allowable velocity in the manifold is given by:

.. math:: {\Pi_{DiffuserFlow}}^{2} * \left(h_{L,parallelpath} + \frac{\Delta{H}_{Manifold}}{2} \right) = h_{L,parallelpath} - \frac{\Delta{H}_{Manifold}}{2}

.. math:: \left({\Pi_{DiffuserFlow}}^{2} - 1 \right) h_{L,parallelpath} + \left({\Pi{DiffuserFlow}}^{2} + 1 \right) \frac{\Delta{H}_{Manifold}}{2} = 0

.. math:: \left(\frac{1 - {\Pi_{DiffuserFlow}}^{2}}{{\Pi_{DiffuserFlow}}^{2} + 1} \right) h_{L,parallelpath} = \frac{\Delta{H}_{Manifold}}{2}

.. math:: \left(\frac{1 - {\Pi_{DiffuserFlow}}^{2}}{{\Pi_{DiffuserFlow}}^{2} + 1} \right) h_{L,parallelpath} = \frac{{v_{manifold}}^{2}}{4g}

Now, we want to find the maximum velocity for an inlet manifold which is dependent on the given flow distribution constraint, :math:`\Pi_{DiffuserFlow}`, and the head loss in the parallel paths, :math:`h_{L,ParallelPath}`.

2. Determine an equation for maximum velocity for an inlet manifold in terms of diffuser exit velocity and the flow distribution constraint.

`Write a function for maximum velocity for an inlet manifold using the equations you just found. <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=mT6cY0pGbzKt&line=1&uniqifier=1>`_

Exit losses from the diffusers dominate the head loss because the velocity in the diffuser slots is much higher than the velocity at the entrance to the diffuser pipes. Using the insight from the previous problem, it is reasonable to neglect the effect of the upflow velocity when calculating the exit head loss for the manifold diffusers.

Head loss in the clarifier is impacted by multiple forms of head loss, inlcuding head loss through the effluent launder and diffusers. Head loss through the effluent launder is about 4 cm. You found head loss through the diffusers in Problem 9.

3. Which form of head loss (effluent launder or diffuser) is in the parallel path, :math:`{h}_{L,ParallelPath}`? `What is the maximum velocity in the clarifier manifold? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=wNjOuUcMPAmN&line=3&uniqifier=1>`_

**Answer:** Only the diffuser head loss is in the parallel paths. The maximum velocity in the clarifier manifold is 0.2313 meter / second.

The ratio of manifold pipe cross-sectional area to total diffuser cross-sectional area determines the flow distribution between diffusers.

4. Calculate the ratio of manifold pipe cross-sectional area to total diffuser cross-sectional area. You can use the velocities of the manifold and the diffusers to calculate the areas.

Since the clarifier has a constant volume, the flow rate into the tank is equal to the flow rate out of the tank:
:math:`Q_{manifold,pipe} = Q_{diff}`

:math:`v_{manifold} * A_{manifold} = v{diff} * A_{diff}`

:math:`\frac{A_{manifold}}{A_{diff}} = \frac{v_{diff}}{v_{manifold}}`

5. `What is the significance of the flow area ratio that you found? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=voeAlHjbPPEV&line=1&uniqifier=1>`_ What does it tell you about the relative areas?

**Answer:** The flow area ratio of manifold pipe to diffusers is 1.509 dimensionless. This means that the manifold flow area is larger than the total diffuser area. The flow distribution is more uniform because the diffuser velocity is higher than the manifold velocity.

The maximum clarifier flow rate is currently set by the constraint of using a single length of pipe for the manifold and launder. The maximum length of the upflow region of the clarifier is 5.8 m, as given below.

6. `What is the corresponding clarifier flow rate? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=4IIQwvYMPh7P&line=2&uniqifier=1>`_ This can be solved using :math:`Q = \bar v A`.

**Answer:** The maximum flow rate in one clarifier is 6.187 liter / second.

The maximum clarifier flow rate dictates the required pipe diameter for the manifold and launder.

7. What is the minimum inner diameter of the clarifier manifold?
:math:`Q = \frac{\bar v*\pi*D^2}{4}`

8. `What is the required nominal pipe diameter given this flow rate? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=lExuIc6SPq58&line=1&uniqifier=1>`_
The function from the pipe database can return the nominal diameter from the diameter and SDR.

**Answer:** The minimum inner diameter of the clarifier manifold is 7.266 inch. The nominal diameter of the clarifier manifold is 8 inch.

Clarifier Bays and Number of Diffusers
===============================================
The design will be for a 60 liter per second plant.

1. `What is the total required plan area for the clarifiers? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=wg6BNPlkP6oz&line=1&uniqifier=1>`_

**Answer:** The plant view area of the floc filter is 60 square meters.

2. `What is the total length of the floc filter zone for all tanks? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=-MHwQyXUQEqp&line=1&uniqifier=1>`_

**Answer:** The total length of the floc filter zone for all tanks is 56.24 meters.

3. `How many clarifiers are required to treat the total plant flow? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=u0J7OWpoQVjy&line=1&uniqifier=1>`_ The plant flow rate is the basis of design and the maximum clarifier flow rate is based on the manifold diameter.

**Answer:** The required number of clarifiers is 10.

4. `How much water (in L/s) can all of the clarifiers for the plant treat? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=YQ314w1LQsEN&line=1&uniqifier=1>`_

**Answer:** The total amount of water this plant could treat is 61.87 liter / second. It is slightly larger than the basis of design due to the needs for an integer number of clarifiers.

5. `How many diffusers are required in each tank? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=VfMU2AIjQzPw&line=1&uniqifier=1>`_ Assume the maximum length of the upflow region of the clarifier is used.

**Answer:** The number of diffuser pipes per clarifier is 98.

Plate Settler Design
=====================

We will assume that the active area of the clarifier is equal to the top area of the floc filter zone. This isn't quite right because of the geometric constraints from the floc hopper, inlet channel, settled water channel, and angled plates. However, it is a good approximation for these long tanks.

1. `What is the required length of the plate settlers? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=xK3Q6UmvRBAL&line=2&uniqifier=1>`_

The equation for this problem can be found in :ref:`Clarification Derivations<heading_Clarifier_Plate_Settlers>`.


**Answer:** The minimum length of the plate settlers is 0.4619 meters.

2. `What is the horizontal spacing (center to center) of the plate settlers? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=AbkEyYAWRHwg&line=2&uniqifier=1>`_

The equation for this problem can be found in :ref:`Clarification Derivations<heading_Clarifier_Plate_Settlers>`.

**Answer:** The horizontal center to center spacing of the plate settlers is 3.118 centimeter.

3. `Approximately how many plate settlers spaces are needed in each clarifier? <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=0uwRgXoGRRdK&line=1&uniqifier=1>`_ Assume the maximum length of the upflow region of the clarifier is used. Neglect the lost space at the end of the clarifier due to the angle of the plate settlers.

**Answer:** The number of plate settlers per clarifier is 180.


Comments, Corrections, or Questions
====================================

This textbook is an ever-evolving project. If you find any errors while you are reading, or if you find something unclear, please let the authors know. Write your comment in `this Github issue <https://github.com/AguaClara/Textbook/issues/86>`_ and it will be addressed as soon as possible. Please look at other comments before writing your own to avoid duplicate comments.
