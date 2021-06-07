import math_func_rs
from random import random
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


def pi_schnee(anz_flocken: int) -> float:
    radius = 1
    im_kreis = 0
    for _ in range(anz_flocken):
        x, y = (random() * 2) - radius, (random() * 2) - radius
        if x ** 2 + y ** 2 < radius ** 2:
            im_kreis += 1
    return (2 * radius) ** 2 / (anz_flocken / im_kreis)


nr = 10000
pi_nr = 10000000
print(math_func_rs.sieve(nr))
print(sieve_of_eratosthenes(nr))
t_rs = timeit.timeit(lambda: math_func_rs.sieve(max_nr=nr), number=1000)
print(f'Zeit Rust-Lib: {t_rs}')
t_py = timeit.timeit(lambda: sieve_of_eratosthenes(nr), number=1000)
print(f'Zeit pure Python: {t_py}')
print('-' * 40)
print(f'The Rust-Extension is about {t_py/t_rs:.2f} times faster!')
print('#' * 40)
print(f'Pi with Rust-Extension: {math_func_rs.pi_schnee(pi_nr)}')
print(f'Pi in Pure Python:      {pi_schnee(pi_nr)}')
t_rs = timeit.timeit(lambda: math_func_rs.pi_schnee(pi_nr), number=1)
print(f'Zeit Rust-Extension: {t_rs}')
t_py = timeit.timeit(lambda: pi_schnee(pi_nr), number=1)
print(f'Zeit pure Python: {t_py}')
print('-' * 40)
print(f'The Rust-Extension is about {t_py/t_rs:.2f} times faster!')

print(f'The GgT of the Numbers [210, 63, 28, 42, 84] is: {math_func_rs.find_multi_ggt([210, 63, 28, 42, 84])}')
