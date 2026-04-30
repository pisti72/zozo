# ============================================================
# MINTA FELADATSOR – PC Játékok (MEGOLDÁS)
# ============================================================

# 1. feladat – Osztály definíciója
class Jatek:
    def __init__(self, adatok: list):
        self.cim = adatok[0]
        self.mufaj = adatok[1]
        self.fejleszto = adatok[2]
        self.ev = int(adatok[3])
        self.ar = int(adatok[4])
        self.ertekeles = int(adatok[5])

    # Bónusz: kategória metódus
    def kategoria(self):
        if self.ertekeles >= 9:
            return "Kötelező"
        elif self.ertekeles >= 7:
            return "Ajánlott"
        else:
            return "Opcionális"


# 1. feladat – Adatok beolvasása fájlból
f = open("jatekaim.txt", encoding="UTF-8")
f.readline()  # fejléc kihagyása
jatekok = []

for sor in f:
    adatok = sor.strip().split(";")
    uj_jatek = Jatek(adatok)
    jatekok.append(uj_jatek)

f.close()


# 2. feladat – Listázás
print("2. feladat: Összes játék listája")
for j in jatekok:
    print(f"{j.cim} ({j.ev}) - {j.fejleszto} - {j.ar} Ft - értékelés: {j.ertekeles}/10")


# 3. feladat – Darabszám
print(f"\n3. feladat: Összesen {len(jatekok)} játék van a nyilvántartásban.")


# 4. feladat – Ingyenes játékok
print("\n4. feladat: Ingyenes játékok (0 Ft)")
for j in jatekok:
    if j.ar == 0:
        print(f"  {j.cim} - {j.fejleszto}")


# 5. feladat – Legdrágább játék
print("\n5. feladat: Legdrágább játék")
legdragabb = jatekok[0]
for j in jatekok:
    if j.ar > legdragabb.ar:
        legdragabb = j
print(f"A legdrágább játék: {legdragabb.cim} - {legdragabb.ar} Ft")


# 6. feladat – Legjobb értékelés
print("\n6. feladat: Legjobb értékelésű játék")
legjobb = jatekok[0]
for j in jatekok:
    if j.ertekeles > legjobb.ertekeles:
        legjobb = j
print(f"A legjobb értékelésű játék: {legjobb.cim} - {legjobb.ertekeles}/10")


# 7. feladat – Szűrés műfaj alapján
print("\n7. feladat: Keresés műfaj alapján")
mufaj = input("Add meg a műfajt: ")
talalt = False
for j in jatekok:
    if j.mufaj.strip().lower() == mufaj.strip().lower():
        print(f"  {j.cim} - {j.fejleszto}")
        talalt = True
if not talalt:
    print("Nem található ilyen műfajú játék.")


# 8. feladat – 9 vagy 10 értékelésű játékok száma
print("\n8. feladat: 9 vagy 10 értékelésű játékok")
darab = 0
for j in jatekok:
    if j.ertekeles >= 9:
        darab += 1
print(f"{darab} játék értékelése 9 vagy 10.")


# 9. feladat – Átlagár
print("\n9. feladat: Átlagár")
osszeg = 0
for j in jatekok:
    osszeg += j.ar
atlag = osszeg / len(jatekok)
print(f"A játékok átlagára: {atlag:.0f} Ft")


# 10. feladat – Top játékok fájlba írása
print("\n10. feladat: 10/10 értékelésű játékok fájlba írva (top_jatekok.txt)")
ki = open("top_jatekok.txt", "w", encoding="UTF-8")
for j in jatekok:
    if j.ertekeles == 10:
        ki.write(f"{j.cim} - {j.ertekeles}/10\n")
ki.close()
print("Fájl elkészült.")


# Bónusz – kategoria metódus bemutatása
print("\nBónusz: Játékok kategória szerint")
for j in jatekok:
    print(f"  {j.cim} --> {j.kategoria()}")
