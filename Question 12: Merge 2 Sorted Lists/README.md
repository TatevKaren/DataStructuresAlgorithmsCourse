# Merge 2 Sorted Lists

    def merge_sorted_lists(nums1, nums2):
        # empty list to store results
        merged = []
        
        # pointers for the smallest elements of the list not yet visited
        i,j = 0,0
        N1,N2 = len(nums1), len(nums2)
        
        # loop through the two lists
        while i < N1 and j < N2:
            # inserting the smaller element in the result and move to next smallest element
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
                
        # get the remaining parts (of these lists is going to be empty)
        nums1_tail = nums1[i:]
        nums2_tail = nums2[j:]
        return(merged + nums1_tail + nums2_tail)


# Merge 2 Sorted List Nodes (objects)
Steps
- 1: create an empty ListNode where we will store the findal merged list and its tail
- 2: while L1 and L2 are non empty, we will iterate through these two list oobjects
- 3: if l1 value is smaller or equal to the l2 value, we will insert the l1 value in the tail.next and we will update the l1 (l1 = l1.next) to move to the next element
- 4: otherwise, l2 value is smaller, then we insert l2 into the tail and update the l2 (l2 = l2.next)
- 5: we update the tail (tail = tail.next)
- 6: we look at the remainings of l1 and l2, if l1 is not empty this should be added to the tail.next = l1
- 7: return the merge.next 

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


