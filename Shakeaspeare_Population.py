import numpy as np
import Shakeaspeare_DNA
import random
import math

class Population:
    def __init__(self, target, mutation_rate, size_population):
        self.target = target
        self.mutation_rate = mutation_rate
        self.size_population = size_population
        self.genes_size = target.size
        self.number_generations = 0
        self.size_mating_pool = 0
        self.finished = False
        # self.perfect_score = math.pow(2,target.size)
        self.perfect_score = self.genes_size
        self.population = []
        self.matingPool = []
        for i in range(0, self.size_population):
            self.population.append(Shakeaspeare_DNA.DNA(self.genes_size))
        
    def calc_fitness(self):
        for i in range(0, self.size_population):
            self.population[i].fitness_function(self.target)

    def natural_selection(self):
        max_fitness = 0
        self.matingPool = []

        for i in range(0, self.size_population):
            if self.population[i].fitness_score > max_fitness:
                max_fitness = self.population[i].fitness_score

        #fitne ja deve ter sido calculado
        for i in range(0, self.size_population):
            n_pool = int((self.population[i].fitness_score * 100)/max_fitness)
            for n in range(0, n_pool):
                self.matingPool.append(self.population[i])
            self.size_mating_pool = len(self.matingPool)

    def generate(self):
        for i in range(0, self.size_population):
            a = random.randint(0, self.size_mating_pool - 1)
            b = random.randint(0, self.size_mating_pool - 1)
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutation_rate)
            self.population[i] = child
        self.number_generations = self.number_generations + 1

    def get_best(self):
        world_record = 0
        for i in range(self.size_population):
            if self.population[i].fitness_score > world_record:
                index_world_record = i 
                world_record = self.population[i].fitness_score
        if world_record == self.perfect_score:
            self.finished = True
        
        return self.population[index_world_record]



    
            


        
