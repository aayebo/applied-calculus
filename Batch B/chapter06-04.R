surface <- integrate(function(x) 2*pi*sqrt(x)*
                     sqrt(1+1/(4*x)), 1, 4)$value
cost_per_m2 <- 18
cat("Lateral surface area:", round(surface, 6), "m^2\n")
cat("Estimated coating cost: $", round(cost_per_m2*surface, 2), "\n")
