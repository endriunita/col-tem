import TETool

# read number of iterations
iterations = 10

# read population size
popsize = int(input("Population size: \n"))

# read number of generations
generations = int(input("Number of generations: \n"))

outputfile = open("output.txt", "a")
x, y = TETool.TETool.read("kroB100.tsp")

for i in range(0, iterations):
    finalpop = TETool.TETool.start(x, y, generations, popsize)

    avg = TETool.TETool.getmean(finalpop, x, y)

    index = TETool.TETool.getbest(finalpop, x, y)
    mindist = TETool.TETool.eval(finalpop[index], x, y)

    outputfile.write("\n" + str(iterations) + "                     " + str(popsize) + "                        " + str(generations) + "                        " + str(avg) + "                                " + str(mindist))


