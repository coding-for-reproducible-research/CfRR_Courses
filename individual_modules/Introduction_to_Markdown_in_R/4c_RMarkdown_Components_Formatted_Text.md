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

Any plain text that is written in the white space below the YAML header of the R Markdown file will then ultimately be included as normal text in the output document when the R Markdown file gets processed. In the case of the above example, the output would look like as follows:

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

!!! LINE BREAK WITH SINGLE SENTENCE OVER TWO LINES

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

In the above case we used a single `#` symbol to induce a header. Nevertheless, it is also possible to invoke sub-headings by adding multiple `#` symbols at the start of the required text. The number of `#` symbols used at the start of a given line then determines the level of the heading. For example:

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---
# Background:
This is my very first R Markdown document.

## Section 1
Some text.

### Section 1, subsection 1
Some more text.

## Section 2
Some text.

### Section 2, subsection 1
Some more text.

### Section 2, subsection 2
Even more text.

```

The resultant HTML output generated upon processing the above in an R Markdown file would subsequently look like:

![multiple headers]()

The lower the level of the heading, the smaller the header text is outputted. Also notice how unlike the case for unformatted plain text, when a header is invoked in R Markdown, the subsequent line is automatically treated as a new line in the output when the `.Rmd` file is processed. Further, if the table of contents (`TOC`) option is set to `TRUE` in the YAML header, the formatted text headers and subheaders will form the resultant table of contents in the output.

#### Font formatting:
Aside from the `#` symbol for invoking headers, dedicated Markdown annotation syntax also exists for boldening and/or italicising text (*via* the `*` symbol), as well as striking through text( *via* the `~` symbol), as follows:

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

When processed, the above R Markdown syntax would generate a HTML output looking like the below:

![font formatting]()

#### Lists:
Various types of lists can also be implemented in R Markdown. Unordered (bullet point) lists can be produced by starting a line with the `-` symbol, with it further possible to introduce sub-listing by indenting the `-` symbol with at least two spaces. For example:

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---

- list element 1
- list element 2
  - list element 2, sub-element 1
  - list element 2, sub-element 2
- list element 3

```

The resultant HTML output generated upon processing the above in an R Markdown file would subsequently look like:

![unordered lists]()

Ordered (numerical) lists just as easily implemented by starting a given line with a number joined to a `.` symbol. Ordered sublists are also possible using this convention, but require at least four spaces to invoke the indentation:

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---

1. list element 1
2. list element 2
    1. list element 2, sub-element 1
    2. list element 2, sub-element 2
3. list element 3

```

The above, when processed, will generate an output that looks like:

![ordered lists]()

Finally, it is possible to create task lists in R Markdown by implementing the following Markdown annotation syntax:

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---

- [ ] task 1
- [X] task 2

```

In the resultant HTML output, this would display as the following:

![task lists]()

### How can tables and images be embedded in an R Markdown document?
When creating an R Markdown document, it is likely that the output will include tables and figures that are directly generated by the R code that is included within the document. However, it is also possible to manually create text-based tables and integrate in external image files.

#### Embedding text-based tables:
Tables can be manually created in R Markdown by using a mix of the `|`, `-` and `:` symbols. The `|` symbol is used to demarcate columns, while the `-` symbol is used to seperate table headers from normal table text. For example:

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Text     | Text     | Text     |
| Text     | Text     | Text     |

```

When processed, the above R Markdown syntax would generate a HTML output that looks like the following:

![table unjustified]()

The `:` symbol can further be implemented to control text justification in the table:

```rmarkdown
---
title: "My html document"
author: "John Smith"
date: "`r Sys.Date()`"
output: html_document
---

| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Text     | Text     | Text     |
| Text     | Text     | Text     |
| Left     | Centre   | Right    |

```

The HTML output generated upon processing the above would subsequently look like:

![table justified]()

#### Embedding external images:
Both web-based images and locally saved images can be embedded into an R Markdown document.

!!! TEXT BASED TABLES ###
Tables
Images
hyperlinks
bibliography?
paragraphing & line breaks
Note on underline and changing colour
OTHER LIKE STRIKETHROUGH
visual items: tables, images

!!! ESCAPING

!!! TASK
