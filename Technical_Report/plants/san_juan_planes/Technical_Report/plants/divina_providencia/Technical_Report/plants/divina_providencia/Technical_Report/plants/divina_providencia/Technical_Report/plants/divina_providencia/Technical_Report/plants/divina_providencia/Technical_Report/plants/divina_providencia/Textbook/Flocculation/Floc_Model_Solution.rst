.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Flocculation/Floc_Model_Solution.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>


***************************
Flocculation Model Solution
***************************

`Remember to run this code block prior to reviewing the solutions to ensure all functions are imported <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=i0Xa-13Uyu33&line=7&uniqifier=1>`_

Please note that certain functions were removed from the aguaclara package as the underlying equations are under suspicison. As a result, this code for this section cannot be run in its entirety and some sections have been commented out.

Many of the fractal floc equations are available in the ``floc_model.py`` file in the aguaclara repository. Look through ```floc_model.py`` <https://github.com/AguaClara/aguaclara/blob/master/aguaclara/research/floc_model.py>`_ within the aguaclara repository. The following constants are defined in that file. NTU has been defined as an approximate empirical relationship between the concentration of kaolin clay and the turbidity, such that 1 NTU is equivalent to 1.7 mg/L. The diameter of a primary clay particle is assumed to be 7 micrometers. The fractal dimension for flocs is defined as ``DIM_FRACTAL`` and is equal to 2.1. We are using PACl as a coagulant for this analysis, so you shall call ``fm.PACl``, when a function within ``floc_model.py`` requires ‘coag’ as an input.

Whenever possible, use variables defined within ``floc_model.py`` instead of redefining them. Relevant variables defined in ``floc_model.py`` include:

#. ``DIM_FRACTAL`` with an estimated value of 2.1.
#. ``PACl``
#. ``Clay``


**1) Estimate the diameter** of the flocs that interact with the tip of the impeller of the mechanical flocculator analyzed above. We don’t yet have a good model to predict maximum floc size as a function of velocity gradient or energy dissipation rate. We have a rough estimate, ``fm.diam_floc_max(EDRmax)`` based on a small amount of data.

`Estimate the diameter <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=wg4zNSOiyyrO&line=9&uniqifier=1>`_

The diameter of the flocs that interact with the impeller is 127 um.


**2) Estimate the terminal velocity** in mm/s of the flocs that interact with the tip of the impeller of the mechanical flocculator analyzed above. Use the function ``fm.vel_term_floc``. You may assume that the flocs were made from a particle suspension that had 1.5 mg/L of aluminum and 100 NTU of clay.

Note: AguaClara has defined the unit NTU as ``u.NTU``.

`Estimate the terminal velocity <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=XyIJbz6O1W-P&line=2&uniqifier=1>`_

The terminal velocity of flocs that interact with the impeller tip is estimated to be 0.738 mm/s


**3) Would these flocs be captured** by a conventional design for a clarifier `(10 State Standards) <http://10statesstandards.com/waterrev2012.pdf>`__ with a capture velocity of 1.2 m/hr? The capture velocity is a property of the clarifier. If the floc settles faster than the capture velocity, then theoretically the floc will be captured by the clarifier.

`Determine if the flocs will be captured <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=3LNMr5OL2Jlo&line=2&uniqifier=1>`_

The 10 State Standards capture velocity is 0.333 mm/s
The 10 State Standards clarifier would capture the flocs that are able to survive the energy dissipation rate at the tip of the propeller.

These flocs would be removed easily in an AguaClara clarifier (capture velocity of 0.12 mm/s). However, our use of the empirical equation to predict the size of these flocs is questionable because we are extrapolating way beyond the original data. We need more experiments to characterize the size of flocs as a function of the velocity gradient.

**4) Estimate the average distance** between primary clay particles at the beginning and end of flocculation given an initial turbidity of 100 NTU and a target effluent unflocculated clay concentration at the end of flocculation of less than 1 NTU. Of course, the clay concentration is actually constant in flocculation since particles are not actually being removed. But here we are referring to the primary clay particles that have escaped aggregation and thus are still unattached.

