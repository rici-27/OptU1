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
a = 1 ## reflexionsfaktor
b = 2 ## ausdehnungsfaktor
g = 1/2 ## kontraktionsfaktor

## zunächst basteln wir unseren initialen simplex
## unsere funktion ist auf \R^2 definiert
## deswegen wählen wir 3 punkte für den simplex
s = c * (np.sqrt(3)+2-1)/(np.sqrt(2)*2)
t = c * (np.sqrt(3)-1)/(np.sqrt(2)* 2)

p = np.array([t,t])
x1 = np.array([0,0])
x2 = x1 + p + (s-t) * np.array([1,0])
x3 = x1 + p + (s-t) * np.array([0,1])
x = np.array([x1,x2,x3])
print("Unser initialer Simplex ist", x)

## als abbruchsbedingung wähle ich erstmal eine feste anzahl an runden

for k in range(30):
    print("Schritt", k)
    xb, xz, xw = sorted(x, key = f)
    x = np.array([xb,xz,xw])
    values = np.array([f(xb),f(xz),f(xw)])
    print("Der aktuelle Simplex ist:", x)
    print("Die Werte sind:", values)
    
    m = (1/2)*(xz+xw)
    print("Der Mittelwert ist:", m)
    
    ## Reflexionsschritt
    
    xr = m + a*(m-xw)
    print("xr ist:", xr)
    if f(xb) <= f(xr) <= f(xz):
        print("wir sind in if")
        xw = xr
    elif f(xr) < f(xb):
        print("wir sind in elif")
        xc = m + b* (xr-m)
        if f(xc) < f(xb):
                xw = xc
        else:
            xw = xr
    else:
        print("wir sind in else")
        if f(xr) < f(xw):
            print("wir sind in if 1")
            xc = m + g * (xw-m)
        else:
            xc = m + g * (xr-m)
            print("wir sind in else 1")
        if f(xc) < f(xw):
            print("wir sind in if 2")
            xw = xc
            print("das ist cx", xc)
        else:
            print("wir sind in else 2")
            for i in [2]:
                x[i] = (1/2) * (x[i] + xb)
    x = np.array([xb,xz,xw])
    