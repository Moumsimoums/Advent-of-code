from time import time
import unittest
import math
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
    for i in range(1, int(math.sqrt(n) + 1)):
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
    it,triangle_number  = 1, 1
    while get_divisors_amount(triangle_number) < 499:
        it += 1
        triangle_number += it
    print(f"The answer is {triangle_number}")
    print(time()-a)

