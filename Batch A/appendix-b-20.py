time = np.array([0, 2, 4, 6, 8], dtype=float)
temperature = np.array([82, 67, 56, 48, 42], dtype=float)
np.savetxt("cooling_data.csv",
           np.column_stack([time, temperature]),
           delimiter=",", header="time,temp", comments="")
data = np.loadtxt("cooling_data.csv", delimiter=",",
                  skiprows=1)
print(data)
