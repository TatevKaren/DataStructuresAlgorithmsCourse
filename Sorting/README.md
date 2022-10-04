# Sorting

## Bubble Sort
Buble sort is a simple way of sorting unsrted lists. The idea behind it is to go though each element of the list and compare it to its right next element and swap it if this left element is larger than its next element. The process is inefficient and has high time complexity O(n^2) because this process (for loop and swapping) needs to happen N times. So, we have two forloops.

    def bubble_sort(nums):
      # copying the list to avoid changing it
      nums = list(nums)
      N = len(nums)
      # repeat the swapping process N-1
      for k in range(N-1):
        # iterate over each element in the list except the last one
        for i in range(N-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

![bubble-short](https://user-images.githubusercontent.com/76843403/193773764-e1d21f32-6aac-4862-8763-7f511ae3c74a.png)

    
## Insertion Sort
Insertion Sorting is more optimal than Bubble Sort, and the idea behind it is to start from left and find the correct position of the element while keeping the initial portion of the list that is sorted. One by one we sort the rest of the elements of the list. Per element we are interested in the turning position where this element is larger than its left predecessor. Because this means that this element is larger than the rest of all the left already sorted elements. In this position is where we insert this element. 

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
     
 
![insertionsort](https://user-images.githubusercontent.com/76843403/193775053-b6a505e7-6600-492b-9e3f-13701be91d28.png)



## Devide and Conquer: Merge Sort
The idea behind Merge Sort is to devide the list into roughly two parts, sort them recursively and merge them back.
### Merging two sorted lists
In order to perform Merge Sort, we need to first know how to merge two sorted lists. 
- 1: check for the terminating conditions (one of the lists empty, or both)
- 2: keep track of the position of the elements we want to compare pairwise i, j
- 3: While loop to compare the smallest elements and append the smallest of the two to result array (Incremenet the pointer for the next comparison)
- 4: Add to the merged list the remaining elements of thw two lists
 
            def merge_two_sorted_lists(nums1, nums2):
                N1, N2 = len(nums1), len(nums2)
                result = []
                if N1 == 0 and N2 != 0:
                      return nums2
                elif N1 != 0 and N2 == 0:
                      return nums1
                elif N1 == 0 and N2== 0:
                      return []
                else:
                     i, j = 0, 0
                     # inserting the smaller element in the result and move to next smallest element
                     while i < N1 and j <N2:
                          if nums1[i] <= nums2[j]:
                              result.append(nums1[i])
                              i += 1
                          elif:
                              result.append(nums2[j])
                              j += 1
                      # get the remaining parts (of these lists is going to be empty)
                      nums1_tail = nums1[i:]
                      nums2_tail = nums2[j:]
                      return result + nums1_tail +nums2_tail


### Merge Sort

- 1: If the input list is empty or contains just one element, it is already sorted. Return it
- 2: If not, divide the list of numbers into roughly equal parts
- 3: Sort each part recursively using the merge sort algorithm to get back two sorted lists
- 4: Merge two sorted lists to get a single sorted list


    def MergeSort(nums):
        nums = list(nums)
        N = len(nums)
        
        # 1: terminating condition
        if N <=1:
            return nums

        # 2: Splitting the list into roughly two parts
        mid_index = N //2
        left = nums[:mid_index]
        right = nums[mid_index:]

        # 3: sorting left and right lists reccrusively
        left_sorted, right_sorted = MergeSort(left), MergeSort(right)
        # 4: combining the sorted left & right lists
        sorted_nums = merge_sorted_lists(left_sorted, right_sorted)
        return sorted_nums

![1*nbyUbRHdgL-Ur5YayV1FJw](https://user-images.githubusercontent.com/76843403/193786939-3b99c92c-d2f3-46da-ac41-241a11efd782.png)

