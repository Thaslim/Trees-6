"""
TC: O(N) N- number  of nodes
SP: O(N) in worst case if tree is skewed
do dfs on tree add all the nodes within the given range
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        res = []
        def dfs(root):
            nonlocal ans
            if root:
                if low <= root.val <= high:
                    res.append(root.val)
                    ans += root.val
                if low < root.val:
                    dfs(root.left)
                if root.val < high:
                    dfs(root.right)

        dfs(root)
        return ans
