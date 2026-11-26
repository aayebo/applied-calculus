# Integral of exp(-x^2) from 0 to 0.5
terms <- function(n) (-1)^n*0.5^(2*n+1)/
  (factorial(n)*(2*n+1))
n <- 0:8
approx <- cumsum(terms(n))
exact <- integrate(function(x) exp(-x^2), 0, 0.5)$value
print(data.frame(n, approximation=approx,
                 abs_error=abs(approx-exact)))
