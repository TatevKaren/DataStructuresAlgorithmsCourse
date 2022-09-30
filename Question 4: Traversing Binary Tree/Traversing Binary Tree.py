# ---------------------- Traversing a Binary Tree --------------------#
# Question 3: Write a function to perform the inorder traversal of a binary tree.
def traverse_in_order(node):
    # if the node is empty
    if node is None:
        return []
    # if the node is not empty
    # left, node, right
    return(traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))



# Question 4: Write a function to perform the preorder traversal of a binary tree.
def traverse_pre_order(node):
    #if node is empty
    if node is None:
        return []
    # node, left, right
    return([node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right))


# Question 5: Write a function to perform the postorder traversal of a binary tree.
def traverse_post_order(node):
    # if node is empty
    if node is None:
       return []
    # left, right, node
    return(traverse_post_order(node.left)+traverse_post_order(node.right)+[node.key])