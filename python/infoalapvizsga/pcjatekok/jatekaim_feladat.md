# Minta Feladatsor – Ágazati Alapvizsga (Programozás)

**Téma:** PC játékok nyilvántartása  
**Adatfájl:** `jatekaim.csv` (fejléccel, pontosvesszővel elválasztva)  
**Mezők:** `cím` ; `műfaj` ; `fejlesztő` ; `év` ; `ár (Ft)` ; `értékelés (1–10)`

---

## 1. feladat – Osztály és beolvasás *(kötelező)*

Hozz létre egy `Jatek` osztályt, amely tárolja egy játék következő adatait:
`cim`, `mufaj`, `fejleszto`, `ev` (egész), `ar` (egész), `ertekeles` (egész).

Olvasd be a `jatekaim.csv` fájl összes sorát (a fejlécet hagyd ki),
és töltsd egy `jatekok` nevű listába!

---

## 2. feladat – Listázás

Írd ki minden játék adatát a következő formában:

```
[cím] ([év]) - [fejlesztő] - [ár] Ft - értékelés: [értékelés]/10
```

---

## 3. feladat – Darabszám

Írd ki, hogy összesen hány játék van a nyilvántartásban!

---

## 4. feladat – Ingyenes játékok

Listázd ki azokat a játékokat, amelyek ára **0 Ft** (ingyenesen játszható)!

---

## 5. feladat – Maximum

Melyik a **legdrágább** játék? Írd ki a nevét és árát!

---

## 6. feladat – Legjobb értékelés

Melyik játék kapta a **legjobb értékelést**? Írd ki a nevét és értékelését!

---

## 7. feladat – Szűrés műfaj alapján

Kérj be egy műfajt a felhasználótól, és listázd ki az összes olyan játékot,
amely abba a műfajba tartozik (cím és fejlesztő elég)!

---

## 8. feladat – Feltételes számlálás

Hány játék értékelése **9 vagy 10**?

---

## 9. feladat – Átlagszámítás

Számítsd ki és írd ki az összes játék **átlagárát** (ingyenes játékokat is beleszámítva)!

---

## 10. feladat – Fájlba írás

Írd ki egy `top_jatekok.txt` nevű fájlba azoknak a játékoknak a **CÍMÉT és ÉRTÉKELÉSÉT**,
amelyek értékelése **10/10**!

---

## Bónusz feladat – Metódus

A `Jatek` osztályba írj egy `kategoria()` metódust, amely visszaadja:
- `"Kötelező"` – ha az értékelés 9 vagy 10
- `"Ajánlott"` – ha az értékelés 7 vagy 8
- `"Opcionális"` – ha az értékelés 6 vagy kevesebb

Írd ki minden játékhoz a kategóriáját!
