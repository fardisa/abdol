```python
import os
from git import Repo
from utils import check_scaffolding, merge_branches, create_pull_request, commit_changes

def process_file2():
    repo = Repo(os.getcwd())
    branches = repo.branches

    for branch in branches:
        if branch.name != 'main':
            merge_branches(repo, branch.name)
            create_pull_request(repo, branch.name)
            commit_changes(repo, f"Merged {branch.name} into main")

    if check_scaffolding(repo):
        print("All files and folders are according to complete project scaffolding and all are in main branch")
    else:
        print("Some files or folders are not according to the project scaffolding or are not in the main branch")

if __name__ == "__main__":
    process_file2()
```