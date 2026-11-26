from math import exp, sqrt, pi, erf
f = lambda x: exp(-x*x)
reference = sqrt(pi)*erf(2)/2
for n in [4,8,16,32]:
    a,b = 0.0,2.0
    h = (b-a)/n
    xs = [a+i*h for i in range(n+1)]
    midpoint = h*sum(f(a+(i+0.5)*h) for i in range(n))
    trap = h*(sum(f(x) for x in xs)-(f(a)+f(b))/2)
    simp = h/3*(f(a)+f(b)+4*sum(f(xs[i]) for i in range(1,n,2))+
                2*sum(f(xs[i]) for i in range(2,n,2)))
    print(n, [round(abs(v-reference),8) for v in [midpoint,trap,simp]])
