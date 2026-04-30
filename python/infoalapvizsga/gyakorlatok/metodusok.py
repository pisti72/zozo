def kiir(szöveg):
    print(szöveg)

def üdv():
    print("Üdvözöllek")

def hello():
    print("Hello - metódusból")
    return "Hello - returnból"

def kiir_sokszor(txt, n):
    for i in range(0, n):
        print(txt)

def páros_e(n):
    return n%2 == 0

def összeg(a,b):
    return a+b

kiir("Zozo")
üdv()
kiir_sokszor("Zozo", 5)
print(páros_e(5))
hello()
szum = összeg(10,5)
print(szum)

def ketbetu(txt):
    return txt[0] + txt[-1]


def atlag(szamok:list):
    összeg = 0
    for sz in szamok:
        összeg = összeg + sz
    return összeg / len(szamok)
        

print(ketbetu("Balaton"))
print(ketbetu("Zozó"))

print(atlag([320,540,870,350,600,230,130]))

