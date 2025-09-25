print("Hello")
nevek=["Laci","Robi","Peti", "Kati","Robi"]
print("A nevek kilistázása")
for név in nevek:
    print ("Név:",név)

print("Robik megszámolása")
robi_számláló=0
for név in nevek:
    if név == "Robi":
        robi_számláló = robi_számláló + 1
print("ennyi robi van a listában:", robi_számláló)