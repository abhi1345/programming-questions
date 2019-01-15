class Solution {
    public int largestPerimeter(int[] A) {
        Arrays.sort(A);
        int start = A.length - 1;
        while (start > 1 && A[start - 1] + A[start - 2] <= A[start]) {
            start--;
        }
        if (start == 1) {
            return 0;
        }
        return A[start] + A[start - 1] + A[start - 2];
    }
}
