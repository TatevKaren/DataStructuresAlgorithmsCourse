# Finding Longest Common Subsequence

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



<img width="1356" alt="Screenshot 2022-10-05 at 6 00 03 PM" src="https://user-images.githubusercontent.com/76843403/194112907-d3936d45-873b-4a0f-a0fd-4301791bbc9a.png">
