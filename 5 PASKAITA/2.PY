import datetime

# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.)
class Sukaktis:
    def __init__(self,metai=2000, menuo=12, diena=12, valandos=12, minutes=12):
        self.metai = metai
        self.menuo = menuo
        self.diena = diena
        self.valandos = valandos
        self.minutes = minutes
        self.data = datetime.datetime(metai, menuo, diena, valandos, minutes)
        
# Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
    def praejo(self):
        now = datetime.datetime.now()
        skirtumas = now - self.data
        print(skirtumas.days/365)
        print(round(skirtumas.days/365*12))
        print(round(skirtumas.days/7))
        print(skirtumas.days)
        print(round(skirtumas.total_seconds()/3600))
        print(round(skirtumas.total_seconds()/60))
        print(skirtumas.total_seconds())
    
# Gražina, ar nurodytos sukakties metai buvo keliamieji
    def keliamieji_metai(self):
        if (self.metai % 400 == 0) or (self.metai % 100 != 0 and self.metai % 4 == 0):
            print("keliamieji metai")
        else:
            print("Nekeliamieji metai")

# Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą

    def atimtiDienas(self, dienos):
        return self.data - datetime.timedelta(days=dienos)


# Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

    def pridetiDienas(self, dienos):
        return self.data + datetime.timedelta(days=dienos)


    def __str__(self):
        return (
            f"Data: {self.metai}-{self.menuo}-{self.diena} {self.valandos}:{self.minutes}")
        
        
date1 = Sukaktis(2014, 8, 14, 15, 15)
date1.praejo()
date1.keliamieji_metai()
print(date1.atimtiDienas(5))
print(date1.pridetiDienas(45))
print(date1)