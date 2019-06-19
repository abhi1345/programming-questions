class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int s = nums.size();
        int n = s*(s+1) / 2;
        for (int i = 0; i < s; i++) {
            n -= nums[i];
        }
        return n; //O(n) time, O(1) space
    }
};
