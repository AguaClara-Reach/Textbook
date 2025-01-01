.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Rapid_Mix/RM_Theory_and_Future_Work.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Rapid_Mix_Theory_and_Future_Work:

********************************
Rapid Mix Theory and Future Work
********************************


Our understanding of the coagulant nanoparticle attachment to suspended particles and dissolved species is currently quite speculative. This is an area that requires substantial research and modeling because it has the potential to significantly influence the design of flocculators. We have anecdotal evidence that the process of transporting coagulant nanoparticles to suspended particle surfaces may be a slow, rate-limiting process, especially when coupled with high rate flocculators. Dissolved organic matter may slow the rate of coagulant nanoparticle transport by effectively increasing the size of the coagulant nanoparticles and thus reducing the diffusion rate.

Developing a fundamental understanding of the mixing and transport processes that occur between coagulant addition and flocculation is a very high priority for the AguaClara program.

.. _heading_Diffusion_and_Shear_Transport_Coagulant_Nanoparticles_to_Clay:

Diffusion and Shear Transport Coagulant Nanoparticles to Clay
================================================================

The time required for shear and diffusion to transport coagulant nanoparticles to clay has previously been assumed to be a rapid process.

Our analysis suggests that this critical step may require significant time especially given our effort to reduce the time allotted for flocculation.

  - Turbulent eddies, viscous shear, and diffusion blends the coagulant with the raw water sufficiently (:ref:`in a few seconds<heading_Mixing_time>`) so that the coagulant precipitates and forms nanoparticles.
  - Dissolved organic molecules diffuse to the coagulant nanoparticles and adhere to the nanoparticle surface.
  - The coagulant nanoparticles are transported to suspended particle surfaces by a combination of diffusion and fluid shear.

The following is a very preliminary estimate of the time required for attachment of the nanoparticles to the clay particles. This analysis includes multiple simplifying assumptions and there is a reasonable possibility that some of those assumptions are wrong. However, the core assumption that coagulant nanoparticles are transported to clay particles by a combination of fluid deformation (shear) and molecular diffusion is reasonable.

The following analysis is similar to the collision analysis that was developed in the AguaClara flocculation model. The core idea is that viscous shear dominated fluid deformation causes relative motion between the coagulant nanoparticles and the clay particles (or other suspended particles) with which they eventually will collide. The collision between these particles that are very different in size is difficult to achieve because there is a viscous layer of fluid around the clay particles that the clay particles drag with them as they rotate in deforming fluid. Diffusion helps transport the coagulant nanoparticles through this viscous layer.

The volume of the suspension that is cleared of nanoparticles is proportional to a collision area defined by a ring around the clay particles with width of the diameter of the nanoparticle diffusion band. This diffusion band is the length scale over which diffusion is able to transport coagulant particles to the clay surface during the time that the nanoparticles are sliding past the clay particles.

If we go backwards in time, the ring of fluid around the clay particles would deform into two separate highly distorted volumes of fluid, one located to the left of the clay particle and one to the right (see figure :numref:`figure_Coagulant_nanoparticle_clay_collisions`). This volume of fluid is assumed to receive nanoparticles that are transported in by fluid deformation.

.. _figure_Coagulant_nanoparticle_clay_collisions:

.. figure:: /Images/Coagulant_nanoparticle_clay_collisions.png
    :width: 400px
    :align: center
    :alt: Coagulant nanoparticle clay collisions

    Fluid deformation moves coagulant nanoparticles close to clay particles and diffusion helps transport the nanoparticles the last nanometers toward a successful collision.

The time required for shear to transport all of the fluid past the clay so that diffusion can transport the coagulant nanoparticles to the clay surface is significant. The diffusion coefficient for coagulant nanoparticles is given by

.. math:: D_{Diffusion} = \frac{k_B T}{3 \pi \mu d_{CN}}

where :math:`d_{cn}` is the diameter of the coagulant nanoparticles. The length scale over which diffusion is occurring can be estimate from the diffusion coefficient and the time allotted.

.. math::
  :label: Diffusion_Length_scale

   L_{Diff} \approx \sqrt{D_{Diffusion} t_{Diffusion}}

The time for coagulant nanoparticles to diffuse through the boundary layer around the clay particles is equal to the distance they travel around the clay particles divided by their velocity. The distance they travel scales with :math:`d_{Clay}` and their average velocity scales with the thickness of the diffusion layer/2 \* the velocity gradient.

