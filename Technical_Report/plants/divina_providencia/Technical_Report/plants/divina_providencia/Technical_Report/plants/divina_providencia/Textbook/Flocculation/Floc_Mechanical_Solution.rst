.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Flocculation/Floc_Mechanical_Solution.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>


*******************************
Mechanical Flocculator Solution
*******************************

`Be sure to run this code block and import packages before working the examples <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=wYlG8hDqwdwn&line=5&uniqifier=1>`_

In this design challenge, you will design a mechanical flocculator and power unit. You will use a flow rate of 50 L/s as your default design value. The coldest temperature that the raw water is expected to have is 10°C.
You will also play with fractal flocculation model equations to get a sense of how fast flocs can aggregate. You will also explore the floc model predictions.

As you define variables, take care not to redefine parameters. One trick is to use a unique name for variables that are estimates. We often add “est” to any variable names that aren’t the final values.

The ``floc_model.py`` file contains many useful functions which includes clay, coagulant and humic acid material properties, fractal model equations, and flocculation model equations. **We recommend that you open the ``floc_model.py`` and have it side by side with this design challenge for easy reference.**


The course slides found on the syllabus will be very useful for obtaining and understanding relevant equations for this design challenge and ones in the future.

Conventional Design Guidelines
==============================

This table for mechanical flocculators is taken from Sincero and Sincero’s 1996 textbook: *Environmental Engineering: A Design Approach*

+-------------+-------------+-------------+-------------+-------------+
| Type        | Velocity    | Energy      | Gt          | t (min)     |
|             | Gradient    | Dissipation |             |             |
|             | (G) (1/s)   | Rate        |             |             |
+=============+=============+=============+=============+=============+
| Low         | 20-70       | 0.4 - 4.9   | 50,000 -    | 11 - 210    |
| turbidity,  |             |             | 250,000     |             |
| color       |             |             |             |             |
| removal     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| High        | 70 - 180    | 4.9 - 32    | 80,000 -    | 7 - 45      |
| turbidity,  |             |             | 190,000     |             |
| solids      |             |             |             |             |
| removal     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Dissolved organic matter impacts the color of the water. Perhaps the reason for lower G values for color removal is because flocs created from dissolved organic matter are weaker or less dense. Hence, a lower G is needed to allow them to grow large enough for removal in the clarifier.

Mechanical Flocculator Design
=============================

The conventional design guidelines provide a range of values with little guidance on how to select “velocity gradient” or G values. One approach is to hope for the best and choose a G value in the middle of the range. We will pick the G value that is apparently appropriate for both low and high turbidity waters.

`Choose your starting variable <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=Op0XXKxUwi3W&line=2&uniqifier=1>`_

**1) The `Ten State Standards** <http://10statesstandards.com/>`__ (with the hilarious acronym GLUMRB) requires the residence time in a mechanical flocculator to be 30 minutes. What is the value of Gt if you use the velocity gradient given above as ``G_mech``?

Note: ``.to(u.dimensionless)`` ensures you don’t get weird dimensions like kilometer/inch or minute/second for dimensionless parameters.

`Determine Gt <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=JhoY0sx5w0G1&line=5&uniqifier=1>`_

The Gt is 126000

**2) Calculate the equivalent average energy dissipation rate** (in mW/kg) for the given velocity gradient at the design temperature.

`Determine rate <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=mYp81kOPw2pW&line=2&uniqifier=1>`_

The equivalent average energy dissipation rate is 6.4 mW/kg

**3) Create a function** to calculate the power requirement for mechanical flocculators. Then, use your function to obtain the power requirement for the design temperature. The equation for power is the same one that we used for mechanical rapid mix units.

`Find the power requirement <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=Ysgn-baWw8HH&line=2&uniqifier=1>`_

The power requirement is 0.57 kW

Fun Fact: although the design guidelines would logically predict that the power requirements are higher for cold water, there is little evidence that mechanical flocculator plants actually increase the power input to their flocculators when the water is cold.

**4) We hypothesize** that the maximum energy dissipation rate in a flocculator determines the size of the flocs, and those flocs may or may not be captured by the clarifier. Clarification tank performance will deteriorate if the maximum energy dissipation rate results in flocs that are so small that their terminal velocity is lower than the capture velocity of the clarifier. This likely occurs for very high maximum energy dissipation rates. Mechanical flocculators have traditionally been designed without insight into the variability of the energy dissipation rate and the need to keep the maximum energy dissipation rate low enough to prevent the creation of flocs that will avoid capture by the clarifiers. At the same time, the traditional standards likely evolved to produce designs that were at least reasonable even in the absence of an understanding of the fluid mechanics of the mixing process.

According to the Ten State Standards, “Agitators (Flocculators) shall be driven by variable speed drives with the peripheral speed of paddles ranging from 0.5 to 3.0 feet per second.” Note that they do not specify the size of the propeller and yet that is a critical dimension that determines the energy dissipation rate in the wake of the spinning propeller.

The wake behind the propeller or paddle is similar in size to the small dimension of the propeller or paddle normal to the velocity. Thus we can use the propeller height to estimate the energy dissipation rate of the plate wake. The relative velocity between the wake and the surrounding fluid is approximately equal to the propeller velocity.

Calculate the maximum energy dissipation rate that occurs in the wake behind the tip of a propeller which has a height of 3 cm and is moving at 3 ft/s. In this case, assume that the plate ratio for the maximum energy dissipation rate in the wake, :math:`\Pi_{Plate}`, is 0.04.

.. math:: \epsilon=\Pi_{Plate}\frac{\left ( V  \right )^{3}}{W_{Plate}}

