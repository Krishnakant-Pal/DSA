class Solution:
    def countSquares(self, N):
        # code here
        sqrt = int(N**0.5)
        if sqrt*sqrt == N:
            return int(N**0.5) -1
        return int(N**0.5)