# Binary Search Tree

## 1: Checking the tree is Binary Search Tree and Min Key/Max Key

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
    
   
   
   
## 2: Storing Key-Value Pairs using BSTs 
where username is the key and user object is the value
     
     class BSTNode():
      def __init__(self, key, value = None):
          self.key = key
          self.value = value
          self.left = None
          self.right = None
          self.parent = None


## 3: Displaying the tree
    def display_keys(node, space='\t', level=0):
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

## 4: Inserting a node in BST
    def insert(node, key, value):
         # creating a new node when left or right node is not existing
         if node is None:
             # we create a new subtree
             node = BSTNode(key, value)
         # if the new key is smaller than the node we insert it in the left subtree
         elif key < node.key:
              node.left = insert(node.left, key, value)
              node.left.parent = node
         # if the new key is larger than the node we insert in the right subtree
         elif key > node.key:
              node.right = insert(node.right, key, value)
              node.right.parent = node
         return node
 
    
## 5: Finding a Subject
Finding an object with given username(key) while knowing also the node from where on we need to search

  def find(node, key):
    if node is None:
        return None
    if key==node.key:
        return node
    # if the key to be search is smaller than the current node key --> search left
    if key < node.key:
        return find(node.left, key)
    # if the key to be search is larger than the current node key --> search right
    if key > node.key:
        return find(node.right, key)

