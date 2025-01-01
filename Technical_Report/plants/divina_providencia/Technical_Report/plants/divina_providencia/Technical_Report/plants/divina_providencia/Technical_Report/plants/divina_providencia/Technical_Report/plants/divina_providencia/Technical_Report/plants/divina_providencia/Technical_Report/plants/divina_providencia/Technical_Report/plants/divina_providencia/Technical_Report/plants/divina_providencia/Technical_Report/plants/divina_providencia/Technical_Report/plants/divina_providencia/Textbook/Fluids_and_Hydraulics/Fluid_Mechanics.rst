.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Fluids_and_Hydraulics/Fluid_Mechanics.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_review_fluid_mechanics:

***********************
Fluid Mechanics
***********************

This chapter is meant to be a refresher on fluid mechanics. It will only cover the topics in fluids mechanics that will be used heavily in the course.

If you wish to review fluid mechanics in (much) more detail, please refer to `this guide <https://github.com/AguaClara/CEE4540_Master/wiki/Fluids-Review-Guide>`_. Note that to view this link, you will need a Github account. If you wish to review from a textbook, you can find a pdf of a good fluid mechanics textbook by Frank White `here <http://ftp.demec.ufpr.br/disciplinas/TM240/Marchi/Bibliografia/White_2011_7ed_Fluid-Mechanics.pdf>`_.

.. _heading_introductory_concepts:

Introductory Concepts
=====================

Before diving in to the rest of this document, there are a few important concepts to focus on which will be the foundation for building your understanding of fluid mechanics. One must walk before they can run, and similarly, the basics of fluid mechanics must be understood before moving on to the more fun (and exciting!) sections of this document.


.. _heading_continuity_equation:

Continuity Equation
-------------------

Continuity is simply an application of mass balance to fluid mechanics. It states that the cross sectional area :math:`A` that a fluid flows through multiplied by the fluid’s average flow velocity :math:`\bar v` must equal the fluid’s flow rate :math:`Q`:

.. math::
  :label: continuity_equation

    Q = \bar v A

.. note:: The line above the :math:`v` is called a ‘bar,’ and represents an average. Any variable can have a bar. In this case, we are adding the bar to velocity :math:`v`, turning it into average velocity :math:`\bar v`. This variable is pronounced ‘v bar.’

In this course, we deal primarily with flow through pipes. For a circular pipe, :math:`A = \pi r^2`. Substituting diameter in for radius, :math:`r = \frac{D}{2}`, we get :math:`A = \frac{\pi D^2}{4}`. You will often see this form of the continuity equation being used to relate a pipe's flow rate to its diameter and the velocity of the fluid flowing through it:

.. math::

    Q = \bar v \frac{\pi D^2}{4}

The continuity equation is also useful when flow is going from one geometry to another. In this case, the flow in one geometry must be the same as the flow in the other, :math:`Q_1 = Q_2`, which yields the following equations:

.. math::

   \bar v_1 A_1 = \bar v_2 A_2

.. math::

   \bar v_1 \frac{\pi D_1^2}{4} = \bar v_2 \frac{\pi D_2^2}{4}

| Such that:
| :math:`Q =` fluid flow rate
| :math:`\bar v =` fluid average velocity
| :math:`A =` pipe area
| :math:`r =` pipe radius
| :math:`D =` pipe diameter


An example of changing flow geometries is when a change in pipe size occurs in a circular piping system, as is demonstrated below. The flow through :math:`{\rm pipe} \, 1` must be the same as the flow through :math:`{\rm pipe} \, 2`.

.. _figure_continuity_pipes:

.. figure:: /Images/continuity_pipes.png
    :align: center
    :alt: internal figure

    Flow going from a small diameter pipe to a large one. The continuity principle states that the flow through each pipe must be the same.


.. _heading_laminar_and_turbulent_flow:

Laminar and Turbulent Flow
--------------------------

Considering that this class deals with the flow of water through a water treatment plant, understanding the characteristics of the flow is very important. Thus, it is necessary to understand the most common characteristic of fluid flow: whether it is **laminar** or **turbulent**. `Laminar <https://en.wikipedia.org/wiki/Laminar_flow>`_ flow is very smooth and highly ordered. `Turbulent <https://en.wikipedia.org/wiki/Turbulence>`_ flow is chaotic, messy, and disordered. The best way to understand each flow and what it looks like is visually, like in the Wikipedia figure below `or in this video <https://youtu.be/qtvVN2qt968?t=131>`_. Please ignore the part of the video after the image of the tap.

.. _figure_wikipedia_laminar_turbulent:

.. figure:: /Images/Wikipedia_laminar_turbulent.png
    :width: 400px
    :align: center
    :alt: Laminar flow, turbulent flow, and the transition

    This is a beautiful example of the difference between ordered and smooth laminar flow and chaotic turbulent flow.

A numeric way to determine whether flow is laminar or turbulent is by finding the `Reynolds number <https://en.wikipedia.org/wiki/Reynolds_number>`_, :math:`{\rm Re}`. The Reynolds number is a dimensionless parameter that compares inertia, represented by the average flow velocity :math:`\bar v` times a length scale :math:`D` to `viscosity <https://en.wikipedia.org/wiki/Viscosity>`_, represented by the kinematic viscosity :math:`\nu`. `Click here <https://www.youtube.com/watch?v=DVQw0svRHZA>`_ for a brief video explanation of viscosity. If the Reynolds number is less than 2,100 the flow is considered laminar. If it is more than 2,100, it is considered turbulent.

.. math::

    {\rm Re = \frac{inertia}{viscosity}} = \frac{\bar vD}{\nu}

`The transition between laminar and turbulent flow is not yet well understood <https://en.wikipedia.org/wiki/Laminar%E2%80%93turbulent_transition>`_, which is why the concept of transitional flow is often simplified and neglected to make it possible to code for laminar or turbulent flow, which are better understood. We will assume that the transition occurs at :math:`\rm{Re} = 2100`. In aguaclara, this parameter is ``pc.RE_TRANSITION_PIPE``.

