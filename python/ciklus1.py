# Feladat: Írj programot, ami bekéri a nevedet majd bekéri, hogy hányszor írja ki a nevedet! 
# Ezután írja ki annyiszor

print("Név kiirás")
print("==========\n")
név = input("Ird be a neved: ")
szorzo  =int(input("Hányszor irjam ki a neved? "))
for i in range(0, szorzo):
    print(f"{i+1}. {név}")