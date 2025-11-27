try:
    szám = int(input("Kérek egy számot: "))
    eredmény = 10 / szám
    print(f"Eredmény: {eredmény}")
except ValueError:
    print("Hiba: Ez nem egy érvényes szám!")
except ZeroDivisionError:
    print("Hiba: Nullával nem lehet osztani!")
except Exception as e:
    print(f"Váratlan hiba: {e}")