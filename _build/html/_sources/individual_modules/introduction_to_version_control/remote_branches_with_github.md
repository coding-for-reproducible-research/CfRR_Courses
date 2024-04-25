# Remote Branches with GitHub

## Learning objectives

By the end of this episode you will be able to create remote branches using
GitHub and track these remote branches locally. You will also learn how to
merge remote branches using a pull request, as well as how to delete branches
in your local and remote repositories.


## Local and remote branches

Branches can reside in our local repository and/or remote repository, in the
same way that commits can. An **upstream** branch is one which resides in the
remote repository and is tracked locally, meaning the local branch is linked to
the remote branch. Our local repository stores references to any remote branches,
prepending their names with `remotes/origin/` (or simply `origin/`). It should
be noted that these remote branches are not updated automatically - we need to
use `git fetch` to update them.


### Viewing branches

We can list _all_ the branches that our local repository is aware of (both
local branches and remote branches) by using `git branch --all` (or
just `git branch -a`):

``` bash
$ git branch -a
  branches-material
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
``` 

There are three branches worth noting here, namely `main` (our local version of
`main`), `remotes/origin/main` (our remote version of `main`) and `branches-material`
(our newly created local branch). We can safely ignore
`remotes/origin/HEAD -> origin/main` for the time being.

As we have only created `branches-material` locally, it does not have a remote
counterpart, unlike `main`. Using GitHub, we can verify there is no remote branch
called `branches-material`. The necessary steps are as follows:

- **Step 1** Navigate to your repository on GitHub.

- **Step 2** Click on _branch(es)_, above the list of files on the left-hand side,
  as indicated in the following screenshot:

  ![Viewing branches on GitHub](images/github-view-branches.png)

- **Step 3** Click on _All branches_, located to the left of the green _New branch_
  button on the right-hand side of the screen — this will display a list of all
  the branches in your remote repository. `branches-material` will be missing
  from this list.


## Working with remote branches

So far, we've seen how to create a local branch, commit to it and merge it into
another branch (e.g. into `main`). This branch didn't have an upstream branch
in the remote repository. We're now going to look at the case where we
use GitHub to create a branch in the _remote repository_, which we then
bring into our local repository to work with. This approach takes advantage of
useful functionality provided by GitHub, promoting collaborative working. We
will look at an alternative workflow that doesn't rely on the features GitHub
provides in a later episode.

Now, let's add some material to the cheatsheet relating to working with remote
branches, using GitHub to drive this development. The basic flow for doing this
will be the following:

* Create a remote branch on GitHub that will receive our additions to the
  cheatsheet.

* Work on the cheatsheet locally, then push the changes up to the remote branch.

* Use GitHub to merge the work into the `main` branch in the remote repository,
  using a pull request.

In order to do this, we need to do the following:

* Create a remote branch on GitHub.

* Update our local repository from the remote repository, so that we have a
  reference to the newly created remote branch.

* Create a local branch that is set up to track the remote one.

* Add new commits to the local branch corresponding to our work on the
  cheatsheet.

* Push these commits to the upstream remote branch.

* Merge the remote branch into the remote `main` branch, using
  a pull request on GitHub.

* Update our local repository to reflect this change to the remote repository.


### Create a remote branch on GitHub

In GitHub, the following steps allow you to create a new remote branch:

- **Step 1** Navigate to your repository on GitHub.

- **Step 2** Click on the dropdown, located to the left of _branches_, on the
  left-hand side of the screen.

- **Step 3** Select the branch you would like to create a branch from. (For this
  course, this will typically be `main`. If it is `main`, this step
  becomes redundant.)

- **Step 4** Click on the dropdown again and type in the name of your new branch
  where it says _Find or create a branch..._.

- **Step 5** Click on _Create branch: new-branch from 'base-branch'_, where
  _new-branch_ is the name of your new branch and _base-branch_ is the name of
  the branch you are branching off of (e.g. `main`).

