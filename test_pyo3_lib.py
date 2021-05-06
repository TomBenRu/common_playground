import math_func_rs
import timeit


def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    res = []
    for p in range(n + 1):
        if prime[p]:
            res.append(p)
    return res


nr = 10000
print(math_func_rs.sieve(nr))
print(sieve_of_eratosthenes(nr))
t_rs = timeit.timeit(lambda: math_func_rs.sieve(max_nr=nr), number=1000)
print(f'Zeit Rust-Lib: {t_rs}')
t_py = timeit.timeit(lambda: sieve_of_eratosthenes(nr), number=1000)
print(f'Zeit pure Python: {t_py}')
print('-' * 40)
print(f'The Rust-Extension is about {t_py/t_rs:.2f} times faster!')
