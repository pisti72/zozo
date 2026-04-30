f = open("gokart-adatok.txt")
f.readline()
NÉV = 0
TELEPÜLÉS = 1
HOSSZ = 2
JEGYÁR = 3
pályák = []

def tizenötszázalékkal(alap):
    return alap * 1.15

for sor in f:
    rekord = sor.split(";")
    pályák.append(rekord)

print("1. Feladat: Írd ki, hogy mennyi az összes pályát vizsgálva a pályák hossza!")
összes_hossz = 0
for pálya in pályák:
    összes_hossz += int(pálya[HOSSZ])
print(f"Az összes pálya hossza: {összes_hossz} m.")
print("\n2. Feladat: Írd ki, hogy mi annak a pályának a neve,\nahol legolcsóbb a jegyár!")
legolcsóbb_jegyár = int(pályák[0][JEGYÁR])
legolcsóbb_név = pályák[0][NÉV]
for pálya in pályák:
    if legolcsóbb_jegyár > int(pálya[JEGYÁR]):
        legolcsóbb_jegyár = int(pálya[JEGYÁR])
        legolcsóbb_név = pálya[NÉV]
print(f"A legolcsóbb jegy {legolcsóbb_név} pályán van, {legolcsóbb_jegyár} Ft.")
print("\n3. Feladat: Az osztályon belül hozz létre egy tagfüggvényt áremelés néven")
print("4. Feladat:")
név = input("Írd be a pályának a nevét! ")
emelt_ár = -1
for pálya in pályák:
    if pálya[NÉV].strip().lower() == név.strip().lower():
        emelt_ár = tizenötszázalékkal(int(pálya[JEGYÁR]))
if emelt_ár == -1:
    print("Nem létezik ilyen pálya!")
else:
    print(f"Ennél a pályánál az áremeléssel {emelt_ár} Ft lenne a jegyár.")
f = open("gokart-export.txt","w")
pályák_budapestiek = ""
for pálya in pályák:
    if pálya[TELEPÜLÉS] == "Budapest":
        pályák_budapestiek += pálya[NÉV] + "\n"
f.write(pályák_budapestiek)
f.close()