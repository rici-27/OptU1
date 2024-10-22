""" Das hier ist die schöne Version von 4.2 """

import numpy as np
import NelderMead

## das sind die drei gegebene Punkte
z1 = np.array([0,0])
z2 = np.array([0,1])
z3 = np.array([1,0])
z = np.array([z1,z2,z3])
print("Die gegebenen Punkte sind", z)


## das ist unsere Zielfunktion
def f(x: np.ndarray):
    d = 0
    for z in [z1,z2,z3]:
        d = d + np.linalg.norm(x-z)
    return d

x1 = np.array([1,1])

NelderMead.NelderMead(f, x1)