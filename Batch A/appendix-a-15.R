f <- function(x) x^3 - 2*x + 1
a <- 1
h <- 0.01
forward <- (f(a + h) - f(a)) / h
central <- (f(a + h) - f(a - h)) / (2*h)
exact <- 3*a^2 - 2
c(forward = forward, central = central, exact = exact)
