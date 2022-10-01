import numpy as np
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Designer
from pyswarms.utils.plotters.formatters import Mesher
c1 = float(input("Input value of Personal Best(c1)= "))
c2 = float(input("Input value of Global Best(c2)= "))
inertia = float(input("Input value of Inertia(W)= "))
options = {'c1': c1, 'c2': c2, 'w':inertia}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
cost, pos = optimizer.optimize(fx.sphere, iters=1000)
m = Mesher(func=fx.sphere)
animation = plot_contour(pos_history=optimizer.pos_history,mesher=m,mark=(0,0))
plt.show()
pos_history_3d = m.compute_history_3d(optimizer.pos_history)
d = Designer(limits=[(-1,1), (-1,1), (-0.1,1)], label=['x-axis', 'y-axis', 'z-axis'])
animation3d = plot_surface(pos_history=pos_history_3d, mesher=m, 
designer=d,mark=(0,0,0)) 
plt.show()
