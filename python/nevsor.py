lista= [
    {
        "id": 1,
        "név": "Kovács János",
        "szül": "2010.06.01" ,
        
    },
    {
        "id": 2,
        "név": "Kiss Marci",
        "szül": "2010.07.02",
        
      
    },
    {
        "id": 3,
        "név": "Tóth Balázs",
        "szül": "2010.08.03",
        
     
    },
    {
        "id": 4,
        "név": "Teszt Elek",
        "szül": "2010.09.04",
        
     
    }
]


keys = lista[0].keys()
for key in keys:
    print(key)


print("--------------------------------------")
for row in lista:
    print(row["id"], " - ", row["név"], " - ", row["szül"])
