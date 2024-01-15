```python
import os
from utils import read_file, write_file, log_error, log_change

def review_code(file_path):
    try:
        code = read_file(file_path)
        # Assuming exec() is used to check if the code is functional
        exec(code)
        log_change(f"Reviewed code in {file_path}")
    except Exception as e:
        log_error(f"Error in {file_path}: {str(e)}")

def review_all_codes(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                review_code(file_path)

def update_code(file_path, new_code):
    try:
        write_file(file_path, new_code)
        log_change(f"Updated code in {file_path}")
    except Exception as e:
        log_error(f"Error updating {file_path}: {str(e)}")

def update_all_codes(directory, new_code):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                update_code(file_path, new_code)

def commit_changes():
    # Assuming a simple git commit command
    os.system("git commit -a -m 'Automated code review and update'")

def main():
    review_all_codes('.')
    update_all_codes('.', 'new_code')  # Replace 'new_code' with actual new code
    commit_changes()
```