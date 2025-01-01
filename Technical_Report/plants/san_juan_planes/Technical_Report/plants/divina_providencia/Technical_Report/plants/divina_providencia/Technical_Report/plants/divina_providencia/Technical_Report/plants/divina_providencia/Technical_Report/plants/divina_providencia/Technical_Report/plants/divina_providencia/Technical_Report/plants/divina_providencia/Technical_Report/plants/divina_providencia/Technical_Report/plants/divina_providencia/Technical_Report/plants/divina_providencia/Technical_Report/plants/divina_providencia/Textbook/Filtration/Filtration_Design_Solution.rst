.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Filtration/Filtration_Design_Solution.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

**************************
Filtration Design Solution
**************************

`Be sure to import all packages before using the code! <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=hTiLSh4XjiAt&line=3&uniqifier=1>`_


DC Stacked Rapid Sand Filtration
================================

The stacked rapid sand filter at Tamara, Honduras is treating 12 L/s of water with six 20 cm deep layers of sand. The sand has an effective size of 0.5 mm and a uniformity coefficient of 1.6. The backwash velocity of the filter is 11 mm/s. Defined below are many of the necessary inputs for the filtration analysis.

`Colab worksheet with filtration inputs predefined <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=F6PVT-H8jj6W&line=6&uniqifier=1>`_


Remember: Don’t break continuity!
---------------------------------

Ensure that you use the variables defined above in your code, do not hard code any numbers if you do not have to.

`1) Calculate the total sand depth of all 6 sand layers. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=F6PVT-H8jj6W&line=6&uniqifier=1>`_

The total depth of the filter sand is 1.2 meter

`2) Calculate the diameter that is larger than 60% of the sand (D60 of the filter sand). <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=DQ2OyZQVj0Wy&line=1&uniqifier=1>`_

The D60 for the sand grain size is 0.8 millimeter

`3) What is the total filter bed plan view area for both filters in Tamara? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=iM-n546Pj8N3&line=1&uniqifier=1>`_



The filter bed plan view area is  1.091 meter ** 2

`4) What is the velocity of water through a filter during filtration? Recall that the flow through the filter is the same in filter and backwash modes. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=zSB4eZTikBPi&line=1&uniqifier=1>`_


The filtration velocity is 1.833 millimeter / second

`5) Create a function to calculate the head loss through the filter at the beginning of filtration with a clean filter bed. Then use that function to find the head loss through the clean bed of the Tamara filter. Assume that each flow path receives the same flow <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=3W9UXgKVkG1f&line=4&uniqifier=1>`_

Recall: - If you have flow paths in parallel, the head loss is NOT the sum of the head loss in each path. - Instead, the head loss in each path is the same as the total head loss.

The head loss through the clean filter sand is 15.20 cm


`6) Create a function to estimate the minimum fluidization velocity for this filter bed. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=I371vnWukNyl&line=4&uniqifier=1>`_  Then use that function to find the minimum fluidization velocity of the Tamara filter. Fluidization occurs at the beginning of backwash as all of the water flows through the bottom inlet. Note that this is not the actual velocity used for backwashing the sand.

The minimum fluidization velocity for this filter bed is 6.1 mm/s


`7) Plot the minimum backwash velocity as a function of water temperature from 0°C to 30°C. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=cLWw4SvhkT0U&line=4&uniqifier=1>`_ Then use your plot to answer the following question: if you have a water treatment plant with a single filter and there is a drought that is reducing flow to the plant, when should you backwash the filter? Should you backwash when the water is coolest or when the water is warmest?

.. _figure_Minimum_backwash_velocity_vs_water_temperature:

.. figure:: /Images/Minimum_backwash_velocity_vs_water_temperature.png
   :width: 400px
   :align: center
   :alt: Minimum backwash velocity vs water temperature

   The minimum backwash velocity increases with temperature. Thus it is best to backwash when the water is coolest.

