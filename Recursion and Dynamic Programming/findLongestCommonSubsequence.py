test0 = {
       "input": {"seq1": "dense",
                 "seq2": "condensed"},
       "output": 5
}
'''General Test Case with 2 strings'''
test1 = {
       "input": {"seq1": "serendipitous",
                 "seq2": "precipitation"},
       "output": 7
}
'''General Test Case with lists'''
test2 = {
        "input": {"seq1": [1,2,3,4,5,7,8],
                  "seq2":[2,3,5,9]},
       "output": 3
}
'''Test Case with No Common subsequence'''
test3 = {
       "input": {"seq1": [1,2,3,4,5,7,8],
                  "seq2":[9,10,11,34]},
       "output": 0
}
'''Test Case where one is a subsequence of the other '''
test4 = {
       "input": {"seq1": [1,2,3,4,5,7,8],
                  "seq2":[1,2,3]},
       "output": 3
}
'''Test Case where one is a empty '''
test5 = {
       "input": {"seq1": [1,2,3,4,5,7,8],
                  "seq2":''},
       "output": 0
}

'''Test Case where both sequences are empty '''
test6 = {
       "input": {"seq1": '',
                  "seq2":''},
       "output": 0
}

'''Multiple sequences with the same length '''
test7 = {
       "input": {"seq1": 'abcdef',
                  "seq2":'badcfe'},
       "output": 3
}

tests = [test0,test1,test2,test3,test4,test5, test6, test7]

def evaluate_test_cases(tests, function):
        for i in range(len(tests)):
            result = function(**tests[i]["input"]) == tests[i]["output"]
            print(tests[i])
            if result == True:
                print("Test Case", i, "PASSED")
            else:
                print("Test Case", i, "FAILED")


'''Brute Force Approach O(n^2)'''
def findLongestCommonSubsequence(seq1, seq2):
    common = []
    if seq1 is None or seq2 is None:
           return 0
    for i in seq1:
           for j in seq2:
                  if i == j:
                         common.append(i)
    return common


'''Recursive Solution O(2^(N+M))'''
def findLongestCommonSubsequence(seq1, seq2, idx1= 0, idx2 = 0):
       # Base Case: if the pointers are at max leen of the sequences, we reached the max
       if idx1 == len(seq1) or idx2 == len(seq2):
              return 0
       elif seq1[idx1] == seq2[idx2]:
              '''when common element found'''
              # if the previous common elementss --> increment the common elements
              return 1 + findLongestCommonSubsequence(seq1, seq2, idx1+1, idx2+1)
       else:
              '''when no common element found'''
              '''Option 1: the left element in seq1 is not common'''
              option1 = findLongestCommonSubsequence(seq1,seq2, idx1+1, idx2)
              '''Option 2: the left element in seq2 is not common'''
              option2 = findLongestCommonSubsequence(seq1,seq2, idx1, idx2+1)
              return max(option1, option2)

print(findLongestCommonSubsequence([1,2,3,4], [3,4,9]))
evaluate_test_cases(tests, findLongestCommonSubsequence)
