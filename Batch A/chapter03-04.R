t <- seq(0, 6, length.out=301)
s <- 12*t - 2*t^2
v <- 12 - 4*t
a <- rep(-4, length(t))
plot(t, s, type="l", col="blue",
     xlab="time (s)", ylab="value")
lines(t, v, col="red", lty=2)
lines(t, a, col="darkgreen", lty=3)
legend("topright", c("s", "v", "a"),
       col=c("blue","red","darkgreen"),
       lty=1:3)
