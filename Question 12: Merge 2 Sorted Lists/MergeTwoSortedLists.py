import timeit

#iterative approach
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
    result = merged + nums1_tail + nums2_tail
    return result


# compute binary search time
def time_complexity_calc():
    SETUP_CODE = '''print("imports here")'''

    TEST_CODE = '''
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
    result = merged + nums1_tail + nums2_tail
    return result
   
list1 = list(range(3,10000))
list2 = list(range(40,8090))
merge_sorted_lists(list1, list2)
    '''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=1,
                          number=10000)

    # printing minimum exec. time
    print('Algorithm time execution: {}'.format(min(times)))

time_complexity_calc()

#print(merge_sorted_lists([1,2,3,4,7,8,9], [6,8,90,100]))
