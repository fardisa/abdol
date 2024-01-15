```python
import os
from utils import read_file, write_file, log_error, log_change

def review_code(file_path):
    try:
        code = read_file(file_path)
        # Here you can add your code review logic
        # If code is not valid, raise an exception
        # If code needs to be updated, update it and log the change
    except Exception as e:
        log_error(f"Error in file {file_path}: {str(e)}")
        return False
    return True

def review_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not review_code(file_path):
                continue
            log_change(f"Reviewed file {file_path}")

if __name__ == "__main__":
    review_all_files('.')
```
This code will review all the files in the given directory and its subdirectories. It uses the utility functions we defined earlier to read files, write files, log errors, and log changes. If there is an error in a file, it logs the error and continues with the next file. If a file needs to be updated, it updates the file and logs the change.