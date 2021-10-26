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
    biggest_steps = defaultdict(int)
    it, register = 0, {'a': first_input, 'b': 0, 'c': 0, 'd': 0}
    while it in range(len(scheme)):
        biggest_steps[it+1] += 1
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
                loop_instructions = scheme[it+val_to_jump:it]
                loop_moves = [loop_instruction[:3] for loop_instruction in loop_instructions]
                if instruction[1].isdigit() or any(b in loop_moves for b in ['tgl', 'cpy', 'jnz']): # Si la condition test est un nombre, alors on ne tente pas d'optimiser car les instructions bouclées sont instables dans le temps, idem s'il y a des commandes jnz tgl ou cpy qui ne sont pas linéaires
                    it += val_to_jump
                else: # Sinon, on optimise
                    # print(instruction, it, register)
                    modif_unit, test = part2(scheme[it+val_to_jump:it], 0) # On regarde l'effet d'une itération de la boucle
                    repetitions = - val_to_test // modif_unit[instruction[1]] # On compte le nombre d'itérations de cette boucle
                    # print(modif_unit, repetitions, register)
                    register = {k: v + modif_unit[k] * repetitions for k, v in register.items()}
                    # print(register)
                    it += 1
            else:
                it += 1
        elif instruction[0] == "tgl":
            line_to_toggle = it + getval(register, instruction[1])
            if line_to_toggle in range(len(scheme)):
                scheme[line_to_toggle] = toggle(scheme[line_to_toggle])
            it += 1

        if time() - a > 3:
            break

    return register, biggest_steps


class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1= part1(scheme[:], 7)
    print(f"Part 1: {p1['a']}")
    p2, test = part2(scheme[:], 12)
    print(test)
    print(f"Part 2: {p2['a']}")
    print(time()-a)

