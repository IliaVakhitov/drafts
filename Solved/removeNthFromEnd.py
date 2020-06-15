# Remove Nth Node From End of List
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
# Brute solution
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 1
        thead = head
        while head.next:
            i += 1
            head = head.next
        if i == n:
            return thead.next
        head = thead
        i -= n 
        phead = head
        while i > 0:
            phead = head
            head = head.next
            i -= 1
        phead.next = head.next
        return thead
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        thead = ListNode(0)
        thead.next = head
        f = thead
        s = thead
        for i in range(n+1):
            f = f.next
            
        while f:
            f = f.next
            s = s.next
        s.next = s.next.next
        return thead.next
        