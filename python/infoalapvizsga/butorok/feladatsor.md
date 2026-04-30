# Minta Feladatsor – Ágazati Alapvizsga (Programozás)

**Téma:** Bútoráruház nyilvántartás  
**Adatfájl:** `butorok.txt` (fejléc nélkül, szóközzel elválasztva)  
**Mezők:** `kód` ; `típus` ; `szín` ; `ár (Ft)`

---

## 1. feladat – Osztály és beolvasás *(kötelező)*

Hozz létre egy `Butor` osztályt, amely tárolja egy bútor következő adatait:
`kod`, `tipus`, `szin`, `ar` (egész).

Olvasd be a `butorok.txt` fájl összes sorát,
és töltsd egy `butorok` nevű listába!

---

## 2. feladat – Listázás

Írd ki minden bútor adatát a következő formában:

```
[kód] ---> [típus] ([szín]) - [ár] Ft
```

---

## 3. feladat – Darabszám

Írd ki, hogy összesen hány bútor van a nyilvántartásban!

---

## 4. feladat – Összegzés

Számítsd ki és írd ki az összes bútor árának összegét!

---

## 5. feladat – Maximum

Melyik a **legdrágább** bútor? Írd ki a kódját, típusát és árát!

---

## 6. feladat – Minimum

Melyik a **legolcsóbb** bútor? Írd ki a kódját, típusát és árát!

---

## 7. feladat – Szűrés

Listázd ki csak a `"szek"` típusú bútorok kódját és színét!

---

## 8. feladat – Feltételes számlálás

Hány bútor ára haladja meg az **50 000 Ft**-ot?

---

## 9. feladat – Felhasználói keresés

Kérj be egy színt a felhasználótól!  
- Ha van ilyen színű bútor a listában, írd ki az összes ilyen bútor kódját és típusát.  
- Ha nincs, írd ki: `"Nem található ilyen színű bútor."`

---

## 10. feladat – Fájlba írás

Írd ki egy `dragak.txt` nevű fájlba azoknak a bútoroknak a **kódját és árát**,
amelyek ára meghaladja az **50 000 Ft**-ot!

---

## Bónusz feladat – Metódus

A `Butor` osztályba írj egy `akcio(szazalek)` metódust,
amely visszaadja az adott százalékkal csökkentett árat!  
Mutasd be a legdrágább bútoron **20%-os** akcióval!
