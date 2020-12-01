from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i.strip()) for i in f.readlines()]

            
def part1(scheme: list):
    sumGoal, tempSum = 2020, False
    while not tempSum:
        currentNumber = scheme.pop()
        if sumGoal - currentNumber in scheme:
            tempSum = True
    return currentNumber * (sumGoal - currentNumber)

def part2(scheme: list):
    return 0

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = [1721,979,366,299,675,1456]
        self.assertEqual(part1(testInput), 514579)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

