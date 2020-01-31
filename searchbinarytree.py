

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.val}: [{self.left},{self.right}]'


# 30 minutes
class Solution(object):

    def run(self):
        tree = []
        for i in range(12):
            tree.append(TreeNode(i))

        tree[8].left = tree[10]
        tree[8].right = tree[11]

        tree[5].left = tree[8]
        tree[5].right = tree[9]

        tree[1].left = tree[4]
        tree[1].right = tree[5]

        tree[2].left = tree[6]
        tree[2].right = tree[7]

        tree[0].left = tree[1]
        tree[0].right = tree[2]

        print(self.searchBSTrecursive(tree[0], 5))

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

        res = self.iteration(root.left, val)
        if res is None:
            return self.iteration(root.right, val)
        return res

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

