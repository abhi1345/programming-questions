def intersects(a, b):
    if a[1] < b[0]:
        return False
    elif b[1] < a[0]:
        return False
    return True

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        while A and B:
            if intersects(A[0], B[0]):
                f = max(B[0][0], A[0][0])
                s = min(B[0][1], A[0][1])
                ans.append([f,s])
            if A[0][1] < B[0][1]:
                A.pop(0)
            else:
                B.pop(0)
        return(ans)
