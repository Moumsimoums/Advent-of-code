from time import time
from hashlib import md5
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline()


def part1(scheme: str):
    comp, indexes = 0, list()
    while len(indexes) != 64:
        currentHash = md5(scheme + str(comp).encode('utf-8')).hexdigest()
    return scheme

def part2(scheme: list):
    return 4

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

