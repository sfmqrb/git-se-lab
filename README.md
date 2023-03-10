# Git

* Sajad Faghfoor Maghrebi | 97106187
* Amirmohammad Mohammadi  | 97106187

## Questions

* .git folder is where all required information necessary for git to work properly is stored (including metadata and object database of git project). It's created with `git init` command.
* in the context of git, the atomic means a single operation that cant be divided into smaller operations with meaningful action. atomic commit means each commit should be dedicated to a single task or sub-task. atomic pull request means each pull request should be assigned to a single high-level change.

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

