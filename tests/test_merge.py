import unittest
from merge import merge_branches

class TestMerge(unittest.TestCase):

    def setUp(self):
        self.branches = ['branch1', 'branch2']

    def test_merge_branches(self):
        result = merge_branches(self.branches)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()