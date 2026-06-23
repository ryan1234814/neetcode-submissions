class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pallindrome(t):
            return t==t[::-1]
        if pallindrome(s):
            return True
        for i in range(len(s)):
            t=s[:i]+s[i+1:]
            if pallindrome(t):
                return True        
        return False