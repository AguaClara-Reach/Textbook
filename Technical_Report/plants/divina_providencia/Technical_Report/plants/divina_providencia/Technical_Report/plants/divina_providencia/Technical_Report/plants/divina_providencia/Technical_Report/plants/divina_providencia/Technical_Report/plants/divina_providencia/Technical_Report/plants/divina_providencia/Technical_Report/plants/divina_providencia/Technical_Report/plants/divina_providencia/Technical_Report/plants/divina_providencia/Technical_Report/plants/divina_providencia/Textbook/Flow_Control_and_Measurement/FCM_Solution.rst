.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Flow_Control_and_Measurement/FCM_Solution.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>


*************************************
Flow Control and Measurement Solution
*************************************

A Brief Programming Guide
=========================

 #. Do not use a numerical or iterative solution when an analytical solution is easily available.
 #. Whenever a function has the potential to be used multiple times, create a function call that includes the parameters that could potentially change.
 #. Do not break dependency. That means that if I change an input parameter at the top of your worksheet, that I should get the correct answers for the new parameter for all related calculations in the worksheet.
 #. Always use dimensions (units). All calculations involving physical units must include those units.
 #. Document your design process with comments.
 #. Do not redefine your variables in subsequent problems. This loses valuable digits of precision on your numbers and can cause a lot of trouble and frustration.
 #. For everyone’s sake, use logical and reasonable variable names. `Here is AguaClara variable naming convention <https://github.com/AguaClara/aguaclara/wiki/Design-Variable-Naming-Conventions>`_

A Brief Design Challenge guide
==============================

 #. Read the problem statement in its entirety before beginning a problem. If you don’t immediately know what to do, read it again, thoroughly. If you are getting stuck, read it a third time. If you have a good understanding of what the problem is asking and are still having trouble, TAs can help through email or office hours.
 #. If you decide to email a TA, make sure the other two are CC’ed. This minimizes the time you will have to wait until one responds.
 #. When in doubt, Kernel -> Restart & Run All
 #. Play around! Print arrays, test inputs, and ask yourself if your answers are reasonable. Should flow have units of km mg/s?


.. note::
   Please remember that whne using Colab, if you wish to run the code to generate plots and solutions, rather than just view them, you will need to run all initializing code blocks for variable and imports!

Vertical Orifice Equation
=========================

**1)** Find the *vena contracta* (VC) coefficient ratio for an orifice in the expert_inputs and print the result in a sentence. Please display 2 significant figures.

`vena contracta calculation <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=CZ5G4LzBRz6y&line=1&uniqifier=1>`_

The *vena contracta* coefficient for an orifice is 0.63.

**2)** The simple orifice Equation :math:`Q = {\Pi _{vc}}{A_{or}}\sqrt {2g\Delta h}` that we normally use is not applicable for vertically oriented orifices that are partially or barely submerged. The `USGS published a great solution <https://il.water.usgs.gov/proj/feq/fequtl98.i2h/4_7aupdate.html>`__ for flow through partially submerged vertically oriented orifices. AguaClara uses a general solution for a vertically oriented orifice, which is available in the physchem file as ``pc.flow_orifice_vert``. That function handles vertically oriented orifices even if they are only partially submerged.

The vertical orifice equation is based on the concept that the velocity through the orifice at any point is equal to :math:`\sqrt{2gh}`, where h is the local depth of submergence. The total flow can be obtained by integration of that velocity over the submerged area of the orifice.

For this question, you will create a well formatted graph with two curves to display flow rate through a 5 cm diameter orifice oriented **vertically and horizontally**.

We want to be able to describe the height of the water in the orifice as relative to the orifice diameter size. The relationship between velocity and orifice diameter is true for orifices of any size, so it is valuable to create a nondimensional model that can be understood for all diameters. The flow rate that you will use for this question is as a function of the normalized depth of water from 1 diameter below the center of the orifice to 2 diameters above the center of the orifice.

