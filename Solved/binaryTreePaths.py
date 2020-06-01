
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

        print(self.binaryTreePaths(tree[4]))

    def binaryTreePaths(self, root: TreeNode) -> int:

        if root is None:
            return []
    
        stack = []
        paths = []
        stack.append({'node':root, 'path':str(root.val)})
        while stack:
            el = stack.pop()
            path = el['path']
            node = el['node']
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append({'node': node.left, 'path': path+'->'+str(node.left.val)})
            if node.right:
                stack.append({'node': node.right, 'path': path+'->'+str(node.right.val)})
                
        return paths

if __name__ == '__main__':
    Solution().run()