In our example `git-good-practice` repository, let's suppose we've just created a
new remote branch called `remote-branches-material`, which is based on top of
`main`. Our local repository doesn't have any knowledge of this new branch, as
can be seen by listing the branches:

``` bash
$ git branch -a
  branches-material
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```


### Fetch the remote branch

In order to update our local repository so that it has knowledge of the new
remote branch, we use the following command from within our local repository:

``` bash
git fetch
```

(Like with `git push` and `git pull`, we can instead run `git fetch origin` to
be explicit about the reference to the remote repository.)
We won't go into too much detail about exactly what `git fetch origin` is doing. For
our purposes, we use it to inspect the remote repository for information about
any new branches, or commits that have been made in remote branches, that our
local repository doesn't yet know about.

In our example, after running `git fetch` in our `git-good-practice`
repository, we see that information about the new remote `remote-branches-material`
has been retrieved:

``` bash
$ git fetch
Username for 'https://github.com': jbloggs9999
Password for 'https://jbloggs9999@github.com':
From https://github.com/jbloggs9999/git-good-practice
 * [new branch]      remote-branches-material -> origin/remote-branches-material

$ git branch -a
  branches-material
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
  remotes/origin/remote-branches-material
```

However, this has only created a reference to the remote branch, indicated
by `remotes/origin/remote-branches-material` in the above output. We still need
to create a _local_ branch that will track the remote branch. 


### Create a new tracking local branch

In order to create a local version of the
`origin/remote-branches-material` branch where we can add commits, we can
perform the following checkout:

``` bash
$ git checkout remote-branches-material 
Switched to a new branch 'remote-branches-material'
branch 'remote-branches-material' set up to track 'origin/remote-branches-material'. 
```

You may be surprised by this: after all, we've asked Git to checkout a branch
that doesn't actually exist! Fortunately, Git is smart enough to realise that
what we want to do is set up a new local branch that tracks the `origin/remote-branches-material`
remote branch. So it automatically creates a new local branch — called `remote-branches-material` — that
will track `origin/remote-branches-material`, and checks out this new local branch for us. We
can verify this by listing all the branches again:

``` bash
$ git branch -a
  branches-material
  main
* remote-branches-material
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
  remotes/origin/remote-branches-material
```

### Add content to the local branch and push

We are now set to add our new material to `Git-cheatsheet.md` about remote
branches. We modify the start of the subsection _Branches_ so that it now reads as
follows:

``` bash
## Branches

`git branch <new-branch-name>` — Create a new branch called `<new-branch-name>`
                                 based at the current commit (i.e. at `HEAD`).

`git checkout <branch>` — Check out the branch `<branch>`, so that new commits
                          are added to `<branch>`.

- Can also be used to create and checkout a new local branch `<branch>` that
  tracks an existing remote branch `origin/<branch>`.

`git merge <branch-to-merge-in>` — Combine the commit history of `<branch-to-merge-in>`
                                   with that of the branch currently checked out.
```

Having included this addition, we commit to our local `remote-branches-material` branch.


#### Markdown syntax
Unordered lists are denoted by using a hyphen (`-`) or an asterisk (`*`), followed by a space, with the text in the list item following. Example:
``` markdown
- Foo
- Bar
- Baz
```
renders as:
- Foo
- Bar
- Baz


We're now in the position where our local branch
`remote-branches-material` is ahead of the remote branch
`origin/remote-branches-material` that it tracks, as can be seen from
the log on `remote-branches-material`:

``` bash
$ git log --oneline -3
5125372 (HEAD -> remote-branches-material) Add note about creating local tracking branches
3b918f2 (origin/remote-branches-material, origin/main, origin/HEAD, main, branches-material) Add entry about merging branches
51da8da Add entry about checking out a branch
```

