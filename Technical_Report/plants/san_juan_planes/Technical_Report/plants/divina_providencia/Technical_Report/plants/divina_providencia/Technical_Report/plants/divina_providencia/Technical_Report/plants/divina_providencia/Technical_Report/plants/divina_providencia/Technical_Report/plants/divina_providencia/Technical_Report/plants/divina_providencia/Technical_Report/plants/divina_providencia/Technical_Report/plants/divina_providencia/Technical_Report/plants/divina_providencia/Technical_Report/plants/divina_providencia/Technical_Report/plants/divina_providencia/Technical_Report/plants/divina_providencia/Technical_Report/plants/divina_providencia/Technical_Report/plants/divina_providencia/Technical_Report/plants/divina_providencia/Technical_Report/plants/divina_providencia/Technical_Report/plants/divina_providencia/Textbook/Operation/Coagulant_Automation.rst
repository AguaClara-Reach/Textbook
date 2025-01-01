.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Operation/Coagulant_Automation.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Coagulant_Automation:

********************
Coagulant Automation
********************

Automating the coagulant dose is difficult because it hasn't been clear what measurement to use that could be driven to a target value by varying the coagulant dose and that would then provide the desired plant performance. Based on the previous understanding of coagulant neutralizing the negative charge of raw water particles, many water treatment plants have attempted to use streaming current meters to set the coagulant dose. That method doesn't work well because it is the fractional coverage of the primary particles with sticky coagulant nanoparticles that sets the attachment efficiency and that does not require a neutral surface charge.

The concentration of primary particles exiting the flocculator could be used to guide the coagulant dose. The flocculated suspension can not be sampled directly with a particle counter because the particle concentration is too high. Given that we are only interested in the concentration of primary particles, we can use a tube settler to quickly reduce the particle concentration of the sample line going to the particle counter while still enabling an accurate count of the primary particle concentration.


.. _figure_TubeSettlerFlocMonitor:

.. figure:: /Images/TubeSettlerFlocMonitor.png
   :width: 400px
   :align: center
   :alt: TubeSettlerFlocMonitor

   Proposed particle counter monitoring of flocculation performance.

Coagulant Dose for Suspended Particles
======================================

The relationship between attachment efficiency and primary particle concentration after flocculation is given by Equation :eq:`CpofGtlamSim`. For the simple case of no coagulant demand by dissolved organic matter it is reasonable to assume that the attachment efficiency is proportional to the ratio of the coagulant dose to the surface area of the particles in the raw water and the particle surface area is proportional to the particle concentration.

.. math::
  :label: coverageofdoseandCp

  \bar{\alpha} = k' \frac{C_{coag_{particle}}}{C_{P_0}}.

This coagulant dose only refers to the coagulant that will end up coating the suspended particles. The coagulant nanoparticles that are coated by dissolved organic matter will be considered in the next section.

The result of the AguaClara flocculation model (Equation :eq:`CPlamint`) is repeated here for convenience.

.. math::
  :label: CPlamintCopied

  \frac{3}{2\pi}\left(\rho_{P}\frac{\pi}{6}\right)^{2/3}\left(C_{P}^{-2/3}-C_{P_0}^{-2/3}\right)=k\bar{\alpha}\tilde{G}\theta.

Substituting Equation :eq:`coverageofdoseandCp` and solving for the coagulant dose we obtain

