# Checking whether the Binary Tree is Complete


   
    class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isCompleteBT(root):
       # Base Case: An empty tree is complete Binary tree
       if root is None:
           return True
        # Create an empty queue
        queue = []
        # Create a flag variable which will be set True when a non-full node is seen
        flag = False

        # Do level order traversal using queue
        queue.append(root)
        while (len(queue) > 0):
            tempNode = queue.pop(0)  # Dequeue
            # Check if left child is present
            if (tempNode.left):
                 # If we have seen a non-full node, and we see a node with non-empty left child, then the given tree is not a complete binary tree
                 
                 if flag == True:
                     return False
                # Enqueue left child
                queue.append(tempNode.left)
                
          # If this a non-full node, set the flag as true
          else:
            flag = True

        # Check if right child is present
        if (tempNode.right):

            # If we have seen a non full node, and we see a node with non-empty right child, then the given tree is not a complete BT
            if flag == True:
                return False
            # Enqueue right child
            queue.append(tempNode.right)
        # If this is non-full node, set the flag as True
        else:
            flag = True
    # If we reach here, then the tree is complete BT
    return True
