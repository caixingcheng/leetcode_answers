//遍历数组两次，时间复杂度O（n2）
func twoSum(nums []int, target int) []int {
    n := len(nums)
    for i:=0; i<n; i++ {
        for j:=i+1; j<n; j++ {
            if (nums[i] + nums[j]) == target {
                return []int{i,j}
            }
        }
    }
    return []int{}
}
