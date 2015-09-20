#巧妙运用了KMP的最大前后缀匹配的思想，想想看确实是这样
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        l = s + '$' + r
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            if j > 0 and l[j] != l[i]:
                j = p[j - 1]
            p[i] = j + (l[j] == l[i])
        
        return r[:len(s) - p[-1]] + s
