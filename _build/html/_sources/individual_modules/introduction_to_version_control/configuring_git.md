# Setting up Git and GitHub

## Learning Objectives

By the end of this episode you will know how to set up Git and GitHub for use
in your projects.


## Setting up Git

When we use Git on a new computer for the first time,
we need to configure a few things. Below are a few examples
of configurations we will set as we get started with Git:

*  Our name and email address.
*  Our preferred text editor to use with Git.

We will also want to set these settings _globally_, meaning they'll apply
whenever we use Git within a given user account on a specific computer.


### Username and email address

On a command line, Git commands are written as `git <command> <options>`,
where `<command>` is what we actually want to do and `<options>` is additional
optional information which may be needed for the `<command>`. To configure Git,
settings, we use the 'command' `config`.

``` bash
$ git config --global user.name "Joe Bloggs"
$ git config --global user.email "joe.bloggs@example.net"
```

This user name and email will be associated with your subsequent Git activity,
which means that any changes pushed to GitHub (or another Git host server)
from here on will include this information. If you work on public repositories
with these services, then this information will be publicly visible.

For this course, we will be interacting with GitHub and
so the email address used should be the same as the one used when setting up
your GitHub account. If you are concerned about privacy, please review
<a href="https://help.github.com/articles/keeping-your-email-address-private/" target="_blank" rel="external noreferrer">GitHub's instructions for keeping your email address private</a>. 

#### Keeping your email private
If you elect to use a private email address with GitHub, then use that same email address for the `user.email` value. It will look something like `nnnnnnnnn-username@users.noreply.github.com` where `nnnnnnnnn-username` is your username prepended with a numerical ID.

The commands we just ran above only need to be run once: the flag `--global` tells Git
to use the settings for _every_ Git repository, in your user account, on this computer.

You can check your global settings at any time:

``` bash
$ git config --global --list
```


### Setting a text editor

Git will use a text editor installed on your computer when you need to write
'commit messages' (more about these later in the course). The default editor on
most operating systems is set to Vim which, while powerful, is difficult to
use if you're not used to it. You can configure Git to instead use something
you're more familiar with. We recommend trying *Nano* for Git usage: it works
at the command line, making it quick to write the short 'commit messages', but
is much simpler to use than Vim. You can change this at any time if you find you'd
prefer to use something else.

#### Git for Windows
If you followed the recommendations in the installation instructions for Git for Windows then Nano should already be the default editor used by Git.

The following table shows how to set the default editor for Git for several popular 
text editors. In some cases, you need to provide the path to the executable
program for the editor — this indicated as `path/to/executable-name` (if you
aren't sure what to enter for this, do some online searching or try a search
on your computer).

| Editor             | Configuration command                            |
|:-------------------|:-------------------------------------------------|
| Atom | `$ git config --global core.editor "atom --wait"`|
| nano               | `$ git config --global core.editor "nano -w"`    |
| BBEdit (Mac, with command line tools) | `$ git config --global core.editor "bbedit -w"`    |
| Sublime Text (Mac) | `$ git config --global core.editor "'path/to/subl' -n -w"` |
| Sublime Text (Win) | `$ git config --global core.editor "'path/to/sublime_text.exe' -w"` |
| Notepad (Win)    | `$ git config --global core.editor "path/to/notepad.exe"`|
| Notepad++ (Win)    | `$ git config --global core.editor "'path/to/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"`|
| Kate (Linux)       | `$ git config --global core.editor "kate"`       |
| Gedit (Linux)      | `$ git config --global core.editor "gedit --wait --new-window"`   |
| Scratch (Linux)       | `$ git config --global core.editor "scratch-text-editor"`  |
| Emacs              | `$ git config --global core.editor "emacs"`   |
| Vim                | `$ git config --global core.editor "vim"`   |
| VS Code                | `$ git config --global core.editor "code --wait"`   |


### Default Git branch naming

Git (2.28+) allows configuration of the name of the branch created when you
initialize any new repository. (We will cover *repositories* and *branches* later
in the course; for now, you can think of a repository as a place where files
for a project are kept and a branch just as a name for the development history
of the files in the repository.)

By default, Git will create a branch called `master` whenever
you start a new repository. However, there is a move in the
<a href="https://github.com/github/renaming" target="_blank" rel="external noreferrer">software development community</a>
to stop using this term in favour of more inclusive language. Most Git
code hosting services have transitioned to using `main` as the default 
branch; for example, any new repository that is opened in GitHub defaults 
to using `main` for the name of the branch.

