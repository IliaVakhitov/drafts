

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

        print(self.searchBST(tree[4], 2))

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
        curr = root
        while True:
            if curr is None:
                return None
            if curr.val == val:
                return curr
            elif curr.val > val:
                curr = curr.left
            elif curr.val < val:
                curr = curr.right

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

        res = self.iteration(root, val)
        return res

