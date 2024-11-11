# GIT 
----------------------

## GIT Global Configuration
1. From the command line, change into the repository directory.
2. Set your username:
```console
$ git config user.name "FIRST_NAME LAST_NAME"
```
3. Set your email address:
```console
$ git config user.email "MY_NAME@example.com"
```
4. Verify your configuration by displaying your configuration file:
```console
$ cat .git/config
```
------------------------------
## GIT Commands CheatSheet

# Git Commands Cheat Sheet

## Git Basics

| Command                     | Description                                                          |
|-----------------------------|----------------------------------------------------------------------|
| `git init`                  | Initialize a new Git repository in the current directory.           |
| `git clone <url>`           | Clone a repository from a remote source.                            |
| `git status`                | Show the working directory and staging area status.                 |
| `git add <file>`            | Stage changes for commit (use `.` for all files).                   |
| `git commit -m "message"`   | Commit staged changes with a message.                               |
| `git log`                   | View the commit history.                                            |
| `git log --oneline`         | View commit history in a concise, one-line format.                  |

---

## Branching and Merging

| Command                          | Description                                                 |
|----------------------------------|-------------------------------------------------------------|
| `git branch`                     | List all branches.                                          |
| `git branch <branch-name>`       | Create a new branch.                                        |
| `git checkout <branch-name>`     | Switch to a specific branch.                                |
| `git switch <branch-name>`       | Switch branches (alternative to `checkout`).                |
| `git merge <branch-name>`        | Merge a branch into the current branch.                     |
| `git branch -d <branch-name>`    | Delete a branch.                                            |
| `git branch -D <branch-name>`    | Force delete a branch (if it has unmerged changes).         |
| `git checkout -b <new-branch>`   | Create and switch to a new branch.                          |

---

## Remote Repositories

| Command                                | Description                                                   |
|----------------------------------------|---------------------------------------------------------------|
| `git remote add <name> <url>`          | Add a remote repository.                                      |
| `git remote -v`                        | List remote repositories.                                     |
| `git fetch <remote>`                   | Fetch changes from the remote without merging.                |
| `git pull <remote> <branch>`           | Fetch and merge changes from the remote branch.               |
| `git push <remote> <branch>`           | Push local changes to a remote branch.                        |
| `git push -u <remote> <branch>`        | Push and set upstream branch (for future `git push`).         |
| `git remote remove <name>`             | Remove a remote repository.                                   |

---

## Staging and Unstaging

| Command                                  | Description                                                  |
|------------------------------------------|--------------------------------------------------------------|
| `git add <file>`                         | Add a file to the staging area.                              |
| `git add .`                              | Add all changed files in the working directory to staging.   |
| `git reset <file>`                       | Unstage a file from the staging area.                        |
| `git reset`                              | Unstage all staged files.                                    |
| `git reset --hard`                       | Reset all changes (committed or not) to the last commit.     |

---

## Viewing and Searching History

| Command                                     | Description                                                  |
|---------------------------------------------|--------------------------------------------------------------|
| `git log`                                   | View commit history.                                         |
| `git log --oneline`                         | View commit history in one line per commit.                  |
| `git log -p`                                | Show patch (diff) for each commit.                           |
| `git show <commit>`                         | Show details for a specific commit.                          |
| `git diff`                                  | View unstaged changes in the working directory.              |
| `git diff --staged`                         | View changes staged for the next commit.                     |

---

## Undoing Changes

| Command                                   | Description                                                  |
|-------------------------------------------|--------------------------------------------------------------|
| `git checkout <file>`                     | Discard changes in a file (to last commit).                  |
| `git restore <file>`                      | Alternative to discard changes in a file.                    |
| `git reset --soft HEAD~1`                 | Undo the last commit, keep changes staged.                   |
| `git reset --mixed HEAD~1`                | Undo the last commit, unstage changes.                       |
| `git reset --hard HEAD~1`                 | Undo the last commit and discard all changes.                |

---

## Stashing

| Command                          | Description                                                  |
|----------------------------------|--------------------------------------------------------------|
| `git stash`                      | Save uncommitted changes and clear the working directory.    |
| `git stash list`                 | List all stashed changes.                                    |
| `git stash apply`                | Reapply the most recent stash without removing it.           |
| `git stash drop`                 | Remove the most recent stash.                                |
| `git stash pop`                  | Reapply and remove the most recent stash.                    |

---

## Tagging

| Command                              | Description                                               |
|--------------------------------------|-----------------------------------------------------------|
| `git tag <tag-name>`                 | Create a new tag.                                         |
| `git tag`                            | List all tags.                                            |
| `git tag -a <tag-name> -m "message"` | Create an annotated tag with a message.                   |
| `git show <tag-name>`                | View details of a tag.                                    |
| `git push <remote> <tag-name>`       | Push a tag to a remote repository.                        |
| `git push --tags`                    | Push all tags to a remote repository.                     |

---

## Advanced Commands

| Command                                     | Description                                                  |
|---------------------------------------------|--------------------------------------------------------------|
| `git rebase <branch>`                       | Rebase the current branch onto another branch.               |
| `git cherry-pick <commit>`                  | Apply changes from a specific commit to the current branch.  |
| `git revert <commit>`                       | Create a new commit that undoes a specific commit.           |
| `git clean -f`                              | Remove untracked files.                                      |

---

This cheat sheet provides a quick reference to essential Git commands, useful for beginners and advanced users alike.
