# Fprma de calcular series de fourier truncadas de orde n , ampliadas y trasladadas.


from sympy import fourier_series, pi, plot
from sympy.abc import x
f = x**2
sn = fourier_series(f, (x, -pi, pi))
sn.shift(5).truncate(7)
sn.shiftx(3).truncate(7)
sn.scale(5).truncate(7)
sn.scalex(7).truncate(7)



# Series de fourier y graficadoras
import numpy as np
from sympy import fourier_series, pi, plot
from sympy.abc import x 
f = x
fser = fourier_series(f,(x,-pi, pi))
fser1 = fser.truncate(3)
fser2 = fser.truncate(7)
fser3 = fser.truncate(14)

p = plot(f,fser1, fser2, fser3, (x,-pi, pi), show = False, legend = True)
