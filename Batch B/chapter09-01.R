n <- 1:100
terms <- (-1)^(n - 1) / n
partial <- cumsum(terms)
plot(n, partial, pch=16, cex=0.45,
     xlab="Number of terms", ylab="Partial sum")
abline(h=log(2), lty=2)
cat("100-term estimate:", tail(partial, 1), "\n")
cat("Exact limit:", log(2), "\n")
