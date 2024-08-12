class Solution:
    def evenlyDivides (self, N):
        count = 0
        n = N
        while n:
            digit = n % 10
            if  digit > 0 and N % digit ==0 :
                count +=1
            n = n//10
        return count