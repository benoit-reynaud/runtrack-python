primes = []
for num in range (2,1001):
    
    is_prime = True
    
    for i in range (2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
        
print(primes)


#Solution 2 Crible d'Eratosthène
sieve = [True] * 1001
sieve[0] = sieve[1] = False
primes = []

for i in range(2, 1001):
    if sieve[i]:
        primes.append(i)
        for j in range(i*i, 1001, i):
            sieve[j] = False

print(primes)