Fluid can flow through very many different geometries, like a pipe, a rectangular channel, or any other shape. To account for this, the characteristic length scale for the Reynolds number, which was written in the equation above as :math:`D`, is quantified as the `hydraulic diameter <https://www.engineeringtoolbox.com/hydraulic-equivalent-diameter-d_458.html>`_, :math:`D_h` when considering a general cross-sectional area. For circular pipes, which are the most common geometry you’ll encounter in this class, the hydraulic diameter is simply the pipe's diameter, :math:`D_h = D`.

Here are other commonly used forms of the Reynolds number equation *for circular pipes*. They are the same as the one above, just with the substitutions :math:`Q = \bar v \frac{\pi D^2}{4}` and :math:`\nu = \frac{\mu}{\rho}`

.. math::
  :label: reynolds_number_equation

    {\rm Re} = \frac{\bar vD}{\nu} = \frac{4Q}{\pi D\nu} = \frac{\rho \bar vD}{\mu}

| Such that:
| :math:`Q` = fluid flow rate in pipe
| :math:`D` = pipe diameter
| :math:`\bar v` = fluid velocity
| :math:`\nu` = fluid kinematic viscosity
| :math:`\mu` = fluid dynamic viscosity

.. seealso:: **Function in aguaclara:** ``pc.re_pipe(FlowRate, Diam, Nu)`` Returns the Reynolds number *in a circular pipe*. Functions for finding the Reynolds number through other flow conduits and geometries can also be found in `physchem.py <https://github.com/AguaClara/aguaclara>`_ within aguaclara.

.. note:: **Definition of Flow Regimes:** Laminar and turbulent flow are described as two different **flow regimes**. When there is a characteristic of flow and different categories of the characteristic, each category is referred to as a flow regime. For example, the Reynolds number describes a flow characteristic, and its categories, referred to as flow regimes, are laminar or turbulent.


.. _heading_streamlines_and_control_volumes:

Streamlines and Control Volumes
-------------------------------

Both `streamlines <https://en.wikipedia.org/wiki/Streamlines,_streaklines,_and_pathlines>`_ and `control volumes <https://www.engineersedge.com/fluid_flow/control_volume.htm>`_ are tools to compare different parts of a system. For this class, this system will always be hydraulic.

Imagine water flowing through a pipe. A streamline is the path that a particle would take if it could be placed in the fluid without changing the original flow of the fluid. A more technical definition is “a line which is everywhere parallel to the local velocity vector.” Computational tools, `dyes (in water) <https://www.nuclear-power.net/wp-content/uploads/2016/05/Flow-Regime.png?4b884b>`_, or `smoke (in air) <https://www.youtube.com/watch?v=E9ZSAX56m0E&t=59s>`_ can be used to visualize streamlines.

A **control volume** is just an imaginary 3-dimensional shape in space. Its boundaries can be placed anywhere by the person applying the control volume, and once set the boundaries remain fixed in space over time. These boundaries are usually chosen to compare two relevant surfaces to each other. These surfaces are called *Control Surfaces*. The entirety of a control volume is usually not shown, as it is often unnecessary. This is demonstrated in the following image:

.. _figure_control_volume_simplification:

.. figure:: /Images/control_volume_simplification.png
    :width: 650px
    :align: center
    :alt: Control volume simplification

    While the image on the left indicates a complete control volume, control volumes are usually shortened to only include the relevant control surfaces, in which the control volume intersects the fluid. This is shown in the image on the right.

.. important:: Many images will be used over the course of this class to show hydraulic systems. A standardized system of lines will be used throughout them all to distinguish reference elevations from control volumes from streamlines. This system is described in the image below.

.. _figure_image_control_volumes:

.. figure:: /Images/image_control_volumes.png
    :width: 650px
    :align: center
    :alt: Image control volumes

    On the left, a control volume is applied to a hydraulic system. On the right, a streamline is applied to a hydraulic system. A figure-convention for control volumes and streamlines will be very helpful throughout this course as there will be very, very many figures.



.. _heading_bernoulli_and_energy_equations:

The Bernoulli and Energy Equations
==================================

As explained in almost every fluid mechanics class, the Bernoulli and energy equations are incredibly useful in understanding the transfer of the fluid’s energy throughout a streamline or through a control volume. The Bernoulli equation applies to two different points along one streamline, whereas the energy equation applies to fluid entering and exiting a control volume. The energy of a fluid has three forms: pressure, potential (deriving from elevation), and kinetic (deriving from velocity).


.. _heading_bernoulli_equation:

The Bernoulli Equation
----------------------

These three forms of energy expressed above make up the Bernoulli equation:

.. math::
  :label: bernoulli_equation

   \frac{p_1}{\rho g} + {z_1} + \frac{v_1^2}{2g} = \frac{p_2}{\rho g} + {z_2} + \frac{v_2^2}{2g}

| Such that:
| :math:`p` = pressure
| :math:`\rho` = fluid density
| :math:`g` = acceleration due to gravity
| :math:`z` = elevation relative to a reference
| :math:`v` = fluid velocity

Notice that each term in this form of the Bernoulli equation has units of :math:`[L]`, even though the terms represent the energy of the fluid, which has units of :math:`\frac{[M] \cdot [L]^2}{[T]^2}`. When energy of the fluid is described in units of length, the term used is called **head** and referred to as :math:`h`.

There are two important distinctions to keep in mind when using head to talk about a fluid's energy. First is that head is dependent on the density of the fluid under consideration. Take mercury, for example, which is around 13.6 times more dense than water. 1 meter of mercury head is therefore equivalent to around 13.6 meters of water head. Second is that head is independent of the amount of fluid being considered, *as long as all the fluid is the same density*. Thus, raising 1 liter of water up by one meter and raising 100 liters of water up by one meter are both equivalent to giving the water 1 meter of water head, even though it requires 100 times more energy to raise the hundred liters than to raise the single liter. Since we are concerned mainly with water in this class, we will refer to ‘water head’ simply as ‘head’.

