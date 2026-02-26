# Feladat: Írd ki a szorzótáblát!
def vesszos_szorzotabla():
    for a in range(1,11):
        text = ""
        for b in range(1,11):
            text += str(a*b) + ","
        print(text)



# Feladat: Írd ki a szorzótáblát html fájlba!
f = open("szorzotabla.html","w")
def html_szorzotabla():
    text = "<table border=\"1\">"
    print(text)
    f.write(text)
    f.close()


# vesszos_szorzotabla()
html_szorzotabla()

