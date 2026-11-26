f <- function(x) exp(-x^2)
for (n in c(10, 20, 40, 80)) {
  h <- 2/n
  mid <- (0:(n-1)+0.5)*h
  midpoint <- h*sum(f(mid))
  cat("n =", n, " midpoint =", midpoint, "\n")
}
cat("Adaptive quadrature:", integrate(f, 0, 2)$value, "\n")
