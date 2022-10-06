    class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


     # function to get the intersection point of two linked lists head1 and head
     def getIntersectionNode(headA, headB):
          # while there are elements in heaadB
          while headB:
              temp = headA
              # while head A is non empty
              while temp:
                   # if both Nodes are same: this is the eintersection node
                   if temp == headB:
                       # return this node
                       return temp
                   # if not the same go to the next element in headA
                   temp = temp.next
              # go on to the next element in headB
              headB = headB.next
              # intersection is not present between the lists
         return None
