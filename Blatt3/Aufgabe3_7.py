import numpy as np
import autograd.numpy as np
from autograd import grad
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

u = np.linspace(-3, 3, 100)



def f(x):
    if x < -1:
        return (3/4) *  (1+x)**2 - 2*(1+x)
    elif np.abs(x) <= 1:
        return x**2 - 1
    else:
        return (3/4) * (1-x)**2 - 2*(1-x)
    
f_vec = np.vectorize(f)
    
plt.plot(u, f_vec(u), color='red')

plt.show()


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
    
nablaf_vec = np.vectorize(nablaf)

plt.plot(u, nablaf_vec(u), color='red')

plt.show()

x = 1
beta = 0.5
sigma = 0.01


## hier sollen wir sigma = 0 und sigma = 0.01 testen


for i in range(20):
    print("Runde:", i)
    print("Punkt:", x)
    d = - nablaf(x)
    print("Abstiegsrichtung:", d)
    t = armijo(f, x, d, beta, sigma, nablaf)
    print("Schrittweite:", t)
    x = x + t * d
