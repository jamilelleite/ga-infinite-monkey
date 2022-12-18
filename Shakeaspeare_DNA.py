import numpy as np 
import random
import math 

# Target eh array de tamanho N com numeros em sequencia (criar em main)
# np.arange(N)

class DNA:
    def __init__(self, N):
        self.genes = np.arange(N)
        np.random.shuffle(self.genes)
        self.fitness_score = 0
        

    def fitness_function(self, target):
        score = 0
        for i in range(0, self.genes.size):
            if self.genes[i] == target[i]:
                score = score + 1
        # self.fitness_score = math.pow(2, score)
        self.fitness_score = score

    def crossover(self, partner):  #DNA partner
        child = DNA(self.genes.size)

        midpoint = random.randrange(self.genes.size)

        for i in range(0, self.genes.size):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]

        return child

    def mutate(self, mutationRate):
        for i in range(0, self.genes.size):
            aux = random.randrange(100)
            if  aux < mutationRate*100:
                self.genes[i] = random.randint(0, self.genes.size -1)

# dna1 = DNA(5)
# print("\nIndividuo 1:")
# print("\nOrdem cidades 1")
# print(dna1.genes)
# dna1.fitness_function()
# print("\nFitness score 1:")
# print(dna1.fitness_score)

# dna2 = DNA(5)
# print("\nIndividuo 2:")
# print("\nOrdem cidades 2")
# print(dna2.genes)
# dna2.fitness_function()
# print("\nFitness score 2:")
# print(dna2.fitness_score)

# child = dna1.crossover(dna2)
# print("\nIndividuo Filho:")
# print("\nOrdem cidades Filho")
# print(child.genes)
# child.fitness_function()
# print("\nFitness score Filho:")
# print(child.fitness_score)

# child.mutate(0.5)
# print("\nFilho pos mut")
# print(child.genes)





