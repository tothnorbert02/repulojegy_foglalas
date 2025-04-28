
class Legitarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def add_jarat(self, jarat):
        self.jaratok.append(jarat)

    def add_foglalas(self, foglalas):
        self.foglalasok.append(foglalas)

    def remove_foglalas(self, foglalasi_szam):
        for foglalas in self.foglalasok:
            if foglalas.foglalasi_szam == foglalasi_szam:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def find_jarat(self, jaratszam):
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None

    def find_foglalas(self, foglalasi_szam):
        for foglalas in self.foglalasok:
            if foglalas.foglalasi_szam == foglalasi_szam:
                return foglalas
        return None

    def list_foglalasok(self):
        if not self.foglalasok:
            print("Nincs foglalás.")
        else:
            for foglalas in self.foglalasok:
                print(foglalas)
