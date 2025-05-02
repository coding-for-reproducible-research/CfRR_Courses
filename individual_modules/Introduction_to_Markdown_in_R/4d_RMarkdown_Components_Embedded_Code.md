# Introduction to Markdown in R

## Components of an R Markdown document: embedded code

As mentioned earlier on in this workshop, one of the primary benefits of R Markdown is the ability to integrate formatted plain text with R code and its outputs into a single dynamic document. Code can be embedded into R Markdown documents in two different forms:

1. In-line code
2. Code chunks

### How is in-line code embedded into an R Markdown document?

In-line code refers to snippets of code that is embedded withn the text element of the R Markdown document. This can be helpful for when results or values need to be dynamically inserted without breaking the textual flow. The Markdown syntax for adding in-line R code in R Markdown is `r <your code>`, for example:

