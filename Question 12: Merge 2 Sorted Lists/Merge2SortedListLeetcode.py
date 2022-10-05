class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> [ListNode]:
            # creating empty list
            merge = ListNode()
            tail = merge
            # while both lists are not empty and existing
            while l1 and l2:
                if l1.val <= l2.val:
                    # taking the smallest value and insert it in the list
                    tail.next = l1
                    # we need to update the pointer, on to the next element and remove from l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    # update the pointer
                    l2 = l2.next
                tail = tail.next
            # remainings of one of the two lists
            if l1 is not None:
                tail.next = l1
            elif l2 is not None:
                tail.next = l2
            return merge.next

list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))

print(Solution.mergeTwoLists(list1, list2))
