# Odd Even Linked List


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
        
class Solution:

    def run(self):
        node_5 = ListNode(5)
        node_4 = ListNode(4)
        node_3 = ListNode(3)
        node_2 = ListNode(2)
        node_1 = ListNode(1)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        print(self.oddEvenList(node_1))

    
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Make sense if len > 2
        # If less return head
        # Set odd_head = head to return
        # Set even_head = head.next to set as tail
        # len is 0
        if not head:
            return head
        # len is 1
        if not head.next:
            return head
        odd_head = head
        even_head = head.next
        # len is 2
        if not even_head.next:
            return head
        # Start with 3rd node
        # set node as even_head.next
        # run cycle until node has next
        odd_node = odd_head
        even_node = even_head
        node = even_head.next
        even = False
        even_node.next = None
        while node:
            print(node.val)
            if even:
                even = False
                even_node.next = node
                even_node = even_node.next
            else:
                even = True
                odd_node.next = node
                odd_node = odd_node.next                
            node = node.next
        # To break cycle
        even_node.next = None
        # set tail to odd_node
        odd_node.next = even_head
        return odd_head
            
        

if __name__ == '__main__':
    Solution().run()
