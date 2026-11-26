h <- 10^(-seq(1, 14, by = 1))
naive <- (sqrt(9 + h) - 3) / h
stable <- 1 / (sqrt(9 + h) + 3)
results <- data.frame(h, naive, stable,
                      absolute_error = abs(naive - 1/6))
print(results, digits = 9)
plot(h, abs(naive - 1/6), log = "xy", pch = 19,
     xlab = "h", ylab = "Absolute error")
points(h, abs(stable - 1/6), col = "red", pch = 1)