In order to update an upstream remote branch with new commits in the local
tracking branch, we can use `git push` (or `git push origin`), like we did when working with
the `main` branch in the episode
[Pushing to and Pulling From the Remote Repository]({{ site.url }}/10_pushing_and_pulling/index.html).
Note however that this will push the commits _on the currently checked out branch_ to its upstream
remote branch. So, in general, if you have a local branch `<foo>` that tracks a
remote branch `origin/<foo>`, then in order to push `<foo>` to `origin/<foo>` we
need to first checkout `<foo>`.


#### Alternative: specify the branch explicitly
Alternatively, if you have a local branch `<foo>` that tracks a remote branch `origin/<foo>`, then you can run `git push origin <foo>` from any local branch to push commits from `<foo>` to `origin/<foo>`.


In our example, we're already on the branch `remote-branches-material` that we want to push,
so we can just go ahead and do `git push`:

``` bash
$ git push
Username for 'https://github.com': jbloggs9999
Password for 'https://jbloggs9999@github.com':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 438 bytes | 219.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/jbloggs9999/git-good-practice.git
   3b918f2..5125372  remote-branches-material -> remote-branches-material
```

The last line of the `git push` message shows that we've successfully updated the remote
branch with the new commit.


## Merge remote branch into remote `main`

Once we have pushed our changes to the remote branch, we can merge said remote
branch into remote `main` by means of a pull request on GitHub. We can create and
complete a pull request (PR) as follows:

- **Step 1** Navigate to your repository on GitHub.

- **Step 2** Click on the _Pull requests_ tab (third tab from the left).

- **Step 3** Click on the green _New pull request_ button on the right-hand side
  of the screen.

- **Step 4** Ensure `main` has been chosen as _base_ and choose your remote branch,
  which in this case is `remote-branches-material`, as _compare_.

- **Step 5** Click on the green _Create pull request_ button.

- **Step 6** GitHub will generate a title based on the name of the branch you
  are comparing, but this can be changed. You are also welcome to add a
  description where it says _Leave a comment_.

- **Step 7** Click on the green _Create pull request_ button.

- **Step 8** Click on the green _Merge pull request_ button, located near the
  bottom of the page.


## Pull changes into our local repository

We have just merged our branch into `main` in the remote repository. To see
the changes made to `main` in our local repository, we need to pull them from
the remote repository.

To update `main`, we first check it out:

``` bash
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

There's an important point to make about the output here. It is stated that
`Your branch is up to date with 'origin/main'.`. This doesn't mean there aren't changes on the remote to
pull in. Instead, it means that Git is not aware of any extra commits in
`origin/main` compared to `main` _since last `fetch`ing from the remote repository_.

So, let us fetch updates from the remote repository:

``` bash
$ git fetch
Username for 'https://github.com': jbloggs9999
Password for 'https://jbloggs9999@github.com':
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (1/1), 667 bytes | 83.00 KiB/s, done.
From https://github.com/jbloggs/git-good-practice
   3b918f2..86ebbee  main       -> origin/main
```

We can see that our local repository is now aware of the change to the remote
`origin/main` branch by checking the status again:

``` bash
$ git status
On branch main
Your branch is behind 'origin/main' by 2 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean
```

In the
[Pushing to and Pulling From the Remote Repository]({{ site.url }}/10_pushing_and_pulling/index.html)
episode, we mentioned that `git pull` can be used to retrieve updates from the
remote repository. To be more precise, `git pull` is used to bring in commits
_in a remote branch into a corresponding local branch_. In general, if you have
a remote branch that has commits not yet in a local tracking
branch `<branch>`, then run the following command _with `<branch>` checked out_
to update `<branch>` with these new commits:

``` bash
git pull
```

(or, to be explicit about the remote repository, `git pull origin`).

#### `pull` automatically `fetch`es
`git pull` actually performs a two step process on a branch `<branch>`. First, it runs a `git fetch` to retrieve all new commits, branches, etc. from the remote repository. Then, it merges the changes that have been fetched into the `origin/<branch>` into `<branch>`. As a result, we did not in fact need to use the `git fetch` command before using `git pull` above.

We pull the changes to `origin/main` into our local `main` branch:

``` bash
$ git pull
Username for 'https://github.com': jbloggs9999
Password for 'https://jbloggs9999@github.com':
Updating 3b918f2..86ebbee
Fast-forward
 Git-cheatsheet.md | 3 +++
 1 file changed, 3 insertions(+)
