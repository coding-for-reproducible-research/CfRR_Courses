# Undoing Changes

## Episode objectives

At the end of this episode you will know how to unstage file changes you didn't
mean to stage and how to undo accidental commits.


## Removing files from the staging area

We've got quite a bit of outstanding stuff we could add to our cheatsheet
and good practice guide. Let's make a note of these things in a `TODO.txt`
file, which we'll put in the root folder of our repository:

``` bash
TODO:

Add note about staging multiple files with `git add` and `git diff`

Add note to commit good practice about perils of `git add .`

Add cheatsheet entries for `git rm` and `git mv`

Add cheatsheet entries for pushing and pulling
```

We might as well tick off the first two items, so let's add the following content
to `Git-cheatsheet.md`:

``` bash

## Specifying multiple files

`git <command> path/to/directory` — Apply `<command>` to all files in and descended
                                    from `path/to/directory`

Examples:

`git add .` — Stage all changes to files in current directory or descended from
              current directory.

`git diff foo/` — Show diffs of all files in directory `foo` or descended from
                  `foo`.

```

And we add the following to `Good-practice-guides/Commit-good-practice.md`:

``` bash

## Make sure you know what you're committing

Take care when staging multiple files with e.g. `git add .` that you don't
stage changes you didn't mean to. Always check what you're committing with
`git diff` or `git status`.

```

We go ahead and stage these, using our recently learnt syntax for staging
changes to multiple files (our working directory is the repository root
folder, as usual):

``` bash
$ git add .
```

Wait! Something doesn't feel right... Let's check the status:

``` bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   Git-cheatsheet.md
        modified:   Good-practice-guides/Commit-good-practice.md
        new file:   TODO.txt

```

Ah, no! We don't want to commit our `TODO.txt` file. This was just to help us
keep track of our work and it doesn't belong in the repository. Fortunately
we can remove changes to a file from the staging area. In fact,
`git status` tells us how to do this. The general command to use is:

``` bash
git restore --staged <files>
```

So let's use this on our `TODO.txt` file. We run the command, then check that
the only differences staged are for the cheatsheet and good practice guide

``` bash
$ git restore --staged TODO.txt

$ git diff --name-only --staged
Git-cheatsheet.md
Good-practice-guides/Commit-good-practice.md
```

That's better, now we can go ahead and commit. (Good thing we checked before
committing the first time round!)

``` bash
$ git commit -m "Add material on basic pathspec usage (directories)"
[main 0984d2b] Add material on basic pathspec usage (directories)
 2 files changed, 21 insertions(+)
```

## Undoing commits

What if we'd gone ahead and actually committed our `TODO.txt` file by accident?
Git offers a couple of ways to address this:

* _Reverting_: Create a new commit that undoes the old commit

* _Resetting_: Move `HEAD` back to a previous commit, so that all the later commits are
  removed from the commit history.


### Reverting (undo a commit by making a new one)

Let's suppose we've 'accidentally' made a new commit which puts `TODO.txt` under
version control, which we want to undo:

``` bash
$ git log --oneline -3
cc01bda (HEAD -> main) Add TODO.txt
0984d2b Add material on basic pathspec usage (directories)
92b2ac2 (origin/main, origin/HEAD) Create general good practice guides directory
```

The command

``` bash
git revert <commit>
```
can be used to create a new commit that undoes a previous `<commit>`. In our
case, we want to undo the commit where we added `TODO.txt`, i.e. commit
`cc01bda`. We'll run that shortly, but first we need to make sure to make
a temporary copy of `TODO.txt` and store it outside the repository. This is
because the revert will return the repository to the state before we'd added
`TODO.txt`, which will involve deleting the file. Having done this, we now
perform the reversion:

``` bash
$ git revert cc01bda
```

Because `git revert` is actually making a new commit, our text editor pops into
life for us to write a commit message. It's been pre-populated with a
helpful message, telling us which commit is being reverted:

``` bash
Revert "Add TODO.txt"

This reverts commit cc01bdaf30a98d5bfaf5e43838d90522695f251e.

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Your branch is ahead of 'origin/main' by 2 commits.
#   (use "git push" to publish your local commits)
#
# Changes to be committed:
#       deleted:    TODO.txt
#
```

We could edit this if we wanted to, but the default is fine, so we just close
the file to complete the commit.

``` bash
$ git revert cc01bda
[main bc9d190] Revert "Add TODO.txt"
 1 file changed, 9 deletions(-)
 delete mode 100644 TODO.txt
```

Now our commit history includes our new 'reverting' commit. Note also that
`TODO.txt` has been deleted.

``` bash
$ git log --oneline -4
bc9d190 (HEAD -> main) Revert "Add TODO.txt"
cc01bda Add TODO.txt
0984d2b Add material on basic pathspec usage (directories)
92b2ac2 (origin/main, origin/HEAD) Create general good practice guides directory

$ ls
Git-cheatsheet.md  Good-practice-guides/  README.md
```
#### Note on `git revert`
The `revert` command will only work if the working tree and staging area have no changes in them.


### Resetting (move back to a previous commit and lose later ones)

