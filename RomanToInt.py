class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }
        
        prev = 0
        ans = 0
        
        for char in s:
            num = values[char]
            if prev != 0 and prev < num:
                ans += num - 2 * prev
                
            else:
                prev = num
                ans += num
                
        return ans