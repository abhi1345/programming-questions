#Merge-sort-esque approach
#Merges pairs of lists
#Divides size of lists by 2 in each loop iteration
#O(nlog(l)) time

def merge(l1, l2):
    answer = ptr = ListNode(0)
    while l1 and l2:
        ptr.next = ListNode(0)
        ptr = ptr.next
        if l1.val < l2.val:
            ptr.val = l1.val
            l1 = l1.next
        else:
            ptr.val = l2.val
            l2 = l2.next
        
    ending = l1 if l1 else l2
    ptr.next = ending
    return answer.next

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            
            temp = None
            
            if len(lists)%2==1:
                temp = lists.pop()

            i = 0 

            while i < len(lists):
                a = lists.pop(0)
                b = lists.pop(0)
                m = merge(a,b)
                if m:
                    lists.append(merge(a,b))
                i += 2
                
            if lists:
                kick = lists[-1]
                lists[-1] = merge(kick, temp)
            else:
                return None
        
        if lists:
            return lists[0]
        
