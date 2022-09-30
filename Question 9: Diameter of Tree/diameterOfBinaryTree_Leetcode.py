# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        self.maxl(root)
        return self.diam
    # fing the max length of 2 nodes
    def maxl(self, root):
        # if it's a node
        if root:
            # max length of left substree
            l = self.maxl(root.left)
            # max length of right subtree
            r = self.maxl(root.right)
            # find out whether the size of the tree with these nodes left plus right is larger tahn the current max diameter
            self.diam = max(self.diam, l+r)
            # if not a root then return 1 + max(l,r)
            return 1+max(l,r)
        return 0



