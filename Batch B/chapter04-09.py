import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2,2,400)
fig, ax = plt.subplots(3,1,figsize=(7,8))
for a,y,label in zip(ax,[x**3-3*x,3*x*x-3,6*x],
                     ["f","f prime","f double prime"]):
    a.plot(x,y); a.axhline(0,color="gray",linestyle="--")
    a.set_title(label)
plt.tight_layout(); plt.show()
