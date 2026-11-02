.. raw:: html

    <embed>
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Flow_Measure_Design_Challenge:

*****************************
Flow Measure Design Challenge
*****************************

You will learn how to:
======================

* show a water surface elevation
* place a linear flow meter (LFOM) in the entrance tank
* find an error in the design logic and then fix it!

Part 1 - Feature Studio Steps
=============================

**If your instructor has not provided you with a link to the starting document**, you can create a copy of the `Flow Measure Template <https://cad.onshape.com/documents/e96b1dc31f9865978dc1316b/w/582d94287ee1ead74b494009/e/863630f2d9361f5eb9ad5c5c>`_.

#. We need the minimum water level in the entrance tank (associated with zero flow through the plant) to be perhaps 10 cm. Create a new param called :code:`lfomHW_min` with a default of 10 cm. (remember that the units of parameters are set by the name of the variable and thus :code:`lfomHW_min` has units of meters). Modify the logic for the water depth to account for this increase in required water depth. When you make this change in Featurescript the part studio should update and the entrance tank depth should increase. What is the height of the entrance tank walls?
#. Our next task is to draw the water surface in the entrance tank and have it adjust as a function of the actual flow rate. Create a dimensionless parameter that represents the fraction of the design flow (:code:`Q_pi`) that is passing through the entrance tank. Here we take advantage of the fact that any variable name that ends in _pi is dimensionless. Create an equation that calculates the depth of water in the entrance tank as a function of :code:`Q_pi`. You can assume that the LFOM creates a linear relationship between flow rate and water depth. Set the default value of :code:`Q_pi` to be 0.5. What is the depth of water in the entrance tank?

Part 2 - Part Studio Steps
==========================

#. Insert an LFOM into the entrance tank. You can add the LFOM to your custom feature list by searching for this `url <https://cad.onshape.com/documents/dee0144c157c5703f51281e7/w/a2ccabbc0ee38a095820fcd7/e/75288022c06a94b868c9d1ae>`_. Use variables for the inputs of the LFOM except for the following that can be the default (Flow safety factor, minimum pipe nominal diameter, minimum spacing between orifices, maximum number of orifice rows, minimum number of orifice rows, maximum drill diameter). Use a mate connector to set the lfom location at the opposite end from the overflow and equal distance from the end and side walls. Note that the LFOM feature has a required Module Name (enter "lfom" without the quotes) and Mate Name (enter "bottom" without the quotes).
#. Create a hole for the LFOM pipe coupling through the bottom of the entrance tank using the Pipe Hole feature.
#. Our next goal is to create the water surface.

    #. Begin by creating a sketch on the Front plane with a line that is the width of the tank and at the water surface. There are many ways to constrain the length of this line including using the end wall of the tank or the origin and then dimensioning the line to be #W long.
    #. The height of the line above the tank bottom must be set using the dimensioning tool and the variable for the water height.
    #. Use the extrude tool with the "Surface" option to create a new surface starting from the line in the sketch and extending for the length of the tank (#L).
    #. Rename "Surface 1" that is below the parts list at the left of the window to "water".
    #. Edit the appearance of the surface to make it blue and 0.2 on the transparency scale so you can see through it.

#. Change Q_pi to 1. What is the distance between the inlet of the overflow pipe and the water surface? The top of the overflow pipe is the inlet.
#. Modify the design so the overflow inlet is 1 cm higher than the water surface at the design flow rate. Do this by creating a new input parameter (call it overflowHSF) in FeatureScript and then adding that as an input to the Overflow Pipe feature.
#. Time to play with the design.

    #. What is the total cost of the Entrance Tank?
    #. Change the lfomHL to 0.1 meter, by entering {"lfomHL":0.1} in the overrides
    #. Does the cost of the entrance tank increase or decrease with this change. Explain why!
    #. Revert to 20 cm of lfomHL and then increase the flow rate to 40 L/s. Find the error in the design that causes the tank to get deeper but the LFOM to not adjust to the correct elevation.
    #. What caused this error (What did we forget to account for)? This error should be a design error, not a Featurescript error. If you are getting Featurescript errors you will also need to debug.
    #. Fix the error by making a simple change to the FeatureScript.
    #. With Q_pi at 1, where is the water surface relative to the top row of orifices in the LFOM?
    #. Change Q_pi to 0. Where is the water surface relative to the bottom row of orifices in the LFOM?
    #. Why are the orifices not centered vertically in their rows? The reason for this does not have to do with flow distribution around the LFOM.
