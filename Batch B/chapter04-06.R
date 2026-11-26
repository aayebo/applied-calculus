newton <- function(f, df, x0, tol=1e-10, maxit=30) {
  x <- x0
  for (k in seq_len(maxit)) {
    fx <- f(x); dfx <- df(x)
    if (!is.finite(fx) || !is.finite(dfx) || abs(dfx)<1e-12)
      stop("Nonfinite value or derivative too small")
    next_x <- x - fx/dfx
    cat("iter",k,"x =",format(next_x,digits=12),
        "residual =",format(abs(f(next_x)),digits=4),"\n")
    if (abs(next_x-x)<tol && abs(f(next_x))<tol)
      return(next_x)
    x <- next_x
  }
  warning("Maximum iterations reached without convergence")
  x
}
newton(function(x) x*x-2, function(x) 2*x, 1)