The steps for making the graph are as follows:

  - Use ``np.linspace`` to generate an array of 100 dimensionless water surface elevations. The surface elevations should be normalized (also referred to as nondimensionalized) by the diameter of the orifice, and should range from -1 to 2 orifice diameters.
  - Create a second array for water elevation (with units) by multiplying the normalized water elevation array by the orifice diameter.
  - Create two arrays of flow rates through the orifice: one for the horizontal orifice orientation and one for the vertical orifice orientation. Use the two orifice equations ``pc.flow_orifice`` and ``pc.flow_orifice_vert`` in the physchem file, with orifice diameter and the dimensional water elevation array you created as inputs.
  - Plot the curves for vertical and horizontal orifice flow in L/s as a function of the normalized height of water.
  - Label the graph with flow rate in L/s as the y-axis and with normalized water elevation above the center of the orifice as the x-axis.
  - Include a legend for the two curves.

`Colab worksheet comparing vertical and horizontal orifice flow <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=F7l7sG0aR24k&line=4&uniqifier=1>`_

.. _figure_Horizontal_vs_Vertical_Orifice_Orientation:

.. figure:: /Images/Horizontal_vs_Vertical_Orifice_Orientation.png
   :width: 400px
   :align: center
   :alt: Horizontal vs. Vertical Orifice Orientation

   Horizontal vs. Vertical Orifice Orientation

**3)** Write a paragraph about what the graph means by explaining the following two items: - Explain why the vertical orifice equation predicts more flow when the water level is below the center of the orifice and predicts less flow when the water level is above the center of the orifice. It might help to draw a picture of what the equations are describing to understand what is happening here! - Explain how the horizontal orifice equation function from ``physchem.py`` predicts the flow rate for submergence depths that are negative. You will need to find the function and look at the code.

Explanation
-----------

The vertical orifice has the lower part of the orifice partially submerged before the horizontal orifice has any part submerged. This explains why the vertical orifice has more flow than the horizontal orifice between -0.5 and 0.

The horizontal orifice has higher flow rates between 0 and 0.5 because it is fully submerged when the vertical orifice is still not fully submerged.

At the elevation where the vertical orifice is first fully submerged the flow rate through the vertical orifice is less than the flow rate through the horizontal orifice. This is a result of the nonlinear relationships between depth of submergence and velocity.

The difference between the two equations becomes negligible for submergence greater than 1 diameter.

For negative depths of submergence the horizontal orifice function uses an if statement to set the flow rate through the orifice equal to zero.

Linear Flow Orifice Meter (LFOM)
================================

A linear flow orifice meter is used in AguaClara plants to measure the plant flow rate and to provide a linear relationship between flow rate and the depth of water in the entrance tank. Below, we use the LFOM code to obtain a design for a linear flow orifice meter. Your task will be to test this design using the orifice equations to see if it is correct. We have a custom `LFOM class <https://aguaclara.github.io/aguaclara/design/lfom.html>`_ that defines the LFOM properties. This code will be updated soon based on the code below. In the meantime, the code below can be used for calculations.

The following questions are all answered in one big block of code to make it easy to change values and then see the resulting graph.

**4)** Create a function that calculates the flow rate through the LFOM as a function of only water elevation using the vertical orifice function. Use the arrays for LFOM key parameters, given above as ``my_LFOM.orifice_diameter``, ``my_LFOM.n_orifices_per_row``, and ``my_LFOM.height_orifices``.

 - Create an array for depth of submergence for each row of orifices at a given a height of water in the LFOM. This array is dependent on the water elevation (which should be your function input) and the height of the LFOM orifices (which is from the LFOM key parameters). Use this submergence depth array as the “height” input to your vertical orifice function. The array should be created within your function.

 - To calculate the flow rate through the LFOM, multiply the calculated flow for each row of orifices by the number of orifices in that row (``my_LFOM.n_orifices_per_row``) to get an array of flows through each row of orifices. Note: the vertical orifice function will report zero flow for any orifices that aren’t submerged, so you can send the whole array of depth of submergence for each row of orifices.

 - At the end of your function, sum flows from each row of the LFOM and return that value with the correct units.

 - Add a comment under the function definition to explain what the function does (see any of the aguaclara design files for examples of descriptive comments).

