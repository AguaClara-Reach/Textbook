.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Flocculation/Floc_Derivations.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Flocculation_Derivations:

*************************
Flocculation Derivations
*************************



.. _heading_Baffle_Loss_Coefficient:

Baffle Minor Loss Coefficient
=============================

For contractions in series the minor loss coefficient is strongly influenced by the distance between the contractions. When the contractions are spaced so closely that the flow can't fully expand between contractions the velocity exiting the contraction is greater and the resulting head loss is greater. The distance required for the flow to expand can be estimated based on jet expansion equations. The flow exiting a rectangular contraction can be modeled as a plane jet and plane jets grow in width at a rate

.. math::
  :label: PlaneJet_expansion

  W_{jet} = 0.116x

where x is the distance along the path of the jet centerline and :math:`\Pi_{PlaneJet_{exp}} = 0.116` for a plane jet in an infinite medium. The location of this expanding jet is shown in Figure :numref:`figure_baffle_geometry`. The jet is influenced by the presence of the baffle on the one side. Andrew Pennock, 2022, used Computational Fluid Dynamics (CFD) to determine that the jet is effectively only expanding on the side that is in contact with the recirculation zone. Thus

.. math::
  :label: BaffleJet_expansion

   \Pi_{BaffleJet_{exp}} = 0.5 \Pi_{PlaneJet_{exp}}

where :math:`\Pi_{BaffleJet_{exp}}` is the dimensionless rate of expansion for the jet that has a baffle on the one side.

.. _figure_baffle_geometry:

.. figure:: /Images/baffle_geometry.png
   :align: center
   :width: 300px
   :alt: CFD vc baffle

   Baffle geometry for a hydraulic flocculator where S is the space between baffles, :math:`L_{jet}` is the distance over which a jet can expand, and :math:`H_e` is the approximate total distance between expansions.

The distance over which the jet can expand is given by :math:`L_{jet}`. The path length is given by

.. math::
  :label: L_jet

  L_{jet} = H_e - 2S + L_{curve}

where :math:`L_{curve}` is the effective length of the curved path of the jet around the end of the baffle.

There may be an additional complication in assessing the jet path length. The jet continues to expand through the flow contraction and a dimensionless path length created by dividing the path length by the local jet width may makes the curved path at the end of the baffle even more significant.

The maximum width of the expanding jet, :math:`W_{jet_{max}}`, occurs immediately upstream of where the streamlines begin to curve to go around the end of the baffle. The jet minimum width (greatest contraction) occurs shortly after going around the 180° bend. Given that the flow might not have fully expanded we can express the jet minimum width as a function of the jet maximum width.


.. math::
  :label: W_jet_min

  W_{jet_{min}} = W_{jet_{max}} \Pi_{vc}^{baffle}

where :math:`\Pi_{vc}^{baffle}` is given by Equation :eq:`theta_slot_vena_contracta_analytical` with an angle of :math:`\pi` and has a value of 0.3733.  The maximum jet width is determined by how much it can expand in distance :math:`L_{jet}`.

.. math::
  :label: W_jet_max_of_W_jet_min

  W_{jet_{max}} = W_{jet_{min}} +  \Pi_{BaffleJet_{exp}}L_{jet}

Equations :eq:`W_jet_min` and :eq:`W_jet_max_of_W_jet_min` provide two equations in two unknowns. Eliminate :math:`W_{jet_{min}}` from Equation :eq:`W_jet_max_of_W_jet_min`.

.. math::
  :label: W_jet_max

  W_{jet_{max}} =  \frac{\Pi_{BaffleJet_{exp}}L_{jet}}{1 - \Pi_{vc}^{baffle}}

The velocity in the expanded jet is higher than would have been obtained based on continuity and the dimensions of the flow passage. The effect of the higher velocity can be factored into Equation :eq:`K_baffle_min` by multiplying by the ratio of the velocity squared. From continuity the ratio of :math:`S` to :math:`W_{jet_{max}}` is the ratio of the velocity in the expanded jet to the velocity that would have occurred if the flow had filled the enter flow passage. Substitute Equation :eq:`W_jet_max` to obtain

.. math::
  :label: baffle_expanded_jet_width_ratio

   \frac{S}{W_{jet_{max}}}  =  \frac{S}{ \frac{\Pi_{BaffleJet_{exp}}L_{jet}}{1 - \Pi_{vc}^{baffle}}}

The ratio of :math:`\frac{L_{jet}}{S}` can be expressed as a function of the baffle ratio, :math:`\Pi_{H_eS}`. The maximum path length for jet expansion is used here.

