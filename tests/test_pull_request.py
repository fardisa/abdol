import unittest
from pull_request import create_pull_request

class TestPullRequest(unittest.TestCase):

    def setUp(self):
        self.branches = ['branch1', 'branch2']

    def test_create_pull_request(self):
        for branch in self.branches:
            response = create_pull_request(branch, 'main')
            self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()