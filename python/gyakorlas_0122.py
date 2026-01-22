# Feladat 1: Kérjünk be két számot! Majd kérjük, hogy mit csináljunk velük [1 - összeadás, 2 - kivonás]!
# Ha kiválasztottuk, hogy összeadni vagy kivonni szeretnénk őket, akkor írja ki az eredményt!



szam1 = int(input("Kérem az elso számot!"))


szam2= int(input("Kérem a második számot!"))

#osszeadas
összead = szam1 + szam2
kivon = szam1 - szam2 
szoroz = szam1 * szam2




művelet = input("Adja meg a műveletet \n[1] az összeadás [2] kivonás [3] a szorzás [4] az osztás!")

if művelet == "1":
    print(összead)
elif művelet == "2":
    print(kivon)
elif művelet == "3":
    print(szoroz)
elif művelet == "4":
    if szam2 == 0:
        print("Nullával nem lehet osztani!")
    else:
        oszt= szam1 / szam2
        print(oszt)
else:
    print("Érvénytelen művelet!")


    

