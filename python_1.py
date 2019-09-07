# Python 3
# Clase 1
# MAT-156

a = input('Introduzca el valor de a: ')
print('El valor de a es:', a)
print('Tipo de dato de la variable a es:', type(a))
b = input('Introduzca el valor de b: ')
# input() leerá la entrada como cadena de texto
# entonces al imprimir a + b, python concatenará las cadenas
# e imprimirá por pantalla
print(a + b)

# para leer números debemos utilizar la funcion int(x)
# que intentara convertir valores al tipo de dato int
# en el caso de no poder un valor a int, python desplegará un error
a = int(input('Introduzca un numero: '))
print('El valor de a es:', a)
print('Tipo de dato de la variable a es:', type(a))
b = int(input('Introduzca un numero: '))

print('La suma de a y b es:', a + b)

# Para leer numeros en una sola linea
a, b, c = map(int, input('Introduzca 3 numeros en una sola linea: ').split())
print('La suma de a + b + c es:', a + b + c)


# Leemos un numero de tipo float
f = float(input())
print(type(f))

# Imprimimos con una presicion de 3
print('{:0.3f}'.format(f))

# Imprimimos con una presicion de 10
print('{:0.10f}'.format(f))

# Tipos de datos
x = 10 # x es el numero entero 10
x = 10. # ahora x es el punto flotante
x = 10.0 # igual que x = 10.
x = 'diez' # x ahora es una cadena
x = (0, 1, 2) # x ahora es una tupla (no se puede modificar)
x = [0, 1 , 3] # x ahora es una lista (se puede modificar)

x = 1; y = 2; z = 3 # asignamos x = 1, y = 2, z = 3
x, y, z = 1, 2, 3 # obtenemos el mismo resultado con esta linea

# Operadores
a = 5
b = 2
print (a + b) # suma
print (a - b) # resta
print (a * b) # multiplicacion
print (a / b) # division 
print (a // b) # division entera
print (a % b) # modulo
print (a ** b) # exponenciacion
print (-a) # negacion

# Comparacion
# a == b
# a != b
# a < b
# a > b
# a <= b
# a >= b

# If
x = 9
if x < 0:
    print(x, 'es un numero negativo') 
elif x > 0:
    print(x, 'es un numero positivo') 
elif x == 0:
    print(x, 'es cero')
else:
    print('estoy confundido! XD')
# NOTA
# > en Python los bloques de codigo estan denotados por indentacion (muy importante)
# > la recomendacion es usar cuatro espacios para denotar la indentacion
# > pero tambien se puede usar tab
# > la indentacion esta precedida por dos puntos ":"
 
