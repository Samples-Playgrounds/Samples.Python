|    | git fetch          | [remote]    | Fetch changes from the remote, but not update tracking branches.          |
|---:|:-------------------|:------------|:--------------------------------------------------------------------------|
|  0 | git fetch [remote] | --prune     | Delete remote Refs that were removed from the remote repository.          |
|  1 | git pull           | [remote]    | Fetch changes from the remote and merge current branch with its upstream. |
|  2 | git push [remote]  | [--tags]    | Push local changes to the remote. Use --tags to push tags.                |
|  3 | git push [branch]  | -u [remote] | Push local branch to remote repository. Set its copy as an upstream.      |