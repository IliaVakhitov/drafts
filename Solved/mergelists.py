# Merge Two Sorted Lists


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def run(self):
        # Input: 1->2->4, 1->3->4
        # Output: 1->1->2->3->4->4
        node_l14 = ListNode(4)
        node_l12 = ListNode(2)
        node_l12.next = node_l14
        node_l11 = ListNode(1)
        node_l11.next = node_l12

        node_l25 = ListNode(5)
        node_l24 = ListNode(4)
        node_l24.next = node_l25
        node_l23 = ListNode(3)
        node_l23.next = node_l24
        node_l21 = ListNode(1)
        node_l21.next = node_l23

        print(self.mergeTwoLists(node_l11, node_l21))
        print(self.mergeTwoLists(node_l25, node_l14))

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        c2 = l2
        res = ListNode(0)
        res_tail = res
        while True:
            if c1 is None or c2 is None:
                break
            if c2.val <= c1.val:
                res_tail.next = ListNode(c2.val)
                res_tail = res_tail.next
                c2 = c2.next
            else:
                res_tail.next = ListNode(c1.val)
                res_tail = res_tail.next
                c1 = c1.next

        while c2:
            res_tail.next = ListNode(c2.val)
            res_tail = res_tail.next
            c2 = c2.next
        while c1:
            res_tail.next = ListNode(c1.val)
            res_tail = res_tail.next
            c1 = c1.next

        return res.next

