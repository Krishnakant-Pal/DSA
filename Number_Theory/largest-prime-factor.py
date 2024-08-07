class Solution:
    def largestPrimeFactor (self, N):
        # Creating sieve
        sieve = [True for i in range(N+1)]
        sieve[0] = sieve[1] = False

        for i in range(int(N**0.5)+1):
            if sieve[i] == True:
                for j in range(i*i,N+1,i):
                    sieve[j] = False
        largest = 0
        
        # fiding the largest factor
        if sieve[N] == True:
            return N
            
        for i in range(N):
            if sieve[i] == True:
                if N %i == 0:
                    largest = i
        return largest