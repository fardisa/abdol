```python
import os
from git import Repo
from merge import merge_branches
from pull_request import create_pull_request
from commit import commit_changes
from scaffolding_check import check_scaffolding

def process_repo():
    repo = Repo(os.getcwd())
    branches = repo.branches

    for branch in branches:
        if branch != 'main':
            merge_branches('main', branch.name)
            create_pull_request('main', branch.name)
            commit_changes('Merged branch ' + branch.name + ' into main')

    check_scaffolding()

if __name__ == "__main__":
    process_repo()
```