Going back to the Bernoulli equation, the :math:`\frac{p}{\rho g}` term is called the pressure head, :math:`z` is called the elevation head, and :math:`\frac{v^2}{2g}` is the velocity head. The following diagram shows these various forms of head via a 1 meter deep bucket (left) and a jet of water shooting out of the ground (right).

.. _figure_different_forms_of_head:

.. figure:: /Images/different_forms_of_head.png
    :width: 650px
    :align: center
    :alt: Different forms of head

    The three forms of hydraulic head.

Though there are `many assumptions needed to confirm that the Bernoulli equation can be used <https://en.wikipedia.org/wiki/Bernoulli%27s_principle#Incompressible_flow_equation>`_, the main one for the purpose of this class is that energy is not gained or lost throughout the streamline being considered. If we consider more precise fluid mechanics terminology, then “friction by viscous forces must be negligible.” What this means is that the fluid along the streamline being considered is not losing energy to viscosity. As a result, using the Bernoulli equation implies that energy can’t be gained or lost. It can only be transferred between its three forms.

`Here is a simple worksheet with very straightforward example problems using the Bernoulli equation. <https://www.teachengineering.org/content/cub_/lessons/cub_bernoulli/cub_bernoulli_lesson01_bepworksheetas_draft4_tedl_dwc.pdf>`_ Note that the solutions use the pressure-form of the Bernoulli equation. This just means that every term in the equation is multiplied by :math:`\rho g`, so the pressure term is just :math:`P`. The form of the equation does not affect the solution to the problem it helps solved.

.. _heading_energy_equation:

The Control Volume Energy Equation
----------------------------------

The assumption necessary to use the Bernoulli equation, which is stated above, represents the key difference between the Bernoulli equation and the control volume energy equation for the purpose of this class. The energy equation accounts for the potential addition or loss of fluid energy within the control volume. (L)oss of energy is usually due to viscous friction resisting fluid flow, :math:`h_L`, or the charging of a (T)urbine, :math:`h_T`. The most common input of fluid energy into a system is usually caused by a (P)ump within the control volume, :math:`h_P`.

.. math::

   \frac{p_{1}}{\rho g} + z_{1} + \alpha_{1} \frac{\bar v_{1}^2}{2g} + h_P = \frac{p_{2}}{\rho g} + z_{2} + {\alpha_{2}} \frac{\bar v_{2}^2}{2g} + h_T + h_L

You’ll also notice the :math:`\alpha` term attached to the velocity head. This is a correction factor for kinetic energy, and will be neglected in this class; we assume that its value is 1. In the Bernoulli equation, the velocity of a streamline of the fluid is considered, :math:`v`. The energy equation, however compares control surfaces instead of streamlines, and the velocities across a control surface may not all be the same. Hence, :math:`\bar v` is used to represent the average velocity. Since AguaClara does not use pumps nor turbines, :math:`h_P = h_T = 0`. With these simplifications, the energy equation can be written as follows:

.. math::
  :label: energy_equation

   \frac{p_{1}}{\rho g} + z_{1} + \frac{\bar v_{1}^2}{2g} = \frac{p_{2}}{\rho g} + z_{2} + \frac{\bar v_{2}^2}{2g} + h_L

**This is the form of the energy equation that you will see over and over again in this book.** To summarize, the main difference between the Bernoulli equation and the energy equation for the purposes of this class is energy loss. The energy equation accounts for the fluid’s loss of energy over time while the Bernoulli equation does not. So how can the fluid lose energy?

.. _heading_head_loss:

Head Loss
=========

**Head (L)oss**, :math:`h_L` is a term that is ubiquitous in both this class and fluid mechanics in general. Its definition is exactly as it sounds: it refers to the loss of energy of a fluid as it flows through space. There are two components to head loss: major losses caused by (f)riction between the fluid and the surface it's flowing over, :math:`h_{\rm{f}}`, and minor losses caused by fluid-fluid internal friction resulting from flow (e)xpansions, :math:`h_e`. These two components combine such that :math:`h_L = h_{\rm{f}} + h_e`.


.. _heading_major_losses:

Major Losses
------------

These losses are the result of friction between the fluid and the surface over which the fluid is flowing. A force acting parallel to a surface is referred to as `shear <https://en.wikipedia.org/wiki/Shear_force>`_. It can therefore be said that major losses are the result of shear between the fluid and the surface it’s flowing over. To help in understanding major losses, consider the following example: imagine, as you have so often in physics class, pushing a large box across the ground. Friction is what resists your efforts to push the box. The farther you push the box, the more energy you expend pushing against friction. The same is true for water moving through a pipe, where water is analogous to the box you want to move, the pipe is similar to the floor that provides the friction, and the major losses of the water through the pipe is analogous to the energy **you** expend by pushing the box.

In this class, we will be dealing primarily with major losses in circular pipes, as opposed to channels or pipes with other geometries. Fortunately for us, Henry Darcy and Julius Weisbach came up with a handy equation to determine the major losses in a circular pipe *under both laminar and turbulent flow conditions*. Their equation is logically and unoriginally named the `Darcy-Weisbach equation <https://en.wikipedia.org/wiki/Darcy%E2%80%93Weisbach_equation>`_. It is shown below:

.. math::
  :label: darcy_weisbach

    h_{\rm{f}} \, = \, {\rm{f}} \frac{L}{D} \frac{\bar v^2}{2g}

Substituting the continuity Equation :math:`Q = \bar vA` in the form of :math:`\bar v^2 = \frac{16Q^2}{\pi^2 D^4}` gives another, equivalent form of Darcy-Weisbach which uses flow, :math:`Q`, instead of velocity, :math:`\bar v`:

