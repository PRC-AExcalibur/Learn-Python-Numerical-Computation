import warnings
import numpy as np


def secant(function, r0, r1, tol, n):
    x0 = r0
    x1 = r1
    for i in range(n):
        xi = x1-function(x0) * (x1 - x0) / (function(x1) - function(x0))
        if abs(xi - x1) < tol:
            return xi
        else:
            x0 = x1
            x1 = xi
    warnings.warn(format("%.16f non convergence" % x1))
    return x1


def test_function(x):  # solve x ^ 3 + x - 1 = 0
    return x ** 3 + x - 1


def test():
    print(secant(test_function, 0, 1, 0.001, 1000))
    print(secant(test_function, 0, 1, 0.001, 3))


if __name__ == '__main__':
    test()
