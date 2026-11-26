work <- function(spout_height) {
  integrate(function(y) 1000*9.8*pi*(spout_height-y),
            0, 3)$value
}
heights <- c(3, 3.5, 4, 5)
results <- data.frame(outlet_m=heights,
                      work_J=sapply(heights, work))
print(results)
plot(results$outlet_m, results$work_J, type="b",
     xlab="Outlet height above bottom (m)", ylab="Work (J)")
