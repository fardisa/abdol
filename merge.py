```python
import git
from git import Repo

def merge_branches(repo_path, branch_name):
    repo = git.Repo(repo_path)
    git_cmd = repo.git

    # Checkout to main branch
    git_cmd.checkout('main')

    # Merge the specified branch into main
    try:
        git_cmd.merge(branch_name)
        print(f"Branch {branch_name} merged successfully into main.")
    except Exception as e:
        print(f"Error occurred while merging: {str(e)}")

def merge_all_branches(repo_path):
    repo = git.Repo(repo_path)
    branches = repo.branches

    for branch in branches:
        if branch != 'main':
            merge_branches(repo_path, branch)

if __name__ == "__main__":
    repo_path = '.'  # Path to your repository
    merge_all_branches(repo_path)
```