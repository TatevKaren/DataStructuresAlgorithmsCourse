import math
'''QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing
order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card
containing a given number by turning over as few cards as possible. Write a function to help Bob locate
the card.'''



tests =[]
#----------------------------- Test Case 1 ---------------------------#
# creating test case, which will be represented as dictionaries
# given card at the middle
tests.append({
    'input': {
         'card_list': [13,11,10,7,4,3,1,0],
         'given_card': 1
    },
    'output': 6
})
#----------------------------- Test Case 2 ---------------------------#
# given card at the beginning
tests.append({
    'input': {
         'card_list': [13,11,10,7,4,3,1,0],
         'given_card': 13
    },
    'output': 0
})
#----------------------------- Test Case 3 ---------------------------#
# given card at the end (last element)
tests.append({
    'input': {
         'card_list': [13,11,10,7,4,3,1,0],
         'given_card': 0
    },
    'output': 7
})
#----------------------------- Test Case 4 ---------------------------#
# card list is just 1 element and it is the given card
tests.append({
    'input': {
         'card_list': [-213],
         'given_card': -213
    },
    'output': 0
})

#----------------------------- Test Case 5 ---------------------------#
# card list is just 1 element and it is not the given card
tests.append({
    'input': {
         'card_list': [20,19,17,14,-3],
         'given_card': 3
    },
    'output': -1
})
# here we make an assumtion that if the array is empty --> return -1


#----------------------------- Test Case 6 ---------------------------#
# card list is empty
tests.append({
    "input":{
         'card_list': [],
         'given_card': 9
    },
    "output": -1

})

# ----------------------------- Test Case 7 ---------------------------#
# the given card appears in the one position but there are other repetitions
tests.append({
    "input": {
        'card_list': [8,8,7,7,7,6,3,2,1,0,0,0],
        'given_card': 6
    },
    "output": 5

})
# ----------------------------- Test Case 8 ---------------------------#
# the given card appears in the multiple position and there are other repetitions
tests.append({
    "input": {
        'card_list': [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0],
        'given_card': 6
    },
    "output": 2

})


print("-------Brute Force Approach-------")
def locate_card(card_list, given_card):
    position  = 0
    while position < len(card_list):
        # while picked card in this position matches the given card
        if card_list[position] == given_card:
            return position
        print("position: ", position)
        # otherwise increase the position to go back and check teh next card
        position+=1
    return -1

print("Number of Test Cases: ", len(tests))
for i in range(len(tests)):
    print(tests[i])
    if (locate_card(**tests[i]["input"]) == tests[i]["output"]):
        print("PASSED")
    else:
        print("ERROR: Test Case", i, "failed")


print("-------Binary Search Approach-------")
# Given that the list is ordered, we can look at the middle element, compare with the target if not right elimiate
# In this way we elimiate the second half that is not suitable and avoid spending time on that part
def locate_card_ba(card_list, given_card):
    print(card_list)
    lo, hi = 0, len(card_list) - 1
    while lo <= hi:
        mid_index = (lo + hi) // 2
        # accessing the mid element from list
        mid_item = card_list[mid_index]
        print("lo: ", lo, ", hi: ", hi, ", mid index", mid_index, ", mid item", mid_item)
        # if the middle element is the given card then great
        if mid_item == given_card:
            return mid_index
        # the list is in decreasing order, then we need to check the left side of the list
        elif mid_item < given_card:
            hi = mid_index - 1  # (moving the hight to the left)
        # the list is in decreasing order, then we need to look in the right part of the list
        elif mid_item > given_card:
            lo = mid_index + 1  # (moving the start to the right)
    return -1

print("Number of Test Cases: ", len(tests))
for i in range(len(tests)):
    print(tests[i])
    if (locate_card_ba(**tests[i]["input"]) == tests[i]["output"]):
        print("PASSED")
    else:
        print("ERROR: Test Case", i, "failed")



# error when we have multiple of the same value,
# because when the query picks the correct card but that card is repetitive the previous value is also the same correct card,
# this becomes a problem since the the query has to pick the first correct element
# we therefore need a helper function for this

# defining the helper function to tell us whetehr we found the location or not
def test_location(card_list, given_card, mid_index):
    mid_item = card_list[mid_index]
    print("mid index, ", mid_index, ", mid item", mid_item)
    if mid_item == given_card:
        # if we have foud the card but it is tnot the first one in the list we need to check the left ones to find the positions of the first occurance
        # making sure the index exists and that the previous element is the same card or not
        if mid_index-1 >= 0 and card_list[mid_index-1] == given_card:
            return 'left'
        else:
            return 'found'
    # if the middle item is smaller than the given card we need to look at left
    elif mid_item < given_card:
        return 'left'
    else:
        return 'right'


def locate_card_new(card_list, given_card):
    lo, hi = 0, len(card_list) - 1
    while lo <=hi:
        mid_index = (lo+hi)//2
        result = test_location(card_list, given_card, mid_index)
        if result == 'found':
            return mid_index
        elif result == 'left':
            hi = mid_index-1
        elif result == 'right':
            lo = mid_index+1
    return -1

print("Number of Test Cases: ", len(tests))
for i in range(len(tests)):
    print(tests[i])
    if (locate_card_new(**tests[i]["input"]) == tests[i]["output"]):
        print("PASSED")
    else:
        print("ERROR: Test Case", i, "failed")


def binary_search_general(lo, hi, condition):
    ''' TO DO - add docs'''
    while lo<= hi:
       mid_index = lo + hi // 2
       mid_item = condition(mid_index)
       print("mid index, ", mid_index, "mid item, ", mid_item)
       if mid_item == 'found':
           return(mid_index)
       # we need to look at left and we need to change the upper hi level
       elif mid_item == 'left':
           hi = mid_index -1
       # we need to look at the right and we need to check the lower lo level
       elif mid_item == 'right':
           lo = mid_index +1
    # return -1 if we end up not finding the solution
    return -1


# here the condition is a helper function with 3 possible outcomes (can also be a function within a function: closure)
# 1:found, 2:left, 3:right
# to write the function without the while loop

















