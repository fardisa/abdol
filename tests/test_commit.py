import unittest
from commit import commit_changes

class TestCommit(unittest.TestCase):

    def setUp(self):
        self.repo = 'path/to/repo'
        self.branch = 'main'
        self.commit_message = 'Test commit'

    def test_commit_changes(self):
        result = commit_changes(self.repo, self.branch, self.commit_message)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()