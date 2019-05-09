import math

def maxsearch(l, n, i, ans, start, end):
    if end-start == 1 and l[start] == n:
        ans[0] = start
        return
    elif end-start == 1 :
        return
    half = int((start + end)/2)
    if l[half] > n:
        maxsearch(l, n, i, ans, start, half)
    else:
        maxsearch(l, n, i, ans, half, end)
        
def minsearch(l, n, i, ans, start, end):
    if end-start == 1 and l[start] == n:
        ans[0] = start
        return
    elif end-start == 1:
        return
    half = start if end-start == 2 else int((start + end)/2)
    if l[half] >= n:
        minsearch(l, n, i, ans, start, half+1)
    else:
        minsearch(l, n, i, ans, half+1, end)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = nums
        min_ans, max_ans = [-1], [-1]
        if l:
            maxsearch(nums, target, 0, max_ans, 0, len(nums))
            minsearch(nums, target, 0, min_ans, 0, len(nums))
        return min_ans + max_ans
        #O(log n) time solution
        #O(1) space
