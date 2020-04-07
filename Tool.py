from random import randint
import random as rnd
import numpy
import copy as copy


class Tool:
    @staticmethod
    def nahc(self, k):
        file = open("input200.txt", "r")
        x = file.read().split("\n")
        vals = []
        wghts = []
        best = []
        startindex = 0

        n = int(x[0])
        print(n)
        W = x[n + 1]

        for i in range(1, n+1):
            vals.append(int(' '.join(x[i].split()).split(' ')[1]))
            wghts.append(int(' '.join(x[i].split()).split(' ')[2]))

        c = Tool.getsolaleatoare(n, vals, wghts, W)
        print(c)

        best = []
        for i in range(0, k):
            x, startindex = Tool.vecin(c, vals, wghts, W, startindex)
            print(x)
            if Tool.eval(x, vals) > Tool.eval(c, vals):
                c = x
            else:
                best.append(c)
                startindex = 0
                c = Tool.getsolaleatoare(n, vals, wghts, W)

        return best, vals

    @staticmethod
    def getsolaleatoare(n, v, w, W):
        sol = str(format(randint(0, 2 ** n - 1), 'b').zfill(len(v)))
        while Tool.verificasol(sol, v, w, W) == 0:
            sol = str(format(randint(0, 2 ** n - 1), 'b').zfill(len(v)))
        return sol

    @staticmethod
    def verificasol(sol, v, w, W):

        suma = 0
        for i in range(0, len(v)):
            if (suma + int(sol[i]) * w[i]) > int(W):
                return 0
            suma = suma + int(sol[i]) * w[i]
        return 1

    @staticmethod
    def vecin(c, vals, wghts, W, index):
        c = list(c)
        for i in range(index,len(c)):
            if c[i] == "1":
                c[i] = str(0)
            else:
                c[i] = str(1)
            if Tool.verificasol(c, vals, wghts, W) == 1:
                index = i + 1
                c = "".join(c)
                return c, index
            else:
                if c[i] == "1":
                    c[i] = str(0)
                else:
                    c[i] = str(1)
        return c, index

    @staticmethod
    def eval(c, vals):
        suma = 0
        for i in range(0, len(c)):
            suma = suma + int(c[i])*vals[i]
        return suma

    @staticmethod
    def genetic_approach(generations, file, popsize, probability):
        totalweight, count, vals, weights = Tool.read(file)
        # get the input data first

        population = []
        for i in range(0, popsize):
            population.append(list(Tool.getsolaleatoare(count, vals, weights, totalweight)))
        # generate starting population, every solution being valid

        resultpop = []

        for i in range(0, generations):
            newpop = []
            print(i)

            while 1:

                print(str(popsize) + " popsize")
                print(str(len(newpop)) + " newpop size")
                if len(newpop) == popsize:
                    print("in IF")
                    break

                ind1 = randint(0, len(population) - 1)
                ind2 = randint(0, len(population) - 1)
                # select 2 random parents within the population

                os1, os2 = Tool.crossover(population[ind1], population[ind2])
                # use single-point crossover here to generate the offspring

                os1 = list(copy.deepcopy(Tool.mutate(os1, probability)))
                os2 = list(copy.deepcopy(Tool.mutate(os2, probability)))
                # mutate the offspring using weak mutation

                os1 = copy.deepcopy(Tool.validateSol(os1, vals, weights, totalweight))
                os2 = copy.deepcopy(Tool.validateSol(os2, vals, weights, totalweight))
                # validate the mutated offspring

                newpop.append(os1)
                print("added 1 into population")
                newpop.append(os2)
                #once the mutated offspring is validated, we add it to the new population

            # we have gathered the number of neurons for the current generation

            population = copy.deepcopy(newpop)
            # replace population with the offspring population

            resultpop.append(Tool.getMax(newpop, vals))
            # end of generation-based loop

        return resultpop, vals


    @staticmethod
    def read(k):
        file = open(str(k), "r")
        x = file.read().split("\n")
        count = int(x[0])
        totalweight = int(x[count+1])

        vals = []
        weights = []

        for i in range(1, count+1):
            vals.append(int(' '.join(x[i].split()).split(' ')[1]))
            weights.append(int(' '.join(x[i].split()).split(' ')[2]))

        return totalweight, count, vals, weights


    @staticmethod
    def elitSelect(vals, population):
        maxim = 0
        sol0 = []
        sol1 = []
        for sol in population:
            aux = sum(numpy.array(vals) * numpy.array(sol))
            if aux > maxim:
                sol0 = copy.deepcopy(sol1)
                sol1 = copy.deepcopy(sol)
                maxim = aux
        return sol0, sol1

    @staticmethod
    def crossover(second, first):
        index = randint(0, len(first))
        os1 = second[0:index] + first[index:len(first)]
        os2 = first[0:index] + second[index: len(second)]

        return os1, os2

    @staticmethod
    def mutate(os, probability):
        if probability >= 1:
            probability = probability/100
        prob = rnd.random()
        if prob < probability:
            index = randint(0, len(os) - 1)
            os = list(os)
            if os[index] == '1':
                os[index] = '0'
            else:
                os[index] = '1'
        return os

    @staticmethod
    def getMax(population, vals):
        max = 0
        res = []
        for sol in population:
            aux = Tool.eval(sol, vals)
            if aux > max:
                max = aux
                res = copy.deepcopy(sol)
        return res

    @staticmethod
    def validateSol(os, vals, weights, totalweight):
        index = 0
        while 1:
            aux = Tool.verificasol(os, vals, weights, totalweight)
            if aux == 1:
                return os
            if os[index] == '1':
                os[index] = 0
            index = index + 1

 #       while  == 0:
 #           print(os)
 #           index = randint(0, len(os) - 1)
 #          if os[index] == '1':
 #               os[index] = '0'
 #       return os