.. math::

    h_{\rm{f}} \, = \,{\rm{f}} \frac{8}{g \pi^2} \frac{LQ^2}{D^5}

| Such that:
| :math:`h_{\rm{f}}` = major loss
| :math:`\rm{f}` = Darcy friction factor
| :math:`L` = pipe length
| :math:`Q` = pipe flow rate
| :math:`D` = pipe diameter

.. seealso:: **Function in aguaclara:** ``pc.headloss_fric(FlowRate, Diam, Length, Nu, PipeRough)`` Returns only major losses. Works for both laminar and turbulent flow. PipeRough describes the pipe roughness :math:`\epsilon` described shortly below.

Darcy-Weisbach is wonderful because it applies to both laminar and turbulent flow regimes and contains relatively easy to measure variables. The one exception is the Darcy friction factor, :math:`\rm{f}`. This parameter is an approximation for the magnitude of friction between the pipe walls and the fluid, and its value changes depending on the whether or not the flow is laminar or turbulent, and varies with the Reynolds number in both flow regimes.

For laminar flow, the friction factor can be determined from the following equation:

.. math::

    {\rm{f}} = \frac{64}{\rm{Re}}

For turbulent flow, the friction factor is more difficult to determine. In this class, we will use the `Swamee-Jain equation <https://en.wikipedia.org/wiki/Darcy_friction_factor_formulae#Swamee%E2%80%93Jain_equation>`_:

.. math::
  :label: swamee_jain

    {\rm{f}} = \frac{0.25} {\left[ \log \left( \frac{\epsilon }{3.7D} + \frac{5.74}{{\rm Re}^{0.9}} \right) \right]^2}

| Such that:
| :math:`\epsilon` = pipe roughness, :math:`[L]`
| :math:`D` = pipe diameter, :math:`[L]`

.. seealso:: **Function in aguaclara:** ``pc.fric(FlowRate, Diam, Nu, PipeRough)`` Returns :math:`\rm{f}` for laminar *or* turbulent flow. For laminar flow, use zero for the ``PipeRough`` input.

The simplicity of the equation for :math:`\rm{f}` during laminar flow allows for substitutions to create a very useful, simplified equation for major losses during laminar flow. This simplification combines the Darcy-Weisbach equation, the equation for the Darcy friction factor during laminar flow, and the Reynold’s number formula:

.. math::

    h_{\rm{f}} \, = \,{\rm{f}} \frac{8}{g \pi^2} \frac{LQ^2}{D^5}

.. math::

    {\rm{f}} = \frac{64}{\rm{Re}}

.. math::

    {\rm{Re}}=\frac{4Q}{\pi D\nu}

To form the `Hagen-Poiseuille equation <https://en.wikipedia.org/wiki/Hagen%E2%80%93Poiseuille_equation>`_ for major losses during laminar flow, and *only* during laminar flow:

.. math::
  :label: hagen_poiseuille

    h_{\rm{f}} = \frac{128\mu L Q}{\rho g\pi D^4}

.. math::

    h_{\rm{f}} = \frac{32\nu L\bar v}{ g D^2}

The significance of this equation lies in its relationship between :math:`h_{\rm{f}}` and :math:`Q`. Hagen-Poiseuille shows that the terms are directly proportional (:math:`h_{\rm{f}} \propto Q`) during laminar flow, while Darcy-Weisbach shows that :math:`h_{\rm{f}}` grows with the square of :math:`Q` during turbulent flow (:math:`h_{\rm{f}} \propto Q^2`). As you will soon see, minor losses, :math:`h_e`, will grow with the square of :math:`Q` in both laminar and turbulent flow. This has implications that will be discussed in a future chapter: :ref:`title_flow_control_design`.

In 1944, Lewis Ferry Moody plotted a ridiculous amount of experimental data, gathered by many people, on the Darcy-Weisbach friction factor to create what we now call the `Moody diagram <https://en.wikipedia.org/wiki/Moody_chart>`_. This diagram makes it easy to find the friction factor :math:`f`. :math:`\rm{f}` is plotted on the left-hand y-axis, relative pipe roughness :math:`\frac{\epsilon}{D}` is on the right-hand y-axis, and Reynolds number :math:`\rm{Re}` is on the x-axis. The Moody diagram is an alternative to computational methods for finding :math:`\rm{f}`.

.. _figure_moody:

.. figure:: /Images/Moody.jpg
    :width: 650px
    :align: center
    :alt: Moody diagram

    This is the famous and famously useful Moody diagram.


.. _heading_minor_losses:

Minor Losses
------------

Unfortunately, there is no simple ‘pushing a box across the ground’ example to explain minor losses. So instead, consider a `hydraulic jump <https://www.youtube.com/watch?v=5spXXZX55C8>`_. In the video, you can see lots of turbulence and eddies in the transition region between the fast, shallow flow and the slow, deep flow. The high amount of mixing of the water in the transition region of the hydraulic jump results in significant friction *between water and water*. This turbulent, eddy-induced, fluid-fluid friction results in  minor losses, much like fluid-pipe friction results in major losses.

As occurs in a hydraulic jump, a flow expansion (from shallow flow to deep flow) creates the turbulent eddies that result in minor losses. This will be a recurring theme  throughout the course: **minor losses are caused by flow expansions**. Imagine a pipe fitting that connects a small diameter pipe to a large diameter one, as shown in :numref:`figure_minor_loss_pipe_FRD` below. The flow must expand to fill up the entire large diameter pipe. This expansion creates turbulent eddies near the union between the small and large pipes, and these eddies result in minor losses. You may already know the equation for minor losses, but understanding where it comes from is very important for effective AguaClara plant design. For this reason, you are strongly recommended to read through its full derivation: :ref:`title_review_fluid_mechanics_derivations`.

