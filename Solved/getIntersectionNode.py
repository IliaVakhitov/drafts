# Intersection of Two Linked Lists


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

    def getIntersectionNodeCount(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        # Count len of list
        # Count len of list 2
        # Find d as abs(l1-l2)
        # dth- node is intersection
        
        # Count len1
        len1 = 0
        l1 = headA
        while l1:
            l1 = l1.next
            len1 += 1
        print(len1)
        
        # Count len2
        len2 = 0
        l1 = headB
        while l1:
            l1 = l1.next
            len2 += 1
        print(len2)
        # Find d and move londer list on d nodes
        if len1 > len2:
            d = len1 - len2
            for i in range(d):
                headA = headA.next
        else:
            d = len2 - len1
            for i in range(d):
                headB = headB.next
        # Traverse both until they meet
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        # No intersection
        return None
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        # Brute. Hash. r = O(n). s = O(n)
        # Brute. 2 loops r J(n^2), s = O(1)
        # Make cycle. Find cycle node
        # Traverse to the tail
        node = headA
        while node.next:
            node = node.next
        tail = node
                
        # Make loop
        tail.next = headB
                
        # Find where loop starts
        f = headA
        s = headA        
        is_cycle = False
        while f and s and s.next:
            f = f.next
            s = s.next.next
            if f == s:
                # Cycle detected
                is_cycle = True
                break
        if not is_cycle:
            # Remove loop
            tail.next = None
            return None
        
        # Detect intersection node
        # Start traverse from head as s
        # f stores cycle node
        f = s
        # Count len of cycle
        k = 1
        while f.next != s: 
            f = f.next
            k += 1
        # Set s as head and s as f as k-node from head
        s = headA
        f = headA
        for i in range(k):
            f = f.next
        # Move both s and f
        while f != s:
            f = f.next
            s = s.next
        # Remove loop
        tail.next = None
        return s
            
        

if __name__ == '__main__':
    Solution().run()
