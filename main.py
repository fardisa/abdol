```python
import merge
import pull_request
import commit
import scaffolding_check

def main():
    # Get all branches in the repo
    branches = merge.get_all_branches()

    # Go through all branches
    for branch in branches:
        # Merge branch into main branch, if applicable
        if merge.is_merge_applicable(branch):
            merge.merge_branches(branch)

    # Create pull requests and commits, if applicable
    if pull_request.is_pull_request_applicable():
        pull_request.create_pull_request()

    if commit.is_commit_applicable():
        commit.commit_changes()

    # Check if all files and folders are according to complete project scaffolding
    if not scaffolding_check.check_scaffolding():
        print("Project scaffolding is not correct. Please check.")

    # Check if all files and folders are in main branch
    if not merge.are_all_files_in_main_branch():
        print("Not all files and folders are in the main branch. Please check.")

if __name__ == "__main__":
    main()
```