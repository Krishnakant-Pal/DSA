class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
    
        # Initialize the list to track the primes
        prime = [True] * n
        # 0 and 1 are non prime
        prime[0] = prime[1] = False 

        # Implement the Seive of Eratosthenes
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
    
        # Return the counts of prime
        return sum(prime)
        
            