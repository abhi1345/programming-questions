# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    h1 = h2 = head

    while True:
        try:
            h1, h2 = h1.next, h2.next.next
            if h1 == h2:
                return True
        except AttributeError:
            return False
    return False
