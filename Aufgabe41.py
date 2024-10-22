import numpy as np

x1 = np.array([0,0])
x2 = np.array([0,1])
x3 = np.array([1,0])

def f(x: np.ndarray):
    d = 0
    for y in [x1,x2,x3]:
        d = d + np.linalg.norm(x-y)
    return d

print(f([0,0]))