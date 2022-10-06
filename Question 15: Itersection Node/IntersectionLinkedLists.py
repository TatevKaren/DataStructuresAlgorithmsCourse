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


newNode = Node(10)
head1 = newNode
newNode = Node(3)
head2 = newNode
newNode = Node(6)
head2.next = newNode
newNode = Node(9)
head2.next.next = newNode
newNode = Node(15)
head1.next = newNode
head2.next.next.next = newNode
newNode = Node(30)
head1.next.next = newNode

print(head1, head2)
print(getIntersectionNode(head1, head2))


