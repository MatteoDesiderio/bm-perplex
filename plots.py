#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 18:00:52 2023

@author: matteo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is 

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

# %% choose 
year = 11 #  which stx-brt database?
c_map = "PRGn"

# %% other details
plt.rcParams["axes.facecolor"] = "lightgray"
plt.style.use("ggplot")
nums = np.linspace(80, 100, 11, dtype=int) # Mg numbers

# %% stagyy
# adiabat of the cobined reference profile 
# I found this is very similar to the average of ol and pxgt, w F_ol = 0.6375)
P = np.loadtxt("Pcombo.txt") 
T = np.loadtxt("Tcombo.txt")
# adiabat of the primpordial material, hotter than combo
Ppr = np.loadtxt("Ppr.txt")
Tpr = np.loadtxt("Tpr.txt")
# density = rho_pxgt * (1 - F_ol) + rho_ol * F_ol
rho_py_stag = np.loadtxt("rho_py_stag.txt", )
# density along Ppr, Tpr
rho_pr_stag = np.loadtxt("rho_pr_stag.txt", )
# depth 
z = np.loadtxt("depth.txt")

# %% perplex
rho_py = np.loadtxt("rho_py-stx%i.txt" % year)

# %% plot 
fig_pr, (ax_pr, ax_py) = plt.subplots(2, 1, sharex="all", sharey="all")
cmap = getattr(plt.cm, c_map)

for i, mgnum in enumerate(nums):
    col = cmap((i + 1)/len(nums))
    if i == 0:
        ax_pr.plot(z, rho_pr_stag, "k--", label="StagYY", zorder=100)
        ax_py.plot(z, rho_py_stag, "--", label="StagYY", zorder=100)
        ax_py.plot(z, rho_py, "-", label="Perplex", zorder=100)
        
    rho_pr = np.loadtxt("%i-stx%i.txt" % (mgnum, year))
    ax_pr.plot(z, rho_pr, c=col, label=mgnum)
    
    ax_pr.legend(ncol=2)
    ax_py.legend()
    
# 
ax_py.set_xlabel("depth [km]")
ax_pr.set_ylabel("density [kg/m^3]")
ax_py.set_ylabel("density [kg/m^3]")
ax_pr.set_title("Primordial")
ax_py.set_title("Pyrolite")
fig_pr.suptitle("Stagyy vs Perplex")

plt.ion()
plt.show()
