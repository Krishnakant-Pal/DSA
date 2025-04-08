class Solution:
    def countSquares(self, N):
        # code here
        sqrt = int(N**0.5)
        if sqrt*sqrt == N:
            return int(N**0.5) -1
        return int(N**0.5)

# Alternate approach using Binary search
class Solution:
    def countSquares(self, n):
        if n <=1:
            return 0
        low = 1
        high = n-1
        res = 0
        
        while low <=high:
            mid = (low +high)//2
            if mid * mid < n:
                res = mid
                low = mid +1
            else:
                high = mid -1
        return res
    
# Simple approach
class Solution:
    def countSquares(self, n):
        # code here 
        sqrt =  int((n**0.5 ))
        if sqrt *sqrt == n:
            return sqrt -1
        else :
            return sqrt 