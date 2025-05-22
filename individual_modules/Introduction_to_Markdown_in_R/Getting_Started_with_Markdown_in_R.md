# Getting Started 

## What are the benefits of using Markdown in R?

Implementing Markdown in R provides many benefits, for example:

| Benefit  | Description |
| :------: | :---------- |
|Dynamic document creation| Using Markdown in R offers a platform to be able to integrate descriptive text, R code and its outputs into a single resource. This enables you to create notebooks for your coding projects in a similar way that a biologist might have a physical notepad for documenting their laboratory experiments. Moreover, Markdown in R permits live interactions and execution of code, meaning that you can still run your code in real time when applying Markdown in R. This can be be very helpful when testing, trialing or debugging your code.|
|Reproducibility| Having R code and plain text together in a single document means that you can provide more detailed descriptions on what the code is doing and the theorical thinking behind things. This is helpful not only for your own understanding but also when sharing your code with others. Reproducibility of R code-based piplelines is therefore enhanced *via* implementation of Markdown in R. Perhaps the best demonstration of this is that many of the tutorials for R packages you might have come across will have been produced using Markdown in R. Reproducibility is also facilitated by the fact that whenever your Markdown file in R is processed, your code can be re-run from top to bottom, ensuring that the output reflects the most up-to-date data and analysis.|
|Felixble outputs| Through implementation of Markdown in R, your R code and plain text can be integrated together in a variety of different output formats, from interactive HTML reports that can be viewed in a browser, to print-friendly PDF files, editable Microsoft Word documents and even Microsoft Powerpoint Presentation format. As such, you have the flexibility to be able to present and share your R code in a way that you most prefer or that is best suited to the context at hand. |
|Multiple languages| While the most logical implementation of Markdown in R is to produce dynamic documents of R code alongside formatted text, it is also possible to integrate and run other programming languages through Markdown in R, such a Python. This can be very useful in cases where you might need to leverage functions or libraries in the same pipeline that are native to different coding languages. |

## How is Markdown implemented in R?

Markdown is predominantly implemented in R *via* RStudio using a dedicated R package called `rmarkdown`.

### Installing the `rmarkdown` package:

The `rmarkdown` package is available for download and installation through the Comprehensive R Archive Network (CRAN). This process can be undertaken by first opening RStudio and then performing the following click-button steps:

1. Click `Tools` at the top of the screen
2. Select `Install Packages...`
3. Keep the `Install from:` box set as `Repository (CRAN)`
4. Type `rmarkdown` into the `Packages` box
5. Ensure `Install dependancies` is ticked
6. Keep the `Install to Library:` box as the default path given
7. Click `Install`

Alternitively, after opening RStudio, `rmarkdown` can be downloaded and installed programatically by running the following command in the RStudio console:

```r
install.packages('rmarkdown')
```

### Creating a new R Markdown document:

Once the `rmarkdown` package has been installed, a new, blank R Markdown document can be created in RStudio by:

1. Clicking `File` at the top of the screen
2. Selecting `New File`
3. Choosing `R Markdown...`
4. Clicking `Create Empty Document` on the resultant pop-up screen

Completing the above four steps should result in an RStudio window that looks like the following:
![Blank RMarkdown file](Embedded_Display_Items/Blank_RMarkdown_View.png)

### Saving a (new) R Markdown document:

After initialising a new R Markdown document, it can be saved by clicking `File` at the top of the screen and selecting `Save`. Alternatively, the save process can be performed by clicking the ![Floppy Disk](./Embedded_Display_Items/floppy_disk.png) button. It is also good practice to repeat the save process regularly when putting together an R Markdown document so that no progress is lost.


