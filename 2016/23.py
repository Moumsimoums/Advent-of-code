from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def is_num(s: str):
    try:
        int(s)
    except:
        return False
    return True

def getval(regs: dict, x: str):
    if is_num(x):
        return int(x)
    else:
        return regs[x]

def toggle(instruction: list):
    sp = instruction.split(" ")
    move = sp[0]
    if move == "inc":
        return " ".join(["dec"] + sp[1:])
    elif move in ["dec", "tgl"]:
        return " ".join(["inc"] + sp[1:])
    elif move == "jnz":
        return " ".join(["cpy"] + sp[1:])
    elif move == "cpy":
        return " ".join(["jnz"] + sp[1:])
    else:
        assert False

def part1(scheme: list, first_input: int):
    it, register = 0, {'a': first_input, 'b': 0, 'c': 0, 'd': 0}
    while it in range(len(scheme)):
        instruction = scheme[it].split()
        if instruction[0] == "cpy":
            val_to_copy = getval(register, instruction[1])
            register[instruction[2]] = val_to_copy
            it += 1
        elif instruction[0] == "inc":
            register[instruction[1]] += 1
            it += 1
        elif instruction[0] == "dec":
            register[instruction[1]] -= 1
            it += 1
        elif instruction[0] == "jnz":
            val_to_test, val_to_jump = getval(register, instruction[1]), getval(register, instruction[2])
            if val_to_test:
                it += val_to_jump
            else:
                it += 1
        elif instruction[0] == "tgl":
            line_to_toggle = it + getval(register, instruction[1])
            if line_to_toggle in range(len(scheme)):
                scheme[line_to_toggle] = toggle(scheme[line_to_toggle])
            it += 1
        print(register)
    return register['a']


class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme[:], 7)
    print(f"Part 1: {p1}")
    p2 = part1(scheme[:], 12)
    print(f"Part 2: {p2}")
    print(time()-a)

