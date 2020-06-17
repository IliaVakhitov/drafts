# Symmetric Tree

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:

    def run(self):        
        root = TreeNode(1)
        
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        
        root.left.right.right = TreeNode(5)
        root.right.left.right = TreeNode(5)

        print(self.isSymmetric(root))

    def isSymmetric(self, root: TreeNode) -> bool:
        # iterative
        if not root:
            return True
        
        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop(0)
            if not left and not right:
                continue
            if not left and right:
                return False
            if left and not right:
                return False                
            if left.val != right.val:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
            
        return True
    
if __name__ == '__main__':
    Solution().run()


    """
    # recursive
    def isSymmetric(self, root: TreeNode) -> bool:
        # recursive
        if not root:
            return True
        return self.isSymmetricNodes(root.left, root.right)
        
    def isSymmetricNodes(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left and right:
            return False
        if left and not right:
            return False                
        res = (left.val == right.val)
        if not res:
            return res
        res = self.isSymmetricNodes(left.left, right.right)
        if not res:
            return res
        return self.isSymmetricNodes(left.right, right.left)
    """

