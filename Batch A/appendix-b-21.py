ambient = 22.0
initial = 82.0
k = 0.18

def temp(t):
    return ambient + (initial-ambient)*np.exp(-k*t)

def cooling_rate(t):
    return -k*(initial-ambient)*np.exp(-k*t)

t = np.linspace(0, 20, 250)
plt.plot(t, temp(t), label="Temperature")
plt.axhline(ambient, linestyle="--", color="gray",
            label="Ambient temperature")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (degrees C)")
plt.title("Newton's cooling model")
plt.legend()
plt.grid(alpha=0.25)
plt.show()
print("Rate at t=5:", cooling_rate(5))
