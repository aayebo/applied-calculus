import numpy as np
h = 10.0**(-np.arange(1,16,2))
naive = (np.exp(h)-1)/h
stable = np.expm1(h)/h
for hi,a,b in zip(h,naive,stable):
    print(f"h={hi:.1e} naive={a:.12f} stable={b:.12f}")
