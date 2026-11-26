import numpy as np
from scipy.integrate import quad
surface = quad(lambda x: 2*np.pi*np.sqrt(x)*
               np.sqrt(1+1/(4*x)), 1, 4)[0]
print(f"Lateral surface area: {surface:.6f} m^2")
print(f"Estimated coating cost: ${18*surface:.2f}")
