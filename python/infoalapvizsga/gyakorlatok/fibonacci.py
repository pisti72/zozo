# Feladat: Készíts Fibonacci sorozatot
# 1,1,2,3,5,8,13,....
print("For ciklussal")
n1 = 1
n2 = 1
text = "1,1,"
for i in range(0, 10000):
    n3 = n1 + n2
    text += str(n3) + ","
    n1 = n2
    n2 = n3
    if n3>100000000:
        break
print(text)


print("\nWhile ciklussal")
n1 = 1
n2 = 1
text = "1,1,"
while n2<100000000:
    n3 = n1 + n2
    text += str(n3) + ","
    n1 = n2
    n2 = n3
print(text)
    
