import numpy as np 
import math
import random
import Shakeaspeare_DNA
import Shakeaspeare_Population

target = np.arange(30)
pop_max = 1000
mut_rate = 0.01

best = 0

population = Shakeaspeare_Population.Population(target, mut_rate, pop_max)

population.calc_fitness()

print("\n Target:")
print("\n ", target)
print("\n Populacao inicial:")
for i in range(0, population.size_population):
    print(population.population[i].genes)
    print(population.population[i].fitness_score)

while not population.finished:
    population.natural_selection()

    # print("\n Mating Pool:")
    # for n in range(0, population.size_mating_pool):
    #     print(population.matingPool[n].genes)

    population.generate()

    population.calc_fitness()

    # print("\n Nova populacao:")
    # for j in range(0, population.size_population):
    #     print(population.population[j].genes)
    #     print(population.population[i].fitness_score)

    best = population.get_best()

print("\n Melhor: ")
print(best.genes)
print("\n Geracoes: ")
print(population.number_generations)
