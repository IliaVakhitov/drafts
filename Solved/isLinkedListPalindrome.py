# Palindrome Linked List

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
        node_5 = ListNode(1)
        node_4 = ListNode(2)
        node_3 = ListNode(3)
        node_2 = ListNode(2)
        node_1 = ListNode(1)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        
        print(str(self.isPalindrome(node_1)))

    def isPalindrome(self, head: ListNode) -> bool:
        # Get middle of the list
        # Save half of it
        # Travelse trought second half and compare with pop() value in list
        
        values = []
        node = head
        fastnode = head
        while fastnode and fastnode.next:  
            fastnode = fastnode.next.next
            values.append(node.val)
            node = node.next
        # If even nodes than skip middle
        if fastnode: 
            node = node.next 
        
        while node:
            if node.val != values.pop():
                return False
            node = node.next
            
        return True

    def isPalindromeBrute(self, head: ListNode) -> bool:
        # Save all values in list
        # use built in function 'reversed' to create reversed list
        # compare list
        values = []
        node = head
        while node:            
            values.append(node.val)
            node = node.next            
        return values == list(reversed(values))
    
        
if __name__ == '__main__':
    Solution().run()

