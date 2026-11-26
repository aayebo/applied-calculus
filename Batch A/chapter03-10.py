import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 6, 301)
s = 12*t - 2*t**2
v = 12 - 4*t
a = np.full_like(t, -4.0)
for values, label in [(s,"s"),(v,"v"),(a,"a")]:
    plt.plot(t, values, label=label)
plt.xlabel("time (s)")
plt.ylabel("value (different units)")
plt.legend(); plt.show()
