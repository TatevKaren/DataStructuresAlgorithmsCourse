# Step 1: State the Problem
# Inputs
# 1: list already rotated

# Outputs
# 1: original sorted list (ascending: increasing order)
# 2: min number rotations
# should have complexity of O(logN) -> binary search
# all number in the list are unique

# Step 2: Edge Cases and Examples
tests = []

#--------------- Test Case 1 ---------------#
# empty list
tests.append({
    'input':[],
    'output': -1
})

#--------------- Test Case 2 ---------------#
# list with single element
tests.append({
    'input':[1],
    'output': 0
})

#--------------- Test Case 3 ---------------#
tests.append({
    'input':[5,6,9,0,2,3,4],
    'output': 3
})

#--------------- Test Case 4 ---------------#
tests.append({
    'input':[5,6,9,10,12,13,24,50,75,100,0,2,3,4],
    'output': 10
})

#--------------- Test Case 5 ---------------#
# list was rotated just once
tests.append({
    'input':[4,1,3],
    'output': 1
})

#--------------- Test Case 6 ---------------#
# list was not rotated at all
tests.append({
    'input':[1,2,3,4],
    'output': 0
})
#--------------- Test Case 7 ---------------#
# list was rotated n-1 times
tests.append({
    'input':[4,3,2,1],
    'output': 3
})




def findMin(nums):
        if len(nums) == 1:
            return nums[0]
        lo, hi = 0, len(nums) - 1
        if nums[hi] > nums[0]:
            return nums[0]
        while hi >= lo:
            # Find the mid element
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                lo = mid + 1
            else:
                hi = mid - 1















