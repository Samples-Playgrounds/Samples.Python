## Git Cheat Sheet

## 01  Git c/uni006Fnfigurati/uni006Fn

| git config --global user.name 'Your Name'         | Set the name that will be attached t/uni006F y/uni006Fur c/uni006Fmmits and tags.           |
|---------------------------------------------------|---------------------------------------------------------------------------------------------|
| git config --global user.email 'you@example. com' | Set the e-mail address that will be attached t/uni006F y/uni006Fur c/uni006Fmmits and tags. |
| git config --global color.ui auto                 | Enable s/uni006Fme c/uni006Fl/uni006Frizati/uni006Fn /uni006Ff Git /uni006Futput.           |

## 02  Starting a pr/uni006Fject

| git init [project name]   | Create a new l/uni006Fcal rep/uni006Fsit/uni006Fry in the current direct/uni006Fry. If [pr/uni006Fject name] is pr/uni006Fvided, Git will create a new direct/uni006Fry named [pr/uni006Fject name] and will initialize a rep/uni006Fsit/uni006Fry inside it.   |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git clone <project url>   | D/uni006Fwnl/uni006Fads a pr/uni006Fject with the entire hist/uni006Fry fr/uni006Fm the rem/uni006Fte rep/uni006Fsit/uni006Fry.                                                                                                                                 |

## 03  Day-t/uni006F-day w/uni006Frk

| git status               | Displays the status /uni006Ff y/uni006Fur w/uni006Frking direct/uni006Fry. /uni004Fpti/uni006Fns include new, staged, and m/uni006Fdified files. It will retrieve branch name, current c/uni006Fmmit identifier, and changes pending c/uni006Fmmit.   |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git add [file]           | Add a file t/uni006F the staging area. Use. in place /uni006Ff the full file path t/uni006F add all changed files fr/uni006Fm the current direct/uni006Fry d/uni006Fwn int/uni006F the direct/uni006Fry tree.                                         |
| git diff [file]          | Sh/uni006Fw changes between w/uni006Frking direct/uni006Fry and staging area.                                                                                                                                                                         |
| git diff --staged [file] | Sh/uni006Fws any changes between the staging area and the rep/uni006Fsit/uni006Fry.                                                                                                                                                                   |
| git checkout -- [file]   | Discard changes in w/uni006Frking direct/uni006Fry. This /uni006Fperati/uni006Fn is unrec/uni006Fverable .                                                                                                                                            |
| git reset -<path>--.]    | Revert s/uni006Fme paths in the index (/uni006Fr the wh/uni006Fle index) t/uni006F their state in HEAD.                                                                                                                                               |
| git commit               | Create a new c/uni006Fmmit fr/uni006Fm changes added t/uni006F the staging area. The c/uni006Fmmit must have a message!                                                                                                                               |

<!-- image -->

| git rm [file]   | Rem/uni006Fve file fr/uni006Fm w/uni006Frking direct/uni006Fry and staging area.   |
|-----------------|------------------------------------------------------------------------------------|

## 04  St/uni006Fring y/uni006Fur w/uni006Frk

| git stash      | Put current changes in y/uni006Fur w/uni006Frking direct/uni006Fry int/uni006F stash f/uni006Fr later use.   |
|----------------|--------------------------------------------------------------------------------------------------------------|
| git stash pop  | Apply st/uni006Fred stash c/uni006Fntent int/uni006F w/uni006Frking direct/uni006Fry, and clear stash.       |
| git stash drop | Delete a specific stash fr/uni006Fm all y/uni006Fur previ/uni006Fus stashes.                                 |

## 05  Git branching m/uni006Fdel

| git branch [-a]                 | List all l/uni006Fcal branches in rep/uni006Fsit/uni006Fry. With -a : sh/uni006Fw all branches (with rem/uni006Fte).                                                                                     |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git branch [branch_name]        | Create new branch, referencing the current HEAD .                                                                                                                                                        |
| git rebase [branch_name]        | Apply c/uni006Fmmits /uni006Ff the current w/uni006Frking branch and apply them t/uni006F the HEAD /uni006Ff [branch] t/uni006F make the hist/uni006Fry /uni006Ff y/uni006Fur branch m/uni006Fre linear. |
| git checkout [-b] [branch_name] | Switch w/uni006Frking direct/uni006Fry t/uni006F the specified branch. With -b : Git will create the specified branch if it d/uni006Fes n/uni006Ft exist.                                                |
| git merge [branch_name]         | J/uni006Fin specified [branch/uni005Fname] branch int/uni006F y/uni006Fur current branch (the /uni006Fne y/uni006Fu are /uni006Fn currently).                                                            |
| git branch -d [branch_ name]    | Rem/uni006Fve selected branch, if it is already merged int/uni006F any /uni006Fther. -D instead /uni006Ff -d f/uni006Frces deleti/uni006Fn.                                                              |

| C/uni006Fmmit   | a state /uni006Ff the c/uni006Fde base                                  |
|-----------------|-------------------------------------------------------------------------|
| Branch          | a reference t/uni006F a c/uni006Fmmit; can have a tracked upstream      |
| Tag             | a reference (standard) /uni006Fr an /uni006Fbject (ann/uni006Ftated)    |
| HEAD            | a place where y/uni006Fur w/uni006Frking direct/uni006Fry is n/uni006Fw |

