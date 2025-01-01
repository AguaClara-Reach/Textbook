
.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Clarification/Clarifier_Theory_and_Future_Work.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Clarification_Theory_and_Future_Work:

***********
Future Work
***********

Here we explore uncharted territory of particle removal mechanisms and failure modes found in clarifiers.

.. _heading_Clarifier_Failure_Modes:

Unsolved Clarifier Failure Modes
================================

#. :ref:`Floc volcanoes <heading_Floc_Volcanoes>`
#. Dissolved air flotation that results from air coming out of solution. Two sources of air include compressed air traveling from the transmission line and dissolved air released due to increased temperature.
#. Slime growth from iron-oxidizing bacteria.
#. NOM impact on floc density.


.. _heading_Floc_Filtration_in_Conventional_Clarifiers:

Floc Filtration in Conventional Clarifiers
==========================================

Flocs that are created by the flocculator settle through the water column in conventional sedimentation tanks. As the flocs settle a fraction of the water passes through the floc where the suspension experiences floc filtration. This particle removal mechanism increases in importance as the raw water turbidity increases and the resulting concentration of flocs increases. To describe the physics of this system we define three volumes.

#. The volume cleared, :math:`\forall_{\rm{Cleared}}` by a floc is equal to the cleared area as the floc moves relative to the suspension multiplied by the total distance traveled relative to the suspension. In a horizontal flow sedimentation tank the average distance traveled could be 1/2 the depth of water in the sedimentation basin. It is possible that the volume cleared is proportional to the fraction coverage of the particles by coagulant nanoparticles. The volume cleared may also be a function of the floc size.

#. The volume surrounding a floc, :math:`\forall_{\rm{Surround}}`, is the volume of the suspension divided by the number of flocs in that suspension.

#. The volume of the reactor or suspension that is an arbitrary large volume that will eventually drop out of the analysis, :math:`\forall_{\rm{Suspension}}`.

We will treat the clearing events when a floc falls through the suspension as sequential events with complete mixing of the primary particles between clearing events. This assumption is based on the mixing caused by turbulence of the flow in the sedimentation tank and the initial random distribution of flocs. The initial nonsettleable particle concentration, :math:`C_{P_0}`, will be reduced by each clearing event. The nonsettleable particle concentration after the first clearing event, :math:`C_{P_{one floc}}`, is given by

.. math::
  :label: sed_Cp_first_clearing_event

  C_{P_{one floc}} = C_{P_0} \left( 1 - \frac{{\forall_{\rm{Cleared}}}}{\forall_{\rm{Suspension}}} \right)

The total number of clearing events is given by the total number of flocs in the suspension.

.. math::
  :label: sed_N_clearing_events

  N_{Clearing} = \frac{{\forall_{\rm{Suspension}}}}{\forall_{\rm{Surround}}}

The nonsettleable particle concentration after :math:`N_{Clearing}` clearing events is given by

.. math::
  :label: sed_Cp_all_clearing_events_1

  C_{P} = C_{P_0} \left( 1 - \frac{{\forall_{\rm{Cleared}}}}{\forall_{\rm{Suspension}}} \right)^{\frac{{\forall_{\rm{Suspension}}}}{\forall_{\rm{Surround}}}}

The exponent, :math:`\frac{{\forall_{\rm{Suspension}}}}{\forall_{\rm{Surround}}}`, can be multiplied by 1 in the form of :math:`\frac{{\forall_{\rm{Cleared}}}}{\forall_{\rm{Cleared}}}` to obtain

.. math::
  :label: sed_Cp_all_clearing_events_2

  C_{P} = C_{P_0} \left( 1 - \frac{{\forall_{\rm{Cleared}}}}{\forall_{\rm{Suspension}}} \right)^{{\frac{{\forall_{\rm{Suspension}}}}{\forall_{\rm{Cleared}}}}\frac{{\forall_{\rm{Cleared}}}}{\forall_{\rm{Surround}}}}

For large n the term :math:`\left( 1-\frac{1}{n}\right)^n` approaches :math:`\frac{1}{e}`. To meet this requirement we simply need the suspension volume to be large compared with the volume cleared by a single floc. Equation :eq:`sed_Cp_all_clearing_events_2` simplifies to

.. math::
  :label: sed_floc_filter_Cp_removal

  \frac{C_{TS_{flocFiltered}}}{C_{TS_{flocculated}}} = \frac{C_{P}}{C_{P_0}} =  \left( \frac{1}{e} \right)^\frac{\forall_{\rm{Cleared}}}{\forall_{\rm{Surround}}}

where :math:`C_{TS_{flocFiltered}}` is the concentration of particles not removed by a tube settler (or equivalent) after passing through the clarifier and :math:`C_{TS_{flocculated}}` is the concentration of particles not removed by a tube settler after flocculation.  The exponent :math:`\frac{\forall_{\rm{Cleared}}}{\forall_{\rm{Surround}}}` increases as the volume surrounding each floc decreases. Thus the particle removal efficiency will increase as the floc concentration increases.

.. _heading_Floc_Floc_Filter:

Flocculator to Floc Filter Transition
=====================================

We now have a published AguaClara hydraulic flocculator model and we have strong evidence that primary particles are removed first order with respect to depth (or time) in the floc filter. Given these two models it is possible for the first time to optimize the design of a flocculator based on minimizing the volume of the flocculator and floc filter reactors.

From the floc model we have

.. math::
  :label: dCPdt_floc

	 \frac{dC_{P}}{dt}=-\pi\bar{\alpha}kC_{P}\left(\frac{6}{\pi}\frac{C_{P}}{\rho_P}\right)^{2/3} \tilde{G}


