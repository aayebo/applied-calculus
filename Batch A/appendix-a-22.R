ambient <- 22
initial <- 82
k <- 0.12
Tmodel <- function(t) ambient + (initial - ambient)*exp(-k*t)
time <- seq(0, 30, length.out = 301)
plot(time, Tmodel(time), type = "l", lwd = 2,
     xlab = "Time (min)", ylab = "Temperature (C)",
     main = "Cooling model")
abline(h = ambient, lty = 2)
