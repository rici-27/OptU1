import numpy as np
import NelderMead


## Rosenbrock Funktion
def f1(x):
    return 100 * (x[0]-x[1]**2)**2 + (1-x[0])**2

x1 = np.array([-1.2, 1])

NelderMead.NelderMead(f1,x1)


## Crescent Funktion
def f2(x):
    return max(np.array([x[0]**2 + (x[1]-1)**2 + x[1]-1, -x[0]**2 - (x[1]-1)**2 + x[1]+1]))

x2 = np.array([-1.5,2])

NelderMead.NelderMead(f2,x2)


## McKinnon
def f3(x):
    def g(y):
        if y >= 0:
            return 1
        else:
            return 60
    return 6 ** (1+g(x[0])) ** x[0]**2 + x[1] + x[1]**2

x1 = np.array([1, 1])
x2 = np.array([0, 0])
x3 = np.array([(1/8) * np.sqrt(33), (1/8) * np.sqrt(33)])
x = np.array([x1, x2, x3])

NelderMead.NelderMead(f3,x)