From the floc filter we know that particle removal is first order with respect to depth of the floc filter or time in the floc filter. We can use floc filter data to estimate the first order rate constant.

.. math::
  :label: dCPdt_fb

	 \frac{dC_{P}}{dt}=-k_{ff}C_{P}

Separate variables to integrate this rate equation.

.. math::
  :label:

	 \frac{dC_{P}}{C_{P}}=-k_{ff}dt

We integrate this to solve for the rate constant.

.. math::
  :label:

	 k_{ff} = -\frac{1}{\theta_{ff}}ln{\frac{C_{P}}{C_{P_0}}}

We will use the previous equation to estimate the rate constant for the floc filter.

We can obtain a minimum volume design by setting the rate of primary particle loss at the end of the flocculator to be equal to the rate of primary particle loss at the beginning of the floc filter.

.. math::
  :label:

	 -k_{ff}C_{P}=-\pi\bar{\alpha}kC_{P}\left(\frac{6}{\pi}\frac{C_{P}}{\rho_P}\right)^{2/3} \tilde{G}

Now we solve the previous equation for the target concentration of primary particles that we should design for at the end of the flocculator.

.. math::
  :label:

	C_{P_{floc out}} = \frac{\pi \rho_P}{6} \left( \frac{k_{ff}}{\pi\bar{\alpha}k \tilde{G}}\right)^{3/2}


The concentration of primary particles at the flocculator effluent will be a function of the flocculator velocity gradient.

The next step is to determine the Gt for the flocculator given this effluent flocculator particle concentration. The approximate equation for

.. math::
  :label:

   \tilde{G}\theta \approx \frac{3}{2} \frac{\Lambda^2}{k \pi D_P^2 \alpha}


where the particle separation distance is given by

.. math::
  :label:

  \Lambda = \left( \frac{\pi D_P^3}{6} \frac{\rho_P}{C_P} \right)^\frac{1}{3}

Putting the previous two equations together we have:

.. math::
  :label:

   \tilde{G}\theta \approx \frac{3}{2} \frac{1}{k \pi D_P^2 \alpha} \left( \frac{\pi D_P^3}{6} \frac{\rho_P}{C_P} \right)^\frac{2}{3}

We can simplify this equation because the particle size cancels out.

.. math::
  :label:

   \tilde{G}\theta \approx \frac{3}{2} \frac{1}{k \pi \alpha} \left( \frac{\pi}{6} \frac{\rho_P}{C_P} \right)^\frac{2}{3}


Now we can substitute the equation for the optimal flocculated water primary particle concentrations into the flocculator performance equation.

.. math::
  :label:

   \tilde{G}\theta \approx \frac{3}{2} \frac{1}{k \pi \alpha} \left( \frac{\pi\bar{\alpha}k \tilde{G}}{k_{ff}}\right)

This simplifies to a very simple relationship that gives the optimal flocculator residence time. This analysis assumes that the cost per volume of flocculator is the same as the cost per volume of floc filter.

.. math::
  :label:

  \theta \approx \frac{3}{2} \left( \frac{1}{k_{ff}}\right)

We now have an equation for the optimal flocculator residence time! It is a function of the floc filter rate constant. The analysis below suggests that the optimal flocculator residence time is about 300 seconds (5 minutes). This analysis does not provide guidance on the optimal amount of energy to be used in that flocculator. Overall plant performance is a function of how much energy is used in flocculation and so that would need to be an economic analysis. Startup performance when the floc filter is not yet formed is a function of the energy dissipation rate.

This analysis suggests that a residence time that is less than what we are currently using for civil works AguaClara plants (about 8 minutes) and greater than what we are using for the PF300 (1-2 minutes) is the optimal solution.
High velocity gradients for flocculators with this long of a residence time will require a lot of head loss. We need to make sure that we are using a reasonable amount of energy.

The flocculator head loss is given by

.. math::
  :label:

   h_{Floc} = \tilde{G} \theta \frac{\nu \tilde{G}}{g}



`Colab worksheet calculating  head loss through the floc filter <https://colab.research.google.com/drive/1lE7cHu3TS1vMs0_yA3FmNdPnk3iktBJw#scrollTo=fMlmtxm_YWJY&line=2&uniqifier=1>`_

The target flocculator Gt of 39,000 is crazy close to the current design. This value will undoubtedly change somewhat as we get better measurements for the floc filter rate constant.

This analysis suggests that the primary particle concentration after flocculation can be quite high when operating with a floc filter. Further work will be required to ensure that startup is not a problem.


.. _heading_Floc_Volcanoes:

Floc Volcanoes
==================

Floc volcanoes are caused by differences in temperature between the water that is in a clarifier and the incoming water. If the incoming water is warmer than the water that is already in the clarifier, then the incoming water will be buoyant and will rise quickly to the top of the clarifier and carry flocs to the effluent launder.

Temperature fluctuations can be especially pronounced with small scale water supplies where small streams and small diameter transmission lines can be exposed to the sun and can warm up dramatically during a few hours of sunshine. Given that temperature changes and density changes can not easily be engineered, the only solution that we have is to reduce the time that water spends in the clarifier so that the influent water is closer to the average temperature of the water in the clarifier. Solar heating causing the raw water temperature to go from a minimum at 6 am to a maximum at 1 pm. AguaClara clarifiers currently have a residence time of approximately 2 m / (1 mm/s) or 2000 s. We anticipate that by increasing the upflow velocity and by introducing floc recycle that the effects of temperature induced floc volcanoes will be reduced.
