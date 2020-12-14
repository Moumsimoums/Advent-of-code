from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        arrivalTime, busList = f.readlines()
        arrivalTime = int(arrivalTime.strip())        
        busList = busList.split(',')
        return arrivalTime, busList

def findGapBetweenTwoMaxes(max1: int, max2: int, max3: int, gap1: int, gap2: int, gap3: int):
    m, n, p, found = 1, 1, 1, 0
    while True:
        if max1*m - max2*n == gap1 - gap2:
            if (max1*m - gap1 + gap3) % max3 == 0:
                found += 1
                p = (max1*m - gap1 + gap3) // max3 + 1                 
                if found == 1:
                    found1 = max1*m
                if found == 2:
                    return max1*m - found1, found1
            m += 1
            n += 1
        elif max1*m - max2*n > gap1 - gap2:
            n += 1 
        else:
            m += 1

            
def part1(arrivalTime: int, busList: list):
    offset = 0
    while True:
        for bus in busList:
            if (arrivalTime + offset) % bus == 0:               
                return bus * offset
        offset += 1

def part2(busList: list):
    orderBusDict = {int(v):k for k, v in enumerate(busList) if v.isdigit()}
    sortedBusIds = sorted(orderBusDict.keys(), reverse=True)
    max1, max2, max3 = sortedBusIds[:3]
    gap1 = orderBusDict[max1]
    it, start = findGapBetweenTwoMaxes(max1, max2, max3, gap1, orderBusDict[max2], orderBusDict[max3])
    del orderBusDict[max1]
    del orderBusDict[max2]
    del orderBusDict[max3]
    res = False
    while not res:
        print(start)
        for busId in orderBusDict:
            if (start - gap1 + orderBusDict[busId]) % busId == 0:
                res = True
            else:
                res = False
                break
        if res:
            return start - gap1
        else:
            start += it


class Tests(unittest.TestCase):

    def testP2(self):
        self.assertEqual(part2(['1789','37','47','1889']), 1202161486)


if __name__ == "__main__":
    # unittest.main()
    arrivalTime, busList = readFile()
    p1 = part1(arrivalTime, [int(i) for i in busList if i.isdigit()])
    print(f"Part 1: {p1}")
    p2 = part2(busList)
    print(f"Part 2: {p2}")
    print(time()-a)

