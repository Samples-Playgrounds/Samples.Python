![](_page_0_Picture_1.jpeg)

## **01 Git configuration**

| git configglobal<br>user.name "Your Name"            | Set the name that will be attached to your commits and tags.              |
|------------------------------------------------------|---------------------------------------------------------------------------|
| git configglobal<br>user.email "you@example.<br>com" | Set the e-mail address that will be attached to your commits<br>and tags. |
| git configglobal<br>color.ui auto                    | Enable some colorization of Git output.                                   |

### **02 Starting a project**

| git init [project name]              | Create a new local repository in the current directory. If<br>[project name] is provided, Git will create a new directory<br>named [project name] and will initialize a repository inside it. |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git clone <project url=""></project> | Downloads a project with the entire history from the remote<br>repository.                                                                                                                    |

#### **03 Day-to-day work**

| git status               | Displays the status of your working directory. Options include<br>new, staged, and modified files. It will retrieve branch name,<br>current commit identifier, and changes pending commit. |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git add [file]           | Add a file to the staging area. Use. in place of the full file path<br>to add all changed files from the current directory down into<br>the directory tree.                                |
| git diff [file]          | Show changes between working directory and staging area.                                                                                                                                   |
| git diffstaged [file]    | Shows any changes between the staging area and the<br>repository.                                                                                                                          |
| git checkout [file]      | Discard changes in working directory. This operation is<br>unrecoverable.                                                                                                                  |
| git reset <path>]</path> | Revert some paths in the index (or the whole index) to their<br>state in HEAD.                                                                                                             |
| git commit               | Create a new commit from changes added to the staging area.<br>The commit must have a message!                                                                                             |

| git rm [file]<br>Remove file from working directory and staging area. |  |
|-----------------------------------------------------------------------|--|
|-----------------------------------------------------------------------|--|

#### **04 Storing your work**

| git stash      | Put current changes in your working directory into stash for<br>later use. |
|----------------|----------------------------------------------------------------------------|
| git stash pop  | Apply stored stash content into working directory, and clear<br>stash.     |
| git stash drop | Delete a specific stash from all your previous stashes.                    |

### **05 Git branching model**

| git branch [-a]                    | List all local branches in repository. With -a: show all branches<br>(with remote).                                                      |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| git branch [branch_name]           | Create new branch, referencing the current HEAD.                                                                                         |
| git rebase [branch_name]           | Apply commits of the current working branch and apply them<br>to the HEAD of [branch] to make the history of your branch<br>more linear. |
| git checkout [-b]<br>[branch_name] | Switch working directory to the specified branch. With -b: Git<br>will create the specified branch if it does not exist.                 |
| git merge [branch_name]            | Join specified [branch_name] branch into your current branch<br>(the one you are on currently).                                          |
| git branch -d [branch_<br>name]    | Remove selected branch, if it is already merged into any other.<br>-D instead of -d forces deletion.                                     |

| Commit | a state of the code base                             |
|--------|------------------------------------------------------|
| Branch | a reference to a commit; can have a tracked upstream |
| Tag    | a reference (standard) or an object (annotated)      |
| HEAD   | a place where your working directory is now          |

### **06 Inspect history**

| git log [-n count]              | List commit history of current branchn count limits list to last<br>n commits.                                            |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| git logoneline<br>graphdecorate | An overview with reference labels and history graph. One<br>commit per line.                                              |
| git log ref .                   | List commits that are present on the current branch and not<br>merged into ref. A ref can be a branch name or a tag name. |
| git log .ref                    | List commit that are present on ref and not merged into current<br>branch.                                                |
| git reflog                      | List operations (e.g. checkouts or commits) made on local<br>repository.                                                  |

# **07 Tagging commits**

| git tag                           | List all tags.                                                                                                           |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| git tag [name]<br>[commit sha]    | Create a tag reference named name for current commit. Add<br>commit sha to tag a specific commit instead of current one. |
| git tag -a [name]<br>[commit sha] | Create a tag object named name for current commit.                                                                       |
| git tag -d [name]                 | Remove a tag from local repository.                                                                                      |

### **08 Reverting changes**

| git reset [hard]<br>[target reference] | Switches the current branch to the target reference, leaving<br>a difference as an uncommitted change. Whenhard is used,<br>all changes are discarded. It's easy to lose uncommitted<br>changes withhard. |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git revert [commit sha]                | Create a new commit, reverting changes from the specified<br>commit. It generates an inversion of changes.                                                                                                |

## **09 Synchronizing repositories**

| git fetch [remote]               | Fetch changes from the remote, but not update tracking<br>branches.          |
|----------------------------------|------------------------------------------------------------------------------|
| git fetchprune<br>[remote]       | Delete remote Refs that were removed from the remote<br>repository.          |
| git pull [remote]                | Fetch changes from the remote and merge current branch with<br>its upstream. |
| git push [tags]<br>[remote]      | Push local changes to the remote. Usetags to push tags.                      |
| git push -u [remote]<br>[branch] | Push local branch to remote repository. Set its copy as an<br>upstream.      |

## **10 Git installation**

For GNU/Linux distributions, Git should be available in the standard system repository. For example, in Debian/Ubuntu please type inthe terminal:

sudo apt-get install git

If you need to install Git from source, you can get it from **[git-scm.com/downloads](https://git-scm.com/downloads)**.

An excellent Git course can be found in the great Pro Git book by Scott Chacon and Ben Straub. The book is available online for free at **[git-scm.com/book](https://git-scm.com/book/en/v2).**

# **11 Ignoring files**

| cat<br><eof> .gitignore</eof> |
|-------------------------------|
| /logs *                       |
| !logs/.gitkeep                |
| /tmp                          |
| *.swp                         |
| EOF                           |

To ignore files, create a .gitignore file in your repository with a line for each pattern. File ignoring will work for the current and sub directories where .gitignore file is placed. In this example, all files are ignored in the logs directory (excluding the .gitkeep file), whole tmp directory and all files \*.swp.