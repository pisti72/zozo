pénzed = int(input("Írd be, hogy mennyi pénzed van: "))
while pénzed > 0:
    költés = int(input("Mennyit szeretnél költeni belőle: "))
    while költés > pénzed or költés < 0:
        print("Ennyit nem költhetsz")
        költés = int(input("Mennyit szeretnél költeni: "))
    pénzed -= költés
    print('Ennyi pénzed maradt: ', pénzed)
    
    