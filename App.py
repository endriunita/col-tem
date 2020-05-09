from Knapsack import *

a = "p01.txt"
b = "p02.txt"
c = "p03.txt"
d = "p04.txt"
e = "p05.txt"
f = "p06.txt"
g = "p07.txt"
h = "p08.txt"
files = [a, b, c, d, e, f, g, h]


for fisier in files:
    for i in range(0,10):
        k = Knapsack()
        k.readFromFile(fisier)
        k.run(5000, 1, 0, 2, 15, fisier)
