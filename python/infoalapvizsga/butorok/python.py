class Butor:
    def __init__(self, adatok:list):
        self.kod = adatok[0]
        self.tipus = adatok[1]
        self.szin= adatok[2]
        self.ar = int(adatok[3])

file = open("butorok.txt", encoding= "UTF-8")
butorok = []


for sor in file:
    lista = sor.strip().split()
    uj_butor = Butor(lista)
    butorok.append(uj_butor)

file.close()
for b in butorok:
    print(f"{b.kod} ---> {b.tipus} {b.szin} {b.ar} Ft")


print(f"Összesen {len(butorok)} bútorunk van")

osszeg = 0
for b in butorok:
     osszeg += b.ar 

print(f"Összesen ennyi {osszeg} ft")

legdragabb = butorok[0]
for b in butorok:
    if b.ar > legdragabb.ar:
        legdragabb = b

print(f"A legdrágább bútor: {legdragabb.kod} ami ennyi {legdragabb.ar} Ft")

legolcsobb = butorok[0]
for b in butorok:
    if b.ar < legolcsobb.ar:
        legolcsobb = b

    

print(f"A legolcsóbb bútor: {legolcsobb.kod} ami ennyi {legolcsobb.ar} Ft")

agyak = []
for b in butorok:
    if b.tipus == "szek":
        agyak.append(b)

for a in agyak:
    print(f'{a.kod}   tipusa: {a.tipus}   szin:{a.szin}')






    
    



