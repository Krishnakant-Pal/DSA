class Solution:
    
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(1,n):
            temp = alist[i]
            j = i -1
            while j >= 0:
                if alist[j] > temp:
                    alist[j+1] = alist[j]
                    alist[j] = temp
                else:
                    break
                j-=1
        return alist
        