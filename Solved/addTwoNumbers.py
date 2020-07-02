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
        node_4 = ListNode(4)
        node_3 = ListNode(3)
        node_2 = ListNode(2)
        node_1 = ListNode(1)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        print(self.addTwoNumbers(node_1, node_1))

    def listToInt(self, node: ListNode) -> int:
        k = 0
        res = 0
        while node:
            res += node.val * 10**k
            node = node.next
            k += 1
        return res
    
    def intToList(self, number: int) -> ListNode:
        # Reverse string
        # Make a list        
        string = str(number)[::-1]
        res = ListNode()
        node = ListNode(int(string[0]))
        res.next = node
        for i in range(1,len(string)):
            node.next = ListNode(int(string[i])) 
            node = node.next
        return res.next
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.intToList(
            self.listToInt(l1) + self.listToInt(l2)
        )
                       

if __name__ == '__main__':
    Solution().run()
