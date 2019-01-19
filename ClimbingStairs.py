def helper(n, arr):
    if arr[n] != 0:
        return arr[n]
    else:
        ans = helper(n-1, arr) + helper(n-2, arr)
        arr[n] = ans
        return ans
    
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1,1,2] + [0]*(n-2)
        helper(n, arr)
        print(arr)
        return helper(n, arr)
