import unittest

from camelMatch import Solution

class TestCase(unittest.TestCase):
    def test_camelMatch(self):
        sol = Solution()
        self.assertEqual(sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FB",[True, False,True,True,False]))

    def test_match(self):
        sol = Solution()
        self.assertEqual(sol.match("ForceFeedBack", "FB"),False)