Reverting a commit is often considered a 'safe' way to undo a commit, because
the original, offending commit is not actually lost. This way, if we decide we
_did_ in fact want to make that commit, we can easily recover it (by doing
`git revert` on it). There is a
more destructive way to undo commit history that will get rid of the commits.

The `git reset` command is used to move back our `HEAD` to an earlier commit.
The default form of the command is:

``` bash
git reset <commit>
```

In effect, this will 'rewind' the commit history back to finish at the given
`<commit>`, dropping later commits as if they'd never happened. However, it will
put all changes since `<commit>` in the working tree, giving us a chance to
work with the files as they currently are before the reset.

For example, let's create an empty file `foo.txt`. We can do this using
the `touch` command within the root folder of our repository:

``` bash
$ touch foo.txt
```

We'll make a commit of this new file and remove it via a reset. First, we make
the commit:

``` bash
$ git add foo.txt

$ git commit -m "Add foo.txt to practice resetting"
[main fcecec0] Add foo.txt to practice resetting
 1 file changed, 1 insertion(+)
 create mode 100644 foo.txt

$ ls
foo.txt  Git-cheatsheet.md  Good-practice-guides/  README.md
```

Let's now reset the commit history back to how it was before
we committed `TODO.txt`. We check the log to get the commit identifier,
perform our reset, then check the status of the repository:

``` bash
$ git log --oneline -5
fcecec0 (HEAD -> main) Add foo.txt to practice resetting
bc9d190 Revert "Add TODO.txt"
cc01bda Add TODO.txt
0984d2b Add material on basic pathspec usage (directories)
92b2ac2 (origin/main, origin/HEAD) Create general good practice guides directory

$ git reset 0984d2b

$ git log --oneline -5
0984d2b (HEAD -> main) Add material on basic pathspec usage (directories)
92b2ac2 (origin/main, origin/HEAD) Create general good practice guides directory
5cf8321 Remove rubbish.txt
d26a698 Add some rubbish to try out 'git rm'
910bb79 Add note about '--name-only' option to 'git diff'
```

We can see that our new `HEAD`, i.e. our new 'current commit', is what we reset
to, namely `0984d2b`. What state will our working tree be in? The answer is that it
will contain the changes that would need to be made to recover the state of
the repository as it was at `HEAD` just before the reset (at the
now-removed commit `fcecec0`). In other words, we expect to see just the change
that adds `foo.txt`. We can verify this with `git status`:

``` bash
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        foo.txt

nothing added to commit but untracked files present (use "git add" to track)
```

We don't want to keep this `foo.txt` file, so let's just delete it with the
usual Unix command `rm` to get a nice, clean working tree again.

``` bash
$ rm foo.txt
```

After all that, we can move that TODO list back into the repository. We'll
finish by removing the tasks we've completed and add some new tasks, leaving our
list like so:

``` bash
TODO:

Add cheatsheet entries for `git rm` and `git mv`

Add cheatsheet entries for pushing and pulling

Add cheatsheet entries about undoing changes

```

#### Hard reset
If you're really sure you don't need to keep the changes from later commits when resetting, then you can automatically discard them by using the `--hard` option: `git reset --hard <commit>`. This will set your working tree to the exact same state as the commit you're resetting to. It thus deletes the work you did after `<commit>`; be sure that this is what you want before running a hard reset!


### Warning: pushing after a reset

Something to be aware of when using `git reset` is that you can't by default push to a
remote repository if the tip of your local `main` branch is pointing to a commit
that is behind where the remote repository (`origin/main`) is.

For example, suppose we had reset our local repository to the commit _before_
`origin/main`, i.e. commit `5cf8321`, "Remove rubbish.txt". If we then tried to push
our local repository to the remote one, Git would not complete the request and
complain to us with the following message:

``` bash
$ git push origin
To https://github.com/jbloggs9999/git-good-practice.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/jbloggs9999/git-good-practice.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

The main reason for this is to avoid a situation where commit history in the
remote repository gets lost. This is especially important when collaborating
with others, which we'll cover in later episodes in this course.

You can read more on the topic of resetting on
<a href="https://www.atlassian.com/git/tutorials/undoing-changes/git-reset" target="_blank" rel="external noreferrer">Atlassian's tutorial</a>.


## Important note: sensitive data

The methods for undoing commits discussed here are appropriate when the commit
you made in error contains changes you didn't want, but don't fundamentally matter
if they've been recorded in the repository. In fact, even with a reset, it is
possible to recover the commit, with some advanced Git use that involves
something called the
<a href="https://www.atlassian.com/git/tutorials/rewriting-history" target="_blank" rel="external noreferrer">reflog</a>.

This means that, if you accidentally commit _sensitive data_, such as passwords
or confidential information, you cannot work on the basis that `git reset` or
`git revert` has removed the data from the repository. Moreover, if you
pushed the commits to a remote repository, the information will be stored there.

In these cases, you need to use specialist tools to remove all traces of the
sensitive data from the repository. See
<a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository" target="_blank" rel="external noreferrer">the GitHub documentation</a> for information on this topic.
