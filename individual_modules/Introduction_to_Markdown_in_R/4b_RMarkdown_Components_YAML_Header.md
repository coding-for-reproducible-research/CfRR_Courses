# Introduction to Markdown in R

## Components of an R Markdown document: the YAML header

### What is the YAML header?
A YAML header is the very first component worth adding to an R Markdown file. Conceptually, it is a short block of text occuring at the start of an R Markdown file that can be used to define metadata for the file as well as instructions on how the R Markdown file should be processed and how to style the output.

### What does a YAML header look like?
The YAML header is itself comprised of key-value pairs that are enclosed above and below by triple-dash (---) lines. An example YAML header is as follows:
```r
---
title: "My html document"
author: "John Smith"
date: "2025-04-29"
output: html_document
---
```
In this particular example, the following YAML key-value pairs have been used:

| Key     | Value               |
|:------: | :-----------------: |
| title   | "my html document"  |
| author  | "John Smith"        |
| date    | "2025-04-29"        |
| output  | html_document       |

Here, the `title`, `author` and `date` YAML keys act to define metadata for the file and their assigned values will get displayed in the resultant output. The output format is itself controlled by the `output` YAML key, which in this case has been assigned the value `html_document` (note the lack of quotation marks) so that a HTML output gets produced.

It is worthwile noting that the `date` key does not necessarily have to be assigned a physical value. If you'd prefer to set things up so that the current date is always given in the output when the R Markdown file gets processed, you could replace the written date as follows:

```r
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---
```
The `r Sys.Date()` syntax used here also provides an example of how R code can embedded into R Markdown documents. We will explore this more later on in the workshop.

### Is HTML the only `output` option in a YAML header? 
The `title`, `author` and `date` fields are core metadata keys of a YAML header in R Markdown documents. Nevertheless, if desired, each can be ignored by setting the assigned value to `NULL` or by simply removing the corresponding line of code. While we will focus on HTML outputs in this workshop for simplicity (can be viewed on a web browser), there are many other possible options that exist when it comes to controlling the output format in a YAML header using the `output` key. For example, we can instruct for a Microsoft Word file (.docx) to get produced when the R Markdown file is processed *via* the following:

```r
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: word_document
---
```
Some output options can be leveraged regardless of output format, whereas other are only valid for specific types of output format. The most common output types and options when defining the `output` key of a YAML header are as follows (sourced from [posit](https://posit.co/wp-content/uploads/2022/10/rmarkdown-1.pdf):


depends on type of output

Embed keys for output example

### Task
