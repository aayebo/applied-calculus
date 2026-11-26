def newton(f,df,x0,tol=1e-10,maxit=30):
    x = float(x0)
    for k in range(1,maxit+1):
        fx, dfx = f(x), df(x)
        if abs(dfx)<1e-12:
            raise ArithmeticError("Derivative too small")
        nxt = x-fx/dfx
        print(f"iter {k}: x={nxt:.12f}, residual={abs(f(nxt)):.3e}")
        if abs(nxt-x)<tol and abs(f(nxt))<tol:
            return nxt
        x = nxt
    raise RuntimeError("Newton iteration did not converge")
root = newton(lambda x:x*x-2,lambda x:2*x,1)
print("Root:",root)
