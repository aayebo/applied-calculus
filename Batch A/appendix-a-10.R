x <- seq(-3, 3, length.out = 401)
y <- x^3 - 2*x + 1
plot(x, y, type = "l", lwd = 2,
     main = "A cubic function",
     xlab = "x", ylab = "f(x)")
abline(h = 0, v = 0, lty = 3)
grid()
