# Ignoring Files

## Learning objectives

By the end of this episode you will know how to get Git to ignore certain files
so that they are not included as part of a repository's commit history. You
will also be able to describe some examples of the kinds of files that shouldn't
be stored in a repository.


## Ignoring files

Currently we still have our `TODO.txt` file hanging around in the working tree:

``` bash
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        TODO.txt

nothing added to commit but untracked files present (use "git add" to track)
```

While this file is recognised by Git, there's always a risk we might accidentally
commit it to the repository. Git provides a way to **ignore** files, so that
any changes to these files are just ignored by Git. We can do this by creating
a special file, which must be named `.gitignore`, in the root folder of the
repository. In this file we specify which files Git should ignore; when doing
this, we need to specify paths relative to the root directory of the repository.

We therefore create a `.gitignore` file in the root folder of `git-good-practice`
and add the following content to it to ensure the `TODO.txt` file is ignored:

``` bash
TODO.txt

```

### `.gitignore` comments
Any line that begins with a hash (`#`) in a `.gitignore` file is treated as a comment and thus not processed by Git. Note that the line must have `#` as the first character to be considered a comment e.g. a comment line cannot begin with whitespace followed by `#`.


Now we check the state of the working tree again:

``` bash
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)
```

The only thing Git notices now is the newly-created `.gitignore` file.
In general, it's useful to keep the `.gitignore` file under version control, so
that other users of the repository can also have the same things ignored as we
do. Let's add and commit `.gitignore`:

``` bash
$ git add .gitignore

$ git commit -m "Ignore TODO list file"
[main 42a9a32] Ignore TODO list file
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore

$ git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

As a bonus, using `.gitignore` helps us avoid accidentally adding files
to the repository that we don't want to track:

``` bash
$ git add TODO.txt
The following paths are ignored by one of your .gitignore files:
TODO.txt
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
```

As the message says, if we really want to override our ignore settings,
we can use `git add -f` to force Git to add something. We can also always see
the status of ignored files if we want:

``` bash
$ git status --ignored
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

Ignored files:
  (use "git add -f <file>..." to include in what will be committed)
        TODO.txt

nothing to commit, working tree clean
```


## Ignore similar files with pathspecs

So far, we have been specifying files individually whenever we want to ignore them.
Git has its own mini-language for referring to multiple, related files
simultaneously, which can give us much more flexibility in certain situations,
such as when specifying files to ignore.

This is done through what are called **pathspecs**. We already touched on these
when we discussed e.g. using `git add` on all files in a directory. We aren't
going to cover everything there is to know about pathspecs, but here are some
examples that cover quite a lot of cases in practice:

* `.` refers to files in the current working directory and all directories
  descended from it (e.g. would include `./foo/bar/baz/file.txt`)

* Specifying a directory `foo` will limit to files that descend from `foo`
  (e.g. `./foo/bar/baz/file.txt` but not `./qux/bar/file.txt`)

* `*.pyc` refers to all `.pyc` files in the current working directory.

* `foo/bar/*.pyc` matches all `.pyc` files in the directory `foo/bar`

Most commands in Git that work on files also work on pathspecs and you'll see
this term in the help pages (try `git add --help` for an example).
For the complete specification of pathspecs, check out the
Git Glossary manual, by running `man gitglossary` and paging down to the entry
for `pathspec`.

Let's create a few dummy files for trying this out, imagining that we've got
some research code that takes in data files, outputs some results and produces
a log file of the run. We use the Unix commands `mkdir`
to create a new `data` directory and `touch` to create new files:

``` bash
$ mkdir data

$ touch data/a.dat data/b.dat data/c.dat

$ touch a.out b.out c.out

$ touch 2023-02-10-15-36-02_modelRun.log

$ ls
2023-02-10-15-36-02_modelRun.log  a.out  b.out  c.out  data/  Git-cheatsheet.md  Good-practice-guides/  README.md  TODO.txt

$ ls data/
a.dat  b.dat  c.dat
```

As expected, Git detects all of these as untracked files:

``` bash
$ git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        2023-02-10-15-36-02_modelRun.log
        a.out
        b.out
        c.out
        data/

nothing added to commit but untracked files present (use "git add" to track)
```

We can succinctly tell Git to ignore these files by adding three different
pathspecs:

``` bash
TODO.txt

# Ignore files in the data folder and subfolder therein
data/

# Ignore .log files in the root folder of the repository
*.log

# Ignore .out files in the root folder of the repository
*.out

```

Now we can see that all these files have become ignored by Git:

``` bash
$ git status --ignored
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

Ignored files:
  (use "git add -f <file>..." to include in what will be committed)
        2023-02-10-15-36-02_modelRun.log
        TODO.txt
        a.out
        b.out
        c.out
        data/

no changes added to commit (use "git add" and/or "git commit -a")
```

Since this was just for experimenting with pathspecs, we'll clean up by setting
our `.gitignore` file back to just containing `TODO.txt` and removing the
files and `data` directory we created.

``` bash
$ rm 2023-02-10-15-36-02_modelRun.log a.out b.out c.out

$ rm -rf data/
```

Having done this, we now have a clean working tree again, with the `TODO.txt`
file still ignored:

``` bash
$ git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Notice how we still have some commits that have not been pushed to the remote
repository. We'll push these commits now, so that our local repository and remote
repository are up-to-date with each other:

``` bash
$ git push origin
Username for 'https://github.com': jbloggs9999
Password for 'https://jbloggs9999@github.com':
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (8/8), 1.11 KiB | 1.11 MiB/s, done.
Total 8 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
To https://github.com/jbloggs9999/git-good-practice.git
   92b2ac2..42a9a32  main -> main
```

Finally, let's add a note to include some material about ignoring files in our
`TODO.txt` file:

``` bash
Add some material about ignoring files

```


## What kind of files should be ignored?

As we've suggested, not all files should be kept under version control in a
Git repository. For one thing, certain files only serve to bloat the repository,
potentially affecting the performance of Git (e.g. when syncing with a
remote repository). For another, some files may contain sensitive information
that should not be shared with others.

Here are some examples of files that should definitely not be kept under version
control:

* Sensitive files that should not be shared with others, e.g. passwords, access
  tokens.

* Artifacts from the process of building software e.g. compiled Python files
  (`.pyc`) or similar, compiled executables, `.o` files, etc.

* Anything that is tied to you, your computer, or the operating system you use,
  which may not work or mean anything to other users of the code.

Here are some examples of files that should generally not be kept under version
control, though there may be legitimate exceptions in some cases:

* Data files, especially if these are quite large.

* Binary files, such as images, audio, certain kinds of data formats, PDFs and
  the like. Git is designed to work with text-based files e.g. source code
  files. Although Git can store binary files in repositories, it will not be able
  to display changes to these files, limiting the benefits gained from Git in
  this case.

* Any files that are output from the software in the repository (including log
  files). If anything can be generated from the software then there's no need
  to store it under version control, since it can be regenerated if needed.

* 3rd party package dependencies. Instead, a suitable
  specification file (e.g. a `requirements.txt` file for
  Python pip packages, a Conda environment specification file, etc.) should be
  kept under version
  control to allow users to obtain software dependencies themselves.