`8) What is the residence time of water in the filter during backwash, when the bed is fluidized? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=G3br_Q8CkZGv&line=1&uniqifier=1>`_ You may assume the sand bed expansion ratio is 1.3.

The residence time in the fluidized bed during backwash is 76.36 second

Our next overall goal is to determine the ratio of water wasted in a Stacked Rapid Sand (StaRS) Filter to water treated in a StaRS. Given that the backwash water that ends up above the filter bed never returns to the filter it isn’t necessary to completely clear the water above the filter bed during a backwash cycle. Therefore we anticipate that backwash can be ended after approximately 3 expanded bed residence times. In addition it takes about 1 minute to initiate backwash by lowering the water level above the filter bed.


`9) Estimate the time between beginning backwash and finishing the cleaning of the bed. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=4KIv2OZMkjQt&line=2&uniqifier=1>`_

The time to backwash the filter is 289.1 second

`10) Estimate the total depth of water that is wasted while backwash is occurring. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=QAudW_F3krtL&line=3&uniqifier=1>`_

The total depth of water that is wasted is 3.18 meter

`11) Estimate the total depth of water that is lost due to refilling the filter box at the end of backwash plus the slow refilling to the maximum dirty bed height. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=wMYPt-XLkzMA&line=1&uniqifier=1>`_ You may ignore the influence of plumbing head loss and you may assume that the dirty bed head loss is about 40 cm. The water level in the filter during backwash is lower than the water level at the end of filtration by both the head loss during backwash AND the head loss at the end of filtration. There is also an additional 20 cm of lost water that is required for the hydraulic controls.

To reiterate, the three components that contribute to the depth of water lost in refilling the filter box after backwash are as follows:

#. Head loss during clean-bed filtration.
#. Difference in head loss between clean-bed filtration and dirty-bed filtration, just before backwash.
#. Height of the pipe that initiates backwash, also called the hydraulic control. This is actually the pipe’s diameter, since it is laying sideways in the filter.


The total depth of water that is lost due to refilling the filter box is 1.8 meter

`12) Calculate the total length (or depth) of water that is wasted due to backwash by adding the two previous lengths. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=jvCvZWB9k45v&line=2&uniqifier=1>`_ The length found in problem 10 represents water wasted while backwash is occurring, while the length in problem 11 represents the water lost in the transition to and from backwash.

The depth of the water that is wasted due to backwash is 4.98 meter

`13) Assume that the filter is backwashed every 12 hours. This means that the filter is producing clean water for 12 hours before it need to be backwashed. What is the total height (or length) of water that would be treated by the filter during this time? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=E1yHTQwwk-8f&line=3&uniqifier=1>`_ This length when multiplied by the area of the filter would give the total volume of water processed by a filter.


The height of water that would enter the filter in 12 hours is 475.2 meter

`14) Finally, what is the ratio** of water lost due to backwash and related water level changes in the filter box to water treated? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=ftRvIVVLlFIi&line=1&uniqifier=1>`_

The fraction of the total water that is lost due to backwash is 0.01048 dimensionless

`15) Now we will evaluate the very first data set from a full scale SRSF. The performance data provided is the settled water turbidity and then the filtered water turbidity during one filter run. The time step is 5 minutes. Plot pC\* for the filter as well as effluent turbidity as a function of time on two separate graphs. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=-I-OQ1YflL87&line=2&uniqifier=1>`_


.. _figure_Filter_run_time_vs_removal_efficiency:


.. figure:: /Images/Filter_run_time_vs_removal_efficiency.png
   :width: 400px
   :align: center
   :alt: Filter run time vs removal efficiency

   The pC* for this filter run was not very good and suggests that either some particles were being released by the new sand or the coagulant dose was not optimal.


.. _figure_Filter_run_time_vs_effluent_turbidity:

