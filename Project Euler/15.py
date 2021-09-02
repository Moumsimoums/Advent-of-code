from time import time
import math
import unittest
from itertools import permutations
a = time()

def gen_primes():
    D = {}
    q = 2
    
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]       
        q += 1

def gen_divisors(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def get_divisors_amount(num):
    count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count += 2
    return count


class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    n = 20
    paths_amount = int(math.factorial(2*n)/(pow(math.factorial(n),2)))
    print(f"The answer is {paths_amount}")
    print(time()-a)

