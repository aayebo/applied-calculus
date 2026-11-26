import numpy as np
from scipy.integrate import quad
a = 1
speed = lambda t: np.sqrt((a*(1-np.cos(t)))**2
                          +(a*np.sin(t))**2)
L,err = quad(speed,0,2*np.pi)
print("Numerical length:",L,"Exact length:",8*a)
