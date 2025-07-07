# Components of an R Markdown Document - A Visual Prelude

So far we have installed the `rmarkdown` package for producing Markdown documents in R, and used it to initialise a blank R Markdown document. It is worthwhile noting that, whereas standard Markdown files hold the `.md` file extention, raw R Markdown documents instead carry the `.Rmd` file extension. 

## What does a complete R Markdown document look like?

Adding contents to a raw R Markdown file will ultimately lead to something in the RStudio window that looks like the following:

![A screenshot of the RStudio IDE, displaying a populated R Markdown document titled "Untitled1" in the "Source" view. The document includes a YAML header defining the title as "Untitled," output as html_document, and date as "2025-04-29." Below the header, there's R code for setup, and a markdown heading "## R Markdown" followed by explanatory text about R Markdown and how the Knit button generates a document. The document also contains R code chunks, including summary(cars) and a chunk for plotting pressure versus plot(pressure), with a note explaining echo=FALSE. The "Environment" pane on the right shows "Environment is empty," and the "Console" at the bottom displays R version information.](Embedded_Display_Items/Completed_RMarkdown_View.png)

## What are the main components of an R Markdown document?

The above image provides a snapshot of the core components that make up an R Markdown document, namely:

1. The YAML header
2. Formatted plain text
3. Embedded code

We will explore each of these in more detail throughout the course of this workshop.
