class TreeNode():
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def height(self):
        if self is None:
           return 0
        return(1 + max(TreeNode.height(self.left), TreeNode.height(self.right)))

    def size(self):
        if self is None:
           return 0
        return(1 + TreeNode.size(self.left) + TreeNode.size(self.right))

    def traverse_inorder(self):
        if self is None:
            return []
        # left, node, right
        return(TreeNode.traverse_inorder(self.left) + [self.key] + TreeNode.traverse_inorder(self.right))

    def traverse_preorder(self):
        if self is None:
            return []
        # node, left, right
        return([self.key] + TreeNode.traverse_preorder(self.left) + TreeNode.traverse_preorder(self.right))

    def traverse_postorder(self):
         if self is None:
            return []
         # left, right, node
         return(TreeNode.traverse_postorder(self.left) + TreeNode.traverse_postorder(self.right) + [self.key])

    # helper function for parsing tuple to the tree (converting tiple to a tree)
    def to_tuple(self):
        # checking whether the node is a tree node or instance eof TreeNode class
        if self is None:
            return None
        if self.left is None and self.right is None:
            return (self.key)
        return(TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right))


    @staticmethod
    def parse_tuple(data):
        # if the data is a tuple instance and has 3 elements
        if isinstance(data, tuple) and len(data) == 3:
            # data[1] is the key
            node = TreeNode(data[1])
            # we need recursion
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return(node)


tree_tuple = ( (1,3,None),(2),((None,3,4),(5),(6,7,8)))
print(tree_tuple)
tree = TreeNode.parse_tuple(tree_tuple)
print(tree)
print(tree.traverse_inorder())
print(tree.traverse_preorder())
print(tree.traverse_postorder())
print(tree.height())
print(tree.size())
print(tree.to_tuple())


# -------------- Displaying the tree------------------#
def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    # If the node is empty
    if node is None:
        print(space * level + '∅')
        return
    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return
    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)
display_keys(tree)





