# Introduction to Markdown in R

## Processing R Markdown documents into final output format

Throughout this workshop, the gap between what syntax looks like in a `.Rmd` file and how things appear in the final output document has been bridged using vague phrases like "*The HTML output generated upon processing the R Markdown document*...". To be more precise, the overall procedure of going from a `.Rmd` file to a final output document is called **rendering**.

### How are R Markdown files rendered into final output format?

The rendering process itself is akin to the following series of steps:

1. Running all code in the `.Rmd` file
2. Converting the `.Rmd` file to a `.md` file
3. Converting the resultant `.md` file to the final output format (e.g. HTML)

#### Rendering programatically:

Rendering can be undertaken programatically by calling the `render` function from the `rmarkdown` package in console, specifying the path to the `.Rmd` file that is to be rendered. For example, to render an R Markdown file called `my_file.Rmd` saved in the downloads folder of a local user's (User1) profile, the following line of R code could be run:

```r
rmarkdown::render("/Users/User1/Downloads/my_file.Rmd")
```

This will automatically produce the output format type as defined in the YAML header of the R Markdown file. Nevertheless, the output format type in the YAML header can also be over-ridden in the `render` function by specifying an alternative output format using the `output_format` argument.

#### Rendering non-programatically:

RStudio offers an alternative, user-friendly functionality for rendering R Markdown files, known as **knitting**. Strictly speaking the knitting process operates programatically, but does so under the hood, enabling the user to complete the rendering process simply by clicking buttons.

Knitting a `.Rmd` file in RStudio can be performed by clicking the <img src = "Embedded_Display_Items/knit_button.png" alt = "knit button" height = "25" style = "vertical-align:middle;"> button. Clicking directly on the blue ball of wool will automatically render the output format type as defined in the YAML header of the R Markdown file. Nevertheless, clicking on the drop-down arrow part of the button will bring up alternative output format options should they be desired. 

It is worth noting that regardless of whether you choose to render programatically or using the RStudio knitting tool, rendering to PDF output format requires LaTeX to work.

### Task

Try to render your R Markdown file. Note that the rendered output should automatically save in the same location on your computer that your `.Rmd` file is saved in.


