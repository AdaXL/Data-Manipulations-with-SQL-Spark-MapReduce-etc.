#!/usr/bin/env Rscript

stopwords <- read.table("stop-word-list.txt")

process <- function (input) {
  # Do something more here!
  if (input %in% stopwords[,1] == FALSE) {
    output <- input
  }
    else {output <- NULL}
  return(output)
}


f <- file("stdin")
open(f)
while(length(line <- readLines(f, n=1)) > 0) {
  line = process(line)
  write(line, stdout())
}
