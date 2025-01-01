.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Flow_Control_and_Measurement/FCM_Intro.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_flow_control_intro:

********************
Constant Head Tanks
********************


.. _heading_qh_as_a_function_of_t:

Flow :math:`Q` and Water Level :math:`h` as a Function of Time
----------------------------------------------------------------

Our first step is to see if we can get constant head out of a simple system. The most simple flow control system is a bucket or tank with a hole in it. This system is too coarse to provide constant head. One step above that is a bucket or tank with a valve. This is where we begin our search for constant head.

Using the setup described in the image below, we derive the following equation for flow :math:`Q` through the valve as a function of time :math:`t`. The derivation is found here: :ref:`heading_flow_for_a_tank_with_a_valve`.

.. _figure_hypochlorinator_variable_explanation_design:
.. figure:: /Images/hypochlorinator_variable_explanation.png
    :width: 600px
    :align: center
    :alt: Drip hypochlorinator variables

    This figure shows the variables that are defined in the equation above.

This equation has historically given students some trouble, and while its nuances are explained in the derivation, they will be quickly summarized here:

* :math:`t_{Design}` is **NOT** the time it takes to drain the tank. It is the time that it *would* take to drain the tank *if* the flow rate at time :math:`t = 0`, :math:`Q_0`, were the flow rate forever, which it is not. :math:`t_{Design}` was used in the derivation to simplify the equation, which is why this potentially-confusing parameter exists. The actual time it takes to drain the tank lies somewhere between :math:`t_{Design}` and :math:`2 \, t_{Design}` and depends on the ratio :math:`\frac{h_{Tank}}{h_0}`.
* :math:`h_{Tank}` is not the same as :math:`h_{0}`. :math:`h_{Tank}` is the height of water level in the tank with reference to the tank bottom. :math:`h_{0}` is the water level in the tank with reference to the valve. Neither change with time, they both refer to the water level at one instance in time, :math:`t = 0`. Therefore, :math:`h_{0} \geq h_{Tank}` is always true. If the tank is elevated far above the valve, then the :math:`h_{0} > > h_{Tank}`. If the valve is at the same elevation as the bottom of the tank, then :math:`h_{0} = h_{Tank}`. Please refer to the figure above to clarify :math:`h_{0}` and :math:`h_{Tank}`.

We can use the proportionality :math:`Q \propto \sqrt{h}`, which applies to both minor losses and orifices to form a relationship between water level in the tank :math:`h` and time :math:`t`. This proportionality comes from rearranging the minor loss Equation :math:`h = K \frac{Q^2}{2 g A^2}` for :math:`Q` instead of :math:`h`. A table of proportionality between :math:`Q` and :math:`h` can be found in :numref:`table_h_Q_proportionality`

Using Equation :eq:`Q_tank_with_valve` and this proportionality relationship, we make the following plots. On the left, the valve is at the same elevation as the bottom of the tank, or :math:`h_{Tank} = h_0`. Our attempt to get a continuous flow rate out of this system is to make :math:`\frac{h_{Tank}}{h_0}` very small by elevating the tank far above the valve. On the right, :math:`\frac{h_{Tank}}{h_0} = \frac{1}{50}`. While the plot looks great and provides essentially constant head, elevating the tank by 50 times its height is not realistic. The ‘tank with a valve’ is not a solution to the constant head problem.

.. _figure_tank_valve_play:
.. figure:: /Images/tank_valve_play.png
    :width: 600px
    :align: center
    :alt: Manipulating hypochlorinator heights

    These graphs show how manipulation of the variables in the :math:`Q(t)` expression can result in effectively constant head.


.. _heading_drain_system_for_a_tank:

Drain System for a Tank
------------------------
While the ‘tank with a valve’ scenario is not a good constant head solution, we can use our understanding of the system to properly design drain systems for AguaClara reactors like flocculators and clarifiers, since they are just tanks with valves. The derivation for the following equation is here, along with more details on AguaClara’s pipe stub method for draining tanks: :ref:`heading_diameter_and_time_tank_drain_equation`. The derived ‘Tank Drain’ equation is as follows:

.. math::

    D_{Pipe} = \sqrt{ \frac{8 L_{Tank} W_{Tank}}{\pi t_{Drain}}} {\left( \frac{H_{Tank} \sum K }{2g} \right)^{\frac{1}{4}}}

The equation can also be rearranged to solve for the time it would take to drain a tank given its dimensions and a certain drain pipe size:

.. math::

    t_{Drain} =  \frac{8 L_{Tank} W_{Tank}}{\pi D_{Pipe}^2} {\left( \frac{H_{Tank} \sum K }{2g} \right)^{\frac{1}{2}}}

| Such that:
| :math:`D_{Pipe}` = Diameter of the drain piping
| :math:`L_{Tank}, W_{Tank}, H_{Tank}` = Tank dimensions
| :math:`t_{Drain}` = Time it takes to drain the tank
| :math:`\sum K` = Sum of all the minor loss coefficients in the system

.. _figure_pipe_stub_drainage_variables_in_derivation:
.. figure:: /Images/pipe_stub_drainage_variables.png
    :width: 600px
    :align: center
    :alt: Variables for draining a tank

    Variables for draining a tank
