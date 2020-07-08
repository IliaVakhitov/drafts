# Linked List Cycle II


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
        #node_5 = ListNode(5)
        node_4 = ListNode(4)
        node_3 = ListNode(3)
        node_2 = ListNode(2)
        node_1 = ListNode(1)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_1
        # Cycle
        #node_5.next = node_1
        print(self.detectCycleCount(node_1).val)

    def detectCycleCount(self, head: ListNode) -> ListNode:
        if not head:
            return None
        # Detect cycle with 2 pointers
        # Count len of cycle -> k
        # Set one to start second to k node after head
        # Traverse for both
        # they meet at loop start node
        f = head
        s = head
        is_cycle = False
        while f and s and s.next:
            f = f.next
            s = s.next.next
            if f == s:
                # Cycle detected
                # Find closest to head node
                is_cycle = True
                break
                
        if not is_cycle:
            return None
        # Start traverse from head as s
        # f stores cycle node
        f = s
        # Count len of cycle
        k = 1
        while f.next != s: 
            f = f.next
            k += 1
        # Set s as head and s as f as k-node from head
        s = head
        f = head
        for i in range(k):
            f = f.next
        # Move both s and f
        while f != s:
            f = f.next
            s = s.next
        return s


    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        # Detect cycle with 2 pointers
        # If cycle detected restart from head for one node
        # run another through cycle until they meet
        f = head
        s = head
        is_cycle = False
        while f and s and s.next:
            f = f.next
            s = s.next.next
            if f == s:
                # Cycle detected
                # Find closest to head node
                is_cycle = True
                break
                
        if not is_cycle:
            return None
        # Start traverse from head as s
        # f stores cycle node
        f = s
        s = head
        while True: 
            # Run through cycle as node
            # 1. Reach start cycle node
            # 2. Reach s -> s is cycle_start node
            node = f
            while(node.next != f and node.next != s): 
                node = node.next              
            if node.next == s:
                return s
            s = s.next
            
        

if __name__ == '__main__':
    Solution().run()
