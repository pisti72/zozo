
while True:
    try:
        szam1 = float(input("Kérem az első számot"))
        break
    
    except: 
        print("Kérlek adj be egy számot!")

while True:
    try:
   
        szam2 = float(input("Kérem a második számot "))
        ter= szam1 * szam2
        ker= (szam1 + szam2)*2
        break
    
    except: 
        print("Kérlek adj be egy számot! ")
                
        

print("A téglalap kerülete:", ker)
print("A téglalap területe:", ter)
        











