class Solution:
    def addDigits(self, num: int) -> int:
        # base case
        if num < 10:
            return num
        # recursion
        sum1 = 0
        while num > 0:
            digit = num % 10
            sum1 += digit
            num = num//10
        return self.addDigits(sum1)