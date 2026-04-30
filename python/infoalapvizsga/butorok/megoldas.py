# ============================================================
# MINTA FELADATSOR – Bútorok (MEGOLDÁS)
# ============================================================

# 1. feladat – Osztály definíciója
class Butor:
    def __init__(self, adatok: list):
        self.kod = adatok[0]
        self.tipus = adatok[1]
        self.szin = adatok[2]
        self.ar = int(adatok[3])

    # Bónusz: akció metódus
    def akcio(self, szazalek):
        return self.ar * (1 - szazalek / 100)


# 1. feladat – Adatok beolvasása fájlból
f = open("butorok.txt", encoding="UTF-8")
butorok = []

for sor in f:
    adatok = sor.strip().split()
    uj_butor = Butor(adatok)
    butorok.append(uj_butor)

f.close()


# 2. feladat – Listázás
print("2. feladat: Összes bútor listája")
for b in butorok:
    print(f"{b.kod} ---> {b.tipus} ({b.szin}) - {b.ar} Ft")


# 3. feladat – Darabszám
print(f"\n3. feladat: Összesen {len(butorok)} bútor van a nyilvántartásban.")


# 4. feladat – Összegzés
print("\n4. feladat: Bútorok árának összege")
osszeg = 0
for b in butorok:
    osszeg += b.ar
print(f"Az összes bútor ára összesen: {osszeg} Ft")


# 5. feladat – Legdrágább bútor
print("\n5. feladat: Legdrágább bútor")
legdragabb = butorok[0]
for b in butorok:
    if b.ar > legdragabb.ar:
        legdragabb = b
print(f"A legdrágább bútor: {legdragabb.kod} - {legdragabb.tipus} - {legdragabb.ar} Ft")


# 6. feladat – Legolcsóbb bútor
print("\n6. feladat: Legolcsóbb bútor")
legolcsobb = butorok[0]
for b in butorok:
    if b.ar < legolcsobb.ar:
        legolcsobb = b
print(f"A legolcsóbb bútor: {legolcsobb.kod} - {legolcsobb.tipus} - {legolcsobb.ar} Ft")


# 7. feladat – Székek szűrése
print("\n7. feladat: Székek listája")
for b in butorok:
    if b.tipus == "szek":
        print(f"  {b.kod} - {b.szin}")


# 8. feladat – 50 000 Ft feletti bútorok száma
print("\n8. feladat: 50 000 Ft feletti árak")
darab = 0
for b in butorok:
    if b.ar > 50000:
        darab += 1
print(f"{darab} bútor ára haladja meg az 50 000 Ft-ot.")


# 9. feladat – Felhasználói keresés szín alapján
print("\n9. feladat: Keresés szín alapján")
szin = input("Add meg a keresett színt: ")
talalt = False
for b in butorok:
    if b.szin.strip().lower() == szin.strip().lower():
        print(f"  {b.kod} - {b.tipus}")
        talalt = True
if not talalt:
    print("Nem található ilyen színű bútor.")


# 10. feladat – Drága bútorok fájlba írása
print("\n10. feladat: 50 000 Ft feletti bútorok fájlba írva (dragak.txt)")
ki = open("dragak.txt", "w", encoding="UTF-8")
for b in butorok:
    if b.ar > 50000:
        ki.write(f"{b.kod} {b.ar} Ft\n")
ki.close()
print("Fájl elkészült.")


# Bónusz – akcio metódus bemutatása
print(f"\nBónusz: {legdragabb.kod} ({legdragabb.tipus}) 20%-os akcióval: {legdragabb.akcio(20):.0f} Ft")
