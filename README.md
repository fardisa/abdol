# Project Title

This project is designed to automate the process of managing a Git repository. It goes through the repository and all branches, files, and folders, merges branches into the main branch if applicable, creates pull requests and commits if applicable, and ensures all files and folders are according to the complete project scaffolding and all are in the main branch.

## Files

Here is a brief description of the files and their roles in this project:

- `.gitignore`: Lists files and directories that are not to be tracked by Git.
- `README.md`: This file, provides an overview of the project.
- `main.py`: The main script that orchestrates the other scripts.
- `utils.py`: Contains utility functions used across the project.
- `merge.py`: Handles the merging of branches into the main branch.
- `pull_request.py`: Handles the creation of pull requests.
- `commit.py`: Handles the creation of commits.
- `scaffolding_check.py`: Checks if all files and folders adhere to the project scaffolding.
- `branches/`: Contains example branches for the project.
- `folders/`: Contains example folders for the project.
- `tests/`: Contains test files for the scripts.

## Usage

To use this project, run the `main.py` script. This will go through the repository and perform the necessary actions based on the current state of the repository.

## Testing

To run the tests for this project, navigate to the `tests/` directory and run the test files. Each test file corresponds to a script in the project.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)