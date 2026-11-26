Q0 <- 120
k <- log(0.6)/4
t <- seq(0, 16, length.out=250)
plot(t, Q0*exp(k*t), type='l', lwd=2,
     xlab='Hours', ylab='Amount (mg)')
abline(h=Q0/2, lty=2)
cat('Decay constant:', k, '\n')
cat('Half-life:', log(0.5)/k, '\n')
