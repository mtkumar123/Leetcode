import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[\W_]+", "", s)
        s = s.lower()
        fp = 0
        lp = len(s) - 1
        while fp < lp:
            if s[fp] != s[lp]:
                return False
            fp+=1
            lp-=1
        return True        
s = Solution()
result = s.isPalindrome("ab_a")
print(result)
        