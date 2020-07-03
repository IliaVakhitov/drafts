# Add Two Numbers


class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = None
    
    def __str__(self):
        if self is not None:
            if self.next:
                return f'{self.val}: {self.next}' 
            else:
                return f'{self.val}'

        return 'None'
        
class Solution:

    def run(self):
        #node_5 = ListNode(5)
        node_4 = ListNode(8)
        node_3 = ListNode(3)
        node_2 = ListNode(9)
        node_1 = ListNode(5)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        print(self.addTwoNumbers(node_1, node_1))
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # TODO
        head = ListNode(0)
        add = 0
        node = head
        while l1 or l2:
            n1 = 0 if not l1 else l1.val
            n2 = 0 if not l2 else l2.val
            val = add + n1 + n2
            add = val // 10
            val = val % 10 
            node.next = ListNode(val)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if add:
            node.next = ListNode(add)

        return head.next                      

if __name__ == '__main__':
    Solution().run()
