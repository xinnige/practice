import unittest

from hindex import Solution


class TestHIndex(unittest.TestCase):
   
    def test_hindex(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([1,2,3,3]),2)
        self.assertEqual(sol.hIndex([3,2,1,3]),2)
        self.assertEqual(sol.hIndex([1,1]),1)
        self.assertEqual(sol.hIndex([3,0,6,1,5]),3)

if __name__ == '__main__':
    unittest.main()
