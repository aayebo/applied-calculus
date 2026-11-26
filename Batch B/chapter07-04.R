t <- seq(0, 20, length.out=300)
y <- 50/(1 + 4*exp(-0.4*t))
plot(t, y, type='l', lwd=2,
     xlab='Time', ylab='Population')
abline(h=50, lty=2)
cat('At t=10:', 50/(1 + 4*exp(-4)), '\n')
