![image 1](cheat-sheet_images/imageFile1.png)

# --print-out

Git Cheat Sheet

<table>
  <tr>
    <th>Getting Started Start a new repo: git init<br><br>Clone an existing repo: git clone <url></th>
  </tr>
</table>


<table>
  <tr>
    <th>Prepare to Commit Add untracked file or unstaged changes: git add <file><br><br>Add all untracked files and unstaged changes: git add .<br><br>Choose which parts of a file to stage: git add -p<br><br>Move file: git mv <old> <new><br><br>Delete file: git rm <file><br><br>Tell Git to forget about a file without deleting it: git rm --cached <file><br><br>Unstage one file:<br><br>git reset <file> Unstage everything: git reset<br><br>Check what you added: git status</th>
  </tr>
</table>


<table>
  <tr>
    <th>Make Commits Make a commit (and open text editor to write message): git commit<br><br>Make a commit: git commit -m 'message'<br><br>Commit all unstaged changes: git commit -am 'message'</th>
  </tr>
</table>


<table>
  <tr>
    <th>Move Between Branches Switch branches: git switch <name><br><br>OR git checkout <name> Create a branch: git switch -c <name><br><br>OR git checkout -b <name> List branches: git branch List branches by most recently committed to: git branch --sort=-committerdate Delete a branch: git branch -d <name> Force delete a branch: git branch -D <name></th>
  </tr>
</table>


<table>
  <tr>
    <th>Diff Staged/Unstaged Changes Diff all staged and unstaged changes: git diff HEAD<br><br>Diff just staged changes: git diff --staged<br><br>Diff just unstaged changes: git diff</th>
  </tr>
</table>


<table>
  <tr>
    <th>Diff Commits Show diff between a commit and its parent: git show <commit><br><br>Diff two commits: git diff <commit> <commit><br><br>Diff one file since a commit: git diff <commit> <file><br><br>Show a summary of a diff:<br><br>git diff <commit> --stat git show <commit> --stat</th>
  </tr>
</table>


## Ways to refer to a commit

Every time we say <commit>, you can use any of these:

#### ★a branch

#### ★a tag

#### ★a commit ID

#### ★a remote branch

★current commit

★3 commits ago

main

v0.1

3e887ab

origin/main

HEAD

HEAD^^^ or HEAD~3

<table>
  <tr>
    <th>Discard Your Changes Delete unstaged changes to one file: git restore <file><br><br>OR<br><br>git checkout <file><br><br>Delete all staged and unstaged changes to one file: git restore --staged --worktree <file><br><br>OR git checkout HEAD <file> Delete all staged and unstaged changes: git reset --hard Delete untracked files: git clean 'Stash' all staged and unstaged changes: git stash</th>
  </tr>
</table>


<table>
  <tr>
    <th>Edit History "Undo" the most recent commit (keep your working directory the same): git reset HEAD^<br><br>Squash the last 5 commits into one: git rebase -i HEAD~6<br><br>Then change "pick" to "fixup" for any commit you want to combine with the previous one<br><br>Undo a failed rebase: git reflog BRANCHNAME<br><br>Then manually find the right commit ID in the reflog, then run:<br><br>git reset --hard <commit><br><br>Change a commit message (or add a file you forgot): git commit --amend</th>
  </tr>
</table>


<table>
  <tr>
    <th>Code Archaeology Look at a branch's history: git log main git log --graph main git log --oneline Show every commit that modified a file: git log <file><br><br>Show every commit that modified a file, including before it was renamed: git log --follow <file><br><br>Find every commit that added or removed some text: git log -G banana<br><br>Show who last changed each line of a file: git blame <file></th>
  </tr>
</table>


Combine Diverged Branches Combine with rebase: git switch banana git rebase main Before:

<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


main

<table>
  <tr>
    <th>D</th>
  </tr>
</table>


<table>
  <tr>
    <th>E</th>
  </tr>
</table>


banana

After:

main banana

<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


<table>
  <tr>
    <th>D′</th>
  </tr>
</table>


<table>
  <tr>
    <th>E′</th>
  </tr>
</table>


D

E

"lost"

Combine with merge: git switch main git merge banana Before:

<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


main

<table>
  <tr>
    <th>D</th>
  </tr>
</table>


<table>
  <tr>
    <th>E</th>
  </tr>
</table>


banana

After:

<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


<table>
  <tr>
    <th>◇</th>
  </tr>
</table>


main

<table>
  <tr>
    <th>D</th>
  </tr>
</table>


<table>
  <tr>
    <th>E</th>
  </tr>
</table>


banana

Combine with squash merge: git switch main git merge --squash banana git commit Before:

<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


main

<table>
  <tr>
    <th>D</th>
  </tr>
</table>


<table>
  <tr>
    <th>E</th>
  </tr>
</table>


banana

After:

<table>
  <tr>
    <th>D<br>E<br></th>
  </tr>
</table>


<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


main

<table>
  <tr>
    <th>D</th>
  </tr>
</table>


<table>
  <tr>
    <th>E</th>
  </tr>
</table>


banana

Bring a branch up to date with another branch (aka "fast-forward merge"): git switch main git merge banana Before:

<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


<table>
  <tr>
    <th>D</th>
  </tr>
</table>


<table>
  <tr>
    <th>E</th>
  </tr>
</table>


main banana

After:

<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


<table>
  <tr>
    <th>D</th>
  </tr>
</table>


<table>
  <tr>
    <th>E</th>
  </tr>
</table>


main

banana

Copy one commit onto the current branch: git cherry-pick <commit>

Before:

<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


main

<table>
  <tr>
    <th>D</th>
  </tr>
</table>


<table>
  <tr>
    <th>E</th>
  </tr>
</table>


After:

<table>
  <tr>
    <th>A</th>
  </tr>
</table>


<table>
  <tr>
    <th>B</th>
  </tr>
</table>


<table>
  <tr>
    <th>C</th>
  </tr>
</table>


<table>
  <tr>
    <th>D′</th>
  </tr>
</table>


main

<table>
  <tr>
    <th>D</th>
  </tr>
</table>


<table>
  <tr>
    <th>E</th>
  </tr>
</table>


<table>
  <tr>
    <th>Restore an Old File Get the version of a file from another commit: git checkout <commit> <file><br><br>OR<br><br>git restore <file> --source <commit></th>
  </tr>
</table>


<table>
  <tr>
    <th>Add a Remote git remote add <name> <url></th>
  </tr>
</table>


<table>
  <tr>
    <th>Push Your Changes Push the main branch to the remote origin : git push origin main<br><br>Push the current branch to its remote "tracking branch": git push<br><br>Push a branch that you've never pushed before: git push -u origin <name><br><br>Force push: git push --force-with-lease<br><br>Push tags: git push --tags</th>
  </tr>
</table>


<table>
  <tr>
    <th>Pull Changes Fetch changes (but don't change any of your local branches): git fetch origin main<br><br>Fetch changes and then rebase your current branch: git pull --rebase<br><br>Fetch changes and then merge them into your current branch: git pull origin main<br><br>OR<br><br>git pull</th>
  </tr>
</table>


<table>
  <tr>
    <th>Configure Git Set a config option: git config user.name 'Your Name'<br><br>Set option globally: git config --global ...<br><br>Add an alias: git config alias.st status<br><br>See all possible config options: man git-config</th>
  </tr>
</table>


<table>
  <tr>
    <th>Important Files Local git config:<br><br>.git/config Global git config: ~/.gitconfig List of files to ignore:<br><br>.gitignore</th>
  </tr>
</table>


