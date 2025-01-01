.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Chemistry_of_Water_Treatment/Chemistry_Derivations.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Chemistry_of_Water_Treatment_derivations:

***************************************
Carbonate Reactions, Buffering, and pH
***************************************

Carbonates provide the majority of the buffering for drinking water as long as the pH is close to neutral. These equations provide a basis to calculate how much base or acid must be added to a natural water to achieve a target pH.


.. _heading_Carbonic_Acid_and_Bicarbonate:

Carbonic Acid and Bicarbonate
-----------------------------

.. math:: {H_2}CO_3^{\star} \overset {K_1} \longleftrightarrow {H^+} + HCO_3^-
  :label: carbonate

Where:
 | :math:`K_1` is the dissociation constant defined below.

.. math:: {K_1} = \frac{{\left[ {{H^ + }} \right]\left[ {HCO_3^ - } \right]}}{{\left[ {{H_2}CO_3^{\star} } \right]}}

Where the [ ] indicates concentration in mole/L. We will use the p function, :math:`p(x)=-log_{10}(x)`, to define the dissociation constant.

.. math:: p{K_1} = 6.3

At the point of equal concentrations of bicarbonate and carbonic acid the dissociation constant, :math:`K_1`, is equal to the hydrogen ion concentration, :math:`H^ +`. Thus we have equal concentrations at :math:`p{K_1} = pH`. This reaction is “centered” at pH = 6.3 and thus there is maximum buffering due to this reaction at pH = 6.3.

.. _heading_Bicarbonate_and_Carbonate:

Bicarbonate and Carbonate
-----------------------------

.. math:: HCO_3^ - \overset {{K_2}} \longleftrightarrow {H^ + } + CO_3^{ - 2}

.. math:: {K_2} = \frac{{\left[ {{H^ + }} \right]\left[ {CO_3^{ - 2}} \right]}}{{\left[ {HCO_3^ - } \right]}}

.. math:: p{K_2} = 10.3

Thus the carbonate system also provides buffering around pH 10.3.

.. _heading_Total_Concentration_of_Carbonates:

Total Concentration of Carbonates
---------------------------------

The total concentration of carbonate species is given by

.. math:: {C_T} = \left[ {{H_2}CO_3^{\star} } \right] + \left[ {HCO_3^ - } \right] + \left[ {CO_3^{ - 2}} \right]

Where: :math:`{C_T}` is the total concentration of carbonates.

The total concentration of carbonates, :math:`{C_T}`, is useful because it is conservative (in a closed system) even though the individual species concentrations change as pH changes.

.. _heading_Alpha_Notation:

Alpha Notation
--------------

The alpha notation is used to show the concentration dependence on pH and to make the equations simpler.

.. math:: \left[ {{H_2}CO_3^{\star} } \right] = {\alpha_0}{C_T}

.. math:: \left[ {HCO_3^-} \right] = {\alpha_1}{C_T}

.. math:: \left[ {CO_3^{-2}} \right] = {\alpha_2}{C_T}

The alphas sum to 1 because each :math:`\alpha` is the fraction of the carbonates corresponding to that species. The alphas are each a function of the proton concentration and the dissociation constants of the carbonate reactions.

.. math:: {\alpha_{\text{0}}} = \frac{1}{{1 + \frac{{{K_1}}}{{[{H^ + }]}} + \frac{{{K_1}{K_2}}}{{{{[{H^ + }]}^2}}}}}

.. math:: {\alpha_{\text{0}}} = \frac{1}{{1 + \frac{{{K_1}}}{{[{H^ + }]}}\left( {1 + \frac{{{K_2}}}{{[{H^ + }]}}} \right)}}

.. math:: {\alpha_{\text{1}}} = \frac{1}{{\frac{{[{{\rm H}^ + }]}}{{{{\rm K}_1}}} + 1 + \frac{{{{\rm K}_2}}}{{[{{\rm H}^ + }]}}}}

.. math:: {\alpha_{\text{2}}} = \frac{1}{{\frac{{{{[{{\rm H}^ + }]}^2}}}{{{{\rm K}_1}{{\rm K}_2}}} + \frac{{[{{\rm H}^ + }]}}{{{{\rm K}_2}}} + 1}}