You can do this by figuring it out empirically (brownie points!) or by looking for a function that finds average distance between particles.

A little extra to think about (not necessary to answer): The AguaClara floccuation model assumes that primary clay particles mostly attach to other primary clay particles and not to larger flocs (aggregates of clay particles). Can you think of why this is?

`Find the distance between clay particles <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=uChIRlm63hvE&line=5&uniqifier=1>`_

The average distance between clay particles at 100 NTU is 0.141 mm
The average distance between clay particles at 1 NTU is 0.654 mm

**5) What is the inner viscous length scale** in the mechanical flocculator at the maximum energy dissipation rate? Given that this is a very high energy dissipation rate for flocculation, it corresponds to a very small inner viscous length scale. This means that eddies are able to survive down to a small size before viscosity damps their motion. If the separation distance between clay particles that haven’t turned into flocs is less than this inner viscous scale, then it is reasonable to assume that all flocculation is dominated by viscosity. The function within ``floc_model.py`` that does this is confusingly named
``lamba_vel()``.

`Calculatethe inner viscous length scale <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=lyE0jgmi3l65&line=1&uniqifier=1>`_

The inner viscous length scale is 2.39 mm


**6) Below is a graph** showing the inner viscous length scale that divides flows that are dominated by inertia (eddies) from flows where viscosity is significant. **Add the data point** representing the maximum energy dissipation rate vs the maximum clay separation distance at the end of flocculation for the mechanical flocculator you have been designing.
`Colab worksheet plotting the maximum energy dissipation rate for the mechanical flocculator <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=lyE0jgmi3l65&line=1&uniqifier=1>`_

0.6541789493547243 millimeter
    422.57902694348155 milliwatt / kilogram


**7) According to the plot** and analysis above, are the collisions between clay particles at a concentration of 1 NTU dominated by inertia or by viscosity? Explain why!

The final spacing between clay particles is still smaller than the inner viscous length scale at which eddies are damped by viscosity. This suggests that all collisions in flocculation are dominated by viscosity.


Real-World Considerations of Flocculation
=========================================

Now that you have an augmented understanding of flocculation theory, we can consider a few ways in which the theory applies to real-world flocculators.

In this section, there are no calculations for you to do or code for you to write - everything has been provided for you. This was done to shorten this design challenge while still detailing relevant and important information.

 **There are two conceptual questions for you to answer at the end of the section.** Read through and focus on understanding the concepts before you try to answer the questions.

Coagulant Distribution in a Reactor
-----------------------------------

The flocculation model accounts for loss of coagulant nanoparticles to the reactor walls. The loss of coagulant nanoparticles is assumed to scale with the area of the flocculator walls divided by the total area of clay and flocculator walls. This loss is significant for low turbidity and small scale flocculators, such as the 1 liter per second flocculator AguaClara recently designed.

We will consider a flocculator built out of pipe, not one contained within a rectangular reactor. The ``diam_tube`` parameter is the flocculator diameter and is needed to estimate how much of the coagulant is lost to the walls of the flocculator. We will assume the flocculator tube is for the 1 L/s plant and has a diameter of 7.5 cm

We will evaluate the situation where the turbidity is 10 NTU and the coagulant dose is 1 mg/L of aluminum. `The Colab worksheet calculates the loss of nanoparticles to the flocculator walls and the fractional clay particle coverage by nanoparticles : <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=5l-cWloClfxa&line=10&uniqifier=1>`_

Time Scale of Flocculation
--------------------------

Now we want to estimate the average time required for an initial successful collision between two primary clay particles that are partially coated with coagulant nanoclusters. Note that for the first collision, the current floc size is the same as the clay size. We will use the average energy dissipation rate for the mechanical flocculator as found above.

The `time required for the first collision is calculated in this Colab worksheet <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=7eHXqjjDljUQ&line=3&uniqifier=1>`_

