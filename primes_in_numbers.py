"""Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)""""

from collections import Counter

def spike_prime_factors(n):
    # ensure n is a positive integer above 1
    # get list of primes below n in size
    # find smallest prime factor of n
    # add to counter
    # divide n by smallest prime factor
    # repeat until n is 1
    
    assert n > 1 and type(n) == int
        
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 
                29, 31, 37, 41, 43, 47, 53, 59, 
                61, 67, 71, 73, 79, 83, 89, 97]
                
    prime_factors = Counter()

    while n > 1:
        for prime in primes:
            if n % prime == 0:
                prime_factors[prime] += 1
                n = n // prime
                break
                
    output_string = ""

    ordered_counter_tuples = sorted(prime_factors.items())
    for prime, frequency in ordered_counter_tuples:
        if frequency == 1:
            output_string += f"({prime})"
        else:
            output_string += f"({prime}**{frequency})"
            
    return output_string
    
    
def prime_factors(n):
    
    factors = Counter()
    prime = 2 # smallest prime number 
    
    while prime * prime <= n: # if prime squared is greater than n, then any larger factors are composite
        if n % prime # if n is not fully divisible by prime, increment prime
            prime += 1
        else:
            factors[prime] += 1 # if n is divisible by prime, divide n by prime and increment prime
            n //= prime # divide n by prime
    
    if n > 1:
        factors[n] += 1 # if n is not 1, then it is prime

    output_string = ""

    ordered_counter_tuples = sorted(factors.items())
    for prime, frequency in ordered_counter_tuples:
        if frequency == 1:
            output_string += f"({prime})"
        else:
            output_string += f"({prime}**{frequency})"
            
    return output_string

        