T <- function(t) 22+58*exp(-0.18*t)
dT <- function(t) -10.44*exp(-0.18*t)
cat("T(5) =", round(T(5), 3), "\n")
cat("T'(5) =", round(dT(5), 3), "\n")
curve(T(x), 0, 30, col="blue",
      xlab="time (min)", ylab="Temp (C)")
