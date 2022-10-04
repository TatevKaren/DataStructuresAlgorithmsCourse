     class Notebook:
       def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

       def __repr__(self):
        return 'Notebook "< {} / {}", {} likes >'.format(self.title, self.username, self.likes)

      
      
     def notebook_comparison_decreasing(obj1, obj2):
         #if notebook 1 has more likes, it should come first
         if obj1.likes > obj2.likes:
             return 'higher'
         elif obj1.likes == obj2.likes:
             return 'equal'
         #if notebook 1 has less likes, it should come later
         elif obj1.likes < obj2.likes:
             return 'lower'

       
      def merge_two_sorted_lists(obj1, obj2):
        N1, N2 = len(obj1), len(obj2)
        result = []
        i, j = 0,0
        res = notebook_comparison_decreasing(obj1, obj2)
        while  i < N1 and j < N2:
            if res == 'higher' or res == 'equal':
                result.append(obj1[i])
                i += 1
            else:
                result.append(obj2[j])
                j+=1
        return result + obj1[i:] + obj2[j:]
        
        
      def mergeSort_notebook(notebooks):
          N = len(notebooks)
          if N <=1:
              return notebooks
          mid = N // 2
          left, right = notebooks[:mid], notebooks[mid:]
          left_sorted, right_sorted = mergeSort_notebook(left), mergeSort_notebook(right)
          return merge_two_sorted_lists(left_sorted, right_sorted)

print(mergeSort_notebook(notebooks))
