""" importing """
import aguaclara
import aguaclara.core.physchem as pc
from aguaclara.core.units import unit_registry as u
import aguaclara.research.floc_model as fm

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
imagepath = 'AguaClara Water Treatment Plant Design/Energy Dissipation and Velocity Gradients/Images/'
Temperature = 15*u.degC
RATIO_JET_ROUND = 0.08
def Energy_dissipation_jet_centerline(D_jet,v_jet,x):
  return (50 * D_jet**3*v_jet**3/(x-2*D_jet)**4).to_base_units()

def Energy_dissipation_jet_max(D_jet,v_jet):
  return RATIO_JET_ROUND*v_jet**3/D_jet

v_jet = 1 * u.m/u.s
D_jet = 0.1 * u.m
EDR_max = Energy_dissipation_jet_max(D_jet,v_jet)
x=np.linspace(7,20,24)*D_jet
fig, ax = plt.subplots()
ax.plot(x/D_jet,Energy_dissipation_jet_centerline(D_jet,v_jet,x))
ax.plot(7,Energy_dissipation_jet_max(D_jet,v_jet),'o')
ax.set(xlabel='Jet diameters downstream', ylabel='Energy dissipation rate (W/kg)')
ax.legend(['centerline energy dissipation rate','Maximum energy dissipation rate'])
plt.show()
