class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a, b)
        count, x = 0, 1
        while x * x <= g:
            if g % x == 0:
                count += 1
                count += x * x < g
            x += 1
        return count