.. math::
  :label: Diffusion_Layer_time

   t_{Diffusion} = \frac{ 2d_{Clay}} {L_{Diff} G}

We can eliminate the diffusion time in Equation :eq:`Diffusion_Length_scale` using Equation :eq:`Diffusion_Layer_time`.

.. math:: L_{Diff} \approx \left( \frac{2k_B T d_{Clay}}{3 \pi \,\mu  \, d_{CN} G}\right)^\frac{1}{3}

This diffusion layer thickness is the length scale over which diffusion becomes the dominant transport mechanism for coagulant nanoparticles. Let’s estimate the diffusion layer thickness.

 `Colab worksheet to estimate the diffusion layer thickness <https://colab.research.google.com/drive/1tq6eHiIw47JGIPd4P_16AsewbC5GsEMk#scrollTo=xLb8eJza5gs0&line=1&uniqifier=1>`_.

.. _figure_Diffusion_band_thickness:

.. figure:: /Images/Diffusion_band_thickness.png
  :width: 400px
  :align: center
  :alt: Diffusion band thickness

  Molecular diffusion band thickness as a function of velocity gradient. This length scale marks the transition between transport by fluid deformation and by diffusion.

Diffusion transports the coagulant nanoparticles a relatively short distance, a fraction of a :math:`\mu m`.

We need to calculate the rate at which coagulant nanoparticles attach to the clay particles. The long range transport is assumed to be the rate limiting step. The volume cleared is proportional to the area of this ring with the ring thickness equal to the molecular diffusion band thickness. Here we assume that the :math:`L_{Diff_{CN}} << d_{Clay}`

.. math:: {\forall_{\rm{Cleared}}} \propto \pi \, d_{Clay} \, L_{Diff_{CN}}

The volume cleared is proportional to time.

.. math:: {\forall_{\rm{Cleared}}} \propto t

The volume cleared is proportional to the relative velocity between clay and nanoparticles. This relative velocity is in the viscous layer of fluid in the ring surrounding the clay particle.

.. math:: {\forall_{\rm{Cleared}}} \propto v_r

We use dimensional analysis to get a relative velocity for the long range transport controlled by shear. The relative velocity between coagulant nanoparticles and the clay particles that they will eventually collide with is assumed to be proportional to the average distance between clay particles. This assumption is both critical for the following derivation and is suspect. It is critical because if we were to assume that the relative velocity caused by shear is proportional to the nanoparticle diameter, the clay diameter, or the diffusion length scale, then the velocity would be extremely small and the time to clear the volume of fluid associated with one clay particle would take a very long time. However, wishing for a speedy process doesn't justify incorrect scaling. The relative velocity is assumed to be the velocity at which coagulant nanoparticles are transported into the two separate fluid volumes that will deform into the ring around the clay particles in the next few seconds.

The assumption that the relative velocity scales with the average distance between clay particles leads to the following steps. The first step is just a proposed functional relationship. We could also have jumped to the assumption that the relative velocity is a function of the length scale and the velocity gradient.

.. math:: v_r = f \left( \varepsilon ,\nu ,\Lambda_{Clay} \right)

In a uniform shear environment the velocity gradient is linear. Thus the relative velocity must be proportional to the length scale.

.. math:: v_r = \Lambda_{Clay} f \left( \varepsilon ,\nu \right)

The only way to for :math:`\varepsilon` and :math:`\nu` to produce dimensions of time is to combine them to create 1/G.

.. math:: v_r \approx \Lambda_{Clay} G

Combining the three equations for :math:`{\forall_{\rm{Cleared}}}` and the equation for :math:`v_r` we obtain the volume cleared as a function of time.

.. math::  {\forall_{\rm{Cleared}}} \approx \pi  d_{Clay} \, L_{Diff_{CN}}  \Lambda_{Clay} G  t_c


.. _heading_Collision_Rates:

Collision Rates and Particle Removal
=====================================

The time for all of the fluid to have had one opportunity for a collision occurs when:

.. math:: {\forall_{\rm{Cleared}}} = {\forall_{\rm{Occupied}}} = \Lambda_{Clay}^3

