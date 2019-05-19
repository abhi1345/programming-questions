# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        route = []
        i = 0
        answer = head
        while head:
            route.append(head)
            head = head.next
            i += 1
        if n == i:
            return answer.next
        elif n == 1:
            route[i-2].next = None
            return answer
        else:
            route[i-n-1].next = route[i-n+1]
            return answer
