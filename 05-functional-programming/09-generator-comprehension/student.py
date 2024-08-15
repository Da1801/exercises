def is_prime(n):
    return all((n % k != 0 for k in range(2,n))) and n >= 2


def primes():
    n = 2

    while True:
        if is_prime(n):
            yield n
        n += 1