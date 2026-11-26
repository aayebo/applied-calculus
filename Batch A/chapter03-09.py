import numpy as np
x = 1.0
for h in 10.0**(-np.arange(1, 8)):
    fw = (np.sin(x+h)-np.sin(x))/h
    ct = (np.sin(x+h)-np.sin(x-h))/(2*h)
    print(h, abs(fw-np.cos(x)),
             abs(ct-np.cos(x)))
