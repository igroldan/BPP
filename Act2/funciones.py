

# BÁSICOS
def sumar(num1, num2):
    return (num1+num2)

def restar(num1, num2):
    return (num1-num2)

def multiplicar(num1, num2):
    return (num1*num2)

def dividir(num1, num2):
    return (num1/num2)

# FACTORIAL DE UN NÚMERO
def factorial(n):
    resultado = 1
    for i in range(1,n+1):
        resultado *= i
    return resultado

# ÁREAS BÁSICAS
def area_circulo(radius):
    pi = 3.1415
    return pi*radius**2

def area_cuadrado(L):
    area=L**2
    return area

def area_triangulo(b,h):
    area=b*h/2
    return area

def area_rectangulo(b,h):
    area=b*h
    return area

