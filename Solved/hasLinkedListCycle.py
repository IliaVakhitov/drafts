# Linked List Cycle

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
        node_5 = ListNode(5)
        node_4 = ListNode(4)
        node_3 = ListNode(3)
        node_2 = ListNode(2)
        node_1 = ListNode(1)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        # Cycle nodes
        node_5.next = node_2
        
        print(str(self.hasCycle(node_1)))

    def hasCycle(self, head: ListNode) -> bool:
        # Two pointer fast and slow
        # If fast == slow -> cycle
        f = head
        s = head
        while s and f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True
            
        return False

    def hasCycleHash(self, head: ListNode) -> bool:
        # Store visited in set
        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
            
        return False
        
if __name__ == '__main__':
    Solution().run()