The general form of the minor loss equation is

.. math::
  :label: minor_loss

    h_e = K_e \frac{\bar v^2}{2g}

where :math:`\bar v` is a characteristic (and perhaps convenient) velocity that is typically based on the flow rate and the dimensions of the fully expanded flow. Thus minor loss coefficients, :math:`K_e` for flow through various pipe fittings are based on the average velocity in the pipe because that is easily known given the pipe internal diameter and the flow rate.

There are three forms of the minor loss equation that you will see in this class:

.. math::

    {\rm{ \mathbf{First \, form:} }} \quad h_e = \frac{\left( \bar v_{in}  - \bar v_{out} \right)^2}{2g}

.. math::
  :label: eq_exp_v_in

    {\rm{ \mathbf{Second \, form:} }} \quad h_e = \left( 1 - \frac{A_{in}}{A_{out}} \right)^2 \, \frac{\bar v_{in}^2}{2g} \, \, = \, \, K_e^{'} \frac{\bar v_{in}^2}{2g}, \quad {\rm where} \quad K_e^{'} = \left( 1 - \frac{A_{in}}{A_{out}} \right)^2

.. math::
  :label: eq_exp_v_out


    {\rm{ \mathbf{Third \, form:} }} \quad h_e = \left(\frac{A_{out}}{A_{in}} -1 \right)^2 \, \frac{\bar  v_{out}^2}{2g} \, \, = \, \, K_e \frac{\bar v_{out}^2}{2g}, \quad {\rm where} \quad K_e = \left( \frac{A_{out}}{A_{in}} - 1 \right)^2


| Such that:
| :math:`K_e^{'}, \,\, K_e` = minor loss coefficients, dimensionless

.. note:: You will most often see :math:`K_e^{'}` and :math:`K_e` used without the :math:`e` subscript,  as :math:`K^{'}` and :math:`K`.

.. seealso:: **Function in aguaclara:** ``pc.headloss_exp_general(Vel, KMinor)`` Returns :math:`h_e`. Can be either the second or third form due to user input of both velocity and minor loss coefficient. It is up to the user to use consistent :math:`\bar v` and :math:`K_e`.

.. seealso:: **Function in aguaclara:** ``pc.headloss_exp(FlowRate, Diam, KMinor)`` Returns :math:`h_e`. Uses third form, :math:`K_e`.

.. _figure_minor_loss_pipe_FRD:

.. figure:: /Images/minor_loss_pipe.png
    :width: 650px
    :align: center
    :alt: Minor loss displayed in a flow expansion

    The :math:`in` and :math:`out` subscripts in each of the three forms of the minor loss equation refer to this diagram that was used for the derivation.

The second and third forms are the ones which you are probably most familiar with. The distinction between them, however, is critical. First, consider the magnitudes of :math:`A_{in}` and :math:`A_{out}`. :math:`A_{in}` can never be larger than :math:`A_{out}`, because the flow is expanding. When flow expands, the cross-sectional area it flows through must increase. As a result, both :math:`\frac{A_{out}}{A_{in}} > 1` and :math:`\frac{A_{in}}{A_{out}} < 1` must always be true. This means that :math:`K^{'}` can never be greater than 1, while :math:`K` technically has no upper limit.

If you have taken CEE 3310, you have seen tables of minor loss coefficients `like this
one <https://www.engineeringtoolbox.com/minor-loss-coefficients-pipes-d_626.html>`_, and they almost all have coefficients greater than 1. This implies that these tables use the third form of the minor loss equation as we have defined it, where the velocity is :math:`\bar v_{out}`. There is a good reason for using the third form over the second one: :math:`\bar v_{out}` is far easier to determine than :math:`\bar v_{in}`. Consider flow through a pipe elbow, as shown in the image below.

.. _figure_minor_loss_elbow:

.. figure:: /Images/minor_loss_elbow.png
    :width: 650px
    :align: center
    :alt: Minor loss displayed in an elbow

    Flow around a pipe elbow results in a minor loss. 'Control surface 1' can be abbreviated as 'CS 1'

In order to find :math:`\bar v_{out}`, we first need to know what (or where) is :math:`out` and what is :math:`in`. A simple way to distinguish the two surfaces is that :math:`in` occurs when the flow is most contracted, and :math:`out` occurs when the flow has fully expanded after that maximal contraction. Going on these guidelines, Control surface '2' (CS 2) in the figure above would be :math:`in`, since it represents the most contracted flow in the elbow-pipe system. Therefore, CS 3 would be :math:`out`, as it represents the flow having fully expanded after its compression at CS 2.

:math:`\bar v_{out}` is easy to determine because it is the velocity of the fluid as it flows through the entire area of the pipe. Thus, :math:`\bar v_{out}` can be found with the continuity equation, since the flow through the pipe and its diameter are easy to measure, :math:`\bar v_{out} = \frac{4 Q}{\pi D^2}`. On the other hand, :math:`\bar v_{in}` is difficult to find, as the area of the contracted flow is dependent on the exact geometry of the elbow. This is why the third form of the minor loss equation, as we have defined it, is the most common:

.. math::
  :label: minor_loss_third_form

    h_e = K \frac{\bar v_{out}^2}{2g} = \,\,\,\, \left( \frac{A_{out}}{A_{in}} -1 \right)^2 \frac{\bar v_{out}^2}{2g}

.. note:: When considering a hydraulic system within a control volume, there can be many sources of minor losses. Instead of saying :math:`h_e = K_1 \frac{\bar v_{out}^2}{2g} + K_2 \frac{\bar v_{out}^2}{2g} + ...` we can simply lump all of the minor loss coefficients into one: :math:`\sum K = K_1 + K_2 + ...`. Thus, it is also common to see this form of the minor loss equation when finding the minor loss across control volumes: :math:`\sum K \frac{v_{out}^2}{2g}`.