.. math::
  :label: CcoagFlocModel

  C_{coag_{particle}} =  \frac{3}{2\pi  k k' \tilde{G}\theta}\left(\rho_{P}\frac{\pi}{6}\right)^{2/3} C_{P_0} \left(C_{P}^{-2/3}-C_{P_0}^{-2/3}\right).

The primary particle properties and flocculator design terms can be treated as a single unknown, :math:`k_{pf}`.

.. math::
  :label: kpf

  k_{pf} =  \frac{3}{2\pi  k k' \tilde{G}\theta}\left(\rho_{P}\frac{\pi}{6}\right)^{2/3}

Thus Equation :eq:`CcoagFlocModel` simplifies to

.. math::
  :label: Ccoagkpf

  C_{coag_{particle}} =  k_{pf} C_{P_0} \left(C_{P}^{-2/3}-C_{P_0}^{-2/3}\right)

Coagulant Dose for Dissolved Organic Matter
===========================================

The next improvement in this simple model is to add a correction factor for dissolved organic matter. The dissolved organic matter effectively inactivates some of the coagulant. The dissolved organic matter is measured as absorbance at 254 nm. The amount of coagulant that is tied up with dissolved organic matter is

.. math::
  :label: UV_coag_consumed

  C_{coag_{DOM}}  = A_{254nm} K_{DOM}

The dissolved organic matter simply reduces the amount of coagulant that is available to make the inorganic particles sticky. The required coagulant dose can be obtained by adding :math:`C_{coag_{DOM}}` to Equation :eq:`Ccoagkpf`.

.. math::
  :label: Ccoagtotal

  C_{coag} =  k_{pf} C_{P_0} \left(C_{P}^{-2/3}-C_{P_0}^{-2/3}\right) + C_{coag_{DOM}}

One method to estimate :math:`K_{DOM}` is based on the experimental results obtained by Yingda Du (see :numref:`figure_floc_model_HA` `by Yingda Du, et al., 2019 <https://www.liebertpub.com/doi/abs/10.1089/ees.2018.0405>`_). Those results suggest that approximately 1 mg/L of aluminum is required to tie up 12 mg/L of humic acid.  The humic acid concentration was based on the dry weight and humic acid is approximately 48% carbon. Thus 6 mg of humic acid as carbon require 1 mg/L of aluminum. The absorbance at 254 nm was measured by `Rodrigues. et al., 2008 <https://core.ac.uk/reader/55618110?utm_source=linkout>`_  to be 0.055(humic acid as carbon in mg/L). Thus :math:`0.33A_{254nm}` is expected to consume 1 mg/L of aluminum where :math:`A_{254nm}` is the UV 254 absorbance in a 1 cm sample cell. The remaining required conversion is from the concentration of aluminum to the coagulant dose as measured at the water treatment plant.

Equation :eq:`Ccoagtotal` can be rewritten with subscripts that indicate when and where the samples are taken for the application of automatic coagulant dosing. The tube settler turbidity in the future, :math:`C_{TS_{flocculated_{t + \theta}}}` is the target turbidity of flocculated water after passing through a tube settler that we are trying to obtain.

.. math::
  :label: CcoagplantFlocculatedTS

  C_{coag_{t}} = k_{pf} C_{raw_{t}} \left(C_{TS_{flocculated_{t + \theta}}}^{-2/3}-C_{raw_{t}}^{-2/3}\right) + C_{coag_{DOM_{t}}}

Equation :eq:`CcoagplantFlocculatedTS` reveals that there is an important time lag due to the hydraulic retention time between the coagulant injection and the clarified water sample. This time lag will require that the dosing algorithm include data from the recent history to account for this time offset.

Simple Corrector Method
=========================

An estimate for the coagulant demand of the DOM is obtained by solving Equation :eq:`CcoagplantFlocculatedTS` for :math:`C_{coag_{DOM_{t}}}` and shifting the time to one hydraulic residence time earlier.

.. math::
  :label: DOMcoagDemand

  C_{coag_{DOM_{t-\theta}}} = C_{coag_{t-\theta}} - k_{pf} C_{raw_{t-\theta}} \left(C_{TS_{flocculated_{t}}}^{-2/3}-C_{raw_{t-\theta}}^{-2/3}\right)

Given the estimate of the DOM coagulant demand a hydraulic residence time earlier we can obtain an estimate of the current required coagulant dose. We will use Equation :eq:`CcoagplantFlocculatedTS` and the assumption that the coagulant DOM demand doesn't change significantly in one hydraulic residence time. The :math:`C_{TS_{flocculated_{t + \theta}}` is the target tube settler turbidity.

.. math::
  :label: CcoagplantofDOM

  C_{coag_{t}} =  k_{pf} C_{raw_{t}} \left(C_{TS_{flocculated_{t + \theta}}}^{-2/3}-C_{raw_{t}}^{-2/3}\right) + C_{coag_{DOM_{t-\theta}}}

The coagulant dosing system must include guardrails to ensure that the coagulant dose is within a reasonable range. The potential failures include:

 * incorrect reading from a turbidimeter due to an air bubble, a dirty sample cell, or during routine maintenance
 * settled water turbidity that is very low because the plant is starting up after an extended shutdown

Another potential failure mode would occur if the raw water turbidity is lower than the target clarified turbidity. This would result in a coagulant dose that could be too low to achieve effective filtration.

To reduce the likelihood of a treatment failure the estimated DOM coagulant demand can be compared with a reasonable range and if it is out of that range the estimated DOM coagulant demand can be forced back into the reasonable range. To prevent an excessively low coagulant dose the DOM coagulant demand can be limited to positive values. If it is known that the DOM coagulant demand is always exceeds a larger value, that larger value can be used as a lower limit. The upper limit can be set based on observation of the raw water quality.

Data processing
---------------

#. Acquire data at some high rate (perhaps 1 s intervals)
#. Set the number of coagulant dose updates per hydraulic residence time (HRT) (perhaps 10) and average the incoming data to that update interval
#. Hold the averaged data in a buffer with each data set including a time stamp.
#. For each coagulant dose update use Equation :eq:`DOMcoagDemand` to estimate the coagulant demand of the DOM and then use Equation :eq:`CcoagplantofDOM` to estimate the new coagulant dose.

Floc Filtration Modification
============================

We hypothesize that there is significant particle removal by floc filtration both in conventional sedimentation tanks and in the floc filter of the AguaClara clarifier. This means that the :math:`C_{TS_{flocculated_{t + \theta}}}` is not a constant value, since it needs to account for the removal efficiency of the floc filter. Equation :eq:`Removal_in_sequential_floc_sed` calculates the total removal based on performance

.. math::
  :label: Removal_in_sequential_floc_sed

  C_{TS_{flocFiltered}} =  C_{raw} \frac{C_{TS_{flocculated}}}{ C_{raw}} \frac{ C_{TS_{flocFiltered}}}{C_{TS_{flocculated}}}

where it is understood that these water samples are all passed through a tube settler, TS, before measuring the particle concentration.

Instead of setting a target for :math:`C_{TS_{flocculated}}` we will set a target for :math:`C_{TS_{flocFiltered}}`. Equation :eq:`sed_floc_filter_Cp_removal` describes particle removal by settling flocs. The Equation :eq:`eq_spacing_of_diameter` gives the relationship between floc concentration and its surrounding volume.

.. math::
  :label: surround_volume_of_Cp

  \forall_{\rm{Surround}} =   \bar{D_P}^3 \left(\frac{\pi}{6}\frac{\rho_P}{C_P}\right)

The :math:`\forall_{\rm{Surround}}` is for the flocs that will be falling through the suspension. Thus it does not include the particles that are too small to settle significantly. The surrounding volume for the flocs in the sedimentation tank  :math:`\forall_{\rm{Surround}}` is a function of the floc concentration, :math:`\left( C_{raw} - C_{TS_{flocculated}} \right)`. From Equation :eq:`surround_volume_of_Cp` we have

.. math::
  :label: surround_volume_of_raw_flocculated

  {\forall_{\rm{Surround}}} =  \bar{D_P}^3 \left(\frac{\pi}{6}\frac{\rho_P}{C_{raw} - C_{TS_{flocculated}}}\right)

The volume cleared can also be thought of as inversely proportional to a high turbidity where the :math:`\forall_{\rm{Surround}}` is equal to the :math:`\forall_{\rm{Cleared}}`. We designate this concentration or turbidity as :math:`C_{Cleared}`.

.. math::
  :label: cleared_volume_as_C_equivalent

  \forall_{\rm{Cleared}} =  \bar{D_P}^3 \left(\frac{\pi}{6}\frac{\rho_P}{C_{Cleared}}\right)

Combining Equations :eq:`surround_volume_of_raw_flocculated` and :eq:`cleared_volume_as_C_equivalent` we obtain

.. math::
  :label: volume_ratio_as_concentration_ratio

  \frac{\forall_{\rm{Cleared}}}{\forall_{\rm{Surround}}} = \frac{C_{raw} - C_{TS_{flocculated}}}{C_{Cleared}}

Now we can simplify Equation :eq:`sed_floc_filter_Cp_removal` by substituting in Equation :eq:`volume_ratio_as_concentration_ratio`.

.. math::
  :label: what is This

  \frac{ C_{TS_{flocFiltered}}}{C_{TS_{flocculated}}} =  \left( \frac{1}{e} \right)^\frac{\forall_{\rm{Cleared}}}{\forall_{\rm{Surround}}}

A possible solution method is to use a running approximation for the exponential term based on the previous measurement of  :math:`C_{TS_{flocculated}}`.

.. math::
  :label: C_TS_flocculated_of_flocFiltered

  C_{TS_{flocculated_{t + \theta}}} = C_{TS_{flocFiltered_{t + \theta}}}  e^\frac{C_{raw_{t - \theta}} - C_{TS_{flocculated_{t}}}}{C_{Cleared}}

The value of :math:`C_{TS_{flocFiltered_{t + \theta}}}` is the target performance for the water leaving the conventional sedimentation tank. At each time step first use Equation :eq:`C_TS_flocculated_of_flocFiltered` to obtain an estimate of the target for the turbidity after flocculation and a tube settler, :math:`C_{TS_{flocculated_{t + \theta}}}`. The result from Equation :eq:`C_TS_flocculated_of_flocFiltered` can then be substituted into Equation :eq:`CcoagplantofDOM` to calculate the new coagulant dose.

Still need to figure out the correction method for
Need to think carefully about the time for measurement of each of these parameters and the various :math:`\theta` involved.


.. math::
  :label: stepping_C_TS_flocculated_of_flocFiltered

  C_{TS_{flocculated}} = C_{TS_{flocFiltered}}  e^\frac{C_{raw} - C_{TS_{flocculated}}}{C_{Cleared}}

Unfortunately this can't be solved for :math:`C_{TS_{flocculated}}`, but we can solve for the settled water turbidity, :math:`C_{TS_{flocFiltered}}`. We invert the fraction and put a negative sign in the exponent.

.. math::
  :label:

  C_{TS_{flocFiltered}} =  C_{TS_{flocculated}} e^\frac{C_{TS_{flocculated}} - C_{raw}}{C_{Cleared}}
