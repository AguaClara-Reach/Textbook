.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Fluids_and_Hydraulics/Fluid_Mechanics_Derivations.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_review_fluid_mechanics_derivations:

***************************************************
Fluid Mechanics Derivations
***************************************************



.. _heading_minor_loss_equation_derivation:

Minor Loss Equation
===================

This section contains the derivation of the minor loss equation using the following figure as a reference. The derivation begins with a slightly simplified energy equation across the control volume shown. Our energy equation begins with :math:`h_P` and :math:`h_T` having been
eliminated.

.. _figure_minor_loss_pipe:

.. figure:: /Images/minor_loss_pipe.png
    :width: 700px
    :align: center
    :alt: Example of flow expansion resulting in a minor loss

    This is the system we will use to derive the minor loss equation.

.. math::

   \frac{p_{in}}{\rho g} + {z_{in}} + \frac{\bar v_{in}^2}{2g} = \frac{p_{out}}{\rho g} + z_{out} + \frac{\bar v_{out}^2}{2g} + h_L

Since the elevations at the center of the :math:`in` and :math:`out` control surfaces are the same, we can eliminate :math:`z_{in}` and :math:`z_{out}`. As we are considering such a small length of pipe, we will neglect the major loss component of head loss. Thus, :math:`h_L = h_e + \cancel{h_f}`. The following three equations are all the same, simply rearranged to solve for :math:`h_e`.

.. math::

   \frac{p_{in}}{\rho g} + \frac{\bar v_{in}^2}{2g} = \frac{p_{out}}{\rho g} + \frac{\bar v_{out}^2}{2g} + h_e

.. math::

   \frac{p_{in} - p_{out}}{\rho g} = \frac{\bar v_{out}^2 - \bar v_{in}^2}{2g} + h_e

.. math::
  :label: minor_loss_energy_eq

    h_e = \frac{p_{in} - p_{out}}{\rho g} + \frac{\bar v_{in}^2 - \bar v_{out}^2}{2g}

This last equation has :math:`h_e` as a function of four variables :math:`(p_{in}, \, p_{out}, \, v_{in}`, and :math:`v_{out})`; we would like it to be a function of only one. Thus, we will invoke conservation of momentum in the horizontal direction across our control volume to remove variables. The difference in momentum from the :math:`in` point to the :math:`out` point is driven by the pressure difference between each end of the control volume. We will be considering the pressure at the centroid of our control surfaces, and we will neglect shear along the pipe walls. After these assumptions, our momentum equation becomes the following:

.. math::

    M_{in, \, x} + M_{out, \, x} = F_{p_{in, \, x}} + F_{p_{out, \, x}}

| Such that:
| :math:`M_{x}` = momentum flowing through the control volume in the x-direction
| :math:`F_{p_x}` = force due to pressure acting on the boundaries of the control volume in the x-direction

Recall that momentum is mass times velocity for solids, :math:`m v`, with units of :math:`\frac{[M][L]}{[T]}`. Since we consider water flowing through a pipe, there is not one singular mass or one singular velocity. Instead, there is a mass flow rate, or a mass per time indicated by :math:`\dot m = \rho Q`, which has units of :math:`\frac{[M]}{[T]}`. Therefore, the momentum for a fluid is :math:`\rho Q \bar v`. Applying the continuity Equation :math:`Q = \bar v A`, we get to the following equation for the momentum of a fluid flowing through a pipe which we will use in this derivation, :math:`M = \rho \bar v^2 A`. The pressure force is simply the pressure at the centroid of the flow multiplied by the area the pressure is acting upon, :math:`p A`.

To ensure correct sign convention, we will make each side of the equation negative for reasons discussed shortly. Since :math:`\bar v_{in} > \bar v_{out}`, the left hand side will be :math:`M_{out} - M_{in}` in order to be negative. The reduction in velocity from :math:`in` to :math:`out` causes an increase in pressure, therefore :math:`p_{in} - p_{out}` is negative. With these substitutions, the conservation of momentum equation becomes as follows:

.. math::

    M_{out} - M_{in} = p_{in} - p_{out}

.. math::

   \rho \bar v_{out}^2 A_{out} - \rho \bar v_{in}^2 A_{in} = p_{in} A_{out} - p_{out} A_{out}

Note that the area term attached to :math:`p_{in}` is actually :math:`A_{out}` instead of :math:`A_{in}`, as one might think. This is because :math:`A_{out} = A_{in}`. We chose our control volume to start a few millimeters into the larger pipe, which means that the cross-sectional area does not change over the course of the control volume.

Dividing both sides of the equation by :math:`A_{out} \rho g`, we obtain the following equation, which contains the very same pressure term as our adjusted energy equation above, Equation :eq:`minor_loss_energy_eq`. This is why we chose a negative sign convention.

