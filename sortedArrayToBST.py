# Convert Sorted Array to Binary Search Tree

from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        if self is not None:
            return f'{self.val}:[{self.left},{self.right}]'
        return 'None'


class Solution(object):

    def run(self):
        print(self.sortedArrayToBST([1,2,3,4,5,6]))

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Create root node from center element of the array
        # Run recursively left sub-array to left node
        # right sub-array to right
        
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        # Center node
        k = len(nums) // 2  
        root = TreeNode(nums[k])
        root.left = self.sortedArrayToBST(nums[:k])
        root.right = self.sortedArrayToBST(nums[k+1:])
        return root

if __name__ == '__main__':
    Solution().run()
