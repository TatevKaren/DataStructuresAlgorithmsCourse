from BinaryTree_Functions import TreeNode
from BinaryTrees_introduction import User, UserDatabase

def remove_none(nums):
    return [x for x in nums if x is not None]

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


# Storing Key-Value Pairs using BSTs where username is the key and user object is the value
class BSTNode():
      def __init__(self, key, value = None):
          self.key = key
          self.value = value
          self.left = None
          self.right = None
          self.parent = None


'''Displaying the tree'''
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

# we need to insert recursively based on the properties of BST
# key is the new username and the node is the current node
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


'''Creating users to parse to the BST'''
t = User("TK", "tg", "tgjudx@gmail.com")
l = User("LK", "lita", "lita@gmail.com")
v = User("hag", "vih", "vih@gmail.com")
s = User("SY", "hig", "hig@gmail.com")
k = User("KK", "vpous", "sp@gmail.com")

database = UserDatabase()
database.insert(t)
database.insert(l)
database.insert(v)
database.insert(s)
database.insert(k)

'''Parsing the users to the BST'''
tree = TreeNode.parse_tuple(((k, l), s, (t,v)))

# creating the node of the BST: level 0
tree = BSTNode(s.username, s)
# creating the level 1 of the BST
tree.left = BSTNode(k.username, k)
tree.left.parent = tree

tree.right = BSTNode(t.username, t)
tree.right.parent = tree

# creating the level 2 of the BST
tree.left.right = BSTNode(l.username, l)
tree.left.right.parent = tree.left

#right node
tree.right.right = BSTNode(v.username, v)
tree.right.right.parent = tree.right

display_keys(tree)


'''Inserting a node in a BST function'''
tania = User("tania", "tan", "tania@gmail.com")
database.insert(tania)


# for the initial step since we don't yet have tree
tree2 = insert(None, s.username, s)
insert(tree2, t.username, t)
insert(tree2, l.username, l)
insert(tree2, v.username, v)
insert(tree2, k.username, k)
insert(tree2, tania.username, tania)
# comparing manually inserted nodes vs with the insert function
display_keys(tree)
display_keys(tree2)

'''Finding an object with given username(key) while knowing also the node from where on we need to search'''
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


'''Updating a value in Tree'''
def update(node, key, value):
    # finding the node using the given node key
    target = find(node,key)
    # if not existing then we create a node
    if target is not None:
        target.value = value

update(tree2, 'TatevK', User("TatevK", "Tatev", "tatevkarenn@gmail.com"))
# checking the key and value
node = find(tree2, 'TatevK')
print(node.key, node.value)



'''Getting Sroted list of key, value pairs of BST'''
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

print(list_all(tree2))


'''Checking whether BST is balanced'''
def is_balanced(node):
    # if the tree is empty than it's balanced (True) and height is 0
    if node is None:
        return True, 0

    # whether the left subtree is balanced and what is the height
    balanced_l, height_l = is_balanced(node.left)
    # whether the right subtree is balanced and what is the height
    balanced_r, height_r = is_balanced(node.right)

    # if the left subtree and right subtree are balanced (True) and height difference <=1
    balanced = balanced_l and balanced_r and abs(height_l-height_r) <=1
    # height of the tree (max  of two heights) + 1
    height = 1+max(height_l, height_r)
    return balanced, height
print(is_balanced(tree2))


tree3 = insert(None, s.username, s)
insert(tree2, k.username, k)
insert(tree2, l.username, l)
print(is_balanced(tree3))



'''Creating Balanced Binary Search Tree'''
def make_balanced_bst(data, lo = 0, hi = None, parent = None):
    # the highest level of the tree
    if hi is None:
        hi = len(data) - 1 # (last index of the data)
    # if the hi is less than 0
    if lo > hi:
        return None
    # we want to determine the key of the root node of the tree, this is the mid position
    mid = (lo + hi) // 2
    # getting the key and the value of this mid position
    key, value = data[mid]

    # creating the tree from the node onwards
    root = BSTNode(key, value)

    root.parent = parent
    # left subtree recursively
    root.left = make_balanced_bst(data, lo, mid-1, root)
    # right subtree recursively
    root.right = make_balanced_bst(data, mid+1, hi, root)
    return(root)

users = database.users
data = [(user.username, user) for user in users]
print(data)

new_tree = make_balanced_bst(data)
display_keys(new_tree)


'''Making unbalanced tree balanced'''
def balance_bst(node):
    inorder_traversal = list_all(node)
    balanced_bst = make_balanced_bst(inorder_traversal)
    return(balanced_bst)

tree3 = balance_bst(tree2)
print(is_balanced(tree3))













