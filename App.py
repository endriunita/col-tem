from Knapsack import *
from Lab1AI import Tool
import numpy


test1 = "knapsack200.txt"
test2 = "knapsack20.txt"
a = "p01.txt"
b = "p02.txt"
c = "p03.txt"
d = "p04.txt"
e = "p05.txt"
f = "p06.txt"
g = "p07.txt"
h = "p08.txt"


files = [a, b, c, d, e, f, g]

for fisier in files:
    for i in range(0,10):

        k = Knapsack()
        k.readFromFile(fisier)
        initpop, vals = Tool.Tool.genetic_approach(500, fisier, 100, 0.2)

        mumbojumbo = []

        for pop in initpop:
            mumbojumbo.append(list(map(int, pop)))

        k.run(500, 1, 2, 2, 10, mumbojumbo, 0, fisier)
