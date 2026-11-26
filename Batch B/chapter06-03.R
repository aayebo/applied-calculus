poly_length <- function(n) {
  x <- seq(0, 1, length.out=n+1)
  y <- x^2
  sum(sqrt(diff(x)^2 + diff(y)^2))
}
exact_num <- integrate(function(x) sqrt(1+4*x^2), 0, 1)$value
for (n in c(4, 8, 16, 32, 64, 128)) {
  cat("n =", n, "polygon =", round(poly_length(n), 8),
      "error =", round(exact_num-poly_length(n), 8), "\n")
}
