# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self is not None:
            if self.next:
                return f'{self.val}: {self.next}' 
            else:
                return f'{self.val}'

        return 'None'

class Solution:

    @staticmethod
    def run():
        # Input: 1->2->3->4
        # Output: 2->1->4->3
        node_l11 = ListNode(1)
        node_l12 = ListNode(2)
        node_l13 = ListNode(3)
        node_l14 = ListNode(4)
        node_l15 = ListNode(5)
        
        node_l11.next = node_l12
        node_l12.next = node_l13
        node_l13.next = node_l14
        node_l14.next = node_l15
        
        print(str(Solution.swapPairs(node_l11)) + ' expected 2')
        #print(str(Solution.swapPairs(node_l11)) + ' expected 2')
    
    @staticmethod
    def swapPairs(head: ListNode) -> ListNode:
        
        if not head:
            return head
        
        tail = None

        if head.next:
            tail = head.next.next
            f = head
            s = head.next

            head = s
            head.next = f
            f.next = tail   
            curr = f         
        
        while tail:
            if tail.next:                
                # swap
                f = tail
                s = tail.next
                tail = s.next
                curr.next = s
                s.next = f
                f.next = tail
                curr = f
            else:

                break

        return(head)        


if __name__ == '__main__':
    Solution.run()


