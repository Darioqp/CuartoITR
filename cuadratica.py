from math import sqrt

a = float(input("Ingrese el valor de a: "))

b = float(input("Ingrese el valor de b: "))

c = float(input("Ingrese el valor de c: "))

def discriminante():

    return b**2-4*a*c

def raices():

    if discriminante() > 0:

        print("La ecuación tiene dos raíces reales distintas")

        return (-b+sqrt(discriminante()))/2*a, (-b-sqrt(discriminante()))/2*a

    elif discriminante() == 0:

        print("La ecuación tiene dos raíces reales iguales")

        return -b/2*a
        
    return "La ecuación no tiene solución real"

print(raices())


