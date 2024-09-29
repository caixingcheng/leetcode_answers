class Solution:
    def generate(self, numRows) :
        ans=[]
        for i in range(numRows):
            iArray = []
            for j in range(i+1):
                if (j == 0 or j == i):
                    iArray.append(1)  ##最左边和最右边的都是1
                else:
                    iArray.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(iArray)
            
        return ans[:numRows]