This collision time is quite fast and is the origin of the question, “why does flocculation require 30 minutes?” as mandated in the Ten State Standards.

AguaClara Flocculation Model
----------------------------

We will now briefly consider an AguaClara flocculator design with an average energy dissipation rate of approximately 11 mW/kg and a residence time of 8.1 minutes. The design temperature is 15 degC.

`Colab worksheet calculation for the Gt value of this flocculator. <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=LOhI18urlnbE&line=4&uniqifier=1>`_

Coagulant Coverage Fraction of a Particle
-----------------------------------------

This section solves the integrated flocculation model for :math:`\Gamma`. We simplify the model by recognizing that the spacing between particles at the end of the flocculation process is much greater than the initial particle spacing. This means that the raw water turbidity drops out of the equation. The value of the rate constant for collisions is k = 0.24. We start with the equation below:

.. math:: \Gamma = \frac{3}{2}\cdot \frac{\Lambda^2 }{\mathit{k} \pi d_{p}^2 Gt }

We then estimate the required coagulant coverage of clay, :math:`\Gamma`, for the AguaClara flocculator to achieve a 2 NTU settled water turbidity when starting with a raw water that is 50 NTU.

Note that the specified flocculation model applies to both hydraulic and mechanical flocculators.

`Find the Gamma value <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=jHjw4X5Flr1C&line=9&uniqifier=1>`_

Residence Time and Coagulant Coverage
-------------------------------------

If you doubled the residence time of the flocculator, the required coagulant coverage of clay changes according to the model. By doubling the residence time, the required coagulant coverage is reduced by a factor of 2.

Modeling Flocculation in the Presence of Humic Acid, With pC\* as the Performance Metric
----------------------------------------------------------------------------------------

The flocculation model predicts the settled water turbidity given the composition of the raw water, the flocculator characteristics, and a fitting parameter that must be a function of the clarifier characteristics. This fitting parameter is k, which is the same as the rate constant for collisions described above. The model is far from complete - it doesn’t yet describe the effects of floc filters. Below we have created a plot showing model predictions for a range of coagulant and humic acid (dissolved organic matter) concentrations. The plot uses our approximation for pC\* described in class and shown below:

.. math::

   pC^*=\frac{3}{2}log{(\frac{2}{3}\pi k \frac{d_p^{2}}{\Lambda_0^{2}}Gt\alpha + 1)}

 `Make this graph! <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=q_ISgbYcl161&line=6&uniqifier=1>`_

There is a lot to learn from this graph! It appears that for any given coagulant dose, humic acid concentration significantly affects pC*. Additionally, notice the diminishing returns of adding more coagulant. This effect appears to be independent of humic acid concentration (see the red curve).

Modeling Flocculation in the Presence of Humic Acid, with Settled Water Turbidity as the Performance Metric
-----------------------------------------------------------------------------------------------------------

`We will now display a similar plot <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=Vi5F6XhAl6oA&line=4&uniqifier=1>`_ which shows settled water turbidity instead of pC*. Our initial turbidity is 10 NTU, and we will four curves for separate humic acid concentrations.


Looking at the interactions between coagulant, clay, and humic acid from this perspective yields even more fun discoveries! For increasing humic acid concentration, more coagulant is required to even begin the process of flocculation.

**8) Why does the AguaClara flocculation model** predict that adding 1 mg/L of aluminum has no effect on turbidity when the humic acid concentration is 20 mg/L?


At low concentrations of coagulant every coagulant nanoparticle surface is completely coated with humic acid and thus they aren’t sticky at all.


**9) It is tempting to assume** that all the coagulant dosed gets attached to clay particles. However, if a plant operator were to make this assumption, their plant would produce low-quality water.

Identify and explain two significant reasons as to why this assumption fails.


#. Coagulant is lost to the walls of the reactors
#. Coagulant is lost to humic acid
   (Students need to write more than this)
