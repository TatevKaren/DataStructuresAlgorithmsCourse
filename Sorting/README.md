# Sorting

## Bubble Sort
    def bubble_sort(nums):
      # duplicating the list to avoid changing it
      nums = list(nums)
      N = len(nums)
      # repeat the swapping pprocess N-1
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

