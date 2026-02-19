mertekegyseg = input("Milyen mértékegységben adod meg? (MB,GB) ")
szorzo = int(input('Írd be az átváltandó számot! '))

if mertekegyseg.lower() == 'gb':
    print('Az eredmény:',szorzo*1024, 'MB')
elif mertekegyseg.lower() == 'mb':
    print('Az eredmény:', szorzo/1024,'GB')
else:
    print('Rossz mértékegységet adtál meg!') 