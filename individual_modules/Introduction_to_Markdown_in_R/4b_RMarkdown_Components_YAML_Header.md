# Introduction to Markdown in R

## Components of an RMarkdown document: the YAML header

### What is the YAML header?
A YAML header is the first component worth adding to an RMarkdown file. Conceptually, it is a short block of text occuring at the start of an RMarkdown file that can be used to define metadata for the file as well as instructions on how the Rmarkdown file should be processed and how to style the output.

### What does a YAML header look like?
The YAML header is itself comprised of key-value pairs that are enclosed above and below by triple-dash (---) lines. An example YAML header is as follows:
```r
---
Author: John Smith
---
```
