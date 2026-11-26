f <- function(x) exp(-x^2)
quad <- function(n) {
  a <- 0; b <- 2; h <- (b-a)/n
  x <- seq(a,b,length.out=n+1)
  mid <- (x[-1]+x[-length(x)])/2
  midpoint <- h*sum(f(mid))
  trapezoid <- h*(sum(f(x))-(f(a)+f(b))/2)
  simpson <- h/3*(f(a)+f(b)+4*sum(f(x[seq(2,n,2)]))+
                       2*sum(f(x[seq(3,n-1,2)])))
  c(midpoint=midpoint,trapezoid=trapezoid,simpson=simpson)
}
reference <- integrate(f,0,2)$value
for (n in c(4,8,16,32)) {
  v <- quad(n)
  cat('n=',n,' errors=',round(abs(v-reference),8),'\n')
}
