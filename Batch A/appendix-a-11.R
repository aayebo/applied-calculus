x <- seq(-2, 2, length.out = 401)
plot(x, x^2, type = "l", lwd = 2,
     ylim = c(-1, 5), xlab = "x", ylab = "y")
lines(x, 2*x + 1, lty = 2, lwd = 2)
legend("topleft", legend = c("x^2", "2x + 1"),
       lty = c(1, 2), lwd = 2, bty = "n")
