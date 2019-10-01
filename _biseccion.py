from math import *

f = lambda x: x**2 - 3

a = 1.0 # limite inferior
b = 2.4 # limite superior
c = 0.0

tolerancia = 0.0000001

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
