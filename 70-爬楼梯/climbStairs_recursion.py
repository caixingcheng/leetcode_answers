class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(hash, n):
            ## 定义初值以让递归可以结束
            if n == 0 or n == 1:
                return 1
            if n == 2:
                return 2
            if n in hash:
                return hash[n]
            else:
                ## N阶爬法的问题f(n)可以被分解为最后一步是爬两个阶梯的爬法的种数f(n-2)加上
                ## 最后一步是爬一个阶梯的爬法种数f(n-1)之和。
                ans = helper(hash, n - 1) + helper(hash, n-2)  
                hash[n] = ans   ##这里将结果集进行缓存以免同样的问题被多次递归
                return ans
            
        ansTab = {}
        return helper(ansTab, n)
        