.. figure:: /Images/Filter_run_time_vs_effluent_turbidity.png
   :width: 400px
   :align: center
   :alt: Filter run time vs effluent turbidity

   The filter performance deteriorated over the length of the filter run. This does not match the expectations that we have based on laboratory experiments with filters. AguaClara has limited data of filter performance as a function of time. However, the `recent data from Tamara <http://aguaclara.github.io/index.html>`__ (select Tamara from the drop down menu of plants) suggests that filtered water turbidity is consistently lower than in this first run of the filter that you plotted above.

`16) How many kg of suspended solids per square meter of filter were removed during this filter run. Use the plan view area for the filter (don’t multiply by the number of layers) <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=cT0s6pXYlWWm&line=3&uniqifier=1>`_

The mass of the suspended solids removed is 2.94 kg/m²

`17) Another useful way to express the solids capacity of the filter is to calculate the turbidity removed the run time and then express the results with units of NTU hrs. What was the capacity of the filter in NTU hrs? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=SaSPisiGlbUx&line=2&uniqifier=1>`_

The filter capacity is 43.72 NTU * hour

`18) How long was the filter run? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=YMGzJLt7lioK&line=2&uniqifier=1>`_

The filter was run for 14.25 hour

`19) What is the total volume of pores per square meter (plan view area) of StarS filter bed (includes all 6 layers) (in L/m^2)? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=yZ7H6G07lsC_&line=2&uniqifier=1>`_

The total volume of pores is 480 liter / meter ** 2

