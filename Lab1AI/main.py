import Tool

get_bin = lambda x, n: format(x, 'b').zfill(n)

itnr = int(input("How many iterations? "))
print(itnr)
for j in range(0, 10):
    best, vals = Tool.Tool.nahc(self=Tool.Tool.nahc, k=itnr)
    sum = 0
    max = 0
    indice = 0
    for i in range(0,len(best)):
        sum = sum + Tool.Tool.eval(best[i], vals)
        if Tool.Tool.eval(best[i], vals) > max:
            max = Tool.Tool.eval(best[i], vals)
            indice = i
    sum = sum / len(best)

    file = open("output", "a")
    file.write( "\n" + str(len(vals)) + "                 " + str(itnr) + "                    " + str(sum) + "                 " + str(max) + "                " + best[indice])


print(sum)