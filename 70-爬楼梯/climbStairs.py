class Solution:
    def climbStairs(self, n: int) -> int:
        ans = {}
        ans[0] = 0
        ans[1] = 1
        ans[2] = 2
        for i in range(n+1):
            if i in ans:
                pass
            else:
                ans[i] = ans[i-1] + ans[i-2]
        return ans[n]
