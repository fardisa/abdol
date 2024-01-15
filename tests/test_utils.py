import unittest
from utils import merge_branches, create_pull_request, commit_changes, check_scaffolding

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.branches = ['branch1', 'branch2']
        self.main_branch = 'main'
        self.files = ['file1.py', 'file2.py']
        self.folders = ['folder1', 'folder2']

    def test_merge_branches(self):
        for branch in self.branches:
            result = merge_branches(self.main_branch, branch)
            self.assertTrue(result)

    def test_create_pull_request(self):
        for branch in self.branches:
            result = create_pull_request(self.main_branch, branch)
            self.assertTrue(result)

    def test_commit_changes(self):
        for file in self.files:
            result = commit_changes(file)
            self.assertTrue(result)

    def test_check_scaffolding(self):
        for folder in self.folders:
            result = check_scaffolding(folder)
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()