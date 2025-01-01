.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Filtration/Filtration_Design_Challenge.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Filtration_Design_Challenge:

***************************
Filtration Design Challenge
***************************

The design of Stacked Rapid Sand Filters involves balancing many constraints. Given that we don't yet have a model of how sand filters work it is not yet possible to optimize the design of sand filters. It is very likely that many of the empirically derived design guidelines such as filtration velocity and number of filter layers will be refined as we continue to learn more.

Learning Objectives
===================

* Discover why Open Stacked Rapid Sand Filters can not be used for low flows.
* Learn how head loss works for flow in parallel.
* Discover how clean backwash water is.

Design Exploration
==================

**If your instructor has not provided you with a link to the starting document**, you can create a copy of the  `StaRS Template <https://cad.onshape.com/documents/7c0d04fa1181c03c2d5966c9/w/e4c32164239a9b866e97d9df/e/d6e1f42043793dd9ae5759c4>`_. We will use a default filter flow rate of 20 L/s for the design calculations. If not stated, use the defaults given in the list of parameters in the Onshape document.

In addition to the questions numbered below please include a brief description in your own words of following variables and parameters insdie the "variableDescriptions" function. Be sure to mention what the units are: layerH, bwVm, fiVm, fibwH_pi,  bwC, poreVOL, bwTI, fiTI, sandPO, cleanSandHL. If there are other variables that you are having a hard time remembering please include those as well!


#. Calculate the minimum flow for an Open Stacked Rapid Sand Filter, OStaRS (ostarsQ_min). An OStaRS is made with a masonry filter box that is open at the top. Given the masonry construction the filter box dimensions must be large enough for the mason to work inside the box. The filter tank width is set by the space required for the hydraulic controls and is approximately 1.43 meter. We estimate that 0.8 meter is the minimum tank length for construction. The backwash velocity is 11 mm/s.
#. What is the minimum plant flow for OStaRS given a minimum of two filters (so that during periods of low flow one filter can still be backwashed)?
#. Given a design filter flow rate of 20 L/s, what is the required filter length? The filter width remains unchanged.
#. What is the bulk sand (sand + pores) volume?
#. What mass of sand is needed for this filter given a sand density of :math:`2650 \frac{kg}{m^3}`? Note this is the sand density, not the bulk sand density which includes the pores.
#. What is the filtration velocity given that the design flow rate is the same for backwash and for filtration modes? Remember that there are 6 filter layers and that the flow is in parallel during filtration and in series during backwash.
#. How much water is filtered in a filter run of 11 hours and 40 minutes?
#. If all of that water were in a tank with the length and width of the filter box, how tall would it be? This is the height of water filtered during a filter run. Note that there are two ways to calculate this.
#. What fraction of the water coming into the plant is wasted by the filter if it takes 20 minutes from initiation of backwash to when the filter is returned to production?
#. If a cubic tank is built to hold all of the backwash water from one filter, what is the inside length of one side of the cube? (ignore the effect of freeboard).
#. If the filter runtime is 11 hours and 40 minutes with a clarified water turbidity of 1 NTU and a filtered water turbidity of 0.1 NTU, then what is the average suspended solids concentration of the backwash water? You can assume that 1 NTU = 1.47 mg/L for kaolin clay `Coagulation behavior of polyaluminum chloride (Wei et al., 2015) <https://doi.org/10.1016/j.cjche.2015.02.003>`_. I have defined NTU in the Onshape document. I suggest simply entering the turbidity inputs in the equation that you write in FeatureScript. You can display the result in NTU by dividing the value by NTU and then include " NTU" in the postString. see ```printAnswer(i, "The average concentration of suspended solids during backwash is", " NTU", design.bwC/NTU, 3);```
#. What fraction of the sand pores were filled with clay particles prior to backwash?  Note that we are ignoring the fact that the clay particles formed flocs and the flocs include water. For this problem simply take the volume of clay particles divided by the sand pore volume.
#. What is the head loss at the coldest water temperature, 0°C, through the clean sand during filtration? Use the Ergun Equation :eq:`eq_Ergun`. Create a function in FeatureScript to calculate the head loss using the Ergun Equation.
#. What is the head loss at the warmest water temperature, 25°C, through the clean sand during filtration?
#. Estimate the depth of the filter box using Equation :eq:`approximate_filter_depth`. Note that this estimate misses about 1 meter of safety factors, freeboard, and plumbing head loss.
#. How much would the depth of the filter increase if the number of layers were increased to 10? Note that the 6 layer design was an engineering decision based on the minimum number of layers that seemed likely to be viable. The number of layers, layer height, and sand diameter are all parameters that deserve further investigation.
#. If the water coming into the filter was as turbid as the backwash water turbidity calculated above, then approximately how long would you expect the filter could run before it reached breakthrough? You can simplify the analysis by assuming that the filter captures all of the particles.
