f <- expression(x^3 - 4*x^2 + 2*x + 1)
df <- D(f, "x")
print(df)
print(eval(df, list(x=2)))