```

We can now see from the log that our changes are fully reflected in `main`:

``` bash
$ git log --oneline -5
86ebbee (HEAD -> main, origin/main, origin/HEAD) Merge pull request #1 from jbloggs9999/remote-branches-material
5125372 (origin/remote-branches-material, remote-branches-material) Add note about creating local tracking branches
3b918f2 (branches-material) Add entry about merging branches
51da8da Add entry about checking out a branch
8124186 Add entry about creating branches
```

## Cleaning up

All the work we've done in our branches has been incorporated into `main` (both
locally and in the remote repository). So, to clean up the state of the repository,
we're going to delete the branches `branches-material` and `remote-branches-material`,
including the remote version of `remote-branches-material`, since these
no longer serve any purpose.


### Good practice: deleting old branches
It is good practice to delete branches that are no longer required. This makes navigating a repository easier and makes it clear what work is still ongoing compared to work that has been finished.


### Deleting branches from a local repository

The general commands for deleting branches are as follows:

* For deleting _local_ branches: `git branch -d <local-branches>`

* For deleting _remote_ branches: `git branch -d -r <remote-branches>`

In both cases, note that you can specify more than one branch by separating the
branch names by a space.

There are a couple of important things to note about deleting branches:

* You can't delete a branch you currently have checked out. So make sure you
  checkout a different branch before deletion e.g. do deletions from `main`.

* Deleting branches removes the commits contained in those branches which don't
  feature in other branches. So, before deleting a branch, be sure that the
  changes you want to keep have been merged into another branch e.g. `main`.

We delete our local branches:

``` bash
$ git branch -d branches-material remote-branches-material 
Deleted branch branches-material (was 3b918f2).
Deleted branch remote-branches-material (was 5125372).
```

Then we delete our remote branch reference `origin/remote-branches-material`:

``` bash
$ git branch -r -d origin/remote-branches-material
Deleted remote-tracking branch origin/remote-branches-material (was 5125372).
```

### Force deletion
Git may stop you from deleting a branch, because it can't verify that all the commits in the branch have been merged into a corresponding remote branch or another local branch. This is a protection mechanism to stop you from potentially losing changes. If you encounter this but are sure you want to proceed with the deletion, you can force the deletion by using `-D` instead of `-d` in the commands above.


Our local repository is now looking cleaner with regards to the branches we have:

``` bash
$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

Note also that the references to the non-`main` branches have disappeared from
the log (note that the _commits_ have _not_ disappeared, however, because these
are part of `main`):

``` bash
$ git log --oneline -5
86ebbee (HEAD -> main, origin/main, origin/HEAD) Merge pull request #1 from jbloggs9999/remote-branches-material
5125372 Add note about creating local tracking branches
3b918f2 Add entry about merging branches
51da8da Add entry about checking out a branch
8124186 Add entry about creating branches
```


### Deleting branches from the remote repository via GitHub

Finally, we need to delete the remote branch `remote-branches-material` from the
remote repository in GitHub. The necessary steps are as follows:

- **Step 1** Navigate to your respository on GitHub.

- **Step 2** Click on _branches_, above the list of files on the left-hand side.

- **Step 3** Click on _All branches_, located to the left of the green _New branch_
  button on the right-hand side of the screen.

- **Step 4** Identify the branch to be deleted and click on the appropriate
  _bin icon_ on the right-hand side of the screen. If you hover over the icon,
  it will show a message stating _Delete chosen-branch_, where _chosen-branch_
  is the name of the branch to be deleted.