.. math:: {\alpha_{\text{2}}} = \frac{1}{{1 + \frac{{[{{\rm H}^ + }]}}{{{{\rm K}_2}}}\left( {1 + \frac{{[{{\rm H}^ + }]}}{{{{\rm K}_1}}}} \right)}}

.. _heading_Acid_Neutralizing_Capacity_(ANC)_or_Alkalinity:

Acid Neutralizing Capacity (ANC) or Alkalinity
----------------------------------------------

Acid neutralizing capacity or alkalinity is the ability of a water sample to react with and neutralize an input of acid. The units of ANC are equivalents (or protons) per liter. Bicarbonate, :math:`HCO_3^-`, can react with one proton, :math:`H^+`, and thus each mole of :math:`HCO_3^-` provides one equivalent per liter of ANC. The other terms in the equation have similar explanations.

.. math:: {\text{ANC}} = [HCO_3^ - {\text{] + 2[CO}}_3^{ - 2}{\text{] + [O}}{{\text{H}}^{\text{ - }}}{\text{] - [}}{{\text{H}}^{\text{ + }}}{\text{]}}

Note that carbonic acid and dissolved carbon dioxide are not in the ANC equation because they have no ability to neutralize protons.

We can write the ANC equation using alpha notation

.. math:: ANC = {C_T}({\alpha_1} + 2{\alpha_2}) + \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]



For completeness we include acid neutralizing capacity for the case where the system is in equilibrium with atmospheric carbon dioxide,
:math:`CO_2`.

.. math:: ANC_{atm\,equilibrium} = \frac{{{P{C{O_2}}}{K_H}}}{{{\alpha_0}}}({\alpha_1} + 2{\alpha_2}) + \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]

.. _heading_pH_Adjustment:

pH Adjustment
-------------

The final ANC, :math:`ANC_1`, after base addition and aluminum coagulant addition is given by

.. math:: ANC_1 = ANC_0 + \Pi_{base}C_B + \Pi_{Al}C_{Al}

| where:
| :math:`ANC_0` is the initial acid neutralizing capacity of the water sample.
| :math:`ANC_1` is the final acid neutralizing capacity of the mixture after the base and aluminum coagulant is added.
| :math:`C_B` is concentration of base in mole/liter
| :math:`\Pi_{base}` is ANC per mole of base
| :math:`C_{Al}` is the concentration of coagulant in mole of aluminum/liter
| :math:`\Pi_{Al}` is ANC per mole of aluminum

The final carbonate concentration is given by

.. math:: C_{T_1} ={C_{T_0}}+ \Pi_{CO_3^{-2}}C_B

| where:
| :math:`C_{T_1}` is the final total carbonate concentration of the mixture after the base is added.
| :math:`\Pi_{CO_3^{-2}}` is mole of carbonate per mole of base (0 for :math:`NaOH` and 1 for :math:`Na_2CO_3`)

Substituting these values into the ANC equation we obtain

.. math:: ANC_0 + \Pi_{base}C_B + \Pi_{Al}C_{Al} = ({C_{T_0}}+ \Pi_{CO_3^{-2}}C_B)({\alpha_1} + 2{\alpha_2}) +  \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]

Now we solve for :math:`C_B`, the concentration of base that must be added to reach a target pH.

.. math::  (\Pi_{base} -\Pi_{CO_3^{-2}}({\alpha_1} + 2{\alpha_2}) )C_B= {C_{T_0}}({\alpha_1} + 2{\alpha_2}) +  \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right] - ANC_0 - \Pi_{Al}C_{Al}

.. math::
  :label: Base_for_pH_Adjust

   C_B= \frac{{C_{T_0}}({\alpha_1} + 2{\alpha_2}) +  \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right] - ANC_0 - \Pi_{Al}C_{Al}}{\Pi_{base} -\Pi_{CO_3^{-2}}({\alpha_1} + 2{\alpha_2})}

Note that the equations above can also be used for the case where acid is added to reduce the pH. In that case :math:`\Pi_{base}` will have a negative value.

An example using this equation to find the required amount of base addition is given in :ref:`heading_Example_pH_Adjustment`.
