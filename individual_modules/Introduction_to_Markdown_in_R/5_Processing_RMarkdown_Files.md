# Introduction to Markdown in R

## Processing R Markdown documuments into final output format

Throughout this workshop, the gap between what syntax look like in a `.Rmd` file and how things appear in the final outputted document has been bridged using vague phrases like "*The HTML output generated upon processing the R Markdown document*...". Strictly speaking, the overall process of going from a `.Rmd` file to a final output document is known as ***rendering***.

### How are R Markdown files rendered into final output format?

The rendering process iself is akin to the following series of steps:

1. Running all code in the `.Rmd` file
2. Converting the `.Rmd` file to a `.md` file
3. Converting the resultant `.md` file to the final output format (e.g., HTML)

#### Rendering programatically:

Rendering can be undertaken programatically by calling the `render` function from the `rmarkdown` package in console, specifying the path to the `.Rmd` file to be rendered. For example, to render an R Markdown file called `my_file.Rmd` 
