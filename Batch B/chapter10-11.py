import numpy as np
from scipy.integrate import quad
r = lambda t: 2*(1+np.cos(t))
dr = lambda t: -2*np.sin(t)
A = quad(lambda t: .5*r(t)**2,0,2*np.pi)[0]
L = quad(lambda t: np.hypot(r(t),dr(t)),0,2*np.pi)[0]
print("Area:",A,"Exact:",6*np.pi)
print("Length:",L,"Exact:",16)
