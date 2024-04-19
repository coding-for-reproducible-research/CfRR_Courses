# Getting Up and Running with R


In this session we are going to cover some background to R and Rstudio and provide you with a guided tour of RStudio. We assume that you already have both of these installed on your machines.

# Why R?

**R** is a free software program primarily used for statistical analysis. It has become incredibly popular, particularly in biological sciences. 

The basis of programming is that we write down instructions for the computer to
follow, and then we tell the computer to follow those instructions. We write, or
*code*, instructions in R because it is a common language that both the computer
and we can understand. We call the instructions *commands* and we tell the
computer to follow the instructions by *executing* (also called *running*) those
commands.

Some reasons for it's popularity are: 

* it’s free, well-documented, and runs almost everywhere
* it has a large (and growing) user base among scientists
* it has a large library of external packages available for performing diverse tasks
* it is a gateway into other programming languages

>
> ## Task: This is a great point you as a learner to reflect on why you are here, how will R help you with your research or daily activities? 
>

We should also note that, the two most important reasons for choosing a language are to use whatever language your colleagues are using, so you can share your work with them easily, and to use that language well.



# What are R and RStudio?

[R](https://www.r-project.org/) is the programming language that we use to tell the computer what to do. 

[RStudio](https://www.rstudio.com/), is an Integrated Development Environment (IDE) that provides an interface designed to improve the experience of programming with R, and to facilitate more efficient and reproducible code development. It is designed so you can have multiple elements visible at the same time within a single programme. For example plots, tables and code, rather than juggle different programmes or windows. 

We will use RStudio IDE to write code, navigate the files found on our computer, inspect the variables we are going to create, and visualize the plots we will generate. RStudio can also be used for other things (e.g., version control, developing packages, writing Shiny apps, creating documents and slides) that we will not cover during the workshop. It can be a very powerful tool for managing how you develop code, software or programmes. 


# Navigating RStudio

When you open RStudio, you will see a screen like the one below, with three windows automatically open. 

![Alt Text](../images/rstudio_screen.png)

<br>

We will add a fourth panel, arguably the most important one. Click on the icon at the top right of the window on the left, to get the screen with four sections. This is the most common set up. 

![Alt Text](../images/rstudio_screen_1.png)

<br>

RStudio is divided into 4 "Panes". 

![Alt Text](../images/rstudio_screen_3.png)

<br>

**Pane 1 (top-left in the default layout):** This pane is a text editor, where you can write the commands/code you intend on running. You can use this editor, you edit any type of file, but it is typically used to record or plan your R code. A file containing programming commands is normally called a script. It can then be saved to your computer as you would do with a word or excel file.

**Pane 2 (bottom-left):** This is the R console, this is where commands are entered for the computer to run.

**Pane 3 (top-right):** This window has multiple tabs including, Environment, History and collates information relating to your current R session. 

**Pane 4 (bottom-right)** This window is also multi-tabbed, but has a file explorer, presents the plots/images you create along with the help pages for the R functions. 

The placement of these panes and their content can be customized
(see menu, RStudio -> Preferences -> Pane Layout). One of the advantages of
using RStudio is that all the information you need to write code is available in
a single window. Additionally, with many shortcuts, autocompletion, and
highlighting for the major file types you use while developing in R, RStudio
will make typing easier and less error-prone.
