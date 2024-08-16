class Solution:
    def printNos(self, n):
        # Code here
        #base case
        if n == 0:
            return 0
        
        print(n,end=" ")
        return self.printNos(n-1)