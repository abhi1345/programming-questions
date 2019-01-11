class Solution {
    public int totalFruit(int[] tree) {
        int answer=0, count=0, left=0, right=0;
        int curr=0;
        for (int i : tree) {
            if (i==left || i==right) {
                curr += 1;
            } else {
                curr = count+1;
            }
            
            if (i==right) {
                count += 1;
            } else {
                left = right;
                right = i;
                count = 1;
            }
            answer = Math.max(answer, curr);
        }
        return answer;
    }
}
