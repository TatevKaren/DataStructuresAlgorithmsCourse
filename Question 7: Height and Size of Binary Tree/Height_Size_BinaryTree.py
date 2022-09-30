# Question 7: Write a function to calculate the height/depth of a binary tree
def tree_height(node):
    if node is None:
        return 0
    # checking the max height of the left node compared to teh right node and add 1 (for the node)
    return (1  +  max(tree_height(node.left),tree_height(node.right)) )

# Question 8: Write a function to count the number of nodes in a binary
def tree_size(node):
    if node is None:
        # check the size of the left subtree and add the size of the right subtree recursively and add 1 (node)
        return (1 + tree_size(node.left) + tree_size(node.right))