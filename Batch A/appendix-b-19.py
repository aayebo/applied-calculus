def bisection(fun, left, right, tol=1e-8):
    if fun(left)*fun(right) > 0:
        raise ValueError("Endpoints must bracket a root")
    while right-left > tol:
        middle = (left+right)/2
        if fun(left)*fun(middle) <= 0:
            right = middle
        else:
            left = middle
    return (left+right)/2

print(bisection(g, 0, 1))