.. math::
  :label: L_jetS_ratio

  \frac{L_{jet_{max}}}{S} = \frac{H_e - 2S + L_{curve}}{S} = \Pi_{H_eS} -2 + \Pi _{LS_{curve}} = \Pi_{H_eS} + \Pi _{LS_{curve}}'

Substitute Equation :eq:`L_jetS_ratio` into Equation :eq:`baffle_expanded_jet_width_ratio` to obtain the ratio of the velocity in the expanded jet to the velocity that would have occurred if the flow had filled the enter flow passage.

.. math::
  :label: baffle_unexpanded_velocity_ratio

  \frac{S}{W_{jet_{max}}}  =   \frac{1 - \Pi_{vc}^{baffle}}{\Pi_{BaffleJet_{exp}}(\Pi_{H_eS} + \Pi _{LS_{curve}}')}

Equation :eq:`baffle_unexpanded_velocity_ratio` has a minimum value of 1 representing fully expanded flow. For large values of :math:`\Pi_{H_eS}` the equation would incorrectly predict values less than 1. This length ratio is also a velocity ratio given continuity and can be factored into the baffle minor loss equation (Equation :eq:`K_baffle_min`) to handle baffles in series where the flow doesn't fully expand between baffles.

.. math::
  :label: K_baffle_expanding_messy

  K_{baffle_{exp}} = \left( \frac{1 - \Pi_{vc}^{baffle}}{\Pi_{BaffleJet_{exp}}(\Pi_{H_eS} + \Pi _{LS_{curve}}')} \right)^2 \left( \frac{1-\Pi_{vc}^{baffle}}{\Pi_{vc}^{baffle}} \right)^2

Equation :eq:`K_baffle_expanding_messy` can be simplified to obtain

.. math::
  :label: K_baffle_expanding

   K_{baffle_{exp}} = \left(\frac{\left(1 - \Pi_{vc}^{baffle}\right) ^ 2}{ \Pi_{vc}^{baffle} \Pi_{BaffleJet_{exp}}(\Pi_{H_eS} + \Pi _{LS_{curve}}')}\right) ^ 2

Equation :eq:`K_baffle_expanding` incorporates two assumptions that need to be checked with computational fluid dynamics.

#. The :math:`\Pi_{BaffleJet_{exp}}` may be missing a correction to account for a secondary effect of the baffle.

#. The effective dimensionless length of the curved and contracted flow path, :math:`\Pi _{LS_{curve}}'`, is unknown.

Andrew Pennock conducted CFD analysis (see :numref:`figure_K_baffle_CFD`) to estimate the baffle loss coefficient as a function of the :math:`\Pi_{H_{e}S}` (see :numref:`figure_K_baffle`) and used error minimization to estimate the previous two factors. The baffle jet expansion rate had a value of approximately :math:`0.5 \Pi_{PlaneJet_{exp}}`. This result is consistent with the idea that the jet is expanding into the zone of recirculation and is not expanding on the side of the jet that is against the baffle.

.. _figure_K_baffle_CFD:

.. figure:: /Images/K_baffle_CFD.png
   :align: center
   :width: 500px
   :alt: CFD vc baffle

   CFD analysis of flow around baffles with :math:`\Pi_{H_{e}S} = 8` showing the gradual flow expansion and return to a nearly uniform velocity before making the next bend (Andrew Pennock, 2022).

If we take :math:`\Pi_{BaffleJet_{exp}} = 0.5 \Pi_{PlaneJet_{exp}}` as a given, then the remaining unknown is the dimensionless length of the curved and contracted flow path, :math:`\Pi _{LS_{curve}}'`. Andrew Pennock found :math:`\Pi _{LS_{curve}}' = 4.3` using CFD. We also obtained one head loss measurement from the Gracias AguaClara plant shortly after the plant was first commissioned. It became apparent that the flocculator head loss exceeded the expected values because water was overflowing at the upstream end of the flocculator. The calculated :math:`K_{baffle_{exp}}` for the original design of the Gracias flocculator is plotted in :numref:`figure_K_baffle`. The model fit through that single data point requires the dimensionless distance for the jet to fully expand to be :math:`\Pi _{LS_{curve}}' = 3`.

Given the slight disagreement between the two sources of information, CFD and a single head loss measurement at the Gracias AguaClara plant, it isn't clear which value to use for :math:`\Pi _{LS_{curve}}'`. Further research is required and hydraulic flume experiments could provide the most definitive answer.

.. _figure_K_baffle:

.. figure:: /Images/K_baffle_model.png
   :align: center
   :width: 300px
   :alt: CFD vc baffle

   Baffle minor loss coefficient (Equation :eq:`K_baffle_expanding`) was fit to the CFD analysis by Andrew Pennock. Additional data is needed to resolve the difference between the CFD analysis and the data point from the Gracias AguaClara plant.

Until further results are obtained we need to make an engineering judgement to select the least risky model for the baffle loss coefficient. Given a fully fabricated flocculator it is easier to reduce the baffle spacing by shortening the spacers between baffles than it is to increase the baffle spacing. Thus it would be best to err on the side of obtaining less head loss than the design specifications. To obtain less head loss than predicted we need to use the maximum estimate of :math:`K_{baffle_{exp}}`. The Gracias measurement gives the maximum estimate of :math:`K_{baffle_{exp}}` based on :math:`\Pi _{LS_{curve}}' = 3`.

Equation :eq:`K_baffle_expanding` may need to be modified when we have more experimental or CFD results to provide a better estimate of the baffle loss coefficient.

The insight that the jet expands at half the rate of a free jet means that the jet doesn't fully expand as quickly as we had thought prior to 2022. It isn't until a :math:`\Pi_{H_eS}` of about 8 that the jet is fully expanded and thus it is very reasonable to use :math:`\Pi_{H_eS}` of 8 for design.

Linking head loss, velocity gradient, and geometry
==================================================

The energy dissipation rate in Equation :eq:`G_Camp_Stein` can be set equal to the energy dissipated in a control volume given by Equation :eq:`eq_EDR_HL` to obtain

.. math::
  :label: eq_gen_G_and_hL

  \nu \tilde{G}^2 \theta = g h_{L}

Equation :eq:`eq_gen_G_and_hL` can be applied to a control volume that contains an entire flocculator or to a control volume containing a single flow expansion. Here we develop the analysis of a single flow expansion. This means that the residence time is the time between expansions, :math:`\theta_e`, and the head loss is for one expansion, :math:`h_{L_{e}}`.

From here we make three subsequent substitutions: first
:math:`h_{L_{e}} = K_{baffle} \frac{\bar v^2}{2g}`, then
:math:`\theta_e = \frac{H_e}{\bar v}`, and finally
:math:`\bar v = \frac{Q}{WS}`.

where :math:`S` is the distance between baffles, :math:`W` is the dimension of the flow that is normal to :math:`S` and :math:`H_e` the distance between expansions. For complex geometry the best way to estimate :math:`H_e` is the volume of water divided by :math:`WS`.

.. math:: \nu \tilde{G}^2 = K_{baffle} \frac{\bar v^2}{2 \theta_e}

.. math:: \nu \tilde{G}^2 = K_{baffle} \frac{\bar v^3}{2 H_e}

.. math::
  :label: flocGeoG

  \nu \tilde{G}^2 = \frac{K_{baffle}}{2 H_e} \left( \frac{Q}{WS} \right)^3

Equation :eq:`flocGeoG` describes the relationship between the geometry of the flocculator, the flow rate, and the resulting velocity gradient.

Channel or Flow Width
=====================

The minimum allowable width of a Horizontal-Vertical flocculator channel is based on the requirements that :math:`\Pi_{H_eS_{min}} < \Pi_{H_eS} < \Pi_{H_eS_{max}}` and that we maintain the :math:`\tilde{G}` that
serves as a basis for design. The final parameter derived is
:math:`W_{min, \, \Pi_{H_eS}}`.

Our two restrictions are:

#. Ensuring that we maintain the :math:`\tilde{G}` we get based on our input parameters.
#. Ensuring that :math:`\Pi_{H_eS_{min}} < \Pi_{H_eS} < \Pi_{H_eS_{max}}`


Now we can solve Equation :eq:`flocGeoG` for channel width, :math:`W`.

.. math:: W = \frac{Q}{S}\left( \frac{K_{baffle}}{2 H_e \nu \tilde{G}^2} \right)^\frac{1}{3}


Substitute :math:`S = \frac{H_e}{\Pi_{H_eS}}` into the previous equation and use the minimum value of :math:`\Pi_{H_eS}` to obtain the minimum channel width such that the flow will expand sufficiently before the next contraction.

The minimum channel width will occur for :math:`\Pi_{H_eS_{min}}`:

.. math::
  :label: W_min_HVFloc


   W_{Min_{exp}} = \frac{\Pi_{H_eS_{min}} Q}{H_e}\left( \frac{K_{baffle}}{2 H_e \nu \tilde{G}^2} \right)^\frac{1}{3}


This equation represents the minimum width of a flocculator channel given the lowest value of :math:`\Pi_{H_eS}` and the highest possible value of :math:`H_e`. The highest value of :math:`H_e` implies that there are no obstacles between baffles.

Minimum Channel Depth
=====================

Another constraint on flocculator design may be a maximum width of the channels given the available baffle material, :math:`W_{max_{baffle}}`. In this case as the flow rate increases the channel depth must increase as flow increases to maintain the required value of :math:`\Pi_{H_eS_{min}}`.

Solve Equation :eq:`W_min_HVFloc` for :math:`H_e`. The minimum depth, :math:`H_{e_{min}}`, occurs for the maximum channel width, :math:`W_{max}`, and minimum :math:`\Pi_{H_eS_{min}}`.

.. math::
  :label: H_min_HVFloc


    H_{e_{min}}=\left[\left( \frac{\Pi_{H_eS_{min}} Q}{W_{max}}\right)^3\left( \frac{K_{baffle}}{2 \nu \tilde{G}^2} \right)\right]^\frac{1}{4}


This equation represents the minimum depth of a flocculator channel given the maximum channel width. This constraint will be important as the flow rate increases.

The volume of a flocculator is defined given :math:`\tilde{G}` and :math:`\tilde{G}\theta`. Given a required length and number of channels, the relationship between depth and width is also constrained.

.. math::
  :label: width_height_H_min_HVFloc

    W_{max} = \frac{Q \theta}{H_{e_{min}} L N_{channel}}

We can substitute Equation :eq:`width_height_H_min_HVFloc` for :math:`W_{max}` in Equation :eq:`H_min_HVFloc` to obtain

.. math::
  :label: H_min_partial_HVFloc


    H_{e_{min}}=\left[\left( \frac{\Pi_{H_eS_{min}} H_{e_{min}} L N_{channel}}{\theta}\right)^3\left( \frac{K_{baffle}}{2 \nu \tilde{G}^2} \right)\right]^\frac{1}{4}

Now solve for :math:`H_{e_{min}}`.

.. math::
  :label: H_min_of_theta_HVFloc


    H_{e_{min}}=\left[\left( \frac{\Pi_{H_eS_{min}} L N_{channel}}{\theta}\right)^3\left( \frac{K_{baffle}}{2 \nu \tilde{G}^2} \right)\right]

The number of channels has to be an integer and thus getting the right number of channels is a critical early step in the design. An estimate of the number of channels can be obtained from Equation :eq:`H_min_of_theta_HVFloc` by assuming that the flocculator depth is approximately the same as the clarifier depth.

.. math::
  :label: channelN_estimate

    N_{channel} =\left( \frac{\theta}{\Pi_{H_eS_{min}} L }\right)\left( \frac{2 \nu \tilde{G}^2 H_{e_{est}}}{K_{baffle}} \right)^\frac{1}{3}


Baffle Spacing
==============
The core equation relating flow geometry and velocity gradient is Equation :eq:`flocGeoG`. If the jet has fully expanded before entering the next contraction then the minor loss coefficient is a constant. Rearranging for :math:`S`, we obtain:

.. math::
  :label: Floc_baffle_spacing_of_K

   S = \left( \frac{K_{baffle}}{2 H_e \tilde{G}^2 \nu } \right)^\frac{1}{3} \frac{Q}{W}

If the jet has not fully expanded before entering the next contraction or if it is unknown if the jet has fully expanded then iteratively use Equation :eq:`Floc_baffle_spacing_of_K` and after each iteration get a better estimate of :math:`K_{baffle}` by using Equation :eq:`K_baffle_expanding`.

One possible set of assumptions for Horizontal-Horizontal and Vertical-Horizontal flow flocculators is that :math:`\Pi_{H_eS}` is specified (perhaps = 6).

.. math::
  :label: HeofPI_HS

  H_e = \Pi_{H_eS} S

If :math:`\Pi_{H_eS}` and the flow width, :math:`W`, are specified we can substitution Equation :eq:`HeofPI_HS` into Equation :eq:`flocGeoG` and solve for the baffle space, :math:`S`.

.. math::
  :label: floc_baffle_spacing_const_PiHS

  S = \left[\frac{K_{baffle}}{2 \nu \tilde{G}^2 \Pi_{H_eS}} \left( \frac{Q}{W} \right)^3\right]^{\frac{1}{4}}

where :math:`K_{baffle}` is obtained using Equation :eq:`K_baffle_expanding`. An alternative assumption is that the flow width and the baffle spacing are equal. Given those assumptions we can make those substitutions and solve Equation :eq:`flocGeoG` for the baffle space, S.

.. math::
  :label: floc_baffle_spacing_squareGeometry

   S = \left(\frac{K_{baffle}Q^3}{2  \nu \tilde{G}^2 \Pi_{H_eS}} \right)^{\frac{1}{7}}
