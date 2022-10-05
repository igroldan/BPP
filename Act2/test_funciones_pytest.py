import pytest
import funciones

def test_suma():
    x=21
    y=5
    resultado=26
    assert resultado==funciones.sumar(x,y)

def test_resta():
    x=21
    y=5
    resultado=16
    assert resultado==funciones.restar(x,y)

def test_multiplicar():
    x=15
    y=3
    resultado=45
    assert resultado==funciones.multiplicar(x,y)

def test_dividir():
    x=45
    y=3
    resultado=15
    assert resultado==funciones.dividir(x,y)
    
def test_factorial():
    x=5
    resultado=120
    assert resultado==funciones.factorial(x)

def test_acirculo():
    x=2
    resultado=12.566
    assert resultado==funciones.area_circulo(x)

def test_acuadrado():
    x=5
    resultado=25
    assert resultado==funciones.area_cuadrado(x)

def test_atriangulo():
    x=4
    y=3
    resultado=6
    assert resultado==funciones.area_triangulo(x,y)

def test_arectangulo():
    x=20
    y=12
    resultado=240
    assert resultado==funciones.area_rectangulo(x,y)