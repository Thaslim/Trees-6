"""
TC: O(N)
SP: O(N)
Encode: Iterate over all the nodes in postorder manner and form a string using values, separate values by a delimenter , marks Null values as "N"
Decode: SPlit the string by delimiter, construct BT by popping elements one by one
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""

        def postorder(root):
            nonlocal res
            if not root:
                res += "N:"
                return

            postorder(root.left)
            postorder(root.right)
            res += str(root.val) + ":"

        postorder(root)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_arr = [x for x in data.split(":") if x]

        def helper():
            if not tree_arr or tree_arr[-1] == "N":
                tree_arr.pop()
                return None
            root = TreeNode(tree_arr.pop())
            root.right = helper()
            root.left = helper()
            return root

        return helper()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
