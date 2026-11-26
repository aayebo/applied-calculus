F <- function(x) -cos(x)^3/3 + cos(x)^5/5
f <- function(x) sin(x)^3*cos(x)^2
h <- 1e-5
x <- seq(-2, 2, length.out=100)
error <- (F(x+h)-F(x-h))/(2*h)-f(x)
cat('Maximum derivative discrepancy:', max(abs(error)), '\n')
plot(x, f(x), type='l', lwd=2, main='Trigonometric integrand')
