shell <- integrate(function(x) 2*pi*x*(4-x^2), 0, 2)$value
disk  <- integrate(function(y) pi*(4-y), 0, 4)$value
exact <- 8*pi
cat("Shell:", round(shell, 6), "\n")
cat("Disk: ", round(disk, 6), "\n")
cat("Difference:", abs(shell-disk), "\n")
cat("Exact:", round(exact, 6), "\n")