.. _heading_head_loss_elevation_difference_trick:

The Head Loss Elevation Trick
-----------------------------

This trick, also called the ‘control volume trick,’ or more colloquially, the ‘head loss trick,’ is incredibly useful for simplifying hydraulic systems and is used all the time in this class.

Consider the following figure:

.. _figure_head_loss_trick:

.. figure:: /Images/head_loss_trick.png
    :width: 650px
    :align: center
    :alt: Image used to explain the head loss trick

    A typical hydraulic system can be used to understand the head loss trick.

In systems like this, where an elevation difference is causing water to flow, the elevation difference is called the **driving head**. In the system above, the driving head is the elevation difference between the water level and the end of the tubing. Usually, driving head is written as :math:`\Delta z` or :math:`\Delta h`, though above it is labelled as :math:`h_L`. Doesn't :math:`h_L` refer to head loss though? Yes it does! Referring to :math:`\Delta h` or :math:`\Delta z` *IS* the head loss trick, and how it works is explained in the following paragraphs and equations.

The figure is technically violating the energy equation by saying that the elevation difference between the water in the tank and the end of the tube is :math:`h_L`. It implies that all of the driving head, :math:`\Delta z`, is lost to head loss. Since all of the energy is gone, there should not be water flowing out of the tubing. But there is. Let’s apply the energy equation across the control surfaces shown in the figure. Pressures at both ends are atmospheric and the velocity of water at the top of tank is negligible.

.. math::

   \cancel{ \frac{p_{1}}{\rho g} } + z_{1} + \cancel{ \frac{\bar v_{1}^2}{2g} } = \cancel{ \frac{p_{2}}{\rho g} } + z_{2} + \frac{\bar v_{2}^2}{2g} + h_L

We now get:

.. math::

   \Delta z = \frac{\bar v_2^2}{2g} + h_L

This equation contradicts the figure above, which says that :math:`\Delta z = h_L` and neglects :math:`\frac{\bar v_2^2}{2g}`. The figure above is correct, however, if you apply the head loss trick. The trick incorporates the :math:`\frac{\bar v_2^2}{2g}` term *into* the :math:`h_L` term as a minor loss. See the math below:

.. math::

   \Delta z = \frac{\bar v_2^2}{2g} + h_e + h_f

.. math::

   \Delta z = \frac{\bar v_2^2}{2g} + \left( \sum K \right) \frac{\bar v_2^2}{2g} + h_f

.. math::

   \Delta z = \left( 1 + \sum K \right) \frac{\bar v_2^2}{2g} + h_f

.. math::

   \Delta z = \left( \sum K \right) \frac{\bar v_2^2}{2g} + h_f

This last step incorporated the kinetic energy term of the energy equation, :math:`\frac{\bar v_2^2}{2g}`, into the minor loss equation by saying that its :math:`K` is 1 and incorporating that 1 into :math:`\sum K`. From here, we reverse our steps to get :math:`\Delta z = h_L`, starting with :math:`h_e = \left( \sum K \right) \frac{\bar v_2^2}{2g}`

.. math::

   \Delta z = h_e + h_f

.. math::

   \Delta z = h_L

By applying the head loss trick, you are considering the entire flow of the fluid out of a control volume as energy lost via minor losses. This is just an algebraic trick, the only thing to remember when applying this trick is that :math:`\sum K` will always be at least 1, even if there are no ‘real’ minor losses in the system.


.. _heading_the_orifice_equation:

Vena Contracta and The Orifice Equation
=======================================

This equation is one that you’ll see and use again and again throughout this class. Understanding it now will be invaluable, as future concepts will use and build on this equation.


.. _heading_what_is_a_vena_contracta:

Vena Contracta
--------------

Before describing the equation, we must first understand the concept of a `vena contracta <https://en.wikipedia.org/wiki/Vena_contracta>`_. Refer to the figure below.

.. _figure_sluice_gate_vena_contracta:

.. figure:: /Images/sluice_gate_vena_contracta.png
    :width: 650px
    :align: center
    :alt: Sluice Gate Vena Contracta

    This figure shows flow around a sluice gate. Since streamlines can't make sharp turns, the flow is forced to gradually curve and contract to an area smaller than the area of the gate.

The flow contracts as the fluid moves past the gate. This happens because the fluid can’t make a sharp turn as it tries to go around the gate, as indicated by the streamline in the figure. Instead, the most extreme streamline makes a gradual change in direction. As a result of this gradual turn, the flow contracts and the cross-sectional area the fluid is flowing decreases.

The term ‘vena contracta’ describes the phenomenon of contracting flow due to streamlines being unable to make sharp turns. :math:`\Pi_{vc}` is a dimensionless ratio comparing the flow area at the point of maximal contraction, :math:`A_{downstream}`, and the flow area *before* the contraction, :math:`A_{gate}`. In the figure above, the equation for the *vena contracta* coefficient would be:

.. math::

   \Pi_{vc} = \frac{A_{downstream}}{A_{gate}}

The *vena contracta* for an infinite slot such as the sluice gate in :numref:`figure_sluice_gate_vena_contracta` has an analytical solution (see `McDonald, 2005: Vena Contracta <../_static/references/vena_contracta.pdf>`_) given by

.. math::
   :label: 90_slot_vena_contracta_analytical

   \Pi_{vc_{\frac{\pi}{2}}} = \frac{\pi}{\pi + 2} = 0.611

where Equation :eq:`90_slot_vena_contracta_analytical` assumes the most extreme turn a streamline must make is :math:`\frac{\pi}{2}`. This parameter value, 0.611, is in aguaclara python library as ``pc.VC_ORIFICE_RATIO``. The *vena contracta* coefficient value is a function of the flow geometry and specifically the most extreme turn a streamline takes. Equation :eq:`90_slot_vena_contracta_analytical` can be generalized to any streamline angle, :math:`\theta`, with the assumption that we need a function that returns 1 for an angle of 0 and for an angle of :math:`\pi` it must return :math:`\left(\Pi_{vc_{\frac{\pi}{2}}}\right)^2`.

