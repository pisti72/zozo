while True:
    try:
        r = float(input("Kérem a kör rádiuszát?"))
        break
    except:
        print("Kérlek adj be számot!")
terület = r**2
print(terület)