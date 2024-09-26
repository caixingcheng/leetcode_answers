//使用hashTab通过一次遍历找到目标和对应的数组中两个数的下标
//算法时间复杂度O(n)
func twoSum(nums []int, target int) []int {
    var hashTab map[int]int = make(map[int]int)
    for i,n := range nums {
        if p, ok := hashTab[target-n]; ok {
            return []int{i, p}
        } else {
            hashTab[n] = i
        }
    }
    return nil
}
