class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        num = str(x)
        numLen = len(num)
        palindrome = True

        for i in range (0, numLen):
            if num[i] != num[numLen - 1 - i]:
                return False
        return True
                


        
