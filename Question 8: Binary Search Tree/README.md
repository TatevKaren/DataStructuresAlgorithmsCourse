# Binary Search Tree


    from BinaryTree_Functions import TreeNode
    from BinaryTrees_introduction import User, UserDatabase
   
    def is_BST(node):
      if node is None:
          return True, None, None

    is_bst_l, min_l, max_l = is_BST(node.left)
    is_bst_r, min_r, max_r = is_BST(node.right)


    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return(is_bst_node, min_key, max_key)
    

