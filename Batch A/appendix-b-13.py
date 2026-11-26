def quotient(x):
    return (x**2 - 4) / (x - 2)

for h in [0.1, 0.01, 0.001, 0.0001]:
    print(f"h={h:.4g}, value={quotient(2+h):.8f}")
