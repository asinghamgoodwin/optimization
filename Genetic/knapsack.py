# defining the knapsack problem, making some example data

# there are a bunch of items, each with a weight and a value
# we want to pack a knapsack of fixed weight capacity
# with the maximum combined values of items

import random

# GLOBAL VARIABLES
CAPACITY = 6404180
ITEMS = {0 : ( 382745 , 825594),
       1 : ( 799601 , 1677009),
       2 : ( 909247 , 1676628),
       3 : ( 729069 , 1523970),
       4 : ( 467902 , 943972),
       5 : ( 44328 , 97426),
       6 : ( 34610 , 69666),
       7 : ( 698150 , 1296457),
       8 : ( 823460 , 1679693),
       9 : ( 903959 , 1902996), 
       10 : ( 853665 , 1844992),
       11 : ( 551830 , 1049289),
       12 : ( 610856 , 1252836),
       13 : ( 670702 , 1319836),
       14 : ( 488960 , 953277),
       15 : ( 951111 , 2067538),
       16 : ( 323046 , 675367),
       17 : ( 446298 , 853655),
       18 : ( 931161 , 1826027),
       19 : ( 31385 , 65731),
       20 : ( 496951 , 901489),
       21 : ( 264724 , 577243),
       22 : ( 224916 , 466257),
       23 : ( 169684 , 369261) } #key: index, value: (weight, value)

# candidate = "010101100101..." where 1 means that item is included
bitstringList = []
def generateRandomBitString(length):
    bitstring = ""
    for i in range(length):
        bitstring = bitstring + str(random.randint(0,1))
    return bitstring
for i in range(10):
    bitstringList.append(generateRandomBitString(24))

class Candidate():
    def __init__(self, bitstring):
        self.bitstring = bitstring
        self.items = ITEMS
        self.weight = self.totalWeight()
        self.isValid = (self.weight <= CAPACITY)
        self.fitness = 0 if not self.isValid else self.totalValue()

    def totalWeight(self):
        totalWeight = 0
        for i in range(len(self.bitstring)):
            if self.bitstring[i] == '1':
                totalWeight += self.items[i][0]
        return totalWeight

    def totalValue(self):
        totalValue = 0
        for i in range(len(self.bitstring)):
            if self.bitstring[i] == '1':
                totalValue += self.items[i][1]
        return totalValue

