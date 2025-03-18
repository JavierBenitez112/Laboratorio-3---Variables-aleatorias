import scipy as sc
import sympy as sy
import numpy as np

y = sy.symbols('y', real=True)
k = sy.symbols('k', real=True)
z = sy.symbols('z', real=True)

g = (2/3) * sy.exp(-2 * z / 3)
F = sy.integrate(g, (z, 0, y))

prob1 = F.subs(y, 0.5).evalf()
prob2 = F.subs(y, 2).evalf()
prob2 = 1 - prob2

print('a)')
print('Probabilidad de llegada en 30 segundos:', prob1)
print('Probabilidad de ausencia en 2 minutos:', prob2)

Q1 = F.subs(y, 1).evalf()
Q1 = 1 - Q1

Q2 = F.subs(y, 2).evalf()
Q2 = 1 - Q2

res_b = Q2 / Q1
print('b)')
print('Probabilidad condicional:', res_b)

h = (2/3) * sy.exp(-2 * y / 3)
esperanza = sy.integrate(y * h, (y, 0, sy.oo))
varianza = sy.integrate(y**2 * h, (y, 0, sy.oo)) - esperanza**2

print('c)')
print('Esperanza:', esperanza)
print('Varianza:', varianza)
