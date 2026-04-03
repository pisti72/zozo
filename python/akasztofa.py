import random
szavak = ["zolika","fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska",
"farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]


szam =  random.randint(0,len(szavak)-1)
feladvany = szavak[szam]
print(feladvany)
tipp = input("Kérem a tippedet! ")
megfejtes = ""
for i in range(0,len(feladvany)):
    if feladvany[i] == tipp:
        megfejtes += tipp
    else:
        megfejtes += "."
print(megfejtes)




