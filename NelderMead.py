""" Hier wird Nelder Mead implementiert, es muss auf jeden Fall die Zielfunktion und entweder der inital point oder alle punkte des initial simplex übergeben werden """

import numpy as np

def NelderMead(f, x, c=1, a=1, b=2, g=1/2):
    if len(x) != 3:
        x1 = x
        s = c * (np.sqrt(3)+2-1)/(np.sqrt(2)*2)
        t = c * (np.sqrt(3)-1)/(np.sqrt(2)* 2)
        p = np.array([t,t])
        x2 = x1 + p + (s-t) * np.array([1,0])
        x3 = x1 + p + (s-t) * np.array([0,1])
        x = np.array([x1,x2,x3])
    print("Unser initialer Simplex ist", x)
    
    xb, xz, xw = sorted(x, key = f)
    size = np.array([np.linalg.norm(xz-xb), np.linalg.norm(xw-xb)])
    k = 1
    ## als abbruchsbedingung haben wir hier die Größe des Simplex

    while np.max(size) >= 10**(-3):
        m = (1/2)*(xz+xb)
    
        ## Reflexionsschritt
        
        xr = m + a*(m-xw)
        if f(xb) <= f(xr) <= f(xz):
            xw = xr
            x = np.array([xb,xz,xw])
        elif f(xr) < f(xb):
            xc = m + b* (xr-m)
            if f(xc) < f(xb):
                    xw = xc
                    x = np.array([xb,xz,xw])
            else:
                xw = xr
                x = np.array([xb,xz,xw])
        else:
            if f(xr) < f(xw):
                xc = m + g * (xw-m)
            else:
                xc = m + g * (xr-m)
            if f(xc) < f(xw):
                xw = xc
                x = np.array([xb,xz,xw])
            else:
                for i in [0,1,2]:
                    x[i] = (1/2) * (x[i] + xb)
        k = k+1
        xb, xz, xw = sorted(x, key = f)
        size = np.array([np.linalg.norm(xz-xb), np.linalg.norm(xw-xb)])
    
    print("Wir haben", k, "Schritte gebraucht.")
    print("Unser finaler Simplex ist:", x, "\n")