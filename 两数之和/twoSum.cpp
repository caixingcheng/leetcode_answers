class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        int n=nums.size();
        unordered_map<int, int> hashTab;
        for (int i=0; i<n; i++) {
            auto it = hashTab.find(target - nums[i]);
            if (it != hashTab.end()) {
                res.push_back(i);
                res.push_back(it->second);
                break;
            } else {
                hashTab[nums[i]] = i;
            }
        }
        return res;
    }
};
