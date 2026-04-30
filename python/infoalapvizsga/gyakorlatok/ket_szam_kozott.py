szam1 = int(input("Írd be az első számot! "))
szam2 = int(input("Írd be a második számot! "))
szamok= "Az alábbi számokat találtam: "
harommal_osztható = 0
for i in range(szam1,szam2+1):
    if i%3 == 0:
        harommal_osztható += 1
    elválasztó = ', '
    if i == szam2:
        elválasztó = ''

    szamok += str(i) + elválasztó
    
print(szamok)
print("A két szám között", harommal_osztható, "db szám van, ami osztható 3-mal!")
print(f"A két szám között {harommal_osztható} db szám van, ami osztható 3-mal!")