# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def postorderTraversal(self, root):

    ans = []

    def defs(node):
        if  not node:
            return

        defs(node.left)

        defs(node.right)

        ans.append(node.val)
    defs(root)
    return ans
        