You may assume that the relative velocity between propeller and water is equal to 75% of the propeller velocity.

`Colab worksheet calculating the propeller energy dissipation rate <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=-DSq8HEHw-su&line=5&uniqifier=1>`_

The maximum energy dissipation rate behind the propeller tip is 430 mW/kg

**5) Calculate the ratio** of maximum to average energy dissipation rate (henceforth referred to as max/Ave EDR) and the ratio of maximum to average velocity gradient (max/Ave G) for the mechanical flocculator described above. What is the relationship between the two ratios?

`Colab worksheet calculating the velocity gradient ratios <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=9Z7jG1xcxCG2&line=6&uniqifier=1>`_

The ratio of maximum to average energy dissipation rate is 67.5
The ratio of maximum to average velocity gradient is 8.2

SOLUTION NOTE: this information is found on extra slide 48 in the Flocculator Design slides, heading is “Results of the the CFD analysis and our model equations.”

High ratios of max/Ave for velocity gradients (and therefore also energy dissipation rates) are common in both mechanical and hydraulic flocculators. A high velocity gradient ratio is a poor design for two reasons. - This high max/Ave G results in significant inefficiency in the use of energy for flocculation. This inefficiency requires longer residence times and/or more energy input to achieve the same extent of flocculation.

The high energy dissipation rate in the propeller wake limits the amount of energy that can be dissipated without causing excessive floc breakup. Excessive floc breakup produces flocs that are too small to be captured by the clarifier.

We hypothesize that the maximum G values specified for mechanical flocculators were likely set by the constraint of not breaking flocs into small sizes. Clarification velocity needs to be less than capture velocity for a floc to settle - the smallest floc that will settle is referred to as the threshold floc because that is the smallest size we want to make. Because well-designed hydraulic flocculators have more uniform shear rates (as compared to mechanical flocculators), hydraulic flocculators are less likely to break up flocs. Therefore, the average G values specified for mechanical flocculators are not expected to apply to well designed hydraulic flocculators.

The high energy dissipation rates at the tip of a propeller in a flocculator may be high enough to create flocs that are too small to be captured by the clarifiers. We will determine if the clarifier could capture these flocs in the analysis below.

These results also suggest that the traditional emphasis on maintaining the same or lesser G value for the transport of flocculated water to the clarifier may have missed the more important point of not exceeding a value of G that produces flocs that are too small to be captured by the clarifier.

**6) A mechanical flocculator** is treating high turbidity water, and therefore is using an average G value of 180 Hz.

If the design guidelines for maximum G for mechanical flocculators are correct and are based on floc breakup, then what is the largest average G that could be used for a well designed hydraulic flocculator with a max/Ave G of :math:`\sqrt{2}`?

Note: important distinctions to make are: - maximum G vs average G - mechanical vs hydraulic flocculators. Conceptual thought coupled with pencil and paper are recommended.

`Find maximum G <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=xtcGnUx0xRUZ&line=2&uniqifier=1>`_

The maximum G for hydraulic flocculators is 1037 Hz

These extremely high average G values are more like traditional rapid mix. It is possible that energy use constraints (too much elevation difference required to power the flocculation) will prevent use of such high G values. It is also possible that these G values would cause excessive floc break up even though they appear to meet conventional standards. It is also likely that the flocculation time required to achieve a target G :math:`\theta` would not be sufficient for the coagulant nanoparticles to be transported to the surfaces of suspended particles.


**7) How much energy** in Joules per liter would be required to treat the water using this mechanical flocculator?

`Energy requirement calculation <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=JD2pFOBNxUc4&line=3&uniqifier=1>`_

The energy required using the mechanical flocculator is 11.5 J/l

**8) How much does the electricity cost** to flocculate a million liters? It isn’t necessary to actually size an electric motor for this assignment. Simply use the shaft power and assume a motor efficiency of 80%. You may assume the price of electricity is 0.15 USD/(kW-hr).

`Determine electricity cost <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=KZJcQjuqxrY5&line=3&uniqifier=1>`_

The cost of electricity for mechanical flocculation is 0.58 USD/Ml

It doesn’t actually cost very much to flocculate water using electricity. We will create cost savings over mechanical flocculators by designing smaller, higher performing flocculators that don’t require any moving parts and thus don’t require much maintenance. Our capital costs will also be lower because we use more efficient plug flow reactors to prevent short circuiting of particles through the flocculator. Thus well designed hydraulic flocculators can be smaller than mechanical flocculators.

**9) What is the equivalent amount** of potential energy that is used to operate this mechanical flocculator (the shaft power) expressed as an elevation drop in meters? What is the required shaft power?

`Determine equivalent height <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=QFSaD7qOxuyj&line=4&uniqifier=1>`_

The equivalent amount of potential energy to run this  mechanical flocculator is 1.17 m
The shaft power required is 0.57 kilowatt


**10) What is the required reactor volume** for the mechanical flocculator?

`Find reactor volume <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=IduDvf7yx14N&line=2&uniqifier=1>`_

The required reactor volume for the mechanical flocculator is 90.0 meter ** 3


**11) If this flocculator** is 4 m deep, then how many square meters of plan view area are required per L/s of flow capacity? This is a measure of required size of this unit process. For comparison, an AguaClara clarifier requires about :math:`\frac{1m^{2}}{L/s}` and are only 2 m deep.

`Find plan view area <https://colab.research.google.com/drive/1HhsaTHEzVKtkoiCQF-XnD0ssGJ93DsXn#scrollTo=lxq0-ITCx5hW&line=2&uniqifier=1>`_

The required plan view area is 0.45 meter ** 2 * second / liter
