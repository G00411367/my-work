# generate primes

primes = []
upto = 100
for candidate in range(2, upto):
    # print (candidate)
    isPrime = True
    # only need to check if divisible by prime
    for devisor in primes:
        if (candidate % devisor == 0):
            isPrime = False
            # so there is no reason to keep checking
            break
    
    if isPrime:
        primes.append(candidate)

    print(primes)