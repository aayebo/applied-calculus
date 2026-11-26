central_diff <- function(f, x, h = 1e-4) {
  (f(x + h) - f(x - h)) / (2*h)
}
central_diff(function(x) sin(x), pi/3)
cos(pi/3)
