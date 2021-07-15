import warnings
import numpy as np


def bisect(function, a, b, tol):
    fa = function(a)
    fb = function(b)
    if np.sign(fa) * np.sign(fb) >= 0:
        if fa == 0:
            return a
        elif fb == 0:
            return b
        else:
            warnings.warn(format("[ %.4f , %.4f ] non convergence" % (a, b)))
            return None

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fa = function(a)
        fc = function(c)
        if fc == 0:
            return c
        if np.sign(fa) * np.sign(fc) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def bisect_np(function, x_array, tol):
    y_array = np.array([])
    x_array.flatten()
    np.sort(x_array, 0)
    for i in range(x_array.size - 1):
        y = bisect(function, x_array[i], x_array[i + 1], tol)
        if y is None:
            break
        else:
            y_array = np.append(y_array, y)
    return y_array


def test_function1(x):  # solve x ^ 3 + x - 1 = 0
    return x ** 3 + x - 1


def test_function2(x):  # solve x ^ 2 - 2x + 1 = 0
    return x * x - 2 * x + 1


def test_function3(x):  # solve cos(x) = 0
    return np.cos(x)


def test():
    print(bisect(test_function1, 0, 1, 0.001))
    print(bisect(test_function2, 0, 1, 0.001))
    x_array = np.arange(0, 20, 3)
    print(bisect_np(test_function3, x_array, 0.001))


if __name__ == '__main__':
    test()
