# ============================================================
# MINTA FELADATSOR – Könyvek (MEGOLDÁS)
# ============================================================

# 1. feladat – Osztály definíciója
class Konyv:
    def __init__(self, adatok: list):
        self.cim = adatok[0]
        self.szerzo = adatok[1]
        self.mufaj = adatok[2]
        self.ar = int(adatok[3])
        self.oldalszam = int(adatok[4])

    # Bónusz: kedvezmény metódus
    def kedvezmeny(self, szazalek):
        return self.ar * (1 - szazalek / 100)


# 1. feladat – Adatok beolvasása fájlból
f = open("konyvek.txt", encoding="UTF-8")
f.readline()  # fejléc kihagyása
konyvek = []

for sor in f:
    adatok = sor.strip().split(";")
    uj_konyv = Konyv(adatok)
    konyvek.append(uj_konyv)

f.close()


# 2. feladat – Listázás
print("2. feladat: Összes könyv listája")
for k in konyvek:
    print(f"{k.cim} - {k.szerzo} ({k.mufaj}) - {k.ar} Ft")


# 3. feladat – Darabszám
print(f"\n3. feladat: Összesen {len(konyvek)} könyv van a listában.")


# 4. feladat – Összegzés
print("\n4. feladat: Könyvek árának összege")
osszeg = 0
for k in konyvek:
    osszeg += k.ar
print(f"Az összes könyv ára összesen: {osszeg} Ft")


# 5. feladat – Legdrágább könyv
print("\n5. feladat: Legdrágább könyv")
legdragabb = konyvek[0]
for k in konyvek:
    if k.ar > legdragabb.ar:
        legdragabb = k
print(f"A legdrágább könyv: {legdragabb.cim} - {legdragabb.ar} Ft")


# 6. feladat – Legolcsóbb könyv
print("\n6. feladat: Legolcsóbb könyv")
legolcsobb = konyvek[0]
for k in konyvek:
    if k.ar < legolcsobb.ar:
        legolcsobb = k
print(f"A legolcsóbb könyv: {legolcsobb.cim} - {legolcsobb.ar} Ft")


# 7. feladat – Fantasy könyvek szűrése
print("\n7. feladat: Fantasy műfajú könyvek")
for k in konyvek:
    if k.mufaj == "fantasy":
        print(f"  {k.cim} - {k.szerzo}")


# 8. feladat – 3000 Ft feletti könyvek száma
print("\n8. feladat: 3000 Ft feletti árak")
darab = 0
for k in konyvek:
    if k.ar > 3000:
        darab += 1
print(f"{darab} könyv ára haladja meg a 3000 Ft-ot.")


# 9. feladat – Felhasználói keresés
print("\n9. feladat: Szerző keresése")
nev = input("Add meg a szerző nevét: ")
talalt = False
for k in konyvek:
    if k.szerzo.strip().lower() == nev.strip().lower():
        print(f"  {k.cim} ({k.mufaj}) - {k.ar} Ft, {k.oldalszam} oldal")
        talalt = True
if not talalt:
    print("Nem található ilyen szerző.")


# 10. feladat – Fájlba írás (300 oldalnál hosszabb könyvek)
print("\n10. feladat: 300 oldalnál hosszabb könyvek fájlba írva (300_felett.txt)")
ki = open("300_felett.txt", "w", encoding="UTF-8")
for k in konyvek:
    if k.oldalszam > 300:
        ki.write(k.cim + "\n")
ki.close()
print("Fájl elkészült.")


# Bónusz – kedvezmény metódus bemutatása
print(f"\nBónusz: {legdragabb.cim} 10%-os kedvezménnyel: {legdragabb.kedvezmeny(10):.0f} Ft")
