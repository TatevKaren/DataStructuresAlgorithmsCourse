import random
def QuickSort(nums, start = 0, end= None):
    N = len(nums)
    if N<=1:
        return nums
    
    def partition(nums, start = 0, end = None):
        if end is None:
            end = N-1
        # Initialize right and left pointers
        l,r = start, end-1
        # Iterate while they're apart
        while r > l:
            # Increment left pointer if number is less or equal to pivot
            if nums[l] <= nums[end]:
                l += 1
            # Decrement right pointer if number is greater than pivot
            elif nums[r] > nums[end]:
                r -= 1
            # Two out-of-place elements found, swap them
            else:
                nums[l], nums[r] = nums[r], nums[l]
        # place pivot between the two parts
        if nums[l] > nums[end]:
            nums[l], nums[end] = nums[end], nums[l]
            return l
        else:
            return end

    if end is None:
        # comping the list to not loos elements
        nums = list(nums)
        end = N-1
    # position of the partition element
    pivot = partition(nums, start, end)
    # recursively quicksort left and right sides
    QuickSort(nums, start, pivot-1)
    QuickSort(nums, pivot+1, end)
    return nums

QuickSort([9,-3,5,2,6,8,-6,1,3])