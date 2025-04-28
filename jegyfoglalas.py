
class JegyFoglalas:
    def __init__(self, foglalasi_szam, jarat, utas_nev):
        self.foglalasi_szam = foglalasi_szam
        self.jarat = jarat
        self.utas_nev = utas_nev

    def __str__(self):
        return (f"Foglalási szám: {self.foglalasi_szam}, Utas: {self.utas_nev}, "
                f"Járat: {self.jarat.jaratszam}, Cél: {self.jarat.celallomas}, Ár: {self.jarat.jegyar} Ft")