At the time of writing, Git has not yet made the same change. For this course,
we will manually configure Git to use the same `main` branch name as most cloud
services.

For versions of Git 2.28 or later, this can be achieved by setting the
`init.defaultBranch` setting to `main` globally:

``` bash
$ git config --global init.defaultBranch main
```

For versions of Git prior to 2.28, the change can only be made on an individual
repository level and we will cover this in the episode on making repositories later.

#### Exercise
Set up Git the way you'd like it by configuring settings for:
- Your username and password
- Your preferred text editor
- (Optional) Changing the default Git branch naming to `main`. If your version of Git is older than 2.28 then you won't be able to do this yet.


### Final notes on configuring Git

#### Changing configuration

You can change your configuration as many times as you want. Use the
same commands as above to choose another editor, update your email address, etc.

#### Git Help and Manual

Always remember that if you forget the subcommands or options of a `git` command,
you can access the relevant list of options typing `git <command> -h`, or
access the corresponding Git manual by typing
`git <command> --help`, e.g.:

``` bash
$ git config -h
$ git config --help
```

While viewing the manual, remember the `:` is a prompt waiting for commands and
you can press <kbd>Q</kbd> to exit the manual.
More generally, you can get the list of available `git` commands and further
resources of the Git manual typing:
``` bash
$ git help
```
 
#### On line Endings

You can sometimes run into issues when using Git if you (or your team) use
different machines when working on files. If you've followed the default
installation instructions (particularly Windows users who are using
*Git for Windows*) then you shouldn't run into problems, but we include a note
here in case you run into trouble.

As with other keys, when you hit <kbd>Enter</kbd> / <kbd>↵</kbd> / <kbd>Return</kbd>
on your keyboard, your computer encodes this input as a character.
Different operating systems use different character(s) to represent the end of a line.
(You may also hear these referred to as newlines or line breaks.)
Because Git uses these characters to compare files,
it may cause unexpected issues when editing a file on different machines. 
You can change the way Git recognizes and encodes line endings
using the `core.autocrlf` setting. The following settings are
recommended:

- **MacOS and Linux:**
  ``` bash
  $ git config --global core.autocrlf input
  ```
- **Windows:**
  ``` bash
  $ git config --global core.autocrlf true
  ```
You can read more about this issue 
<a href="https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_core_autocrlf" target="_blank" rel="external noreferrer">in the Pro Git book</a>.


## Setting up GitHub credentials

We're going to be using Git to communicate with GitHub. To do this, we need to
set up some authentication to enable us to do this securely. The approach we
will adopt in this course is to use GitHub
<a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token" target="_blank" rel="external noreferrer">Personal Access Tokens</a> (PAT). A PAT is
a way for some application or service (such as Git) to identify itself as being
authorised to interact with GitHub on your behalf. Part of setting up a PAT
involves specifying the scope of what an application using that PAT is allowed
to do on GitHub. PATs are generated via your GitHub account and then saved for
later use.

### Look after your PATs!
**You should treat PATs with the same level of care you would your GitHub account password. Store the PAT somewhere secure, such as in a password manager. If you ever suspect a PAT has been exposed, then you should delete the token and generate a new one.**
### Note on classic tokens
At the time of writing, GitHub is in the process of creating newer, so-called 'fine  grained' personal access tokens. These provide more fine grained control, but are still in a developmental phase. The older, 'classic', PATs are sufficient forour needs and simpler to set up, so we'll use them throughout this course.

To set up a PAT, follow the
<a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic" target="_blank" rel="external noreferrer">instructions provided by GitHub for classic tokens</a>. Note:

- You will need to set an expiration time on your token. This is part of the
  GitHub's security and we strongly suggest you don't select the _No expiration_
  option, however tempting it may be. You should get an email a few days before the
  token expires reminding you to regenerate it.

- As part of the process, you will need to select scopes for the token.
  All that is needed for this course (and likely for your standard, day-to-day use
  of Git) is to select the **repo** option: this will enable you to interact
  with repositories you have been invited to work on. More information about
  scopes can be found in the
  <a href="https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps" target="_blank" rel="external noreferrer">GitHub documentation on OAuth scopes</a>.

- You can regenerate a PAT that has expired
  by going to your _Personal access tokens (classic)_ as described
  in the link above, selecting the affected token and then clicking on _Regenerate token_.

- To delete a token (e.g. if you suspect it's been compromised), go to your
  _Personal access tokens (classic)_ as described in the link above and then
  click on _Delete_ next to the token.
  
### Exercise
Using the instructions on GitHub linked above, create a PAT and save it somewhere safe for later use in this course.