.. math::
   :label: theta_slot_vena_contracta_analytical

   \Pi_{vc_{\theta}} = \left(\frac{\pi}{\pi + 2}\right)^\frac{2\theta}{\pi}

Equation :eq:`theta_slot_vena_contracta_analytical` will be useful when we evaluate flocculator baffles that have an angle of :math:`\pi` as the water flows around the end of a baffle.

.. important:: A *vena contracta* coefficient is not a minor loss coefficient. Though the equations for the two both involve contracted and non-contracted areas, these coefficients are not the same. Minor losses coefficients imply energy loss, and *vena contractas* do not. Minor losses coefficients deal with flow expansions, and *vena contractas* deal with flow contractions. Confusing the two coefficients is common mistake that this paragraph will hopefully help you to avoid.

.. note:: Note that :math:`\Pi_{vc}` is often referred to as a ‘Coefficient of Contraction,’ :math:`C_c`, in other engineering courses and textbooks.

The Orifice Equation
------------------------------

The orifice equation is derived from the Bernoulli equation as applied to the purple points in the following image:

.. _figure_hole_in_a_bucket:

.. figure:: /Images/hole_in_a_bucket.png
    :width: 650px
    :align: center
    :alt: Minor loss displayed in an elbow

    Flow through a hole in the bottom of a bucket is a great example of the orifice equation.

At point 1, the pressure is atmospheric and the instantaneous velocity is negligible as the water level in the bucket drops slowly. At point 2, the pressure is also atmospheric. We define the difference in elevations between the two points, :math:`z_1 - z_2`, to be :math:`\Delta h`. With these simplifications :math:`(p_1 = \bar v_1 = p_2 = 0)` and assumptions :math:`(z_A - z_B = \Delta h)`, the Bernoulli equation becomes:

.. math::

   \Delta h = \frac{\bar v_2^2}{2g}

Substituting the continuity Equation :math:`Q = \bar v A` in the form of :math:`\bar v_2^2 = \frac{Q^2}{A_{vc}^2}`, the *vena contracta* coefficient in the form of :math:`A_{vc} = \Pi_{vc} A_{or}` yields:

.. math::

  \Delta h = \frac{Q^2}{2g \Pi_{vc}^2 A_{or}^2}

Which, rearranged to solve for :math:`Q` gives **The Orifice Equation:**

.. math::
  :label: orifice_equation

    Q = \Pi_{vc} A_{or} \sqrt{2g\Delta h}

| Such that:
| :math:`\Pi_{vc}` = 0.62 = *vena contracta* coefficient, as ``pc.VC_ORIFICE_RATIO``
| :math:`A_{or}` = orifice area- NOT contracted flow area
| :math:`\Delta h` = elevation difference between orifice and water level

.. seealso:: **Equation in aguaclara:** ``pc.flow_orifice(Diam, Height, RatioVCOrifice)`` Returns flow through a horizontal orifice.

.. seealso:: **Equation in aguaclara:** ``pc.flow_orifice_vert(Diam, Height, RatioVCOrifice)`` Returns flow through a vertical orifice. The height parameter refers to height above the center of the orifice.

There are two configurations for an orifice in the tank holding a fluid: horizontal and vertical. These are both displayed in the figure below. The orifice equation written is for a horizontal orifice; the equation for flow through a vertical orifice equation requires integration or the orifice equation across its height to return the correct flow. This is explored in the Flow Control and Measurement Examples section.

.. _figure_vertical_and_horizontal_orifices:

.. figure:: /Images/vertical_and_horizontal_orifices.png
    :width: 650px
    :align: center
    :alt: Vertical and horizontal orifices

    The descriptions 'vertical' and 'horizontal' **apply to the orientation of the orifices,** not to the orientation of the fluid coming out of the orifices.


.. _heading_FR_section_summary:

Section Summary
===============

1. **Introductory Concepts:**

    * **Continuity** means that the mass of a fluid is conserved as it flows, and implies a constant density. The continuity equation has two purposes:

        #. Relating the average velocity of a fluid, :math:`\bar v`, to its flow rate, :math:`Q`, via the cross-sectional area, :math:`A`, that it flows through. When the fluid is flowing in a pipe, we can simply expand this even further to relate the flow rate and velocity to the pipe's diameter, :math:`D`. The final equation below is only used for circular pipes, as it includes a pipe diameter.

        .. math::

            Q = \bar v A = \bar v \frac{\pi D^2}{4}

        #. Finding the average velocity or flow when the geometry of a fluid's flow changes, as the mass of the fluid must be conserved when it transitions through flow geometries.

        .. math::

            Q_1 = Q_2

        .. math::

         \bar v_1 A_1 = \bar v_2 A_2

        .. math::

         \bar v_1 \frac{\pi D_1^2}{4} = \bar v_2 \frac{\pi D_2^2}{4}

    * **Laminar and Turbulent flow** describe the disorder and chaos of fluid flow. The **Reynolds number,** :math:`{\rm Re}` is used to distinguish laminar from turbulent flow. For :math:`{\rm Re} < 2100`, flow is considered laminar. For :math:`{\rm Re} > 2100`, flow is considered turbulent. The equations for the Reynolds number are below:

    .. math::

        {\rm Re} = \frac{\bar vD}{\nu} = \frac{4Q}{\pi D\nu} = \frac{\rho \bar vD}{\mu}

    * **Control volumes vs Streamlines.** This section is quite short, a summary would simply repeat what the section says. The section is its own summary; read it here: `Streamlines and Control Volumes`_


