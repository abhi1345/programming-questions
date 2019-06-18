# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def record_save(prev, curr, even, odd, num):
    if curr is None:
        return
    new = curr.next
    newprev = curr
    if num % 2 == 1:
        odd.next = curr
        odd = odd.next
        odd.next = None
    else:
        even.next = curr
        even = even.next
        even.next = None
    record_save(newprev, new, even, odd, num+1)

class Solution:
    def oddEvenList(self, head):
        c = head
        length = 0
        while c:
            length += 1
            c = c.next
        if length <= 2:
            return head
        if length == 3:
            first = head
            second = head.next
            third = second.next
            first.next = third
            third.next = second
            second.next = None
            return first
        odd_head, odd_start = head, head
        even_head, even_start = head.next, head.next
        prev = head.next
        head = head.next.next
        record_save(prev, head, even_head, odd_head, 1)
        while odd_head.next:
            odd_head = odd_head.next
        odd_head.next = even_head
        return odd_start
