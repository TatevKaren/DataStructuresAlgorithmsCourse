# Binary Search Tree

'''
    from BinaryTree_Functions import TreeNode
    from BinaryTrees_introduction import User, UserDatabase
   
    def is_BST(node):
      if node is None:
          return True, None, None

    # checking whether the left and right subtrees are BST
    is_bst_l, min_l, max_l = is_BST(node.left)
    is_bst_r, min_r, max_r = is_BST(node.right)

    '''Checking whether the tree is a Binary Search Tree'''
    # 1.1 is Left Subtree a BST, is Right Subtree a BST
    # 1.2 max_l is None or the node key is larger than the max_l
    # 1.3 min_r is None or the node key is smaller than min_r
    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    '''Returning the Minimum Key of Binary Tree'''
    # 2 removing the Nones and returning the minimum of the left or right subtree nodes
    min_key = min(remove_none([min_l, node.key, min_r]))

    '''Returning the Maximum Key of Binary Tree'''
    # 3 removing the Nones and returning the maximum of the left or right subtree nodes
    max_key = max(remove_none([max_l, node.key, max_r]))

    # output 1: whether the tree under the given node is BST
    # output 2: what is the minimum key
    # output 3: what is the maximum key
    return(is_bst_node, min_key, max_key)
    

