from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[int(it) for it in i.strip().split()] for i in f.readlines()]

class Tree:
    def __init__(self, firstNode, int_triangle):
        # Données du problème
        self.states = defaultdict(int)
        self.states[firstNode.state] = firstNode.total
        # Données relatives à l'arbre
        self.bestValue = 0
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
        self.int_triangle = int_triangle
        self.maxRow = [max(row) for row in self.int_triangle]

    
    def expandTree(self):
        currentNode = self.openNodes.pop() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.total > self.bestValue and currentNode.row == len(self.int_triangle) - 1: # Définir ici la condition de succès
            self.bestValue = currentNode.total
        else:
            for son in currentNode.reachableNodes(self.int_triangle):
                if self.states[son.state] < son.total:
                    if son.total + sum(self.maxRow[son.row + 1:]) > self.bestValue:
                        self.states[son.state] = son.total
                        self.openNodes.append(son)


class Node:
    def __init__(self, row, column, total):
        self.row = row
        self.column = column
        self.total = total
        self.state = (row, column) # Définir ici comment qualifier un noeud avec un état unique
    
    def reachableNodes(self, int_triangle):
        # Définir ici comment rechercher les prochains noeuds
        for it in range(2):
            if self.row in range(len(int_triangle) - 1):
                yield Node(self.row + 1, self.column + it, self.total + int_triangle[self.row + 1][self.column + it])

def resolution(int_triangle: list):
    firstNode = Node(0, 0, int_triangle[0][0])
    tree = Tree(firstNode, int_triangle)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp

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
    for i in range(1, n):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(int(n / i))


def get_divisors_amount(num):
    count = 0
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            count += 2
    return count


class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    passed, amicables_sum = [], 0
    for elem in range(10001):
        if elem not in passed:
            divisors_sum = sum(gen_divisors(elem))
            if sum(gen_divisors(divisors_sum)) == elem and elem != divisors_sum:
                amicables_sum += elem + divisors_sum
            passed.append(elem)
            passed.append(divisors_sum)
    print(f"The answer is {amicables_sum}")
    print(time()-a)

