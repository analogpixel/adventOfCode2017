
input <-as.list(read.delim("/Volumes/ANALOG/classes/adventOfCode/day2.tab", header = FALSE))
sl <- lapply(input, function(x) sort(x))

f <- function(n,l) Find(function(x) x %% n == 0, l, nomatch = -1 )

