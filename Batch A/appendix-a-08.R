concentration <- function(t, initial = 18, rate = 0.3) {
  2 + initial * exp(-rate * t)
}
concentration(0)
concentration(5)
concentration(c(0, 5, 10), rate = 0.2)
