# Olvassuk be a fájlokat és készítsünk belőle egy HTML táblázatot!
NAME = 0
PRICE = 1
UNIT = 2


file = open("gyumolcsok.csv", "rt", encoding="UTF-8")
fruits = []
for row in file:
    fruit = row.strip().split(",")
    fruits.append(fruit)

html = "<table border=\"1\">\n"
row = 0
for f in fruits:
    
    html += "\t<tr>\n"
    if row==0:
        html += "<th> sorszám </th>" + "\t\t<th>" + f[NAME] + "</th><th>" + f[PRICE] + "</th><th>" + f[UNIT] + "</th>\n"
    else:
        html += "<td>"+ str(row) +"</td>" + "\t\t<td>" + f[NAME] + "</td><td>" + f[PRICE] + "</td><td>" + f[UNIT] + "</td>\n"
    html += "\t</tr>\n"
    row += 1
html += "</table>"
print(html)
file = open("gyumolcsok.html","wt")
file.write(html)
