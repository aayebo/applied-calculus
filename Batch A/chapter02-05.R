epsilon <- 0.4
delta <- min(1, epsilon/5)
x <- seq(1.7, 2.3, length.out = 400)
plot(x, x^2, type = "l", col = "navy",
     xlab = "x", ylab = "x^2")
abline(h = c(4-epsilon, 4+epsilon), col = "red", lty = 2)
abline(v = c(2-delta, 2+delta), col = "blue", lty = 2)
cat("epsilon =", epsilon, "delta =", delta, "\n")
