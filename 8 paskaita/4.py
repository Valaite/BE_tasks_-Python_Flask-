# Sukurti programą, kuri:
# Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius
        
    def __repr__(self):
        return (f"({self.vardas}, {self.amzius})")

# Inicijuoti kelis Zmogus objektus su vardais ir amžiais
zmogus1 = Zmogus("Monika", 64)
zmogus2 = Zmogus("Justas", 58)
zmogus3 = Zmogus("Jonas", 44)
zmogus4 = Zmogus("Aiste", 88)

# Įdėti sukurtus Zmogus objektus į naują sąrašą
sarasas = [zmogus1, zmogus2, zmogus3, zmogus4]

# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)

# Patarimai:
# Naudoti sorted, attrgetter, reverse, funkciją repr


vardas_surikiuotas = sorted(sarasas, key=attrgetter("vardas"))
print(vardas_surikiuotas)

vardas_surikiuotas_atgal = sorted(sarasas, key=attrgetter("vardas"), reverse=True)
print(vardas_surikiuotas_atgal)

amzius_surikiuotas = sorted(sarasas, key=attrgetter("amzius"))
print(amzius_surikiuotas)

amzius_surikiuotas_atgal = sorted(sarasas, key=attrgetter("amzius"), reverse=True)
print(amzius_surikiuotas_atgal)
 