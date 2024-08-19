class Solution:
    def findTwoElement( self,arr, n):
        mis = 0
        
        arr.sort()
        for i in range(0,n):
            if i not in arr and i != 0:
                mis = i
            if arr[i] == arr[i-1] :
                rep = arr[i]
        if n not in arr:
            mis = n
        return rep,mis