lista= [
    {
        "id": 1,
        "név": "Kovács János",
        "szül": "2010.06.01" ,
        "osztály": "10i"
    },
    {
        "id": 2,
        "név": "Kiss Marci",
        "szül": "2010.07.02",
        "osztály": "9a"
    },
    {
        "id": 3,
        "név": "Tóth Balázs",
        "szül": "2010.08.03",
        "osztály": "8b"
    },
    {
        "id": 4,
        "név": "Teszt Elek",
        "szül": "2010.09.04",
        "osztály": "7a"
    }
]

keys = lista[0].keys()
print("A keys listám hossza:", len(keys))
for key in keys:
    print(key)

print("--------------------------------------")
for row in lista:
    print(row["id"], " - ", row["név"], " - ", row["szül"])

print("--------------------------------------")
for row in lista:
    txt = ""
    i = 0
    for key in keys:
        delimiter = ""
        if i != len(keys) - 1:
            delimiter = " - "
        txt += str(row[key]) + delimiter
        i += 1
    print(txt)
