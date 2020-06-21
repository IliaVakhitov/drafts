# Binary Tree Level Order Traversal

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
        root = TreeNode(22)

        root.left = TreeNode(11)

        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        root.right = TreeNode(33)
        root.right.right = TreeNode(24)

        print(root)
        print(self.levelOrder(root))

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []            
        queue.append(root)
        res = []
        if not root:
            return res
        res.append([])
        level = []
        ind = 0
        while queue:
            node = queue.pop(0)
            if not node:
                continue
            res[ind].append(node.val)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
            if len(queue) == 0:
                ind += 1    
                queue = level
                if level:
                    res.append([])
                level = []
                
        return res

if __name__ == '__main__':
    Solution().run()
