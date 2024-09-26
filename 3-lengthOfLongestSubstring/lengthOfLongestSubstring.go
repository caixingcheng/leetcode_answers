func lengthOfLongestSubstring(s string) int {
    ans := 0
    length := len(s)
    start := 0
    end := 0
    for end < length {
        for i := start; i<end; i++ {
            if s[i] == s[end] {
                start = i+1
            }
        }
        ans = max(ans, end-start+1)
        end += 1
    }
    return ans
}
