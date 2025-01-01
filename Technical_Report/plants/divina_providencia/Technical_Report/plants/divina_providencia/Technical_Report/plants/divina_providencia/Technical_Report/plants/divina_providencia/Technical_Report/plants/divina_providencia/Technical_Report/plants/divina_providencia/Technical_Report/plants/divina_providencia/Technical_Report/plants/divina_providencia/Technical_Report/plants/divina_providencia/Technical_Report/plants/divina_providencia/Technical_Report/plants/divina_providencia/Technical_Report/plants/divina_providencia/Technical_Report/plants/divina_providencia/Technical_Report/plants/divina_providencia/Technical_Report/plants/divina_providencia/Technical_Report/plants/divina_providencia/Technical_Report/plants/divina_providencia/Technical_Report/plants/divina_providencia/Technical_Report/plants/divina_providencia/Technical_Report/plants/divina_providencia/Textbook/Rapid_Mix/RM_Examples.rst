.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Rapid_Mix/RM_Examples.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_rapid_mix_examples:

***************************************************
Rapid Mix: Examples
***************************************************

.. _heading_Example_pH_Adjustment:

Example: pH Adjustment
======================

Find the required dose of several bases to raise the pH at the Manzaragua Water Treatment Plant. The Manzaragua AguaClara plant consists of two 1 L/s plants operating in parallel. The plant is located in the municipality of Guinope, the department of El Paraiso, Honduras.

.. _figure_Manzaragua_WTP:

.. figure::    /Images/Manzaragua_WTP.jpg
    :width: 700px
    :align: center
    :alt: Manzaragua WTP

    Manzaragua water treatment plant using two of the AguaClara 1 L/s plants in parallel.

The plant performed very poorly from the first day of operation. The first attempted fix was to double the flocculator residence time by increasing the number of flocculator pipes (3 inch diameter by 1.5 m long) from 12 to 24. This improved performance, but the plant continued to perform poorly. A raw water sample was analyzed on May 30, 2018 and the following results were obtained.

.. _figure_Manzaragua_Water_Analysis:

.. figure::    /Images/Manzaragua_Water_Analysis.jpg
   :width: 700px
   :align: center
   :alt: Manzaragua Water Analysis

   Water quality analysis for Manzaragua.


.. _Table_Manzaragua_water_quality_analysis:

.. csv-table:: Manzaragua water quality analysis
   :header: "Parameter", "Units", "Standard", "Results"
   :widths: 20, 20, 20, 20
   :align: center

   "Turbidity","NTU", "5", "71"
   "Color", "color units", "15", "150"
   "pH", "pH", "6.5 - 8.5", "5.91"
   "Conductivity", ":math:`\mu s/cm`", "400", "69.15"
   "Alkalinity", ":math:`mg/L` as :math:`CaCO_3`", "-", "24.5"
   "Bicarbonates",":math:`mg/L` as :math:`CaCO_3`", "-","24.5"
   "Carbonates", ":math:`mg/L` as :math:`CaCO_3`", "-", "0"
   "Hardness", ":math:`mg/L` as :math:`CaCO_3`", "400", "15.68"

This water has high color which suggests a high concentration of dissolved organic matter. The pH is a clear problem because the pH is too low for the coagulant nanoparticles to precipitate. As the water sample has a pH of 5.91 a significant fraction of the coagulant will remain soluble.

Our goal is to determine how much base will need to be added to raise the pH. We do not have data on the *optimal* pH for treating high color water with PACl and so we will use pH 7 as the target.

At circumneutral pH (pH close to 7) the buffering capacity of the water is dominated by carbonate chemistry and specifically by the equilibrium between :math:`{H_2}CO_3^{\star}` and :math:`HCO_3^-` . We will use the acid neutralizing capacity (reported as calcium carbonate alkalinity) and the pH from the sample analysis to estimate the total concentration of carbonates. We will not use the sample analysis carbonate concentrations because they can not be precisely correct.

We will find the amount of base that must be added using Equation :eq:`Base_for_pH_Adjust`.


.. _Table_ANC_and_carbonate_values_for_several_bases_and_acids:

.. csv-table:: ANC and carbonate values for several bases and acids
   :header: "Base/Acid", ":math:`\Pi_{ANC}`", ":math:`\Pi_{CO_3^{-2}}`"
   :widths: 20, 20, 20
   :align: center

   ":math:`Na_2CO_3` or :math:`CaCO_3`", "2", "1"
   ":math:`NaHCO_3`", "1","1"
   ":math:`NaOH`", "1", "0"
   ":math:`HCl` or :math:`HNO_3`", "-1", "0"
   ":math:`H_2SO_4`", "-2", "0"

For :math:`Na_2CO_3` \* :math:`\Pi_{ANC}` = 2 we are adding
:math:`CO_3^{-2}` which is multiplied by two in the ANC equation because
:math:`CO_3^{-2}` can react with two protons. \* :math:`\Pi_{CO_3^{-2}}`
= 1 because there is one mole of :math:`CO_3` per mole of
:math:`Na_2CO_3`

`Colab worksheet calculating the required base addition <https://colab.research.google.com/drive/1tq6eHiIw47JGIPd4P_16AsewbC5GsEMk#scrollTo=EYj26XBJa9DD&line=6&uniqifier=1>`_.

