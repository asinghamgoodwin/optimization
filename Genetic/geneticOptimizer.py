# optimize a problem that can be represented as a bitstring
import random
import knapsack

# population size
# generations to end?
# condition to fulfil?
# mutation rate
# parents per generation
# candidate representation length (?)


class Optimizer():
    def __init__(self, candidateClass, bitstringLength,
                    terminationType, terminationCondition):
        ''' terminationType should be either "generations" or "fitness"
        terminationCondition is the number of either generations or fitness goal '''

        self.bitstringLength = bitstringLength
        self.populationSize = 100
        self.mutationRate = 0.05
        self.numParents = 5
        self.candidateClass = candidateClass
        self.terminationType = terminationType
        if self.terminationType == "generations":
            self.generations = terminationCondition
        elif self.terminationType == "fitness":
            self.fitnessGoal = terminationCondition
        self.solutionFound = False
        self.bestSolution = ""

        self.currentPopulation = self.initialPopulation()

    def generateRandomBitString(self):
        bitstring = ""
        for i in range(self.bitstringLength):
            bitstring = bitstring + str(random.randint(0,1))
        return bitstring

    def initialPopulation(self):
        population = [self.candidateClass(self.generateRandomBitString())
                        for i in range(self.populationSize)]
        return population

    def pickParents(self):
        potentialParents = self.currentPopulation[:]
        parents = []
        for i in range(self.numParents):
            newParent = (max(potentialParents, key=lambda cand:cand.fitness))
            potentialParents.remove(newParent)
            parents.append(newParent)
        return parents

    def populationFromParents(self, parents):
        couples = [(0,1),(0,2),(0,3),(0,4),(1,2),
                    (1,3),(1,4),(2,3),(2,4),(3,4)]
        newPopulation = []
        for a,b in couples:
            parentA = parents[a].bitstring
            parentB = parents[b].bitstring
            children = []
            for i in range(0,20,2):
                newBitString = parentA[:i]+parentB[i:]
                children.append(self.candidateClass(newBitString))
            newPopulation = newPopulation+children
        return newPopulation

    def step(self):
        parents = self.pickParents()
        newPopulation = self.populationFromParents(parents)
        self.currentPopulation = newPopulation

    def run(self):
        while not self.solutionFound:
            print("taking a step...")
            self.step()
            overallFitness = sum([cand.fitness for cand in self.currentPopulation])
            print("overall fitness of this generation: "+str(overallFitness))
            if self.terminationType == "generations":
                self.generations -= 1
                if self.generations == 0:
                    self.solutionFound = True
                    self.bestSolution = max(self.currentPopulation, key=lambda cand: cand.fitness)
            elif self.terminationType == "fitness":
                potentialWinners = []
                for cand in self.currentPopulation:
                    if cand.fitness <= self.fitnessGoal:
                        potentialWinners.append(cand)
                if len(potentialWinners) > 0:
                    self.solutionFound = True
                    self.bestSolution = max(potentialWinners, key=lambda cand: cand.fitness)


        print("Best Solution: "+self.bestSolution.bitstring)
        print("Fitness: "+str(self.bestSolution.fitness))
        print("Cost: "+str(self.bestSolution.weight))
        return None


## testing ##
tester = Optimizer(knapsack.Candidate, 24, "generations", 5)
tester.run()