.. math:: t_c = \frac{\Lambda_{Clay}^3}{\pi d_{Clay} L_{Diff_{CN}} \Lambda_{Clay} G}

The successful collision rate (the attachment rate) is given by:

.. math:: \frac{dN_c}{dt} = \frac{1}{t_c}

Substitute the equation for :math:`t_c`.

.. math:: dN_c = \pi d_{Clay} L_{Diff_{CN}}{\Lambda^{-2}_{Clay}} G dt

A fraction of the remaining coagulant nanoparticles are removed during the time required for one sweep past the clay particles.

.. math:: \frac{dn_{CN}}{ - k \, n_{CN}} = dN_c

.. math:: \frac{dn_{CN}}{ - k \, n_{CN}} = \pi d_{Clay} L_{Diff_{CN}}{\Lambda^{-2}_{Clay}} G dt

Integrate from the initial coagulant nanoparticle concentration to the concentration at time t.

.. math:: \int \limits_{n_{CN_0}}^{n_{CN}} n_{CN}^{- 1} \, dn_{CN}  =  - \pi d_{Clay} L_{Diff_{CN}} \Lambda^{-2}_{Clay} G \, k  \int \limits_0^t {dt}

Use pC notation to be consistent with how we describe removal efficiency of other contaminants.

.. math:: 2.3 p C_{CN} = \pi d_{Clay}\,  L_{Diff_{CN}}\,  \Lambda^{-2}_{Clay}\,  G k  t

Solve for the time required to reach a target efficiency of application of coagulant nanoparticles to clay.

.. math::

  t_{coagulant, \, application} = \frac{2.3p C_{CN} \Lambda_{Clay}^2}{\pi G k \, d_{Clay}  L_{Diff_{CN}} }

If we assume that we are willing to invest a certain amount of energy in the process, then we can estimate the time required to achieve a target coagulant nanoparticle application efficiency. The velocity gradient in the reactor where the coagulant is attaching to the clay particles is related to the head loss or drop in water level, :math:`\Delta h`, through the reactor.

.. math::  \Delta h =  \frac{G^2 \nu \theta}{g}

Replace :math:`\theta` with :math:`t_{coagulant, \, application}`.

.. math::  \Delta h =  \frac{G^2 \nu}{g} \frac{2.3p C_{CN} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}\,  L_{Diff_{CN}} }

.. math:: L_{Diff} \approx \left( \frac{2k_B T d_{Clay}}{3 \pi \,\mu  \, d_{CN} G}\right)^\frac{1}{3}

.. math::  \Delta h =  \frac{G^2 \nu}{g} \frac{2.3p C_{CN} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}} \left( \frac{3 \pi \,\mu  \, d_{CN} G}{2k_B T d_{Clay}}\right)^\frac{1}{3}

Solve for the velocity gradient.

.. math::  \Delta h =  \frac{G^\frac{4}{3} \nu}{g} \frac{2.3p C_{CN} \, \Lambda_{Clay}^2}{\pi k \, d_{Clay}} \left( \frac{3 \pi \,\mu  \, d_{CN} }{2k_B T d_{Clay}}\right)^\frac{1}{3}

.. math::


  G_{coagulant, \, application} =  d_{Clay}\left(\frac{\pi k \,g\Delta h }{2.3p C_{CN} \, \Lambda_{Clay}^2 \nu} \right)^\frac{3}{4} \left( \frac{2k_B T }{3 \pi \,\mu  \, d_{CN} }\right)^\frac{1}{4}




Using the equation for :math:`L_{Diff}` above, we can solve for  the time required to reach a target efficiency of application of coagulant nanoparticles to clay:

.. math:: t_{coagulant, \, application} = \frac{2.3p C_{CN} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}\,  L_{Diff_{CN}} }

The time required for the coagulant to be transported to clay surfaces is strongly dependent on the turbidity as indicated by the average spacing of clay particles, :math:`\Lambda_{Clay}`. As turbidity increases the spacing between clay particles decreases and the time required for shear to transport coagulant nanoparticles to the clay decreases. Increasing the shear also results in faster transport of the coagulant nanoparticles to clay surfaces. The times required are strongly influenced by the size of the coagulant nanoparticles because larger nanoparticles diffuse more slowly.

