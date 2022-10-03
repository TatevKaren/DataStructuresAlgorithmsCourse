# we keep the initial portion of the array ssorted and insert the remaining elements one by one at the right position
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


def evaluate_test_cases(tests, function):
        for i in range(len(tests)):
            result = function(tests[i]["input"]["nums"]) == tests[i]["output"]
            if result == True:
                print("Test Case", i, "PASSED")
            else:
                print("Test Case", i, "FAILED")


test0 = {
    'input': {'nums': [4,2,6,3]
              },
    'output': [2,3,4,6]
}
test1 = {
    'input': {'nums': [3,5,7,9,11]
              },
    'output': [3,5,7,9,11]
}

test2 = {
    'input': {'nums': [11,9,7,5,3]
              },
    'output': [3,5,7,9,11]
}
test3 = {
    'input': {'nums': [11,9,1,1,1,1,7,5,5,3]
              },
    'output': [1,1,1,1,3,5,5,7,9,11]
}

test4 = {
    'input': {'nums': []
              },
    'output': []
}

test5 = {
    'input': {'nums': [24]
              },
    'output': [24]
}

test6 = {
    'input': {'nums': [42,42,42,42,42,42,42,42]
              },
    'output': [42,42,42,42,42,42,42,42]
}
import random
t = list(range(10000))
random.shuffle(t)
test7 = {
    'input': {'nums':t},
    'output': list(range(10000))
}

tests = [test0,test1,test2,test3,test4,test5, test6, test7]
evaluate_test_cases(tests, InsertionSort)
