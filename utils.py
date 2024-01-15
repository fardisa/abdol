```python
import os
import subprocess
import git

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def log_change(change):
    with open('LOG.md', 'a') as log_file:
        log_file.write(change + '\n')

def log_error(error):
    with open('ERROR.md', 'a') as error_file:
        error_file.write(error + '\n')

def check_code(file_path):
    result = subprocess.run(['python', '-m', 'py_compile', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        log_error(f'Error in {file_path}: {result.stderr.decode()}')
        return False
    return True

def update_code(file_path):
    code = read_file(file_path)
    # Here you can add code to update the code if necessary
    write_file(file_path, code)
    log_change(f'Updated {file_path}')

def commit_changes():
    repo = git.Repo(os.getcwd())
    repo.git.add(update=True)
    repo.index.commit('Updated code')

def review_all_codes():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                if check_code(file_path):
                    update_code(file_path)
    commit_changes()
```