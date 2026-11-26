n <- 1:300
geo <- cumsum(0.7^(n-1))
harmonic <- cumsum(1/n)
plot(n, harmonic, type="l", lwd=2,
     xlab="Number of terms", ylab="Partial sum")
lines(n, geo, lty=2, lwd=2)
legend("topleft", c("Harmonic", "Geometric"),
       lty=c(1,2), bty="n")
cat("Geometric limit:", 1/(1-0.7), "\n")
