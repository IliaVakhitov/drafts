# Rotate List

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
        node_l15 = ListNode(5)
        node_l14 = ListNode(4)
        node_l13 = ListNode(3)
        node_l12 = ListNode(2)        
        node_l11 = ListNode(1)

        node_l11.next = node_l12
        node_l12.next = node_l13
        node_l13.next = node_l14
        node_l14.next = node_l15

        print(str(self.rotateRight(node_l11, 1)))
        #print(str(self.mergeTwoLists(node_l25, node_l14)))
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Find len of list
        # Find n = k % len
        # Rotate n
        # Find n-th from end with two pointers
        # Set end.next = head
        # Set nth.next = None

        if not head or k == 0:
            return head
        
        # list len
        ln = 1
        end = head
        while end.next:
            end = end.next
            ln += 1
        # Actual rotation
        n = k % ln
        if n == 0:
            return head

        # new end
        node = head
        for i in range(ln - n - 1):
            node = node.next
        end.next = head
        t = node.next
        node.next = None
        
        return t

if __name__ == '__main__':
    Solution().run()
