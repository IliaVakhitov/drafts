

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        if self is not None:
            return f'{self.val}: [{self.left},{self.right}]'
        return 'None'


class Solution(object):

    def run(self):
        root = TreeNode(22)

        root.left = TreeNode(11)

        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        root.right = TreeNode(33)
        root.right.left = TreeNode(24)

        print(self.isValidBST(root))

    def isBST(self, root: TreeNode, left: TreeNode = None, right: TreeNode = None):

        if not root:
            return True
        
        # Check left and right values
        if left and left.val >= root.val:
            return False
        if right and right.val <= root.val:
            return False

        # Check recursively all tree nodes
        return (self.isBST(root.left, left, root)
            and self.isBST(root.right, root, right))
        

    def isValidBST(self, root: TreeNode) -> bool:
        # Check if left substree is valid BST 
        # and right subtree is valid BST
        # Max val in left subtree should be less
        # than root val
        # Min val for right subtree shoul be more 
        # than root val

        return self.isBST(root)

if __name__ == '__main__':
    Solution().run()
