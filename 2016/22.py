from time import time
from math import inf
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return {tuple(int(pos) for pos in elem[0].replace('/dev/grid/node-x', '').replace('y', '').split('-')) : {'size': int(elem[1][:-1]), 'used': int(elem[2][:-1]), 'available': int(elem[3][:-1]), 'use': int(elem[4][:-1])} for elem in [i.strip().split() for i in f.readlines() if i.startswith('/')]}


class Tree:
    def __init__(self, firstNode):
        # Données du problème
        self.states = {firstNode.state: firstNode.value}
        # Données relatives à l'arbre
        self.bestValue = inf
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
    
    def expandTree(self):
        currentNode = self.openNodes.pop() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.value < self.bestValue: # Définir ici la condition de succès
            self.bestValue = currentNode.value
        else:
            for son in currentNode.reachableNodes(self, currentNode.value):
                if son.value < min(self.bestValue, self.states[son.state]):
                    self.states[son.state] = son.value
                    self.openNodes.append(son)


class Node:
    def __init__(self, value):
        self.value = value
        self.state = "" # Définir ici comment qualifier un noeud avec un état unique
    
    def reachableNodes(self, value):
        # Définir ici comment rechercher les prochains noeuds
        yield Node(value)

def emptiable_node(scheme: dict):
    emptiable_node_amount = 0
    for key_A, value_A in scheme.items():
        if value_A['used'] != 0:
            explorable_nodes = [tuple((key_A[0] + xDelta, key_A[1] + yDelta)) for xDelta in range(-1, 2) for yDelta in range(-1, 2) if xDelta**2 + yDelta**2 == 1 and tuple((key_A[0] + xDelta, key_A[1] + yDelta)) in scheme]
            for explorable_node in explorable_nodes:
                if value_A['used'] <= scheme[explorable_node]['available']:
                    emptiable_node_amount += 1
                    print(key_A, explorable_node)
                    break
    
    return emptiable_node_amount

class Tests(unittest.TestCase):

    def testP1(self):
        pass

def part1(scheme: dict):
    viable_pairs_amount = 0
    for key_A, value_A in scheme.items():
        if value_A['used'] != 0:
            for key_B, value_B in scheme.items():
                if key_A != key_B and value_A['used'] <= value_B['available']:
                    viable_pairs_amount += 1
    
    return viable_pairs_amount



def part2(scheme: dict):
    tree = Tree(scheme)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp
        
if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    # print(f"Part 2: {p2[0]} in {p2[1]} iterations")
    # print(time()-a)

