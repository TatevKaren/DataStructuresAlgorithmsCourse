# Binary Tree Functions





   
    class TreeNode():
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        
    # returns the height of the tree
    def height(self):
        if self is None:
           return 0
        return(1 + max(TreeNode.height(self.left), TreeNode.height(self.right)))
    
    # returns the size of the tree
    def size(self):
        if self is None:
           return 0
        return(1 + TreeNode.size(self.left) + TreeNode.size(self.right))
    
    # returns an array containig all the nodes in InOrder sorting
    def traverse_inorder(self):
        if self is None:
            return []
        # left, node, right
        return(TreeNode.traverse_inorder(self.left) + [self.key] + TreeNode.traverse_inorder(self.right))
    
    # returns an array containig all the nodes in PreOrder sorting
    def traverse_preorder(self):
        if self is None:
            return []
        # node, left, right
        return([self.key] + TreeNode.traverse_preorder(self.left) + TreeNode.traverse_preorder(self.right))
    
    # returns an array containig all the nodes in PostOrder sorting
    def traverse_postorder(self):
         if self is None:
            return []
         # left, right, node
         return(TreeNode.traverse_postorder(self.left) + TreeNode.traverse_postorder(self.right) + [self.key])

    # helper function for parsing tree to tuple (converting tree to tuple)
    def to_tuple(self):
        # checking whether the node is a tree node or instance eof TreeNode class
        if self is None:
            return None
        if self.left is None and self.right is None:
            return (self.key)
        return(TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right))
    
    # static function to convert tuple to a tree
    @staticmethod
    def parse_tuple(data):
    
        # if the data is a tuple instance and has 3 elements
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return(node)

