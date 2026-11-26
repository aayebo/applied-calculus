F <- function(x) exp(2*x) * (x^2/2 - x/2 + 1/4)
f <- function(x) x^2 * exp(2*x)
h <- 1e-5
for (x in c(0, 0.5, 1, 2)) {
  derivative <- (F(x+h)-F(x-h))/(2*h)
  cat('x:', x, ' numerical derivative:', round(derivative,6),
      ' integrand:', round(f(x),6), '\n')
}
