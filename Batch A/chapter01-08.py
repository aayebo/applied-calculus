import math
k = -math.log(50/80)/6
half_life = math.log(2)/k
print(f"Rate: {k:.5f} per hour")
print(f"Half-life: {half_life:.2f} hours")
assert abs(80*math.exp(-k*6) - 50) < 1e-10
