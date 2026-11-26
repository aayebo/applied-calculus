Tfun <- function(t) 22 + 60*exp(-0.12*t)
threshold_time <- -log(0.3)/0.12
cat('Threshold time:', threshold_time, '\n')
cat('Temperature check:', Tfun(threshold_time), '\n')
curve(Tfun(x), from=0, to=30, lwd=2,
      xlab='Minutes', ylab='Temperature (C)')
abline(h=c(22, 40), lty=2)