`Colab worksheet estimating the time required to achieve 80% attachment of nanoparticles in a 10 NTU clay suspension in a reactor with a G of 100 Hz <https://colab.research.google.com/drive/1tq6eHiIw47JGIPd4P_16AsewbC5GsEMk#scrollTo=FiqAt0PF6L1t&line=13&uniqifier=1>`_.

.. _figure_Coag_attach_time:

.. figure:: /Images/Coag_attach_time.png
  :width: 400px
  :align: center
  :alt: Coag attach time

  An estimate of the time required for 80% of the coagulant nanoparticles to attach to clay particles given a raw water turbidity of 10 NTU.


.. _heading_Energy_Tradeoff_for_Coagulant_Transport:

Energy Tradeoff for Coagulant Transport
========================================

.. math::  \Delta h =  \frac{G^2 \nu \theta}{g}

`This code <https://colab.research.google.com/drive/1tq6eHiIw47JGIPd4P_16AsewbC5GsEMk#scrollTo=lSrjJEAT6-Gd&line=8&uniqifier=1>`_ shows how the following plot can be generated

.. _figure_Coag_attach_head_loss:

.. figure:: /Images/Coag_attach_head_loss.png
    :width: 400px
    :align: center
    :alt: Coag attach head loss

    The total energy required to attach coagulant nanoparticles to raw water inorganic particles increases rapidly with the velocity gradient used in the rapid mix process.

There is an economic tradeoff between reactor volume and energy input. The reactor volume results in a higher capital cost and the energy input requires both higher operating costs and higher capital costs. This provides an opportunity to optimize rapid mix design once we have a confirmed model characterizing the process.

The total potential energy used to operate an AguaClara plant is approximately 2 m. This represents the difference in elevation between where the raw water enters the plant and where the filtered water exits the plant. If we assume that the rapid mix energy budget is a fraction of that total and thus for subsequent analysis we will assume somewhat arbitrarily that the energy available to attach the coagulant nanoparticles to the raw water particles is 50 cm.

We solve the coagulant transport model,
:math:`t_{coagulant, \, application} = \frac{2.3p C_{CN} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}\, L_{Diff_{CN}} }`,
for G given a head loss.

.. math:: G_{coagulant, \, application} =  d_{Clay}\left(\frac{\pi k \,g\Delta h }{2.3p C_{CN} \, \Lambda_{Clay}^2 \nu} \right)^\frac{3}{4} \left( \frac{2k_B T }{3 \pi \,\mu  \, d_{CN} }\right)^\frac{1}{4}



`The maximum velocity gradient <https://colab.research.google.com/drive/1tq6eHiIw47JGIPd4P_16AsewbC5GsEMk#scrollTo=6cWi2zks8tiD&line=10&uniqifier=1>`_  that can be used to achieve 80% coagulant nanoparticle attachment using 50 cm of head loss is 283 Hz. This requires a residence time of 61 seconds. These model results must be experimentally verified and it is very likely that the model will need to be modified.

The analysis of the time required for shear and diffusion to transport the coagulant nanoparticles the last few millimeters suggests that it is the last step of diffusion to the clay particles that requires the most time. Indeed, the time required for coagulant nanoparticle attachment to raw water particles is comparable to the time that will be required for the next step in the process, flocculation.

.. _heading_Coagulant_Attachment_Mechanism:

Coagulant Attachment Mechanism
===============================
We do not yet understand the origin of the bonds that form between coagulant nanoparticles, between a coagulant nanoparticle and a suspended particle, and between coagulant nanoparticles and dissolved organic molecules. Historically the role of the coagulant was assumed to be to reduce the repulsive force between particles so that the particles could get close enough for Van der Waals forces to hold the particles together. That neglected the fact that Van der Waals forces were already acting between the water molecules and the suspended particle surfaces. In order for the water molecules to be pushed out of the way it is necessary for the coagulant nanoparticles to have stronger bonds with the suspended particles than the bonds between water molecules and the suspended particles.

The water molecules are subject to Brownian motion and thus it is possible that they are frequently vibrated free from the Van der Waals attractive forces. The coagulant nanoparticles are much larger, less affected by Brownian motion, and thus less likely to be vibrated. The fractal nature of the coagulant nanoparticles may also make it possible for multiple well aligned connections between the two surfaces. The fractal tentacles of the coagulant nanoparticle can align as needed to enable many strong bonding connections to the clay surface.
