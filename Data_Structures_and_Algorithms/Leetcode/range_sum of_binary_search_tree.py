# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if node:
                if node.val >= low and node.val <= high:
                    self.run_sum += node.val
                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        self.run_sum = 0
        dfs(root)
        return self.run_sum