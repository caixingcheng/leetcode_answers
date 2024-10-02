class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        return quickSearch(nums,0,n-1,n-k)
        
def quickSearch(nums,l,r,k):
    if r==l:
        return nums[k]
    i=l-1
    j=r+1
    partition=nums[l]
    while i<j:
        i+=1
        while nums[i]<partition:
            i+=1
        j-=1
        while nums[j]>partition:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]
    if k<=j:
        return quickSearch(nums,l,j,k)
    else:
        return quickSearch(nums,j+1,r,k)
