# Current Level OrderTraversal Printing


   class BSTNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # to get the height of the tree
    def get_tree_height(self):
         if self is None:
             return 0
         return(1+max( BSTNode.get_tree_height(self.left), BSTNode.get_tree_height(self.right) ))

    # to print the nodes at the current given level
    def printCurrentLevel(self, level):
         if self is None:
             return None
         # if at 1 level return the root key
         if level == 1:
             print(self.key, end=' ')
         # if at level higher than 1 then we need to print recursively left and right subtrees
         elif level > 1:
             # printing the previous levels nodes of left subtree and right subtree
             BSTNode.printCurrentLevel(self.left, level - 1)
             BSTNode.printCurrentLevel(self.right, level - 1)

    def LevelOrderTraversal(self):
        h = BSTNode.get_tree_height(self)
        # per level in height print the nodes
        for i in range(1, h + 1):
            BSTNode.printCurrentLevel(self, i)