2. **Bernoulli vs Energy equations:** The Bernoulli equation assumes that energy is conserved throughout a streamline or control volume. The Energy equation assumes that there is energy loss, or head loss :math:`h_L`. This head loss is composed of major losses, :math:`h_{\rm{f}}`, and minor losses, :math:`h_e`.

  Bernoulli equation:

  .. math::

   \frac{p_1}{\rho g} + {z_1} + \frac{\bar v_1^2}{2g} = \frac{p_2}{\rho g} + {z_2} + \frac{\bar v_2^2}{2g}

  Energy equation, simplified to remove pumps, turbines, and :math:`\alpha` factors:

  .. math::

  \frac{p_{1}}{\rho g} + z_{1} + \frac{\bar v_{1}^2}{2g} = \frac{p_{2}}{\rho g} + z_{2} + \frac{\bar v_{2}^2}{2g} + h_L

3. **Major losses:** Defined as the energy loss due to shear between the walls of the pipe/flow conduit and the fluid. The Darcy-Weisbach equation is used to find major losses in both laminar and turbulent flow regimes. The equation for finding the Darcy friction factor, :math:`\rm{f}`, changes depending on whether the flow is laminar or turbulent. The Moody diagram is a common graphical method for finding :math:`\rm{f}`. During laminar flow, the Hagen-Poiseuille equation, which is just a combination of Darcy-Weisbach, Reynolds number, and :math:`{\rm{f}} = \frac{64}{\rm{Re}}`, can be used

  Darcy-Weisbach equation:

  .. math::

      h_{\rm{f}} = {\rm{f}} \frac{L}{D} \frac{\bar v^2}{2g}

  For water treatment plant design we tend to use plant flow rate, :math:`Q`, as our master variable and thus we have.

  .. math::

      h_{\rm{f}} = {\rm{f}} \frac{8}{g \pi^2} \frac{LQ^2}{D^5}

  :math:`\rm{f}` for laminar flow:

  .. math::

      {\rm{f}} = \frac{64}{\rm{Re}} = \frac{16 \pi D \nu}{Q} = \frac{64 \nu}{\bar v D}

  :math:`\rm{f}` for turbulent flow:

  .. math::

      {\rm{f}} = \frac{0.25} {\left[ \log \left( \frac{\epsilon }{3.7D} + \frac{5.74}{{\rm Re}^{0.9}} \right) \right]^2}

  Hagen-Poiseuille equation for laminar flow:

  .. math::

      h_{\rm{f}} = \frac{32\mu L \bar v}{\rho gD^2} = \frac{128\mu Q}{\rho g\pi D^4}

4. **Minor losses:** Defined as the energy loss due to the generation of turbulent eddies when flow expands. Once more: minor losses are caused by flow expansions. There are three forms of the minor loss equation, two of which look the same but use different coefficients (:math:`K^{'}` vs :math:`K`) and velocities (:math:`\bar v_{in}` vs :math:`\bar v_{out}`). *Make sure the coefficient you select is consistent with the velocity you use*. The third form, written in purple, is the most commonly used form of the minor loss equation.

.. math::

    {\rm{ \mathbf{First \, form:} }} \quad h_e = \frac{\left( \bar v_{in}  - \bar v_{out} \right)^2}{2g}

.. math::

    {\rm{ \mathbf{Second \, form:} }} \quad h_e = \left( 1 - \frac{A_{in}}{A_{out}} \right)^2 \, \frac{\bar v_{in}^2}{2g} \, \, = \, \, K_e^{'} \frac{\bar v_{in}^2}{2g}, \quad {\rm where} \quad K_e^{'} = \left( 1 - \frac{A_{in}}{A_{out}} \right)^2

.. math::

   \color{purple}{
    {\rm{ \mathbf{Third \, form:} }} \quad h_e = \left( \frac{A_{out}}{A_{in}} -1 \right)^2 \, \frac{\bar  v_{out}^2}{2g} \, \, = \, \, K_e \frac{\bar v_{out}^2}{2g}, \quad {\rm where} \quad K_e = \left( \frac{A_{out}}{A_{in}} - 1 \right)^2
    }

5. **Major and minor losses vary with flow:** While it is generally important to know how increasing or decreasing flow will affect head loss, it is even more important for this class to understand exactly how flow will affect head loss. As the table below shows, head loss will always be proportional to flow squared during turbulent flow. During laminar flow, however, the exponent on :math:`Q` will be between 1 and 2 depending on the proportion of major to minor losses.

.. _table_h_Q_proportionality:

.. csv-table:: Proportionality between head loss :math:`h_L` and flow rate :math:`Q` for different flow regimes and types of head loss.
  :header: :math:`h_L \propto Q^?`, "Major Losses", "Minor Losses"
  :widths: 10, 10, 10
  :align: center

  "Laminar", :math:`Q`, :math:`Q^2`
  "Turbulent", :math:`Q^2`, :math:`Q^2`

6. The **head loss trick**, also called the control volume trick, can be used to incorporate the ‘kinetic energy out’ term of the energy equation, :math:`\frac{\bar v_2^2}{2g}`, into head loss as a minor loss with :math:`K = 1`, so the minor loss equation becomes :math:`\left( 1 + \sum K \right) \frac{\bar v^2}{2g}`. This is used to be able to say that :math:`\Delta z = h_L` and makes many equation simplifications possible in the future.

7. **Orifice equation and vena contractas:** The orifice equation is used to determine the flow out of an orifice given the elevation of water above the orifice. This equation introduces the concept of vena contracta, which describes flow contraction due to the inability of streamlines to make sharp turns. The equation shows that the flow out of an orifice is proportional to the square root of the driving head, :math:`Q \propto \sqrt{\Delta h}`. Depending on the orientation of the orifice, vertical (like a hole in the side of a bucket) or horizontal (like a hole in the bottom of a bucket), a different equation in AguaClara should be used.

  The Orifice Equation:

  .. math::

      Q = \Pi_{vc} A_{or} \sqrt{2g\Delta h}