In following through the example it becomes apparent that the choice of base matters. The most efficient (on a mass or mole basis) base is :math:`NaOH` because it doesn't add any carbonates that don't fully react with the hydrogen ions. The decision about which base to use will be influenced by economics, operator safety, and by whether additional carbonate buffering simplifies plant operation with changing raw water quality.



.. _Table_Calcium_bases:

.. csv-table:: Calcium base.
   :header:  "Chemical Name",   "Common Name",  "Chemical Formula"
   :widths: 20, 20, 20

   "Calcium carbonate","Limestone or chalk",":math:`CaCO_3`"
   "Calcium hydroxide","Slaked lime or hydrated lime",":math:`Ca(OH)_2`"
   "Calcium oxide","Quicklime",":math:`CaO`"

The calcium bases are relatively inexpensive and have the disadvantage of lower solubility than sodium bases. Calcium carbonate has a low solubility, carbon dioxide is present in the atmosphere, and thus calcium carbonate precipitation limits the concentration that can be used for chemical feeds.

.. _figure_mole_base_for_target_pH:

.. figure::    /Images/mole_base_for_target_pH.png
    :width: 700px
    :align: center
    :alt: mole base for target pH

    Dose of three bases (in mole/L) required to achieve a target pH for the Manzaragua water. Carbonates provide more buffering and less change in the pH compared with :math:`NaOH`.

.. _figure_mg_base_for_target_pH:

.. figure::    /Images/mg_base_for_target_pH.png
    :width: 700px
    :align: center
    :alt: mg base for target pH

    Dose of two bases (in mg/L) required to achieve a target pH for the Manzaragua water. Carbonates provide more buffering and less change in the pH compared with :math:`NaOH`.

The required dose for each of the bases is summarized below.

.. _table_Base_table:

.. csv-table:: Dose of each base required to change the pH of the Manzaragua water to 7.
   :header: "Units", ":math:`NaOH`", ":math:`NaHCO_3`", ":math:`Na_2CO_3`"
   :widths: 20, 20, 20, 20

   "[mmoles/L]",  "0.45",     "2.8",    "0.53"
   "[mg/L]",     "47.21",   "235.0",   "21.19"



.. _heading_LFOM_and_Coag_Injection_sizing:

LFOM and Coagulant Injection Sizing
================================================

A water treatment plant that is treating 120 L/s of water injects the coagulant into the middle of the pipe that delivers the raw water to the plant and then splits the flow into 2 parallel treatment trains for subsequent flocculation. The pipe is PVC 24 inch nominal pipe diameter SDR 26. The water temperature is :math:`0^{\circ}C`. Estimate the minimum distance between the injection point and the flow split.

We will use a :ref:`linear flow orifice meter <heading_lfom>` with 20 cm of head loss. The first step is to determine the diameter of the LFOM.

`Colab worksheet designing LFOM <https://colab.research.google.com/drive/1tq6eHiIw47JGIPd4P_16AsewbC5GsEMk#scrollTo=900qlLctzxLj&line=9&uniqifier=1>`_.

This analysis shows that the LFOM requires a 24 inch diameter pipe.


Example Problem: Energy Dissipation Rate in a Straight Pipe
=============================================================


#. Calculate the friction factor.
#. Use Equation :eq:`mixing_pipe_diameters` to estimate the mixing length in pipe diameters.
#. Convert to pipe length in meters.

`Colab worksheet calculating the mixing length in pipe diameters <https://colab.research.google.com/drive/1tq6eHiIw47JGIPd4P_16AsewbC5GsEMk#scrollTo=tsf9Xo4a1Tjp&line=10&uniqifier=1>`_

The previous analysis provides a minimum distance for sufficient mixing so that equal mass flux of coagulant will end up in both treatment trains. This assumes that the coagulant was injected in the pipe centerline. Injection at the wall of the pipe is a poor practice and would require many more pipe diameters because it takes significant time for the coagulant to be mixed out of the slower fluid at the wall. The time required for mixing at the scale of the flow in the plant is thus accomplished in a few seconds. This ends up being the fastest part of the transport of the coagulant nanoparticles on their way to attachment to the clay particles.  Next we will determine a typical flow rate of coagulant. **Aluminum** concentrations for polyaluminum chloride (PACl) typically range from 1 to 10 mg/L. The maximum PACl stock solution concentration is about 70 g/L as **Al**.

`Colab worksheet calculating the coagulant flow <https://colab.research.google.com/drive/1tq6eHiIw47JGIPd4P_16AsewbC5GsEMk#scrollTo=Fly3_gop3GDZ&line=1&uniqifier=1>`_.

We can estimate the diameter of the injection port by setting the kinetic energy loss where the coagulant is injected into the main flow to be large enough to exceed the pressure fluctuations downstream of the LFOM. The amount of energy we invest in injecting the coagulant into the raw water is a compromise between having to raise the entire chemical feed system including the stock tanks to increase the potential energy and a goal of not having pressure fluctuations inside the LFOM pipe cause flow oscillations in the chemical dosing tube. Thus our goal is to have the kinetic energy at the injection point be large compared with the expected pressure fluctuations in the LFOM. Given that the head loss through the LFOM is often 20 cm, we expect the pressure fluctuations from turbulence to be a small fraction of that head loss. Thus we set the kinetic energy to be equivalent to 2 cm.

`Colab worksheet calculating the diameter of the dosing tube <https://colab.research.google.com/drive/1tq6eHiIw47JGIPd4P_16AsewbC5GsEMk#scrollTo=gO_quuJh4HpS&line=1&uniqifier=1>`_
