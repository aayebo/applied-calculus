error <- abs(estimate - 8/3)
if (error < 0.001) {
  cat("The approximation meets the tolerance.\n")
} else {
  cat("Increase the number of subintervals.\n")
}
