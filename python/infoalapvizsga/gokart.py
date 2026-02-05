f = open("gokart-adatok.txt")
f.readline()
pályák = list()
for sor in f:
    rekord = sor.split(";")
    pályák.append(rekord)

print(pályák[1][1])