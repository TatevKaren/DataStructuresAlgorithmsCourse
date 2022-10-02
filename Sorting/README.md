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
