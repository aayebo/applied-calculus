partial_power <- function(x, N) {
  n <- 1:N
  sum((x-2)^n/(n*3^n))
}
for (x in c(-1, 0, 2, 4, 5)) {
  cat("x =", x, " S100 =", partial_power(x, 100), "\n")
}
