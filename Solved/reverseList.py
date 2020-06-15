# Reverse Linked List

# Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        if self is not None:
            if self.next:
                return f'{self.val}: {self.next}' 
            else:
                return f'{self.val}'

        return 'None'

class Solution(object):
    def run(self):
        # Input: 1->2->3->4->5
        # Output: 5->4->3->2->1
        node_5 = ListNode(5)
        node_4 = ListNode(4)
        node_3 = ListNode(3)
        node_2 = ListNode(2)
        node_1 = ListNode(1)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        
        print(str(self.reverseList(node_1)))
    
    def reverseNode(self, head: ListNode, tail: ListNode) -> ListNode:
        t = tail.next
        #head.next = None
        tail.next = head
        if t:
            return self.reverseNode(tail, t)
        return tail

    def reverseListRecurcsion(self, head: ListNode) -> ListNode:
        if head.next:
            t = head.next
            head.next = None
            return self.reverseNode(head, t)
        return head   

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        tail = head.next
        head.next = None
        while tail:
            t = tail.next
            tail.next = head
            head, tail = tail, t
        
        return head 
        
if __name__ == '__main__':
    Solution().run()

