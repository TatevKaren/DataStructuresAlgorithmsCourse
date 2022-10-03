def MergeSort(nums):
    nums = list(nums)
    N = len(nums)
    # 0: function for merging two sorted lists
    def merge_sorted_lists(nums1, nums2):
        # empty list to store results
        merged = []
        # pointers for the smallest elements of the list not yet visited
        i, j = 0, 0
        N1, N2 = len(nums1), len(nums2)
        # loop through the two lists
        while i < N1 and j < N2:
            # inserting the smaller element in the result and move to next smallest element
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        # get the remaining parts (of these lists is going to be empty)
        nums1_tail = nums1[i:]
        nums2_tail = nums2[j:]
        result = merged + nums1_tail + nums2_tail
        return result

    # 1: terminating condition
    if N <=1:
        return nums

    # 2: Splitting the list into roughly two parts
    mid_index = N //2
    left = nums[:mid_index]
    right = nums[mid_index:]

    # 3: sorting left and right lists reccrusively
    left_sorted, right_sorted = MergeSort(left), MergeSort(right)
    # 4: combining the sorted left & right lists
    sorted_nums = merge_sorted_lists(left_sorted, right_sorted)
    return sorted_nums

print(MergeSort([2,3,4,5,7,10,2,3]))