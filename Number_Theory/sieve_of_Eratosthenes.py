
def create_sieve(n):
    sieve = [True for i in range(n+1)]
    sieve[0] = sieve[1] = False

    for i in range(int(n**0.5)):
        if sieve[i] == True:
            for i in range(i*i,n,i):
                sieve[i] = False
    return sieve

def is_prime(n):
    return create_sieve(n)[n]

def give_prime(n):
    sieve = create_sieve(n)
    for i in range(n):
        if sieve[i] == True:
            print(i,end=",")

# give_prime(10)


def largest_prime(n):
    sieve = [True for i in range(n+1)]
    sieve[0] = sieve[1] = False

    for i in range(int(n**0.5)+1):
        if sieve[i] == True:
            for j in range(i*i,n+1,i):
                sieve[j] = False
    largest = 0
    print(sieve)
    if sieve[n] == True:
            return n
    for i in range(n):
        if sieve[i] == True:
            print(largest)
            if n %i == 0:
                largest = i
        
    return largest


print(largest_prime(8))