.. math::

   \frac{p_{in} - p_{out}}{\rho g} = \frac{\bar v_{out}^2 - \bar v_{in}^2 \frac{A_{in}}{A_{out}}}{g}

Now, we combine the momentum, continuity, and adjusted energy equations:

.. math::

    {\rm{Energy \, equation:}} \,\,\,  h_e = \frac{p_{in} - p_{out}}{\rho g} + \frac{\bar v_{in}^2 - \bar v_{out}^2}{2g}

.. math::

    {\rm{Momentum \, equation:}} \,\,\, \frac{p_{in} - p_{out}}{\rho g} = \frac{\bar v_{out}^2 - \bar v_{in}^2 \frac{A_{in}}{A_{out}}}{g}

.. math::

    {\rm{Continuity \, equation:}} \,\,\, \frac{A_{in}}{A_{out}} = \frac{\bar v_{out}}{\bar v_{in}}

To obtain an equation for minor losses with just two variables, :math:`\bar v_{in}` and :math:`\bar v_{out}`.

.. math::

    h_e = \frac{\bar v_{out}^2 - \bar v_{in}^2\frac{\bar v_{out}}{\bar v_{in}}}{g} + \frac{\bar v_{in}^2 - \bar v_{out}^2}{2g}

Now we will combine the two terms. The numerator and denominator of the first term, :math:`\frac{\bar v_{out}^2 - \bar v_{in}^2\frac{\bar v_{out}}{\bar v_{in}}}{g}` will be multiplied by :math:`2` to become :math:`\frac{2 \bar v_{out}^2 - 2 \bar v_{in}^2\frac{\bar v_{out}}{\bar v_{in}}}{2 g}`. The equation then looks like:

.. math::

    h_e = \frac{\bar v_{out}^2 - 2 \bar v_{in} \bar v_{out} + \bar v_{in}^2}{2g}


.. _heading_final_minor_loss_equations:

Final Forms of the Minor Loss Equation
--------------------------------------

Factoring the numerator yields to the first ‘final’ form of the minor loss equation:

.. math::

    {\rm{ \mathbf{First \, form:} }} \quad h_e = \frac{\left( \bar v_{in}  - \bar v_{out} \right)^2}{2g}

From here, the two other forms of the minor loss equation can be derived by solving for either :math:`\bar v_{in}` or :math:`\bar v_{out}` using the ubiquitous continuity Equation :math:`\bar v_{in} A_{in} = \bar v_{out} A_{out}`:

.. math::

    {\rm{ \mathbf{Second \, form:} }} \quad h_e = \left( 1 - \frac{A_{in}}{A_{out}} \right)^2 \, \frac{\bar v_{in}^2}{2g} \, \, = \, \, K_e^{'} \frac{\bar v_{in}^2}{2g}, \quad {\rm where} \quad K_e^{'} = \left( 1 - \frac{A_{in}}{A_{out}} \right)^2

.. math::
 :label: minor_loss_equation


    {\rm{ \mathbf{Third \, form:} }} \quad h_e = \left( \frac{A_{out}}{A_{in}} -1 \right)^2 \, \frac{\bar  v_{out}^2}{2g} \, \, = \, \, K_e \frac{\bar v_{out}^2}{2g}, \quad {\rm where} \quad K_e = \left( \frac{A_{out}}{A_{in}} - 1 \right)^2


You will often see :math:`K_e^{'}` and :math:`K_e` used without the :math:`e` subscript, they will appear as :math:`K^{'}` and :math:`K`.

Being familiar with these three forms and how they are used will be of great help throughout the class. The third form is the one that is most commonly used.

We can convert the minor loss coefficient, :math:`K_e`, into a flow contraction using the minor loss equation (see Equation :eq:`minor_loss_equation`)

.. math::
  :label: minor_K_of_pi_vc

   K_e = \left(\frac{1}{\Pi_{vc}}  - 1 \right)^2

where :math:`\Pi_{vc}` is the ratio of the contracted area to the full expanded flow area.

.. math::
  :label:

  \Pi_{vc} = \frac{A_{in}}{A_{out}}

Given that :math:`\Pi_{vc}` is the ratio of the contracted area to the full expanded flow area we obtain the relationship between the contracted diameter, :math:`D_{vc}`, and the expanded diameter, :math:`D_{pipe}`.

.. math::
  :label: D_pipe_of_D_vc

  D_{pipe} = \frac{D_{vc}}{\sqrt{\Pi_{vc}}}

Solving Equation :eq:`minor_K_of_pi_vc` for :math:`\Pi_{vc}` we obtain

.. math::
  :label: pi_vc_of_minor_K

  \Pi_{vc} = \frac{1}{\sqrt{K_e} + 1}

The extent of a flow contraction, :math:`\Pi_{vc}` can be estimated from the measured minor loss coefficient.
