import math
import copy
import numpy as nm
import random as rnd

class TETool:

    @staticmethod
    def read(file):
        filehandler = open(file, "r")
        lines =  filehandler.read().split('\n')
        x = []
        y = []
        for i in range(6, 106):
            x.append(lines[i].split(" ")[1])
            y.append(lines[i].split(" ")[2])
        return x, y

    @staticmethod
    def start(x, y, generations, popsize):
        resultpop = []
        population = []
        fitness = []

        # initial population
        for i in range(0, popsize):
            perm = list(nm.random.permutation(len(x)))
            population.append(perm)
            fitness.append(TETool.eval(perm, x, y))

        for i in range(0, generations):

            newpop = []
            print(i)
            print(str(popsize) + " popsize")
            print(str(len(newpop)) + " newpop size")

            # I generate half of the new population through crossover
            popleft = popsize - TETool.crossover(newpop, population)

            # I generate a quarter of the new population by mutating the parents
            popleft = popleft - TETool.mutation(newpop, population, popleft)

            # the last quarter of chromosomes will be generated randomly
            while popleft != 0:
                newpop.append(nm.random.permutation(len(x)))
                popleft = popleft - 1
            # we have gathered the number of neurons for the current generation

            population = copy.deepcopy(newpop)
            # replace population with the offspring population

            bestindex = TETool.getbest(newpop, x, y)
            resultpop.append(population[bestindex])
            # end of generation-based loop

        return resultpop

    @staticmethod
    def crossover(newpop, oldpop):
        popsize = len(oldpop)
        contor = 0
        for i in range(0, int(popsize/2)):
            contor = contor + 1
            newpop.append(TETool.crossgenes(oldpop, i, i+1))

        return contor

    @staticmethod
    def getbest(population, x, y):
        minim = 999999999
        index = 0
        for i in range(0, len(population)):
            chromosome = population[i]
            aux = TETool.eval(chromosome, x, y)
            if aux < minim:
                minim = aux
                index = i

        return index

    @staticmethod
    def mutation(newpop, oldpop, popleft):
        contor = 0
        for i in range(0, int(popleft/2)):
            contor = contor + 1
            newpop.append(TETool.mutate(oldpop[ int( len(oldpop) / 2) + i]))
        return contor

    @staticmethod
    def mutate(chromosome):

        index1 = rnd.randint(0, len(chromosome) / 2)
        index2 = rnd.randint(len(chromosome) / 2, len(chromosome))

        selection = chromosome[index1:index2]

        left = chromosome[0:index1]
        right = chromosome[index2:len(chromosome)]
        selection.reverse()

        chromosome = []
        [chromosome.append(elem) for elem in left]
        [chromosome.append(elem) for elem in selection]
        [chromosome.append(elem) for elem in right]

        return chromosome

    @staticmethod
    def crossgenes(pop, i, j):
        print(len(pop))
        print(i)
        print(j)
        parent1 = pop[i]
        parent2 = pop[j]

        # the way of crossing the genes is by 2-point selection
        # i'm taking 2 random indexes from parent1 and what's between them i delete from the 2nd parent
        # after deletion i append the selection to the 2nd parent and return him back

        index1 = rnd.randint(0, len(parent1)/2)
        index2 = rnd.randint(len(parent1)/2, len(parent1))

        selection = parent1[index1:index2]
        parent2 = list(parent2)

        for i in range(0, len(selection)):
            parent2.remove(selection[i])

        [parent2.append(elem) for elem in selection]
        return parent2

    @staticmethod
    def getmean(population, x, y):
        suma = 0
        for chromosome in population:
            suma = suma + TETool.eval(chromosome, x, y)
        suma = suma / len(population)
        return suma

    # calculates the fitness of the solution
    @staticmethod
    def eval(perm, x, y):
        fitness = 0
        for i in range(0, len(perm)-1):
            fitness = fitness + math.sqrt((int(x[perm[i]])-int(x[perm[i+1]]))**2 + (int(y[perm[i]])-int(y[perm[i+1]]))**2)
        return fitness