class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        return 1 + (num - 1) % 9


print addDigits(0)
print addDigits(65535)
print addDigits(9)
print addDigits(38)

