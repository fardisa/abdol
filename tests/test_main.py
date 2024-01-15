import unittest
from main import merge_branches, create_pull_request, commit_changes, check_scaffolding

class TestMain(unittest.TestCase):

    def setUp(self):
        self.repo = 'path_to_your_repo'

    def test_merge_branches(self):
        result = merge_branches(self.repo)
        self.assertTrue(result)

    def test_create_pull_request(self):
        result = create_pull_request(self.repo)
        self.assertTrue(result)

    def test_commit_changes(self):
        result = commit_changes(self.repo)
        self.assertTrue(result)

    def test_check_scaffolding(self):
        result = check_scaffolding(self.repo)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()