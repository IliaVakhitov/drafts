

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


# 30 minutes
class Solution(object):

    def run(self):
        tree = []
        for i in range(7):
            tree.append(TreeNode(i))

        tree[2].left = tree[1]
        tree[2].right = tree[3]

        tree[4].left = tree[2]
        tree[4].right = tree[6]

        print(self.searchBSTrecursive(tree[4], 2))

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return []

        if root.val == val:
            return root

        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == val:
                return curr

            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)

        return None

    def iteration(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        if root.left is not None and root.val > val:
            return self.iteration(root.left, val)
        elif root.right is not None and root.val < val:
            return self.iteration(root.right, val)
        return None

    def searchBSTrecursive(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return []

        if root.val == val:
            return root

        res = self.iteration(root, val)
        if res is None:
            return None
        return res

