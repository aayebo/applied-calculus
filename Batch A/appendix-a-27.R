target <- 40
threshold <- uniroot(function(t) Tmodel(t) - target,
                     interval = c(0, 30))$root
cat("The model reaches", target, "C at about",
    round(threshold, 2), "minutes.\n")
