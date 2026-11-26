for (n in c(10, 100, 1000)) {
  estimate <- midpoint_sum(function(x) x^2, 0, 2, n)
  cat("n =", n, ": estimate =", round(estimate, 6), "\n")
}
