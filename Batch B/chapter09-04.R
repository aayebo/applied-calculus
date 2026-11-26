x <- seq(-2, 2, length.out=401)
t3 <- x - x^3/factorial(3)
t5 <- t3 + x^5/factorial(5)
plot(x, sin(x), type="l", lwd=2,
     xlab="x", ylab="Function value")
lines(x, t3, lty=2)
lines(x, t5, lty=3)
legend("topleft", c("sin(x)", "Degree 3", "Degree 5"),
       lty=1:3, bty="n")
cat("Degree-5 error at 0.5:",
    abs(sin(0.5) - (0.5-0.5^3/6+0.5^5/120)), "\n")
