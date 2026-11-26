v <- function(t) t - 2
net <- integrate(v, 0, 4)$value
distance <- integrate(function(t) abs(v(t)), 0, 4)$value
cat("Displacement:", net, "m\n")
cat("Distance:", distance, "m\n")
curve(v(x), from=0, to=4, xlab="Time (s)", ylab="Velocity (m/s)")
abline(h=0, lty=2)