**5)** Calculate the total flow through the LFOM using the vertical orifice equation for the case when the water level is at the maximum water level for the LFOM, ``HeadlossLfom``. You are checking to make sure that the LFOM produces the correct target flow (given as ``Flow``) at the maximum height. Does it?




**6)** We want to compare the actual flow rate through the LFOM to the expected flow rate through the elevation as a function of water depth. Create a graph of the normalized actual and expected flow rates, using the following steps:

  - Create an 100-unit long array of water depths using ``np.linspace``. Note: the expected flow rate at elevation zero is zero, which makes the normalized flow rate undefined for zero elevation. An undefined normalized flow will not run and Python will report an error. You can solve this by beginning your water depth array at a very small (nonzero) elevation. You can end your water depth array at the maximum water depth. Recall that an array of elevations should have units of length.
  - Create an array of normalized actual flow rates at each water depth; use the function you created in Problem 4 and a ``for`` loop (the function you created in Problem 4 probably can’t handle an array of depths as input, so you need the ``for`` loop to cycle through each depth value to make your array of flows).

     - Start by creating an empty array for actual flow rates that is the same shape as the 100-unit water depth array you just created.
     - In your ``for`` loop, normalize the actual flow rates by using the following relationship: normalized actual flow rate = (actual flow rate)/[(water depth \* target flow rate)/maximum water level]

  - Plot a straight horizontal line at y = 1, which is your normalized expected flow value if the LFOM were perfect.



.. _figure_Normalized_Flow_Rate_vs_Water_Depth:

.. figure:: /Images/Normalized_Flow_Rate_vs_Water_Depth.png
   :width: 400px
   :align: center
   :alt: Normalized Flow Rate vs. Water Depth

   Normalized Flow Rate vs. Water Depth

**7)** Play with the value for the plant flow rate, ``LFOM_flow``, and try a bunch of different flows over the range 1 to 100 L/s. The LFOM isn’t accurate for the first couple of rows.


**8)** Do you observe any failure modes where the design produces very inaccurate flow measurements? If so, then create an issue!


**9)** Explain why all LFOMs perform poorly when the water depth is in the first row of orifices.

The relationship between head and flow is nonlinear for a single row of orifices. Thus it is impossible for the LFOM to be accurate when there is only one row of orifices.


Laminar Flow Based Flow Controller
==================================

You will design (by completing the following questions) a laminar flow controller for chlorine feed for a plant design flow rate of 50 L/s.

For the following steps do NOT use the aguaclara cdc code. Instead, create the functions that you need to solve this problem. At the end, we will compare your solution to the aguaclara cdc solution.

You may assume that the chlorine stock solution kinematic viscosity is approximately the same as water. The dose controller is to have a maximum head loss of 20 cm through the dosing tubes. We will start with commercially available liquid bleach (equivalent to 51.4 gm/L of chlorine gas), which we will use in our chemical stock tanks without dilution. Our goal is to provide a constant chlorine dose of 2 mg/L to the water entering the storage tank. We will be following the guidelines given below.

 #. Calculate the maximum flow rate through each available dosing tube diameter that keeps error due to minor losses below 10%.

 #. Calculate the total chemical flow rate that would be required by the treatment system for the maximum chemical dose and the maximum allowable stock concentration.

 #. Calculate the number of dosing tubes required if the tubes flow at maximum capacity (round up).

 #. Calculate the length of the dosing tubes that correspond to each available tube diameter.

 #. Select the longest dosing tube that is shorter than the maximum tube length allowable based on geometric constraints.

 #. Select the dosing tube diameter, flow rate, and stock concentration corresponding to the selected tube length.

`Solution for dosing tube diameter, flow rate, and stock concentration <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=hLjYn9CzR-Jv&line=3&uniqifier=1>`_


**11)** At the given water treatment plant design flow rate, what is the required flow of bleach (the chlorine stock solution)?

`Solution for flow of bleach <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=mVINIWLbSL51&line=2&uniqifier=1>`_


**12)** How many liters of liquid bleach are required in one day? (you can simply change the units on the flow rate!)