`20) The next step is to estimate the volume** of flocs per plan view area of the filter. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=1kFJ_GoDltxm>`_ Assume the density of the flocs being captured by the filter are approximated by the density of flocs that have a terminal velocity of 0.10 mm/s (slightly less than the capture velocity of the plate settlers). (see slides in flocculation notes for size of the floc and then density of that floc. `This value is provided here to simplify the analysis <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=5QW7qgdHlw26&line=1&uniqifier=1>`_

Given the floc density, calculate fraction of floc volume that is clay.

Given that floc mass is the sum of clay mass and water mass and given that floc volume is the sum of clay volume and water volume, derive an equation for the volume of flocs per plan view area of a stacked rapid sand filter (includes all 6 layers) given the floc, clay, and water densities and the mass of the clay. Show the equations that you derive using Latex

Mass conservation gives

.. math::  Vol_{Floc} \cdot \rho_{Floc} = M_{Clay} + M_{Water}

:math:`M_{Water}` is an unknown.

.. math::  M_{Water} = Vol_{Floc} \cdot \rho{Floc} - M_{Clay}

Volume conservation gives

.. math::  Vol_{Floc} = Vol_{Clay} + Vol_{Water}

.. math::  Vol_{Floc} = \frac{M_{Clay}}{\rho_{Clay}} + \frac{M_{Water}}{\rho_{Water}}

Substitute to eliminate :math:`M_{Water}`

.. math::  Vol_{Floc} = \frac{M_{Clay}}{\rho_{Clay}} + \frac{Vol_{Floc} \cdot \rho_{Floc}}{\rho_{Water}} -\frac{M_{Clay}}{\rho_{Water}}

Solve for :math:`Vol_{Floc}`

.. math::  Vol_{Floc} - \frac{Vol_{Floc} \cdot \rho_{Floc}}{\rho_{Water}} = \frac{M_{Clay}}{\rho_{Clay}} - \frac{M_{Clay}}{\rho_{Water}}

.. math::  Vol_{Floc}\left ( 1-\frac{\rho_{Floc}}{\rho_{Water}} \right ) = M_{Clay}\left ( \frac{1}{\rho_{Clay}} -\frac{1}{\rho_{Water}}\right )

.. math::  Vol_{Floc} = M_{Clay}\left ( \frac{\frac{1}{\rho_{Clay}}-\frac{1}{\rho_{Water}}}{ 1-\frac{\rho_{Floc}}{\rho_{Water}}} \right )

.. math::  Vol_{Floc} = { \frac{M_{Clay}\rho_{Water}}{\rho_{Floc}-\rho_{Water}}}\left ( \frac{1}{\rho_{Water}}-\frac{1}{\rho_{Clay}} \right )

`To determine the flocs per plan view area <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=IbhGFltil2nn&line=2&uniqifier=1>`_

The volume of the flocs per plan view area is 18.34 liter / meter ** 2

`21) What percent of the filter pore volume is occupied by the flocs? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=9ZrPAB0ul7dE&line=1&uniqifier=1>`_ This fraction of pore space occupied is quite small and suggests that much of the filter bed has a very low particle concentration at the end of a filter run.

The fraction of filter pore volume that is occupied by flocs is 0.0382

This result is surprising and intriguing. It indicates that the pores in the filters are 96% empty when the filter run is complete! Thus filters don't fail because the pores get full. There is a different mechanism at play here.























Filter Constriction Hypothesis
==============================

The following analysis is completed for you and is intended to illustrate the hypothesis that flocs that are removed by the filter form a small diameter flow constriction at each place where the sand grains form a flow constriction.

Final head loss for the filter was 50cm. Assume that this is caused by minor losses due to creation of a floc orifice (constriction) in each pore. `Find the minor loss contribution by subtracting the clean bed head loss to find the head loss created by the flow constrictions that were created by the flocs. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=OlPwd_BNmDoC&line=2&uniqifier=1>`_

The minor loss contribution is 34.8 centimeter

If we assume that at the end of the filter run every pore in the filter had a flow constricting orifice from the deposition of flocs in the pore, then what was the diameter of each of the flow constrictions? We will calculate this in several steps. To begin, estimate how many flow constrictions are created by the sand grains before any flocs are added with the assumption that there is one flow constriction per sand grain. `How many sand grains are there per cubic meter of filter bed? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=mTuzOAZFmFXU&line=2&uniqifier=1>`_ Use D60_filter_sand to estimate the number of sand grains. We will assume there is a one to one correspondence between sand grains and flow constrictions.

There are this many sand grains in a cubic meter: 2.238 / millimeter ** 3

`Estimate the average vertical distance between flow constriction based on the cube root of the volume occupied by a sand grain. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=Lnv-Lr3rmH26&line=2&uniqifier=1>`_

The distance between flow constriction is 0.7645 millimeter

`On average, how many sand grain flow constriction does a water molecule flow through on its way through the filter? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=vh2-U1SXmKP2&line=2&uniqifier=1>`_

A water molecule flows through 262 dimensionless constrictions in a StaRS filter

`Head loss per flow constriction <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=08iP2d2zmL9z&line=1&uniqifier=1>`_

The head loss per constriction is 1.33 millimeter

If each constriction was partially clogged with flocs at the end of the filter run, `estimate the velocity in the constriction using the expansion head loss equation. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=4zM3jTJNmNcp&line=3&uniqifier=1>`_ You can use the average pore water velocity as a good estimate of the expanded flow velocity.

.. math::  h_{e} = \frac{(V_{in}-V_{out})^2}{2g}

The velocity in the constriction is 166.1 millimeter / second

`The flow rate of water through each pore can be estimated from the number of pores per square meter given the average separation distance. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=IT7ymBB-mWNh&line=4&uniqifier=1>`_


  The flow rate through each pore is 1.071 microliter / second

`What is the inner diameter of the flow constriction created by the flocs if the *vena contracta* is 0.62? <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=1P7WvFqRma4G&line=2&uniqifier=1>`_

The inner diameter of the flow constriction created by the flocs is 115.1 micrometer

This suggests that this flow constriction is stable because the high velocity results in shear levels that are too high for flocs to attach. Thus once the constriction forms and reaches the shear level that prevents deposition it remains stable.

`Plot the fractional removal per constriction as a function of particle size. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=6R407jBRmcPm&line=7&uniqifier=1>`_

.. _figure_Diameter_vs_fractional_remaining:

.. figure:: /Images/Diameter_vs_fractional_remaining.png
   :width: 400px
   :align: center
   :alt: Diameter vs fractional remaining

   There are many constrictions in series and the filter fraction remaining is the pore fraction remaining raised to the power of the number of pores in series.
