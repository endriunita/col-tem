from Lab1AI import Tool
import numpy


# read name of input file
file = input("Which file? \n")

# read population size
popsize = int(input("Population size: \n"))

#read number of generations
generations = int(input("Number of generations: \n"))

#read factor de mutatie
probabilitate = float(input("Mutation probability: \n"))

outputfile = open("output.txt", "a")

for i in range(0, 10):
    resultset, vals = Tool.Tool.genetic_approach(generations, file, popsize, probabilitate)
    sum = 0
    for sol in resultset:
        sum = sum + Tool.Tool.eval(sol, vals)
    sum = sum / len(resultset)
    maximum = Tool.Tool.getMax(resultset, vals)
    print(" Maximum fitness: " + str(Tool.Tool.eval(maximum, vals)))
    print(" Average fitness: " + str(sum) + " \n")

    outputfile.write("\n" + str(file) + "                   " + str(popsize) + "                       " + str(generations)
               + "                    " + str(probabilitate) + "                   " + str(sum) + "                  " + str(Tool.Tool.eval(maximum, vals)))