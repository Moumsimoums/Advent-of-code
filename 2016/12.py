from time import time
from collections import defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def treatInstruction(registers, indix, scheme):
    instruction = scheme[indix].split()
    if instruction[0] == "cpy":
        if instruction[1].isdigit():
            registers[instruction[2]] = int(instruction[1])
        else:
            registers[instruction[2]] = registers[instruction[1]]
        indix += 1
    elif instruction[0] == "inc":
        registers[instruction[1]] += 1
        indix += 1
    elif instruction[0] == "dec":
        registers[instruction[1]] -= 1
        indix += 1
    elif instruction[0] == "jnz":
        if instruction[1].isdigit() and instruction[1] != '0':
            indix += int(instruction[2])
        elif not instruction[1].isdigit() and registers[instruction[1]] != 0:
            indix += int(instruction[2])
        else:
            indix += 1
    return registers, indix
            
def part1(scheme: list):
    indix = 0
    registers = defaultdict(int)
    while indix < len(scheme):
        registers, indix = treatInstruction(registers, indix, scheme)
    return registers['a']

def part2(scheme: list):
    indix = 0
    registers = defaultdict(int)
    registers['c'] = 1
    while indix < len(scheme):
        registers, indix = treatInstruction(registers, indix, scheme)
    return registers['a']

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

