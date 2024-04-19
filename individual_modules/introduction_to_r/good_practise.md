# Establishing Good Practices when Coding
# Becoming a proficient coder

It is imperative to document the commands that you ran when performing an analysis. These should be saved in a file, often known as a script, and with the suffix .r or .R which indicates that it is specifically an R script. 

When you create your scripts there are a number of common conventions you should consider 

- *Commenting (#).* When R sees a # it ignores anything that comes after in until a new line is started. So you can use to add any comments for the human reader as opposed to the computer. Because the R commands are written for the computer to read, a script containing just R code is not the easiest for a human to read. For these reason we need to add comments. There is an art to commenting effectively, often less is more. Comments should not just repeat what the code is doing they should be used to explain the reasoning behind various choices and explain things that are not obvious. 

- *Set the working directory.* Use a command so that when you reopen your script, you know where everything is.

- *Coding convention*. Define your personal coding style and stick to it. An example can be found [here](http://adv-r.had.co.nz/Style.html).


- *One script per job.* It is very tempting to just add to the end of an existing script but it is more efficient and effective to limit each script  to a single task. This makes them easier to navigate but also protects from errors or bugs negatively affecting everything else downstream. 

- *Don't hoard your workspace* It can be really tempting to save everything you have ever done, so you can trace back any mistakes. But an chaotic environment is hard and confusing to navigate. Identify what you really need to keep, a well maintained script should mean you can easily recreate your analysis and debug that way rather than save all the stages of the analysis.

- *Outline.* Use the outline feature in Rstudio to apply a consistent structure to all your scripts.

- *The devil is in the details* Compared to other languages R error messages can be informative, try reading them and looking for key words to indicate what the problem might be. 

- *Google it out* If you want to do something complicated chances are somebody else has tried before. Google for solutions to your problems. If there is no solution, use Stackoverflow.


- *Create a pseudocode.* Start your script by setting up the titles of your sections. Then progresively, populate the sections with subtitles and lastly, fill out your code with commands. Normally, I would add the sections: Set up, Data, Data Cleaning, Data analysis, Data plotting, and Wrap up. 

## Structuring your data and analysis 

It is good practice to keep a set of related data, analyses, and text
self-contained in a single folder, called the **working directory**. All of the
scripts within this folder can then use *relative paths* to files that indicate
where inside the project a file is located (as opposed to absolute paths, which
point to where a file is on a specific computer). Working this way makes it
a lot easier to move your project around on your computer and share it with
others without worrying about whether or not the underlying scripts will still
work.

RStudio provides a helpful set of tools to do this through its "Projects"
interface, which not only creates a working directory for you but also
remembers its location (allowing you to quickly navigate to it) and optionally
preserves custom settings and open files to make it easier to resume work after
a break. Below, we will go through the steps for creating an RProject for this
tutorial.


* Start RStudio (presentation of RStudio -below- should happen here)
* Under the `File` menu, click on `New project`, choose `New directory`, then
  `Empty project`
* Enter a name for this new folder (or "directory", in computer science), and
  choose a convenient location for it. This will be your **working directory**
  for the rest of the day (e.g., `~/data-carpentry`)
* Click on "Create project"
* Under the `Files` tab on the right of the screen, click on `New Folder` and
  create a folder named `data` within your newly created working directory. (e.g., `~/data-carpentry/data`)
* Create a new R script (File > New File > R script) and save it in your working
  directory (e.g. `data-carpentry-script.R`)

Your working directory should now look like this:

![How it should look like at the beginning of this lesson](../images/r_starting_how_it_should_like.png)

## Organizing your working directory

Using a consistent folder structure across your projects will
help keep things organized, and will also make it easy find/file things in the
future. This can be especially helpful when you have multiple projects. In
general, you may create directories (folders) for **scripts**, **data**, and
**documents**.

 - **`data/`** Use this folder to store your raw data and intermediate
   datasets you may create for the need of a particular analysis. For the sake
   of transparency and [provenance](https://en.wikipedia.org/wiki/Provenance),
   you should *always* keep a copy of your raw data accessible and do as much
   of your data cleanup and preprocessing programmatically (i.e. with scripts,
   rather than manually) as possible. Separating raw data from processed data
   is also a good idea. For example, you could have files
   `data/raw/tree_survey.plot1.txt` and `...plot2.txt` kept separate from
   a `data/processed/tree.survey.csv` file generated by the
   `scripts/01.preprocess.tree_survey.R` script.
 - **`documents/`** This would be a place to keep outlines, drafts, and other text.
 - **`scripts/`** This would be the location to keep your R scripts for
   different analyses or plotting, and potentially a separate folder for your
   functions (more on that later).

You may want additional directories or subdirectories depending on your project
needs, but these should form the backbone of your working directory. For this
workshop, you only need a `data/` folder.

![Example of a working directory structure](../images/R-ecology-work_dir_structure.png)

# Performing reproducible analyses

Once you are happy with your script or analysis, it is highly recommended that you run the whole script from top to bottom in one execution.
This ensures that your script is complete and that your record of what you did is accurate. It can be very easy when developing a script by copying and pasting chunks of code, to forget to record something, or to run commands out of order. This may have an effect on the final output, and it may be impossible to work out what happened or why, or you may even not be aware of the effect. For this reason, we recommend rerunning your script at the end. If something goes wrong, and you get an error or a warning you know, you've missed a step out or need to fix it. 

Most importantly, if you detect the mistake further down the line, it will be much easier to troubleshoot because you know that your script is a genuine
reflection of what you did to the data, rather than an incomplete record of some of the steps you ran, in some order. 