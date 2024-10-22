import numpy as np

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


## wir nehmen die standard parameter
c = 1 ## initiale simplex größe
a = 1.2 ## reflexionsfaktor
b = 2 ## ausdehnungsfaktor
g = 1/2 ## kontraktionsfaktor

## zunächst basteln wir unseren initialen simplex
## unsere funktion ist auf \R^2 definiert
## deswegen wählen wir 3 punkte für den simplex
s = c * (np.sqrt(3)+2-1)/(np.sqrt(2)*2)
t = c * (np.sqrt(3)-1)/(np.sqrt(2)* 2)

p = np.array([t,t])
x1 = np.array([1,2])
x2 = x1 + p + (s-t) * np.array([1,0])
x3 = x1 + p + (s-t) * np.array([0,1])
x = np.array([x1,x2,x3])
print("Unser initialer Simplex ist", x)
