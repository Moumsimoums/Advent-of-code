from time import time
from collections import defaultdict
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
            # if instruction[1].isdigit():
            #     print(instruction[1], register[instruction[2]])
            if val_to_test:
                it += val_to_jump
            else:
                it += 1
        elif instruction[0] == "tgl":
            line_to_toggle = it + getval(register, instruction[1])
            if line_to_toggle in range(len(scheme)):
                # print(line_to_toggle)
                scheme[line_to_toggle] = toggle(scheme[line_to_toggle])
            it += 1
    return register

def part2(scheme: list, first_input: int):
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
                if instruction[1].isdigit(): # Si la condition test est un nombre, alors on ne tente pas d'optimiser car les instructions bouclées sont instables dans le temps
                    it += val_to_jump
                else:
                    loop_instructions =  {sub_instruction[-1:]: sub_instruction[:3] for sub_instruction in scheme[it+val_to_jump:it]}
                    loop_moves = list(loop_instructions.values())
                    if not any(b in loop_moves for b in ['tgl', 'cpy', 'jnz']): # Cas des boucles linéaires inc dec jnz
                        repetitions = abs(register[instruction[1]])
                        for entry, sub_instruction in loop_instructions.items():
                            register[entry] += (1 if sub_instruction == 'inc' else -1) * repetitions
                        it += 1
                    else:
                        it += val_to_jump
            else:
                it += 1
        elif instruction[0] == "tgl":
            line_to_toggle = it + getval(register, instruction[1])
            if line_to_toggle in range(len(scheme)):
                scheme[line_to_toggle] = toggle(scheme[line_to_toggle])
            it += 1


    return register


class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1= part2(scheme[:], 7)
    print(f"Part 1: {p1['a']}")
    # p2, test = part2(scheme[:], 12)
    # print(test)
    # print(f"Part 2: {p2['a']}")
    print(time()-a)

