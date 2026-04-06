|    | 0                               | 1                                                                                                                                  |
|---:|:--------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
|  0 | git branch [-a]                 | List all local branches in repository. With -a : show all branches (with remote).                                                  |
|  1 | git branch [branch_name]        | Create new branch, referencing the current HEAD .                                                                                  |
|  2 | git rebase [branch_name]        | Apply commits of the current working branch and apply them to the HEAD of [branch] to make the history of your branch more linear. |
|  3 | git checkout [-b] [branch_name] | Switch working directory to the specified branch. With -b : Git will create the specified branch if it does not exist.             |
|  4 | git merge [branch_name]         | Join specified [branch_name] branch into your current branch (the one you are on currently).                                       |
|  5 | git branch -d [branch_ name]    | Remove selected branch, if it is already merged into any other. -D instead of -d forces deletion.                                  |