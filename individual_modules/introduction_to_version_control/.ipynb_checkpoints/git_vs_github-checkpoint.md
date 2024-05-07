# Git vs Github

## Learning Objectives

At the end of this episode you will be able to tell your friends and colleagues
what Git and GitHub are and describe how they are different.


## Git: our version control system of choice

In the last episode we explained what version control systems are and why they
are useful. This course teaches you the basics of using a particular version
control system, called
<a href="https://git-scm.com/" target="_blank" rel="external noreferrer">Git</a>.

Git is one of the most popular and relied-upon version control systems used
today, both in research and commercially. Git is simply a piece of software that
you run on your computer. You can use it
directly from the command line, using the command `git`.

### Terminals
In this course we will work through examples with command line syntax that you would find on most Unix-style systems (MacOS or Linux). If you are using Windows and have followed the installation instructions, you will have installed _Git for Windows_. This comes with the _Git Bash_ program, which emulates a Unix Bash shell (e.g. it uses forward slashes `/` for path separators and comes with common Unix programs like `ls` for listing the contents of a directory). We recommend you use Git Bash to follow through the course. You can launch Git Bash by opening the Start menu and typing `Git Bash` to find the program.


If you have Git installed
on your machine, you can run it right now: open up a terminal and try running the following
command:

``` bash
git --version
```

If you have Git installed, your output should look something like this (your
version number may differ):

``` output
git version 2.25.1
```

Because Git is so popular, there is a lot of software that integrates with it,
which can lead to confusion about exactly what Git is. For example,
you may have used programs like Visual Studio Code, RStudio or PyCharm to write
your code. These additionally provide graphical user interfaces to help
developers interact with Git via 'point and click' while you work on code,
giving developers a more 'integrated' experience. But it's helpful to remember
that these programs are just using Git under the hood and that it's perfectly
possible to use Git without these. Indeed, it's best _not_ to rely on these
integrated facilities for using Git, because you may well come up against
situations in your work where you need to use Git in environments which force
you to use it at the command line, such as remote servers.

Chances are that, at some
point, you will want to share your work, either with collaborators as the code is developed or
in order to publicise your work. On it's own, Git doesn't provide the means to
do this — for that, you also need somewhere to host a 'remote' version
of your code which others can access. Many web platforms have been created to
provide this service. They use Git as the core version control technology, while
providing additional layers of functionality to facilitate sharing and collaboration
with other developers. Examples of these platforms include
<a href="https://about.gitlab.com/" target="_blank" rel="external noreferrer">GitLab</a>,
<a href="https://codeberg.org/" target="_blank" rel="external noreferrer">Codeberg</a> and
<a href="https://github.com/" target="_blank" rel="external noreferrer">GitHub</a>.
It is possible to use Git completely 'locally'; that is,
without interacting over the internet with some remote service. This is
perfectly fine if you just want to version control your own software project
that you have no intention of sharing with anyone. 


## Managing collaboration with GitHub

As well as teaching you the basics of using Git, this course will give you an
introduction to using GitHub as a way of sharing your code and managing its
development.

In some ways, the naming of GitHub is unfortunate, because it could easily sound
like it's Git but 'on the web'. But that's not really true and to think
of it in these terms can lead to confusion, especially early on. Remember that
_Git_ is a tool that software developers use as they write code on their machines.
_GitHub_ is a web
platform that makes it easy to share code and provides extra functionality to
support teams of software developers in their collaboration. Taking an analogy
from scientific research, Git is more
akin to a lab book that a scientist might use day-to-day to record what they
did that day, the results of experiments, etc., whereas GitHub sits more at the
level of planning and project management that a Principal Investigator would do
to ensure the project runs smoothly and everyone is kept on the same page. It
should also be noted that GitHub is not a replacement for Git. In fact, you will
typically interact with GitHub _via Git_ while you develop your code. 

The full suite of facilities that GitHub provides is multi-faceted and it is far
beyond the scope of this course for us to cover all of it. We will focus on
features that support:

* Sharing your code within your development team and the wider world

* Ways to keep track of proposed additions or improvements to a codebase (via
  GitHub _issues_) and to ensure significant changes to the codebase are
  integrated in a controlled way (via GitHub _pull requests_).

If you feel somewhat hazy on exactly how Git and GitHub differ, then don't worry:
this should become clearer as we go through the course. For now, the key thing
to bear in mind is that they play different roles: Git for day-to-day
record-keeping while writing code, and GitHub for sharing and collaborating with
others.
