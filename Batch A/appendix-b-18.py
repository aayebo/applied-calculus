def g(x):
    return np.cos(x) - x

root = optimize.brentq(g, 0, 1)
print(f"Root: {root:.8f}")
print(f"Residual: {g(root):.2e}")
