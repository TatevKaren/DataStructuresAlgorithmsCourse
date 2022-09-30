# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # if there is no left subtree we will look at the right subtree and  find its min depth
        if root.left is None:
            return self.minDepth(root.right) + 1
        # if there is no right subtree we will look at the left subtree and find its  min depth
        if root.right is None:
             return self.minDepth(root.left) + 1
        else:
            return(1+ min(self.minDepth(root.left), self.minDepth(root.right)))