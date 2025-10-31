# Text Formatting in Markdown

## Learning Objectives
By the end of this lesson, you will be able to understand and apply the following Markdown formatting features:

- Structuring content with headings
- Styling text (bold, italics, strikethrough)
- Creating ordered and unordered lists
- Embedding code, links, and images
- Building tables and inserting horizontal lines

Mastering these fundamentals will enable you to produce clean, well-organised documents efficiently.

## Key Points
This table is a helpful summary of the key Markdown features we're going to cover in this section and can serve as a useful reference when using Markdown in the future.

| Feature         | Syntax Example                  |
|---------------|--------------------------------|
| **Headings**   | `## Heading 2`                 |
| **Bold**       | `**Bold**`                     |
| **Italic**     | `*Italic*`                     |
| **Bold & Italic** | `***Bold & Italic***`     |
| **Strikethrough** | `~~Strikethrough~~`       |
| **Lists**      | `- Item` (bullets) <br> `1. Item` (numbered) |
| **Task Lists** | `- [ ] Task` (unchecked) <br> `- [x] Task` (checked) |
| **Blockquotes** | `> Quote`                     |
| **Inline Code** | `` `code` ``                  |
| **Code Blocks** | ```` ```python `print("Hello")` ``` ```` |
| **Tables**     | `| Col1 | Col2 |`              |
| **Horizontal Line** | `---`                   |
| **Links**      | `[Url](URL)`                  |
| **Images**     | `![Alt text](URL/path)`             |

Let's now explore how to implement each of these features.

## Create a MD file in Jupyter Notebook.
You can create a Markdown (MD) file using many different tools or environments, such as VS Code, plain text editors, or browser-based platforms like GitHub. For this course, we will focus on using JupyterLab, which offers an easy and integrated way to work with both Markdown and Python.

## What is an `md` file? 

A `.md` file is a plain text file that contains Markdown-formatted text. The `.md` extension stands for Markdown, and it is commonly used for documentation files because it is simple to write and renders cleanly across many platforms.

A common example you’ll see is `README.md`, which often appears in GitHub repositories. This file usually contains an introduction to a project, instructions, or other relevant notes, and is automatically rendered as formatted text when viewed on GitHub.

## Creating an `.md` file in JupyterLab

To create a Markdown file within the JupyterLab interface:

1. Open JupyterLab.
   - if you're already running it, go to your browser window.
   - if not, launch it from your terminal with 'jupyter lab'.
3. Click the file menu.
   - At the top left, select File > New > Markdown File.
4. Rename the file.
   - In the file browser on the left, right-click the new text file and choose `Rename`.
5. Start writing Markdown!
   - Right-click on the file and choose `Show Makdown Preview` from the drop-down menu.
   - The rest of this section will guide you through the various formatting features you can use to present your content effectively.


## 1. Headings 

Headings are essential for organising your content and making documents easier to navigate. In Markdown, headings are created by placing one or more hash `#` symbols at the beginning of a line. The number of hash symbols you use determines the level of the heading.


Here is how you can create headings of different levels:
```
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

```
When rendered, the headings will appear with different font sizes and weights, visually indicating their hierarchy within the document:

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

Use headings thoughtfully to create a clear structure. Typically, you should use one Heading 1 per document (usually for the title), and then use Heading 2, Heading 3, and so on, to organise sections and subsections logically.


## 2. Paragraphs & Line Breaks

Paragraphs and line breaks are fundamental to writing clear, readable documents. In Markdown, controlling the flow of text is simple but requires attention to a few small details.

A line break within a paragraph is created by adding two spaces at the end of a line and then pressing `Enter`(or creating a new line).

To create a full paragraph break (a blank line between paragraphs), you simply press Enter twice.

Here is **an example:**

```
This is the first paragraph.  

This is the second paragraph with a  
line break inside.
```

**Output:**
This is the first paragraph.  

This is the second paragraph with a  
line break inside.

## 3. Text and Text Styling

Typing plain text directly into your Markdown file will produce normal text in the output document. No special formating is required and it will simply be treated as plain text.

Markdown makes it easy to emphasise text by applying styles such as bold, italics, or strikethrough. Styling your text appropriately can help draw attention to key points or indicate changes in meaning.

Here are the main text styles:

 - **Bold**: `**Bold text**`
   
 - *Italic*: `*Italic*`

 - ***Bold and italic text***: `***Bold and italic text***`

 - **Strikethrough**: `~~Strikethrough text~~`

These styles help make your writing easier to read. Use them to highlight important points, but keep it simple so your document stays clean and easy to follow.

## 4. Lists

Lists are a great way to make your documents easier to scan and helps readers find key information quickly. In Markdown, you can create both unordered lists (bullet points) and ordered lists (numbered steps).

### Unordered Lists (Bullets)
To make a bullet point, start a line with `-`, `+`, or `*`. It is of note that the different symbols you can use to create a bulleted list are all treated the same by the Markdown processor and will therefore render identically as a disc bullet. Whilst they render the same, for consistency we recommend you use the same symbol within a list and not mix between them, because some Markdown parsers or linters may warn about inconsistent style. You can also create sublists by indenting with at least two spaces.

