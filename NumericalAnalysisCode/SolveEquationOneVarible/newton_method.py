import warnings
import numpy as np


def newton(function, d_function, r, tol, n):
    x = r
    for i in range(n):
        xi = x - function(x) / d_function(x)
        if abs(xi - x) < tol:
            return xi
        else:
            x = xi
    warnings.warn(format("%.16f non convergence" % x))
    return x


def test():
    def test_function(x):  # solve x ^ 3 + x - 1 = 0
        return x ** 3 + x - 1

    def test_d_function(x):  # solve x ^ 3 + x - 1 = 0
        return 3 * x ** 2 + 1

    x0 = 1
    print(newton(test_function, test_d_function, x0, 0.001, 100))
    print(newton(test_function, test_d_function, x0, 0.001, 3))


if __name__ == '__main__':
    test()
