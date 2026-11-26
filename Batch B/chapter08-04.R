f <- function(x) (5*x+1)/(x^2-x-2)
g <- function(x) (11/3)/(x-2)+(4/3)/(x+1)
x <- seq(-0.8, 1.8, length.out=200)
cat('Largest decomposition error:', max(abs(f(x)-g(x))), '\n')
plot(x, f(x), type='l', lwd=2,
     main='Rational integrand away from poles')
