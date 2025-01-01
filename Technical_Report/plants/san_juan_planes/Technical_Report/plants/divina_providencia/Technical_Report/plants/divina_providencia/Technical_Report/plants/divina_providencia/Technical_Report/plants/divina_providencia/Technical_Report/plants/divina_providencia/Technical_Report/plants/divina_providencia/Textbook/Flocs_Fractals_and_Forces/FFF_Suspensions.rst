.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Flocs_Fractals_and_Forces/FFF_Suspensions.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Fluidized_Suspensions:

*********************
Fluidized Suspensions
*********************

Suspension Density
==================

Suspension densities will be of interest both in understanding the physics of floc filters fluidized sand beds. The density of a suspension of particles is equal to the mass of the particles and water divided by the suspension volume. In the case of flocs we can track the concentration of the core particles in the suspension and ignore the diameter of the flocs when calculating the suspension density.

.. math::
  :label: density_suspension_1

  \rho_{suspension}
  = \frac{M_{H_2O} + M_{particles}}{\forall_{suspension}}

  =\frac{M_{H_2O} }{\forall_{suspension}} + C_{particles}

The mass of water in a suspension, :math:`M_{H_2O}`, must take into account the fraction of the suspension volume occupied by the particles.

.. math::
  :label: water_mass_in_suspension

  \frac{M_{H_2O}}{\forall_{suspension} } =
  \rho_{H_2O} \left( 1 - \frac{C_{particles}}{\rho_{particles}} \right)

where :math:`\frac{C_{particles}}{\rho_{particles}}` is the fraction of the suspension volume occupied by the particles. Substituting Equation :eq:`water_mass_in_suspension` into Equation :eq:`density_suspension_1` we obtain the density of the suspension.

.. math::
  :label: density_suspension_2

  \rho_{suspension} =
  \rho_{H_2O} \left( 1 - \frac{C_{particles}}{\rho_{particles}} \right) + C_{particles}


Equation :eq:`density_suspension_2` can be rewritten in terms of the buoyant density to obtain

.. math::
  :label: buoyant_density_suspension

  \rho_{suspension} - \rho_{H_2O} =
    C_{particles}\left(1 - \frac{\rho_{H_2O}}{\rho_{particles}}\right)


Fluidized Bed Porosity
======================

AguaClara plants have two fluidized beds. The first is the floc filter that forms in the bottom of the clarifiers and the second is the sand in the filters during backwash. The equations describing fluidized beds require multiple steps in the calculations and are easily handled in Python. The following equations are available in a `Colab worksheet <https://colab.research.google.com/github/AguaClara/Textbook/blob/master/Flocs_Fractals_and_Forces/Colab/FFF.ipynb>`_ and the equations are from `this paper <https://doi.org/10.1016/j.ijheatmasstransfer.2004.08.008>`_.

The hydraulic diameter is needed to account for wall effects for small reactors.

.. math::
  :label: hydraulic_diameter

  D_{H}={\frac {4A}{P}}

| where
| :math:`D_{H}` is the hydraulic diameter
| :math:`A` is the plan view area
| :math:`P` is the wetted perimeter

For reactors with dimensions that are not much larger than the dimensions of the flocs it is necessary to correct for wall effects. This correction will be important for laboratory scale and some pilot scale reactors. The terminal velocity of a particle corrected for wall effects is

.. math::
  :label: v_t_wall

  v_{t_w} = \frac{v_t}{10^{\frac{D_{particle}}{D_H}}}

| where
| :math:`v_t` terminal velocity in an infinite fluid obtained from Equation :eq:`v_t_general`

The Reynolds number :math:`Re_t` is based on the terminal velocity of the particle.

.. math::
  :label: Re_terminal

  Re_t = \frac{v_t D_{particle}}{\nu}

The fluidization index, z, is a function of the Reynolds number at the terminal velocity.

.. math::
  :label: fluidization_index

  z=\frac{0.65\left(2+0.5 Re_t^{0.65}\right)}{\left(1+0.5 Re_t^{0.65}\right)}

The following equation is used to find the porosity of a fluidized bed.

.. math::
  :label: fluidized_bed_porosity

  \phi=\left(\frac{\bar v_z}{v_{t_w}}\right)^{1 / z}\left(1-\phi_{\mathrm{SB}}\right)+\phi_{\mathrm{SB}}

| where
| :math:`v_{t_w}` particle terminal velocity corrected for wall effect
| :math:`\bar v_z` superficial liquid velocity (our upflow velocity)
| :math:`z` is the fluidization index
| :math:`\phi_{\mathrm{SB}}` is the static bed pore volume fraction which we will assume is 0.4
