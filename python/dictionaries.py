# Dictionaries [key - value] azaz [kulcs - érték]
lista = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "land": "USA"
    },
    {
        "brand": "Mercedes",
        "model": "SLK",
        "year": 1995,
        "land": "GER"
    },
    {
        "brand": "Opel",
        "model": "Astra G",
        "year": 1998,
        "land": "GER"
    },
    {
        "brand": "Toyota",
        "model": "Yaris",
        "year": 1999,
        "land": "JAP"
    }
]

for row in lista:
    print(row["brand"], " - ", row["model"], " - ", row["year"]  , " - ", row["land"])

print("-----------------------------------")
for i in range(0, len(lista)):
    row = lista[i]
    print(row["brand"], " - ", row["model"], " - ", row["year"], " - ", row["land"])
print("-----------------------------------")
# Sűrés országra.
# Listázzuk ki csak a GER-t

for row in lista:
    if row["land"] == "GER":
        print(row["brand"], " - ", row["model"], " - ", row["year"], " - ", row["land"])



# Lista

masik_lista = ["Zozo", "Mici cica", "István tanárbá"]

for elem in masik_lista:
    print(elem)
