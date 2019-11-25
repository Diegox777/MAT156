from math import *
from sympy import * #importamos la libreria sympy
from sympy import lambdify

import matplotlib.pyplot as plt
import numpy as np

x = symbols('x') # establecemos a x como variable simbolica

a = int(input('Introduzca a = ')) # limite inferior
b = int(input('Introduzca b = ')) # limite superior

ca = a
cb = b

tolerancia = float(input('Introduzca la tolerancia = '))

c = 0.0

#introducimos la funcion por teclado
#ej: 
#   x**2
#   sin(x)
#   exp(x)
#   x**3 + cos(x**2)

expr = input('Introduzca f(x) = ') 
# transformamos de cadena a una expresion sympy
expr = sympify(expr)

#evaluamos la funcion
f = lambda xk: expr.subs(x, xk).evalf()

N = int(log(b - a) - log(tolerancia) / log(2))
print('N = ', N)
if f(a) * f(b) > 0: # verificamos que exista una raiz
    print('No existe raiz en el intervalo')
else:
    for i in range(N):
        c = (a + b) / 2.0 # hallamos el punto medio
        print('k = %d, a = %.3f, c = %.3f, b = %.3f' %(i + 1, a, c, b))
        if f(a) * f(c) < 0: # la raiz esta en [a,c]
            b = c
        elif f(c) * f(b) < 0: # la raiz esta en [b, c]
            a = c
        else:
            break # encontramos la raiz
    print('La raiz es %.5f' %(c)) # imprimir con formato

lam_x = lambdify(x, expr, modules=['numpy'])
x_vals = np.linspace(-10, 10, 50)
y_vals = lam_x(x_vals)

plt.plot(x_vals, y_vals)
plt.grid(True)
plt.axvline(x=c, color='red', label='raiz')
plt.axvline(x=ca, color='black', label='a')
plt.axvline(x=cb, color='black', label='b')


plt.show()