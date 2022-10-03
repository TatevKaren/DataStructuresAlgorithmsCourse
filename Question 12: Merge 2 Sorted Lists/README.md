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

