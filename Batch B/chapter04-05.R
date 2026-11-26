volume <- function(x) x*(30-2*x)*(20-2*x)
answer <- optimize(volume, interval=c(0,10), maximum=TRUE)
print(answer)
curve(volume(x), from=0, to=10, lwd=2,
      xlab="Cut size (cm)", ylab="Volume (cm^3)")
abline(v=answer$maximum, col="red", lty=2)
