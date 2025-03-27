
def sum_of_all_primes_below(limit):
    

    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False # 0 and 1 are not prime numbers

    # Sieve of Eratosthenes
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    #calulate the sum of all prime numbers
    sum_of_primes = 0
    for i in range(2, limit):
        if is_prime[i]:
            sum_of_primes += i  
    
    return sum_of_primes    



limit = 20
sum_of_prime = sum_of_all_primes_below(limit)
print(f'The sum of all primes below {limit} is:{sum_of_prime}') # 142913828922