1

## 06  Inspect hist/uni006Fry

| git log [-n count]                   | List c/uni006Fmmit hist/uni006Fry /uni006Ff current branch. -n c/uni006Funt limits list t/uni006F last n c/uni006Fmmits.                                   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git log --oneline --graph --decorate | An /uni006Fverview with reference labels and hist/uni006Fry graph. /uni004Fne c/uni006Fmmit per line.                                                      |
| git log ref-.                        | List c/uni006Fmmits that are present /uni006Fn the current branch and n/uni006Ft merged int/uni006F ref . A ref can be a branch name /uni006Fr a tag name. |
| git log -.ref                        | List c/uni006Fmmit that are present /uni006Fn ref and n/uni006Ft merged int/uni006F current branch.                                                        |
| git reflog                           | List /uni006Fperati/uni006Fns (e.g. check/uni006Futs /uni006Fr c/uni006Fmmits) made /uni006Fn l/uni006Fcal rep/uni006Fsit/uni006Fry.                       |

## 07  Tagging c/uni006Fmmits

| git tag                        | List all tags.                                                                                                                                                         |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git tag [name] [commit sha]    | Create a tag reference named name f/uni006Fr current c/uni006Fmmit. Add c/uni006Fmmit sha t/uni006F tag a specific c/uni006Fmmit instead /uni006Ff current /uni006Fne. |
| git tag -a [name] [commit sha] | Create a tag /uni006Fbject named name f/uni006Fr current c/uni006Fmmit.                                                                                                |
| git tag -d [name]              | Rem/uni006Fve a tag fr/uni006Fm l/uni006Fcal rep/uni006Fsit/uni006Fry.                                                                                                 |

## 08  Reverting changes

| git reset [--hard] [target reference]   | Switches the current branch t/uni006F the target reference , leaving a difference as an unc/uni006Fmmitted change. When --hard is used, all changes are discarded. It's easy t/uni006F l/uni006Fse unc/uni006Fmmitted changes with --hard.   |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| git revert [commit sha]                 | Create a new c/uni006Fmmit, reverting changes fr/uni006Fm the specified c/uni006Fmmit. It generates an inversi/uni006Fn /uni006Ff changes.                                                                                                   |

## 09  Synchr/uni006Fnizing rep/uni006Fsit/uni006Fries

| git fetch [remote]            | Fetch changes fr/uni006Fm the rem/uni006Fte , but n/uni006Ft update tracking branches.                         |
|-------------------------------|----------------------------------------------------------------------------------------------------------------|
| git fetch --prune [remote]    | Delete rem/uni006Fte Refs that were rem/uni006Fved fr/uni006Fm the rem/uni006Fte rep/uni006Fsit/uni006Fry.     |
| git pull [remote]             | Fetch changes fr/uni006Fm the rem/uni006Fte and merge current branch with its upstream.                        |
| git push [--tags] [remote]    | Push l/uni006Fcal changes t/uni006F the rem/uni006Fte . Use --tags t/uni006F push tags.                        |
| git push -u [remote] [branch] | Push l/uni006Fcal branch t/uni006F rem/uni006Fte rep/uni006Fsit/uni006Fry. Set its c/uni006Fpy as an upstream. |

## 10  Git installati/uni006Fn

F/uni006Fr GNU/uni002FLinux distributi/uni006Fns, Git sh/uni006Fuld be available in the standard system rep/uni006Fsit/uni006Fry. F/uni006Fr example, in Debian/uni002FUbuntu please type inthe terminal:

sud/uni006F apt-get install git

If y/uni006Fu need t/uni006F install Git fr/uni006Fm s/uni006Furce, y/uni006Fu can get it fr/uni006Fm git-scm.c/uni006Fm/uni002Fd/uni006Fwnl/uni006Fads .

An excellent Git c/uni006Furse can be f/uni006Fund in the great Pr/uni006F Git b/uni006F/uni006Fk by Sc/uni006Ftt Chac/uni006Fn and Ben Straub. The b/uni006F/uni006Fk is available /uni006Fnline f/uni006Fr free at git-scm.c/uni006Fm/uni002Fb/uni006F/uni006Fk.

## 11  Ign/uni006Fring files

| cat            | -<EOF > .gitignore   |
|----------------|----------------------|
| /logs-*        | /logs-*              |
| !logs/.gitkeep | !logs/.gitkeep       |
| /tmp           | /tmp                 |
| *.swp          | *.swp                |
| EOF            | EOF                  |

T/uni006F ign/uni006Fre files, create a .gitign/uni006Fre file in y/uni006Fur rep/uni006Fsit/uni006Fry with a line f/uni006Fr each pattern. File ign/uni006Fring will w/uni006Frk f/uni006Fr the current and sub direct/uni006Fries where .gitign/uni006Fre file is placed. In this example, all files are ign/uni006Fred in the l/uni006Fgs direct/uni006Fry (excluding the .gitkeep file), wh/uni006Fle tmp direct/uni006Fry and all files *.swp.