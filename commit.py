```python
import git

def commit_changes(repo_path, commit_message):
    try:
        repo = git.Repo(repo_path)
        repo.git.add(update=True)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    repo_path = "<your-repo-path>"
    commit_message = "Commit made by automated script"
    commit_changes(repo_path, commit_message)
```