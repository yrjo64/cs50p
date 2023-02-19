import timeit

import numpy as np

f = lambda x: x ** 2
vf = np.vectorize(f)

def test_array(x, n):
    t = timeit.timeit(
        'np.array([f(xi) for xi in x])',
        'from __main__ import np, x, f', number=n)
    print('array: {0:.3f}'.format(t))

def test_fromiter(x, n):
    t = timeit.timeit(
        'np.fromiter((f(xi) for xi in x), x.dtype, count=len(x))',
        'from __main__ import np, x, f', number=n)
    print('fromiter: {0:.3f}'.format(t))

def test_direct(x, n):
    t = timeit.timeit(
        'f(x)',
        'from __main__ import x, f', number=n)
    print('direct: {0:.3f}'.format(t))

def test_vectorized(x, n):
    t = timeit.timeit(
        'vf(x)',
        'from __main__ import x, vf', number=n)
    print('vectorized: {0:.3f}'.format(t))


x = np.arange(1000)
n = 1000
test_direct(x, n)      # 0.007
test_fromiter(x, n)    # 0.479
test_array(x, n)       # 0.516
test_vectorized(x, n)  # 0.945
print(vf(x))