#este script utiliza el metodo de Euler para resolver una ecuacion diferencial
#implementarlo para un pendulo idealizado
#usar dos ecuaciones diferenciales de primer orden

import numpy as np
import matplot.pylab as plt

#theta
h=0.01
max_x=0.0
min_x=2*3.1415
n_points=int((max_x-min_x)/h)

#alpha