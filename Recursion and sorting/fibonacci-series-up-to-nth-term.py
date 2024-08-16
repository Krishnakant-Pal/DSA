class Solution:
    def series(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        res = self.series(n-1) + self.series(n-2)
        return res