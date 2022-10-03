# Sorting

## Bubble Sort
    def bubble_sort(nums):
      # duplicating the list to avoid changing it
      nums = list(nums)
      N = len(nums)
      # repreat the swapping pprocess N-1
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
       for i in range(N):
         # remove the current element from the list
         current = nums.pop(i)
         j = i-1
         # while the index is existing and previous value is larger than the current
         while j>=0 and nums[j] > current:
              j-=1
         nums.insert(j+1, current)
     return(nums)

