mport sympy as sym
import math

def function(x,y):
    return x**2+y**3

x, y =sym.symbols('x y')

def derivatef(x,y):
    return sym.diff(function(x,y),x)

while i < n:
derivatef(x, y).evalf(subs={x: 1, y: 1})
3.00000000000000
