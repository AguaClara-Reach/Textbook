.. _title_LFOM:

*************************
Linear Flow Orifice Meter
*************************


The LFOM is a weir shape cut into a pipe. It was meant to imitate `the Sutro Weir <https://confluence.cornell.edu/display/AGUACLARA/LFOM+sutro+weir+research>`_ while being far easier to build. The LFOM is a pipe with rows of holes, or orifices, drilled into it. There are progressively fewer holes per row as you move up the LFOM, as the shape is meant to resemble half a parabola on each side. The size of all holes is the same, and the amount of holes per row are precisely calculated. Water in the entrance tank flows into and down the LFOM, towards the rapid mix orifice and flocculator.

.. _figure_sutro_v_lfom:

.. figure:: /Images/sutro_v_lfom.png
    :width: 600px
    :align: center
    :alt: A sutro weir and an LFOM

    On the left is a sutro weir. On the right is AguaClara's approximation of the Sutro weir's geometry. This elegant innovation is called a linear flow orifice meter, or LFOM for short.


The LFOM does one thing and serves two purposes.

What it does:

**The LFOM creates a linear relationship between water level in the entrance tank and the flow out of the entrance tank.** *It does not control the flow through the plant*. If the LFOM were replaced with a hole in the bottom of the entrance tank, the same flow rate would go through the plant, the only difference being that the water level in the entrance tank would scale with flow squared :math:`h \propto Q^2` instead of :math:`h \propto Q`.

Why it is useful:

#. Allows the operator to measure the flow through the plant quickly and easily.
#. Allows for the Linear Chemical Dose Controller, which will be explained next, to automatically adjust the flow of coagulant and chlorine into the plant as the plant flow rate changes. This means the operators only need to adjust the coagulant when there is a need to change the **dose** due to a change in turbidity or organic matter concentration.

This is best understood with examples. By shaping a weir differently, different relationships between :math:`Q` and :math:`h` are formed:
* In the case of a `rectangular weir <https://swmm5.files.wordpress.com/2016/09/image00124.jpg>`_, :math:`Q \propto h^{\frac{3}{2}}`
* In the case of a `v-notch weir <https://swmm5.files.wordpress.com/2016/09/image0096.jpg>`_, :math:`Q \propto h^{\frac{5}{2}}`
* In the case of a `Sutro weir <http://www.engineeringexcelspreadsheets.com/wp-content/uploads/2012/11/Sutro-Weir-Diagram1.jpg>`_ and thus LFOM, :math:`Q \propto h`.


Before the water level reaches the second row of holes, the LFOM is simulating a rectangular weir, and thus :math:`h \not\propto Q`. The Sutro weir also experiences this problem. Similarly, if the water level exceeds the topmost row of the LFOM’s orifices, the linearity also breaks down. The entire LFOM begins to act like an orifice, the exponent of :math:`Q` in :math:`h \propto Q` becomes greater than 1. This is because the LFOM approaches orifice behavior, and for orifices, :math:`h \propto Q^2`.

The diameter of the LFOM pipe is set by the velocity of the falling water inside the LFOM at the bottom of the bottom row of orifices. This velocity is obtained by summing up all of the momentum of the falling water and dividing by the total flow for the case where the LFOM is operating at maximum capacity. The Sutro weir equations can be integrated to obtain an equation for the falling velocity of the water inside the LFOM. 

.. math::
  :label: LFOM_V_max

    V_{max} = \frac{4}{3 \pi} \sqrt{2gh_L}

This maximum vertical velocity of the falling water sets the minimum flow area of the LFOM and hence continuity can be used to obtain the minimum pipe diameter. The orifice pattern was developed to approximate the Sutro weir while simplifying the fabrication.

.. _figure_lfom_overview:

.. figure:: Images/lfom_overview.png
    :width: 150px
    :align: center
    :alt: An LFOM

    An AguaClara LFOM showing the flow rate in L/s.


    ====  ============
    Key   Description
    ====  ============
    1     maximum flow rate in L/s and maximum water level
    2     zero flow and minimum water level
    3     pipe stub that can be removed
    4     invert of entrance tank
    5     pipe coupling that is embedded in concrete
    ====  ============


The LFOM specifications are given below.

.. _table_LFOM_Specifications:

.. csv-table:: LFOM Specifications.
   :header: "Parameter", "value"
   :align: center
   :widths: 30 70
   :class: wraptable

   Nominal diameter, :sub:`($..et.lfom.ND) no-sub` inch
   Number of rows of orifices, :sub:`($..et.lfom.rowN) no-sub`
   Max flow rate, :sub:`($..et.lfom.Qm_max) no-sub`
   Head loss at max flow, :sub:`($..et.lfom.HL_max) no-sub`
   Diameter of orifices, :sub:`($..et.lfom.orificeD) no-sub`
   Space between orifices measured on the outside of the pipe,  :sub:`($..et.lfom.orificeS) no-sub`
   Orifices in each row starting from bottom row, :sub:`($..et.lfom.rowOrificeN_VEC) no-sub`
   Elevation of each row from zero flow datum, :sub:`($..et.lfom.rowOrificeH_VEC) no-sub`
