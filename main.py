
from belfoldijarat import BelfoldiJarat
from nemzetkozijarat import NemzetkoziJarat
from legitarsasag import Legitarsasag
from jegyfoglalas import JegyFoglalas

def main():
    legitarsasag = Legitarsasag("ChatAir")

    jarat1 = BelfoldiJarat("B1", "Debrecen", 15000)
    jarat2 = NemzetkoziJarat("N1", "London", 50000)
    jarat3 = NemzetkoziJarat("N2", "New York", 80000)
    legitarsasag.add_jarat(jarat1)
    legitarsasag.add_jarat(jarat2)
    legitarsasag.add_jarat(jarat3)

    foglalas1 = JegyFoglalas(1, jarat1, "Kiss János")
    foglalas2 = JegyFoglalas(2, jarat1, "Nagy Anikó")
    foglalas3 = JegyFoglalas(3, jarat2, "Peter Parker")
    foglalas4 = JegyFoglalas(4, jarat2, "Mary Jane")
    foglalas5 = JegyFoglalas(5, jarat3, "Hulk Hogan")
    foglalas6 = JegyFoglalas(6, jarat3, "Bruce Wayne")
    legitarsasag.add_foglalas(foglalas1)
    legitarsasag.add_foglalas(foglalas2)
    legitarsasag.add_foglalas(foglalas3)
    legitarsasag.add_foglalas(foglalas4)
    legitarsasag.add_foglalas(foglalas5)
    legitarsasag.add_foglalas(foglalas6)

    while True:
        print("\n--- Repülőjegy foglalási rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy opciót (1-4): ")

        if valasztas == '1':
            jaratkod = input("Add meg a járat kódját: ")
            jarat = legitarsasag.find_jarat(jaratkod)
            if jarat:
                utas_nev = input("Add meg az utas nevét: ")
                foglalasi_szam = len(legitarsasag.foglalasok) + 1
                foglalas = JegyFoglalas(foglalasi_szam, jarat, utas_nev)
                legitarsasag.add_foglalas(foglalas)
                print(f"Sikeres foglalás! Foglalási szám: {foglalasi_szam}, Ár: {jarat.jegyar} Ft")
            else:
                print("Hibás járat kód!")
        elif valasztas == '2':
            szam = input("Add meg a törlendő foglalási számot: ")
            try:
                szam = int(szam)
                if legitarsasag.remove_foglalas(szam):
                    print("Foglalás sikeresen törölve.")
                else:
                    print("Nem található ilyen foglalási szám.")
            except ValueError:
                print("Érvénytelen foglalási szám.")
        elif valasztas == '3':
            legitarsasag.list_foglalasok()
        elif valasztas == '4':
            print("Kilépés a rendszerből...")
            break
        else:
            print("Hibás opció, próbáld újra!")

if __name__ == "__main__":
    main()
