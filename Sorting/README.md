# Sorting

## Bubble Sort
Buble sort is a simple way of sorting unsrted lists. The idea behind it is to go though each element of the list and compare it to its right next element and swap it if this left element is larger than its next element. The process is inefficient and has high time complexity O(n^2) because this process (for loop and swapping) needs to happen N times. So, we have two forloops.

    def bubble_sort(nums):
      # copying the list to avoid changing it
      nums = list(nums)
      N = len(nums)
      # repeat the swapping process N-1
      for k in range(N-1):
        # iterate over each element in the list except the last one
        for i in range(N-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums
    
## Insertion Sort
    def InsertionSort(nums):
       # copying the list to not lose it during switcches
       nums = list(nums)
       N = len(nums)
       # looping through each element 
       for i in range(N):
         # remove the current element from the list
         current = nums.pop(i)
         # getting the left elements index
         j = i-1
         # while the index is existing and current value is larger than the left predesccesorwe continue looking left
         while j>=0 and nums[j] > current:
              j-=1
         # inserting the current value right next to the element smaller than current value
         nums.insert(j+1, current)
     return(nums)


## Devide and Conquer: Merge Sort

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

   
