#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number
# we need to look at left and we need to change the upper hi level
# we need to look at the right and we need to check the lower lo level

def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def first_position(nums,target):
    def condition(mid_index):
        # if we have found the solution: check whether there is one in the left?
        if nums[mid_index] == target:
            # if there is an item in the left and this left value is again the target
            if mid_index > 0 and nums[mid_index - 1] == target:
                return 'left'
            return 'found'
        elif nums[mid_index] < target:
            return 'right'
        else:
            return 'left'
    return(binary_search(0,len(nums)-1,condition))

def last_position(nums,given_value):
    def condition(mid_index):
        # if we have found the solution: check whether there is one in the right?
        if nums[mid_index] == given_value:
            # if there is an item in the right and this right value is again the target
            if mid_index < len(nums)-1 and nums[mid_index + 1] == given_value:
                return 'right'
            return 'found'
        elif nums[mid_index] < given_value:
            return 'right'
        else:
            return 'left'
    return(binary_search(0,len(nums)-1,condition))

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)
tests = []
tests.append({"input": {
    'nums': [5,7,7,8,8,10],
    'target': 8},
    'output': [3,4]
})

print(first_and_last_position(**tests[0]["input"]))





