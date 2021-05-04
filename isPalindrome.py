class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            x_str = str(x)
            if len(x_str) == 1:
                return True
            else:
                if(x == int(x_str[::-1])):
                    return True
                else:
                    return False