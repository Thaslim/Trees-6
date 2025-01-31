"""
TC: O(N) 
SP: O(N)
DO level order traversal, store values at each column,
keep track of min, max column, 
Iterate over min, max column range and append node values to results
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_items = defaultdict(list)
        min_col = float("inf")
        max_col = float("-inf")
        q = deque([(root, 0, 0)])
        while q:
            for _ in range(len(q)):
                curr, x, y = q.popleft()
                min_col = min(min_col, y)
                max_col = max(max_col, y)
                level_items[y].append(curr.val)
                if curr.left:
                    q.append((curr.left, x + 1, y - 1))
                if curr.right:
                    q.append((curr.right, x + 1, y + 1))
        res = []
        for i in range(min_col, max_col + 1):
            res.append(level_items[i])
        return res
