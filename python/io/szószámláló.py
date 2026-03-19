file = open("versike.txt", "rt", encoding="UTF-8")
összeg = 0
sorok = list()
for f in file:
    sorok.append(f.strip())
    sor = f.split()
    összeg += len(sor)
print(összeg, 'Szavad van')

tyúk = 0
for s in sorok:
    print(s)
    if "tyúk" in s:
        tyúk += 1
print("\n\nTyúk:",tyúk,"db")

    