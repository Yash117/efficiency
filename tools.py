#!/usr/bin/env python3

"""Example usage of the pyalgo lib.

Run from ALGO root directory.
"""

__author__ = 'Ronja Schnur'
__email__ = 'rschnur@students.uni-mainz.de'

import math
# from pyalgo import QuadraticSpline, Intervall


def falke(r0, x):
    e = 1.4502
    d = r0 / (e * e - 1)
    t = r0 + d - math.sqrt(d * d + 1 / (e * e - 1) * x * x)
    return t**2


def parabola(r0, length, x):
    radius_end = math.sqrt(falke(r0, length))
    r = (radius_end - r0) / (length * length) * x * x + r0
    return r**2


def circle(r0, length, x):
    y_1 = r0
    x_2 = length
    y_2 = math.sqrt(falke(r0, length))

    y = (y_1**2 - y_2**2 - x_2**2) / (2*y_1 - 2*y_2)
    d = y_1 - y

    r = math.sqrt(d**2 - x**2) - (d - y_1)
    return r**2


def sumkey(p, k):
    r = 0
    for v in p:
        if v % 64 == k:
            r += 1
    return r
