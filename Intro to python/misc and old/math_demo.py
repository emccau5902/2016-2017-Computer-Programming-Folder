# This program contains functions that evaluate formulas used in geometry.
#
# Your Name
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def parallelogram(b, h):
    a = b * h
    return a
print(parallelogram(7, 8))

def trapezoid(a, b, h):
    a = ((a + b)/2) * h
    return a
print(trapezoid(7, 8, 9))

def volrectangularprism(w, h, l):
    v = w * h * l
    return v
print(volrectangularprism(7, 8, 9))

def cone(r, h):
    v = (math.pi * r ** 2) * h / 3
    return v
print(cone(7,8))

def sphere(r):
    v = 4 / 3 * (math.pi * r ** 3)
    return v
print(sphere(4))

def sarectangleprism(l, w, h):
    a = 2 * (w * l + h * l + h *w)
    return a
print(sarectangleprism(7,8, 9))

def susphere(r):
    a = 4 * math.pi * r ** 2
    return a
print(susphere(4))

def hypotenuse(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c
print(hypotenuse(2, 4))

#CHALLENGE

def herons_formula(a, b, c):
    a = math.sqrt(x * Y * Z)
    b = math.sqrt(y * Z * X)
    c = math.sqrt(z * X * Y)
    d = math.sqrt(x * y * z)
    X = (w - U + v)(U + v + w)
    x = (U - v + w)(v - w + U)
    Y = (u - V + w)(V + w + u)
    y = (V - w + u)(w - u + V)
    Z = (v - W + u)(W + u + v)
    z = (W - u + v)(u - v + W)
    return a
    print(herons_formula(3, 5, 7))
