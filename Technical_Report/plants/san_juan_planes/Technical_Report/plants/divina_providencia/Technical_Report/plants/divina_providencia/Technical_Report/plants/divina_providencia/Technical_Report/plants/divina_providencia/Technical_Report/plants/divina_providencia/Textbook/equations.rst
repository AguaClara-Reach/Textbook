.. _equations:

**************************
Equation Quick Reference
**************************

.. _table_equations_table:

.. csv-table:: Equations
    :header: Number, Name, Equation
    :align: center

    :eq:`eq_laminar_terminal_velocity`, Particle terminal velocity, :math:`\bar v_t = \frac{D_{particle}^2 g}{18 \nu} \frac{\rho_p - \rho_w}{\rho_w}`
    :eq:`continuity_equation`, Continuity, :math:`Q = \bar v A`
    :eq:`reynolds_number_equation`, Reynold's Number, :math:`{\rm Re} = \frac{\bar vD}{\nu} = \frac{4Q}{\pi D\nu} = \frac{\rho \bar vD}{\mu}`
    :eq:`bernoulli_equation`, Bernoulli, :math:`\frac{p_1}{\rho g} + {z_1} + \frac{v_1^2}{2g} = \frac{p_2}{\rho g} + {z_2} + \frac{v_2^2}{2g}`
    :eq:`energy_equation`, Control Volume Energy, :math:`\frac{p_{1}}{\rho g} + z_{1} + \frac{\bar v_{1}^2}{2g} = \frac{p_{2}}{\rho g} + z_{2} + \frac{\bar v_{2}^2}{2g} + h_L`
    :eq:`darcy_weisbach`, Darcy-Weisbach, :math:`h_{\rm{f}}  = {\rm{f}} \frac{L}{D} \frac{\bar v^2}{2g}`
    :eq:`swamee_jain`, Swamee-Jain, :math:`{\rm{f}} = \frac{0.25} {\left[ \log \left( \frac{\epsilon }{3.7D} + \frac{5.74}{{\rm Re}^{0.9}} \right) \right]^2}`
    :eq:`hagen_poiseuille`, Hagen-Poiseuille, :math:`h_{\rm{f}} = \frac{128\mu L Q}{\rho g\pi D^4}`
    :eq:`orifice_equation`, Orifice, :math:`Q = \Pi_{vc} A_{or} \sqrt{2g\Delta h}`
    :eq:`minor_loss_equation`, Minor loss, :math:`{ {\rm{ \mathbf{Third form:} }} \quad h_e = \left( \frac{A_{out}}{A_{in}} -1 \right)^2 \frac{\bar v_{out}^2}{2g} = K_e \frac{\bar v_{out}^2}{2g} \quad {\rm where} \quad K_e = \left( \frac{A_{out}}{A_{in}} - 1 \right)^2 }`
    :eq:`V_floc_of_n_cp`, Fractal floc volume, :math:`\forall_{floc} = \forall_{cp} n_{cp}^\frac{3}{\Pi_{fractal}}`
    :eq:`vt_of_floc`, Floc terminal velocity, :math:`v_t = \frac{D_{cp}^2g}{18\nu}\frac{\rho_{cp} - \rho_{H_2O}}{\rho_{H_2O}} \left( \frac{D_{floc}}{D_{cp}} \right) ^{\Pi_{fractal}-1}`
    :eq:`Gmax_of_d_floc`, max floc velocity gradient, :math:`G_{max} = \frac{4F_{bond}}{3 \pi \mu D_{floc_{max}}^2}`
    :eq:`G_Camp_Stein`, Camp-Stein velocity, :math:`\tilde{G} = \sqrt{\frac{P}{\rho \nu \forall}}`
    :eq:`einstein_diffusion`, Einstein’s diffusion, :math:`D_{Diffusion} = \frac{k_B T}{3 \pi \mu D_P}`
    :eq:`cdc_tube_Q_max`, Linear CDC, :math:`Q_{max Tube} = \frac{\pi D^2}{4} \sqrt{\frac{2 h_L g \Pi_{Error}}{\sum{K} }}`
    :eq:`Q_tank_with_valve`, Tank with a valve, :math:`\frac{Q}{Q_0} = 1 - \frac{1}{2} \frac{t}{t_{Design}} \frac{h_{Tank}}{h_0}`
    :eq:`power_of_Q_h`, Mechanical power, :math:`P = \rho g Q \Delta h`
    :eq:`Q_max_served_per_injection_port`, Flow per chemical injection port, :math:`Q_{mixer} = g h_e t_{eddy}^2 \bar v_{exp}`
    :eq:`Gtheta_of_hL`, Collision potential, :math:`\tilde{G} \theta = \sqrt{\frac{g h_L \theta}{\nu}}`
    :eq:`W_min_HVFloc`, Channel width, :math:`W_{min \Pi_{H_eS}} = \frac{\Pi_{H_eS}Q}{H_e}\left( \frac{K}{2 H_e \nu \tilde{G}^2} \right)^\frac{1}{3}`
    :eq:`floc_He_max_const_K`, Distance between expansions, :math:`H_{e_{max}} = \left[ \frac{K}{2 \nu \tilde{G}^2} \left( \frac{Q \Pi_{{HS}_{max}}}{W_{channel}} \right)^3 \right]^\frac{1}{4}`
    :eq:`Floc_baffle_spacing_of_K`, Baffle spacing, :math:`S = \left( \frac{K}{2 H_e \tilde{G}^2 \nu } \right)^\frac{1}{3} \frac{Q}{W_{channel}}`
    :eq:`planejet_v_max_of_q`, Maximum jet velocity , :math:`\bar v_{Jet_{max}} = \left(\frac{q\nu G_{max}^2}{\Pi_{JetPlane} }\right)^\frac{1}{4}`
    :eq:`Q_tube_settler`, Tube settler flow, :math:`Q_{Tube}=\frac{\bar v_{c}\pi D^2}{4} \left(\frac{L}{D} \cos \alpha +\sin \alpha \right)`
    :eq:`Plate_S_min_of_fractal`, Minimum plate settler spacing, :math:`S_{min} \approx \frac{3 \bar v_{z_{Plate}}}{\sin^2 \alpha} \left( \frac{18 \nu}{g D_{cp}} \frac{\rho_{H_2O}}{\rho_{cp} - \rho_{H_2O}} \right)`
    :eq:`plate_settler_headloss`, Plate settler head loss, :math:`h_L = 2 \frac{\mu}{\rho g} \left( \frac{6 \bar v_{z_{Plate}}}{S sin^2 \alpha cos\alpha} \right) \left( \frac{ \bar v_{z_{Plate}}}{\bar v_c} -1 \right)`
    :eq:`floc_filter_head_loss`, Floc filter head loss, :math:`h_L = H_{ff} \left( \frac{\rho_{clay}}{\rho_{H_2O}} - 1 \right) \frac{C_{clay}}{\rho_{clay}}`
    :eq:`eq_Carman_Kozeny`, Clean bed head loss, :math:`\frac{h_l}{H_{FiSand}} = 36 k \frac{\left( 1 - \phi_{FiSand} \right)^2}{\phi_{FiSand}^3} \frac{\nu \bar v_a}{g D_{60}^2}`
    :eq:`headloss_bw_sand`, Backwash head loss, :math:`h_{l_{FiBw}} = H_{FiSand} \left( 1 - \phi_{FiSand} \right)  \left( \frac{\rho_{Sand}}{\rho_{Water}} - 1 \right)`
    :eq:`minimum_fluidization_velocity_sand`, Fluidization velocity, :math:`\bar v_{MinFluidization} = \frac{\phi_{FiSand}^3 g D_{60}^2}{36 k \nu \left( 1 - \phi_{FiSand} \right)} \left( \frac{\rho_{Sand}}{\rho_{Water}} - 1 \right)`
    :eq:`Sharp_weir_Q_of_channel_depth`, Sharp crested weir, :math:`Q = \Pi_{vc}\frac{2}{3} \sqrt{2g} w \left(H_{channel}\right)^\frac{3}{2}`
