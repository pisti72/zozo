class Jatek :
    def __init__(self ,adatok:list):
        self.cim = adatok[0]
        self.mufaj = adatok[1]
        self.fejleszto = adatok[2]
        self.ev = adatok[3]
        self.ar = adatok[4]
        self.ertekeles = adatok[5]

file = open("jatekaim.csv", encoding="UTF-8")
jatekok = []
file.readline()

for f in file:
    jatek_lista = f.strip().split(";")
    uj_jatek = Jatek(jatek_lista)
    jatekok.append(uj_jatek)
print(jatekok[0].cim)
file.close()
