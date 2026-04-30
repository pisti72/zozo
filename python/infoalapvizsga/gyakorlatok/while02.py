# Feladat: Írd ki a négyzet számokat 1-től 10000-ig 
#      - for ciklussal, majd
#      - while ciklussal
#
# Példa: 1,4,9,16,25,......

print("For ciklussal:")
text = ""
for i in range(100+1):
    text = text + str(i*i) + ','
print(text)
print("\nWhile ciklussal:")
text = ""
i = 1
while i < 100:
    i+=1
    text = text + str(i*i) + ','
print(text)
