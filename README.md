# Git

* Sajad Faghfoor Maghrebi | 97106187
* Amirmohammad Mohammadi  | 97107126

## Questions

* .git folder is where all required information necessary for git to work properly is stored (including metadata and object database of git project). It's created with `git init` command.
* In the context of git, the atomic means a single operation that cant be divided into smaller operations with meaningful action. Atomic commit means each commit should be dedicated to a single task or sub-task. Atomic pull request means each pull request should be assigned to a single high-level change.
* `git fetch` downloads all changes from main repository to local repository (without merging changes). `git merge` merge all changes and conflicts from remote repository on a new local merge commit. `git pull` downloads new chamges from remote repository (like fetch) and merging them (like merge).
* `git restore` discards all changes and restores every thing to a specified commit. `git revert` undo changes of last commit but unlike git revert it removing changes by creating a new commit and dose not change git history. `git rebase` is rewriting last commit of branch. `git reset` update branch by moving git pointer in thread of commits in branch.
* If a file adds to stage, the next commit will contain this file. in the other hand, if someone stash some files the next commit will not contain this file. stash is used to save uncommit changes localy. So it means that it takes the uncommitted changes (both staged and unstaged), saves them away for later use locally, and then reverts them from the working copy using `git stash pop`.
* snapshot is a representation of current state of project (including all tracked files) in the form of manifest. this manifests can be used to compare different states of a git project.

## Notes

### Itemized list of the activities in the repo

* Created a branch called `multiply` and added a multiplication implementation and its tests.
* Created a branch called `hotfix-test` to address an issue in `test.py`, and merged it with the `main` branch.
* Added multiple tests for summation in the `main` branch.
* Implemented function for addition in the `main` branch.
* Ignored certain files (`__pycache__` directory + `secret.txt`) using gitignore.
* Added a `README.md` file.
* Resolved conflicts on the `main` and `multiply` and `hotfix-test` branches.
* Protect `main` branch.

### Terminal commands


```bash
touch .gitignore
git commit -h
git add .gitignore
git commit -m "add gitignore"
touch secret.txt
git add .gitignore
git commit -m "modify gitignore"
git push
git add .
git commit -m "implement add function"
git checkout -b multiply
git add .
git commit -m "implement mult function"
git checkout main
git reset --hard
cd src
python3 test.py
cd ..
git add .gitignore
git commit -m "add pycache to gitignore"
git status
git add .
git commit -m "test add function"
git push 
git push -u origin multiply
git merge multiply
git push
git checkout -b hotfix-test
git add . && git commit -m 'fix test'
git checkout main
git add . && git commit -m 'add another test' -m 'new test for add function'
git merge hotfix-test
git log --oneline --decorate 
git checkout hotfix-test
git reset --hard
git checkout hotfix-test
git checkout main
git push
git checkout hotfix-test
git push -u origin hotfix-test
git pull
git checkout multiply
git pull
touch test.py
rm test.py
cd src
touch test.py
python3 test.py
git add . && git commit -m 'add mult test' -m 'two new tests for mult function in main'
git reset 
git status
git log --oneline --decorate 
git push
git checkout main
git add . && git commit -m 'add summation test' -m 'new test for add function in main'
git push (rejected)
git pull
git add . && git commit -m 'resolve conflict main branch' 
git push (rejected)
git merge multiply
git add . && git commit -m 'resolve conflict multiply branch' 
git push
git rm --cached __pycache__/
git rm --cached -r __pycache__/
git add . 
git commit -m "ignore pycache"
git push
git log --oneline --decorate 
```

