class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        recurse(nums, 0, answer, new ArrayList<Integer>());
        return answer;
    }
    private void recurse(int[] nums, int i, List<List<Integer>> answer, List<Integer> curr) {
        answer.add(curr);
        for (int k=i; k < nums.length; k++) {
            List<Integer> temp = new ArrayList<Integer>(curr);
            temp.add(nums[k]);
            recurse(nums, k+1, answer, temp);
        }
    }
}
