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
p[0].line_color = (0,0,0)
p[0].label = 'x'
p[1].line_color = (1,0,0)
p[1].label = 'n=3'
p[2].label = 'n=7'
p[3].label = 'n=14'
p.show()
