# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
        if not head or not head.next:
            return head
        
        ret = head
        
        ptr = head.next
        
        ret.next = None

        while ptr:
            temp = ptr.next
            ptr.next = ret
            ret = ptr
            ptr = temp

        return ret
