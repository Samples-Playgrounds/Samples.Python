**Git Cheat Sheet** 

1 

## **01  Git configuration** 

```
git config --global
user.name “Your Name”
```

Set the name that will be attached to your commits and tags. 

`git config --global` Set the e-mail address that will be attached to your commits `user.email “you@example.` and tags. `com” git config --global` Enable some colorization of Git output. `color.ui auto` 

## **02  Starting a project** 

Create a new local repository in the current directory. If `git init [project name]` **[project name]** is provided, Git will create a new directory named **[project name]** and will initialize a repository inside it. Downloads a project with the entire history from the remote `git clone <project url>` repository. 

## **03  Day-to-day work** 

Displays the status of your working directory. Options include `git status` new, staged, and modified files. It will retrieve branch name, current commit identifier, and changes pending commit. 

Add a file to the **staging** area. Use. in place of the full file path `git add [file]` to add all changed files from the **current directory** down into the **directory tree.** 

`git diff [file]` Show changes between **working directory** and **staging area.** Shows any changes between the **staging area** and the `git diff --staged [file]` **repository.** Discard changes in **working directory.** This operation is `git checkout -- [file]` **unrecoverable** . Revert some paths in the index (or the whole index) to their `git reset -<path>--.]` state in **HEAD.** Create a new commit from changes added to the **staging area.** `git commit` The **commit** must have a message! 

`git rm [file]` Remove file from **working directory** and **staging area.** 

## **04  Storing your work** 

Put current changes in your **working directory** into **stash** for `git stash` later use. Apply stored **stash** content into **working directory,** and clear `git stash pop` **stash.** `git stash drop` Delete a specific **stash** from all your previous **stashes.** 

## **05  Git branching model** 

**==> picture [357 x 163] intentionally omitted <==**

**----- Start of picture text -----**<br>
List all local branches in repository. With  -a : show all branches<br>git branch [-a]<br>(with remote).<br>git branch [branch_name] Create new branch, referencing the current  HEAD .<br>Apply commits of the current working branch and apply them<br>git rebase [branch_name] to the HEAD of [branch] to make the history of your branch<br>more linear.<br>git checkout [-b] Switch working directory to the specified branch. With  -b : Git<br>[branch_name] will create the specified branch if it does not exist.<br>Join specified  [branch_name]  branch into your current branch<br>git merge [branch_name]<br>(the one you are on currently).<br>git branch -d [branch_ Remove selected branch, if it is already merged into any other.<br>name] -D  instead of  -d  forces deletion.<br>**----- End of picture text -----**<br>


**Commit** a state of the code base 

**Branch** a reference to a commit; can have a **tracked upstream Tag** a reference (standard) or an object (annotated) **HEAD** a place where your **working directory** is now 

2 

## **06  Inspect history** 

**==> picture [357 x 153] intentionally omitted <==**

**----- Start of picture text -----**<br>
List commit history of current branch.  -n count  limits list to last<br>git log [-n count]<br>n  commits.<br>git log --oneline  An overview with reference labels and history graph. One<br>--graph --decorate commit per line.<br>List commits that are present on the current branch and not<br>git log ref-.<br>merged into  ref . A  ref  can be a branch name or a tag name.<br>List commit that are present on  ref  and not merged into current<br>git log -.ref<br>branch.<br>List operations (e.g. checkouts or commits) made on local<br>git reflog<br>repository.<br>**----- End of picture text -----**<br>


## **07  Tagging commits** 

**==> picture [357 x 111] intentionally omitted <==**

**----- Start of picture text -----**<br>
git tag List all tags.<br>git tag [name]    Create a tag reference named  name  for current commit. Add<br>[commit sha] commit sha  to tag a specific commit instead of current one.<br>git tag -a [name]<br>Create a tag object named  name  for current commit.<br>[commit sha]<br>git tag -d [name] Remove a tag from local repository.<br>**----- End of picture text -----**<br>


## **08  Reverting changes** 

**==> picture [357 x 92] intentionally omitted <==**

**----- Start of picture text -----**<br>
Switches the current branch to the  target reference , leaving<br>git reset [--hard]  a difference as an uncommitted change. When --hard is used,<br>[target reference] all changes are discarded. It's easy to lose uncommitted<br>changes with  --hard.<br>Create a new commit, reverting changes from the specified<br>git revert [commit sha]<br>commit. It generates an  inversion  of changes.<br>**----- End of picture text -----**<br>


## **09  Synchronizing repositories** 

**==> picture [357 x 153] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fetch changes from the  remote , but not update tracking<br>git fetch [remote]<br>branches.<br>git fetch --prune  Delete remote Refs that were removed from the  remote<br>[remote] repository.<br>Fetch changes from the  remote  and merge current branch with<br>git pull [remote]<br>its upstream.<br>git push [--tags]<br>Push local changes to the  remote . Use  --tags  to push tags.<br>[remote]<br>git push -u [remote]  Push local branch to  remote  repository. Set its copy as an<br>[branch] upstream.<br>**----- End of picture text -----**<br>


## **10  Git installation** 

For GNU/Linux distributions, Git should be available in the standard system repository. For example, in Debian/Ubuntu please type inthe terminal: 

sudo apt-get install git 

If you need to install Git from source, you can get it from **git-scm.com/downloads** . 

An excellent Git course can be found in the great Pro Git book by Scott Chacon and Ben Straub. The book is available online for free at **git-scm.com/book.** 

## **11  Ignoring files** 

```
cat   -<EOF >  .gitignore
/logs-*
!logs/.gitkeep
/tmp
*.swp
EOF
```

To ignore files, create a .gitignore file in your repository with a line for each pattern. File ignoring will work for the current and sub directories where .gitignore file is placed. In this example, all files are ignored in the logs directory (excluding the .gitkeep file), whole tmp directory and all files *.swp. 

