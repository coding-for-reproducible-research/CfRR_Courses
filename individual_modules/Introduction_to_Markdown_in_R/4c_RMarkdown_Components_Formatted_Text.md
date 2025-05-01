# Introduction to Markdown in R

## Components of an R Markdown document: formatted plain text

Many of the features that you might implement in other text-based applications like Microsoft Word can also be easily implemented in R Markdown documents. This could range from basic alterations to text aesthetics, through to the addition of tables and images, or even the inclusion of hyperlinks.

### How is plain text added to an R Markdown document?

Adding text to an R Markdown document is as straightforward as typing what you want to write in any of the white space below the YAML header, for example:

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---
Background:
This is my very first R Markdown document.
```

Any plain text that is written in the white space below the YAML header of the R Markdown file will then ultimately be included as normal text in the output document when the R Markdown file gets processed. In the case of the above example, the output would look like as follows (opened in Google Chrome):

![initial written text output]()

Notice how, despite typing the text over two lines in R Markdown itself, it all falls on the same line in the HTML output. To display unformatted plain text in a `.Rmd` file on seperate lines in the processed output, you can use the Markdown line break syntax `<br>` (only works for HTML), end the above of the lines with two spaces, or (for a slightly larger gap) simply include a blank line (both the latter work for HTML, Word and PDF outputs). For example: 

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---
Background: <br>
This is my very first R Markdown document (Markdown line break syntax).

Background:  
This is my very first R Markdown document (two spaces at end of the above line).

Background:

This is my very first R Markdown document (blank line in-between).

```

When processed, the above would then produce a HTML output looking like the following:

![written text output with spacing]()

### How can the aethetics of plain text be adjusted in R Markdown?

The aethetics of text written in an R Markdown document can be easily modified by applying the annotation syntax that underlies the Markdown language. This can include making headers, boldening and/or italicising text, and creating lists.

#### Adding headers:
In Markdown language, a line of plain text can be converted into a header by placing a `#` symbol at the start of that line (making sure there is a space between the `#` symbol and the first letter of text). For example: 

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---
# Background:
This is my very first R Markdown document.
```

Notice how the plain text on the line starting with the `#` now appears blue. This is an example of annotation syntax highlighting in R Markdown, which usefully makes the specific bits of text being formatted stand out. Processing the above in an R Markdown file would then generate a HTML output that displays like the following:

![single header]()

In the above case we used a single `#` symbol to induce a header. Nevertheless, it is also possible to invoke sub-headings by adding multiple `#` symbols at the start of the required text. Accordingly, the number of `#` symbols used at the start of a given line determines the level of the heading. For example:

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---
# Background:
This is my very first R Markdown document.

## Background subsection 1
Subsection 1 text goes here.

### Subsection 2
Subsection 2 text goes here.
```

The resultant HTML output generated upon processing the above in an R Markdown file would then look like:

![multiple headers]()

Notice how unlike the case for unformatted plain text, when a header is invoked in R Markdown, the subsequent line is automatically treated as a new line in the output when the `.Rmd` file is processed.

!!! HEADERS = TOC

#### Font formatting:
Aside from the `#` symbol for invoking headers, dedicated Markdown annotation syntax also exists for boldening text, itallicising text, striking through text, and even illustrating quotes, as follows:

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---

*italic text*

**bold text**

***bold and italic text***

~~strike-through text~~

# *Italic header*

```


!!! HEADERS = TOC

!!! TEXT BASED TABLES ###
Tables
Images
hyperlinks
bibliography?
paragraphing & line breaks
Note on underline and changing colour
OTHER LIKE STRIKETHROUGH
visual items: tables, images


Many of the text formatting like in Microsoft Word, such as altering text appearance, including tables and images, and even embedding hyperlinks can be straightforwardly applied in R Markdown documents

can be straighforwardly applied in R Markdown documents
