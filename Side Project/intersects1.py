#  Copyright (c) 2016 Jon Cooper
#   
#  This file is part of py-collide.
#  Documentation, related files, and licensing can be found at
# 
#      <https://github.com/joncoop/py-collide>.

"""
Parameter definitions for the intersects module:

A point is defined by a list or tuple in the form [x, y] or (x, y).

A circle is defined as a list or tuple in the form [x, y, r] 
where (x, y) represents the center of the circle and r is its radius.

A rect is defined as a list or tuple in the form [x, y, width, height] 
where (x, y) represents the coordinates of the upper left corner of 
the rectangle.
"""
import math

def point_circle(point, circle):
    a = point[0] - circle[0]
    b = point[1] - circle[1]
    r = circle[2]

    return a**2 + b**2 <= r**2

