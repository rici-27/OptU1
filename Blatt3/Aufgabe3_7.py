import numpy as np
import autograd.numpy as np
from autograd import grad

def f(x):
    if x < -1:
        return (3/4) *  (1+x)**2 - 2*(1+x)
    elif np.abs(x) <= 1:
        return x**2 - 1
    else:
        return (3/4) * (1-x)**2 - 2*(1-x)


def armijo(f, x, d, beta, sigma, nablaf):
    l = 0
    t = 1
    while f(x+t*d) > f(x) + sigma * t * nablaf(x) * d:
        l = l + 1
        t = beta ** l
    return t

def nablaf(x):
    if x < -1:
        return (3/2) *  (1+x) - 2
    elif np.abs(x) <= 1:
        return 2*x
    else:
        return -(3/2) * (1-x) + 2  

x = 1
beta = 0.5
sigma = 0.01

for i in range(20):
    print(x)
    d = - nablaf(x)
    t = armijo(f, x, d, beta, sigma, nablaf)
    x = x + t * d
