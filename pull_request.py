```python
from github import Github
import os

def create_pull_request(branch_name, main_branch='main'):
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_user().get_repo(os.getenv('REPO_NAME'))

    main = repo.get_branch(main_branch)
    branch = repo.get_branch(branch_name)

    repo.create_pull(
        title='Merge {0} into {1}'.format(branch_name, main_branch),
        body='This is an automated pull request to merge {0} into {1}'.format(branch_name, main_branch),
        head=branch_name,
        base=main_branch
    )

if __name__ == "__main__":
    branches_to_merge = ['branch1', 'branch2']  # Add your branches here
    for branch in branches_to_merge:
        create_pull_request(branch)
```