**Example:**
```
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2

```

**Output:**
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2

### Ordered Lists (Numbers)

To make a numbered list, just start each line with a number followed by a full stop `.` and a space.

```
1. First item
2. Second item
   1. Subitem 2.1
   2. Subitem 2.2
```

**Output:**
1. First item
2. Second item
   1. Subitem 2.1
   2. Subitem 2.2

## 5. Task Lists

Task lists are useful when you want to show items that need to be completed — like a to-do list. In Markdown, you can create checkboxes easily.

- to make an unchecked box, use `- []`.
- to make a checked box, use `- [x]`.

**Example:**
```
- [ ] Task 1
- [x] Task 2

```

**Output:**

- [ ] Task 1
- [x] Task 2

Task lists can make your document more interactive and organised. 

## 6. Blockquotes

Blockquotes are used to highlight quotes, important information, or notes in your document.

To create a blockquote, start a line with a `>` symbol. If you want to create a nested blockquote (a quote inside a quote), use `>>`.

**Example:**
```
> This is a blockquote.
>> This is a nested blockquote.
```

**Output:**
> This is a blockquote.
>> This is a nested blockquote.


## 7. Code Formatting

Markdown makes it easy to format code, whether it's a single line or multiple lines. Code formatting helps distinguish code from regular text, making it easier to read and understand.

### Inline Code

To format a short piece of code inline, wrap it in single backticks (`).

**Example**:
```
Use the `print()` function in Python. 
```

**Output:**
Use the `print()` function in Python. 


### Code Blocks

For longer code or multi-line code blocks, use triple backticks (```) to create a block. You can also specify the programming language after the first set of backticks to enable syntax highlighting.

**Example**:
```
```python
def greet():
    print("Hello, World!")
```

**Output:**

```python
def greet():
    print("Hello, World!")
```

In order to execute the code block, we need to use Jupyter Notebook (`.ipynb`). We will learn how to do this in the following section.

## 8. Tables

Tables help make data clearer and more structured, especially when you need to present multiple pieces of information side by side. In Markdown, you can create tables easily using the `|` symbol to separate columns and `-` to create row separators.

```
| Name  | Age | Job       |
|-------|-----|----------|
| Alice | 30  | Engineer |
| Bob   | 25  | Designer |

```

**Output:**

| Name  | Age | Job       |
|-------|-----|----------|
| Alice | 30  | Engineer |
| Bob   | 25  | Designer |


## 9. Horizontal Lines

Horizontal lines are used to separate sections of your document, providing a clear visual break. In Markdown, you can create a horizontal line using three `-`, `*`, or `_` symbols.

```
---
```

**Output:**

---


## 10. Links and Images

Adding links and images is a great way to enrich your documents. In Markdown, adding links and images is simple and can be done with a straightforward syntax.

**Links** 

To create a link, use the format `[Url](URL)`. This will display the text as a clickable link that directs to the specified URL.

**Example:**
```
[University of Exeter](https://www.exeter.ac.uk/)
```

**Output:**
[University of Exeter](https://www.exeter.ac.uk/)

**Images - Web** 

To add an image from the web, use the format `![alt text](image URL)`. The '!' at the beginning of the syntax distinguishes an image from a link and is telling Markdown to display an image rather than render the line as a hyperlink. The "alt text" is important for accessibility, providing a description for screen readers.

```
![This is the alt text for the image: Close-up of a gray-and-white tabby cat with a pink nose, looking over its shoulder against a black background.](https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187.jpg?w=1436&h=958)
```

**Output:**
![This is the alt text for the image: Close-up of a gray-and-white tabby cat with a pink nose, looking over its shoulder against a black background.](https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187.jpg?w=1436&h=958)

**Images - Local** 

To add an image from your computer, use the same format but specify the file path instead of a URL.

Format: `![alt text](image path)`.

```
![alt text for screen readers](cat_pic.png)
```

**Output:**
![A white and tabby cat with large, wide blue eyes and prominent pink nose, looks curiously over its right shoulder. The cat's whiskers are long and extend out to the left, standing out against the plain black background.](cat_pic.png)

## 11. Escaping
Sometimes, you might want to display special characters (like `*`, `_`, or `#`) in your text without them being interpreted as formatting. To do this, you can escape the character by placing a backslash (`\`) before it.

For example, if you want to display `*` before a word without it making the text italic, use `\*`.

**Example:**
`\*Not italicized\*`

**Output:**
\*Not italicized\*

## Final Thoughts
These are the basics of Markdown formatting, most often used when creating a `README.md` file. A `README.md` file explains the purpose, setup, and usage of a coding project. It serves as the project's main documentation and is usually the first thing users see in a repository. Every Git repository typically includes one, making Markdown a great way to document and showcase your work clearly and effectively.

While `md` files support rich formatting, `README` can also be plain `txt` files, though they won't include formatting like headings or lists. 
