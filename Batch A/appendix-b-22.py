for n in [4, 8, 16, 32]:
    approximation = midpoint_rule(lambda x: x**2, 0, 2, n)
    error = abs(approximation - 8/3)
    print(f"n={n:2d}, error={error:.6f}")

if error < 0.001:
    print("The final approximation met the tolerance.")
else:
    print("Increase n or use a better method.")
