#FINISHED
import math

def derivative(f,x,h=0.0001):
    approximate = (f(x+h) - f(x)) / h
    return approximate

def squareFunction(x):
    return x**2

result = derivative(math.sin, 1)
print("Dla sin(x) w punkcie 1: ", result)

result = derivative(math.sin, 0)
print("Dla sin(x) w punkcie 0: ", result)

result = derivative(squareFunction, 1, 0.00001)
print("Dla x^2 w punkcie 1:    ", result)
