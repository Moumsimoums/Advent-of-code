from time import time
import math
import unittest
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

def sequence(num: int):
    return num / 2 if num % 2 == 0 else 3 * num + 1

def chain_length(num: int):
    length = 1
    while num != 1:
        num = sequence(num)
        length += 1

    return length


class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    max_length, starting_number = 1, 1
    for it in range(1, 1000000):
        it_length = chain_length(it)
        if it_length > max_length:
            max_length, starting_number = it_length, it
    print(f"The answer is {starting_number}")
    print(time()-a)

