from Particle import *

class Knapsack():

    def __init__(self):
        self.n = 0 #objects
        self.values = []
        self.weights = []
        self.maxW = 0
        self.noPop = 0
        self.particles = []

    def readFromFile(self, fisier):
        # f = open("knapsack20.txt", "r")
        #f = open("knapsack200.txt", "r")
        f = open(fisier, "r")
        self.n = f.readline()
        self.values = []
        self.weights = []
        for i in range( int(self.n)):
            line = f.readline()
            elements = line.split()
            self.values.append(int(elements[1]))
            self.weights.append(int(elements[2]))
        self.maxW = f.readline()

    def validate(self, v):
        s = 0
        for i in range( int(self.n) ):
            s = s + v[i]*self.weights[i]
        if (s <= int(self.maxW)):
            return 1
        return 0

    def fitness(self, sol):
        s = 0
        for i in range(int(self.n)):
            s = s + sol[i]*self.values[i]
        return s

    def randomSolution(self):
        sol = []
        for i in range(int(self.n)):
            sol.append(random.randint(0,1))
        while ( self.validate(sol) == 0):
            sol.clear()
            for i in range(int(self.n)):
                sol.append(random.randint(0, 1))
        return sol

    def randomVelocity(self):
        vel = []
        for i in range(int(self.n)):
            vel.append(random.uniform(-1,1))
        return vel

    def initiliase(self):
        for i in range(self.noPop):
            position = self.randomSolution()
            fitness = self.fitness(position)
            velocity = self.randomVelocity()
            self.particles.append(Particle(position, velocity, fitness))

    def run(self, noPop, w, c1, c2, maxIter, fisier):
        self.noPop = noPop
        self.initiliase()

        #just checking if everything is alright
        for p in self.particles:
            print(p.getParticle())

        gBest = [0]*int(self.n)
        t = 0
        avg = 0
        cont = 0

        while (t <= maxIter):

            for p in self.particles:
                p.updateVelocity(w, c1, c2, gBest)
                #print("velocity: ", p.getVelocity())

            for p in self.particles:
                fit = self.fitness(p.getPosition())
                p.updateFitness(fit)
                if (self.fitness(p.getPBest()) < fit):
                    p.updatePBest(p.getPosition())

                if self.validate(p.getPosition()) == 1:
                    avg = avg + fit
                    cont = cont + 1

                #update gBest
                if ( self.fitness(p.getPBest()) > self.fitness(gBest) and self.validate(p.getPBest()) == 1):
                    gBest = p.getPBest()
                    print("best fitness: ", gBest, " fitness: ", self.fitness(gBest))

                p.updatePosition()


            t = t + 1

        output = open("SPSO.txt", "a")
        avg = avg / cont
        output.write(fisier + "                   " + str(avg) + "                  " + str(gBest) + "                     " + str(self.fitness(gBest)) + "\n")
        print("\nbest fitness: ", gBest, " fitness: ", self.fitness(gBest))