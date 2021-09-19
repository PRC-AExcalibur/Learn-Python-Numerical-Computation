import warnings
import numpy as np


def fpi(function, r, tol, n):
    x = r
    for i in range(n):
        xi = function(x)
        if abs(xi - x) < tol:
            return xi
        else:
            x = xi
    warnings.warn(format("%.16f non convergence" % x))
    return x


def test():
    def test_function1(x):  # solve x ^ 3 + x - 1 = 0
        return x ** 3 + x - 1

    def test_function2(x):  # solve x = 2.8 * x - x ^ 2
        return 2.8 * x - x * x

    def test_function3(x):  # solve x = cos(x)
        return np.cos(x)

    x0 = 1
    print(fpi(test_function1, x0, 0.001, 100))
    print(fpi(test_function2, x0, 0.001, 100))
    print(fpi(test_function3, x0, 0.001, 100))
    print(fpi(test_function3, x0, 0.001, 10))


if __name__ == '__main__':
    test()
