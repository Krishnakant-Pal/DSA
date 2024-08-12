#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self, n):
       # palindrome checking
        def is_palindrome(number):
            n = number
            rev_num = 0
            while n > 0:
                digit = n % 10
                rev_num = rev_num * 10 + digit
                n = n//10
            if rev_num == number:
                return 1
            return 0
        # Sum of digits
        sum1 = 0
        while n > 0:
            digit  = n %10
            sum1 += digit
            n = n//10
        return is_palindrome(sum1)
            
            