`Solution for liters of liquid bleach <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=fPuBw6MZSNPg&line=1&uniqifier=1>`_


**13)** Our next big goal is to choose a tubing size for the dosing tube (or tubes). This requires multiple steps. Begin by first creating a numpy array of tubing sizes between 1/16" and 5/16" with a 1/16" interval. Your list should contain 5 elements. Does ``np.linspace`` work here? What about ``np.arange``? Remember to always attach the units to the entire array and not to array elements!

`Solution for tubing size arrays <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=Dy4MxbuHSQpL&line=1&uniqifier=1>`_

**14)** What is the maximum average velocity in a dosing tube based on the constraint that minor losses must be small? This means that the minor losses account for ``RatioError`` fraction of the total losses (10% when ``RatioError`` is 0.1). Note that this velocity is independent of the tube diameter.

`Solution for maximum average velocity <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=sR2IN1hYSUaR&line=1&uniqifier=1>`_

The maximum average velocity in a dosing tube is 0.443 m/s

**15)** What is the head loss due to minor losses in the tube when the tube is flowing at maximum capacity? Solve for this value algebraically by substituting your equation for the velocity in the tube into the minor loss equation and then calculate the value.

`Solution for minor head losses <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=kQ0RVEOBSVag&line=1&uniqifier=1>`_


**16)** Create an array of the maximum flow rates corresponding to the array of tubing diameters. The flow rates must meet the error constraint.

.. math::

  Q_{max} = \frac{\pi D^2}{4}\sqrt{\frac{2gh_L \Pi_{error}}{\sum K_e}}

First, create a function that uses diameter and velocity as inputs to return flow rate. Note that ``ac.area_circle(diam)`` returns a circle’s area given its diameter, and you have already calculated the maximum average velocity in Problem 14.
Create the array of maximum flow rates using the array of tubing diameters and the maximum head loss through the dosing tubes.

`Solution for dosing tube flow rate <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=6fqFroCkSYch&line=1&uniqifier=1>`_


**17)** Find the minimum number of tubes for each of the available tube diameters that would be required to deliver the maximum flow of bleach.

`Solution for maximum bleach flow rate <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=bKpCtXdGSbdp&line=1&uniqifier=1>`_


**18)** Create an array of the maximum flow rate per tube for each of the available tubing diameters, given the number of tubes that would be used. This will be the flow through each dosing tube at the maximum flow of bleach.

`Solution for maximum flow rate per tube <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=Ogt6D8WaSjqz&line=2&uniqifier=1>`_

**19)** We now know the target flow in the dosing tubes, the diameter of the tubes, and the target head loss through the tubes. Thus, we can solve for the length of the tube that will deliver that target flow. Write a function to find the length of each tube that could handle the entire flow. Your function should use the following equation:

.. math:: L = \frac{g h_{L}\pi D^4}{128 \nu Q_{max}}-\frac{Q_{max}}{16 \pi \nu}\sum K_{e}

Call your function to return the length of tubing required for each tube
size.

`Solution for length of the tubing <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=znrdVDf5SmCs&line=3&uniqifier=1>`_

**20)** Which option do you think is best? You can simply set the array index to your choice and then display your solution by using that index value on your arrays for number of tubes, flow rates, tube diameters, and length of tubes.

`Selected solution for doser design <https://colab.research.google.com/drive/1fWZQ-BsXeINM31NgzbJO2Piv7NZug0cI#scrollTo=sc07AVmCS6fw&line=2&uniqifier=1>`_

**21)** What physical constraints might you use to select the best solution? How did you make your selection in Problem 19?

The ideal solution will have - a “reasonable” number of tubes and thus one possibility is to select the smallest diameter of tubing that uses a single tube. However, this won’t work for plants with high flow rates of chemicals. - tubes that are short enough to mount in the water treatment plant

**22)** AguaClara has coded these dosing tube size functions in the CDC Functions (ac.CDC). Find the function calls for the length, diameter, and number of dosing tubes and use those functions to calculate the values for the problem that you solved above. Compare your answers. Your answers should agree!

Pending new solution using updated CDC code.
