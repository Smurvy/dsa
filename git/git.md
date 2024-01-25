# Git

##### What is Git?
- a FOSS control system
- the tool which tracks your versions
- NOT github, which is used as a portfolio
##### What is Version Control
- the management of changes to documents, computer programs, large web sites, and other collections of information

##### Basic commands
`clone` - bring a repo that is hosted somewher like github int oa folder on your local machine
`status` - retrieve what files are tracked/untracked and what and how many changes have been done to them
`add` - track your files and changes in git
    - if you add a file to an active repo, it is not automatically tracked by git, so you must add it manually
    **Quick Tip**: if you run `git add .` it will automatically add all untracked files to the repo
`commmit` - save your files in git
    `-m` - adds a title to your commit
    - if you use it again, it will add a message to your commit
    - this does not update the repo fully, you must use the following `push` command to push your changes to the master repo
`push` - upload git commits to a remote repo like github
`pull` - download changes from remote repo to your local machine, the opposite of a push
`init` - initialies a local directory to create repo

##### Creating a local repo -> pushing to github
- begin with creating a local repo
    -> `git init`
- Go to github, create an empty repo, 