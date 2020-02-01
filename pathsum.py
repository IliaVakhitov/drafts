# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run(self):
        sum = 10
        tree = []
        for i in range(0, 9):
            tree.append(TreeNode(i))

        tree[6].val = 7
        tree[7].val = 2
        tree[8].val = 1

        tree[3].val = 11
        tree[4].val = 13
        tree[5].val = 4

        tree[0].val = 5
        tree[1].val = 4
        tree[2].val = 8

        tree[3].left = tree[6]
        tree[3].right = tree[7]
        tree[5].right = tree[8]
        tree[1].left = tree[3]
        tree[2].left = tree[4]
        tree[2].right = tree[5]
        tree[0].left = tree[1]
        tree[0].right = tree[2]

        print(f'{self.hasPathSum(tree[0], 22)} expected True')
        print(f'{self.hasPathSum(tree[0], 27)} expected True')
        print(f'{self.hasPathSum(tree[0], 26)} expected True')
        print(f'{self.hasPathSum(tree[0], 18)} expected True')
        print(f'{self.hasPathSum(tree[0], 21)} expected False')
        print(f'{self.hasPathSum(tree[0], 19)} expected False')
        print(f'{self.hasPathSum(tree[0], 11)} expected False')

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.right is None and root.left is None:
            return root.val == sum

        res = False
        if root.left is not None:
            res = self.hasPathSum(root.left, sum - root.val)
        if root.right is not None:
            res = res or self.hasPathSum(root.right, sum - root.val)
        return res


