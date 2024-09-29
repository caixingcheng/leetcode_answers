class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expend(s, left, right):
            n = len(s)

            while left >= 0 and right < n:
                if s[left] == s[right]:
                    left = left - 1
                    right = right + 1
                else:
                    break
            
            return s[left+1: right]
        

        ans = ''
        if len(s) == 1:
            return s
        for i in range(len(s)):
            a1 = expend(s, i, i)
            a2 = expend(s, i, i+1)
            if len(a1) > len(ans):
                ans = a1
            if len(a2) > len(ans):
                ans = a2

        return ans

        

