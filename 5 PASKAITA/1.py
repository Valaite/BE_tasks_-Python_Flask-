# Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:
class Sakinys:
    def __init__(self, tekstas="Zen of Python"):
        self.tekstas = tekstas

# Gražina tekstą atbulai
    def atbulai(self):
        print(self.tekstas[::-1])
        
# Gražina tekstą mažosiomis raidėmis
    def mazosios(self):
        print(self.tekstas.lower())
        
# Gražina tekstą didžiosiomis raidėmis
    def didziosios(self):
        print(self.tekstas.upper())
        
# Gražina žodį pagal nurodytą eilės numerį
    def numeris(self, num):
        suskirstytas = self.tekstas.split()
        index = num - 1
        word = suskirstytas[index]
        print(word)
            
# Gražina, kiek tekste yra nurodytų simbolių arba žodžių
    def ieskoti(self, ieskomas):
        print(self.tekstas.count(ieskomas))
    
# Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu      
    def pakeisti(self, senas, naujas):
        print(self.tekstas.replace(senas, naujas))
    
# Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
    def info(self):
        
        upper=0
        number=0
        lower=0
        for i in self.tekstas:
            if i.islower():
                lower+=1
            if i.isupper():
                upper+=1
            if i.isnumeric():
                number+=1
        words = len(self.tekstas.split())
        print(f"Upper: {upper}, lower: {lower}, numbers: {number} words: {words} ")
   
tekstas1 = Sakinys("Mano batai buvo 2")
tekstas1.atbulai()
tekstas1.mazosios()
tekstas1.didziosios()
tekstas1.numeris(1)
tekstas1.ieskoti("a")
tekstas1.pakeisti("Mano", "Tavo")
tekstas1.info()

print(tekstas1)





