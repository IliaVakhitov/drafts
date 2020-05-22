
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
        tree = []
        for i in range(7):
            tree.append(TreeNode(i))

        tree[2].left = tree[1]
        tree[2].right = tree[3]

        tree[4].left = tree[2]
        tree[4].right = tree[6]

        print(self.minDepth(tree[4]))

    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0
    
        queue = []
        queue.append({'node':root, 'd':1})
        while queue:
            el = queue.pop(0)
            depth = el['d']
            node = el['node']
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append({'node': node.left, 'd': depth+1})
            if node.right:
                queue.append({'node': node.right, 'd': depth+1})
                
        return 0

if __name__ == '__main__':
    Solution().run()


