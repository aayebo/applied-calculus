import numpy as np
import matplotlib.pyplot as plt
time = np.array([0, 5, 10, 15, 20, 25], dtype=float)
temp = np.array([82, 69, 58.9, 51, 44.8, 39.8])
slope, intercept = np.polyfit(time, np.log(temp - 22), 1)
k = -slope
pred = 22 + 60*np.exp(-k*time)
for t, obs, p in zip(time, temp, pred):
    print(f"{t:4.0f} min  observed={obs:5.1f}  "
          f"predicted={p:6.2f}  residual={obs-p:6.2f}")
plt.scatter(time, temp, label="Teaching data")
t = np.linspace(0, 30, 301)
plt.plot(t, 22 + 60*np.exp(-k*t), label="Exponential model")
plt.xlabel("Time (min)")
plt.ylabel("Temperature (C)")
plt.legend()
plt.show()
