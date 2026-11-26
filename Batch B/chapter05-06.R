C <- function(t) 3 + 12*exp(-0.4*t)
auc <- integrate(C, 0, 8)$value
average <- auc/8
cat("AUC:", auc, "mg*h/L\n")
cat("Mean concentration:", average, "mg/L\n")
curve(C(x), from=0, to=8, lwd=2,
      xlab="Time (h)", ylab="Concentration (mg/L)")
