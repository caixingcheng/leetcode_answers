class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        n = len(strX)
        for i in range(0,int(n/2)):
            if strX[i] != strX[n-i-1]:
                print("false")
                return False
        return True
