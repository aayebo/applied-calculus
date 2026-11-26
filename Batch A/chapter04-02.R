f <- function(x) x^2
slope <- (f(3)-f(1))/(3-1)
c_value <- slope/2
curve(f(x), from=0.5, to=3.5, lwd=2,
      xlab="x", ylab="f(x)")
abline(a=-3, b=slope, col="red", lwd=2)
abline(a=-4, b=slope, col="blue", lty=2)
cat("Secant slope:", slope, " MVT point:", c_value, "\n")
