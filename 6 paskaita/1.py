# Sukurti programą, kuri:
# Turėtų klasę Automobilis
# Automobilis turėtų savybes: metai, modelis, kuro_tipas
# Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie atitinkamai 
# atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
# Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą

class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        
    def vaziuoti(self):
        print("Važiuoja")
        
    def stoveti(self):
        print("Priparkuota")
        
    def pildyti_degalu(self):
        print("Degalai įpilti")
        
    def __str__(self):
        return f"{self.metai}, modelis: {self.modelis}, {self.kuro_tipas} "

# Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
# Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, 
# kad jis atspausdintų „Baterija įkrauta“
# Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“

class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")
        
    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")
        

# Sukurti norimą Automobilio objektą

auto1 = Automobilis(2022, "Ibiza", "D")
print(auto1)

# Sukurti norimą Elektromobilio objektą

auto2 = Elektromobilis(2021, "Prius", "EV")
print(auto2)

# Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu

auto1.vaziuoti()
auto1.stoveti()
auto1.pildyti_degalu()

# Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti, 
# pildyti_degalu, vaziuoti_autonomiskai

auto2.vaziuoti()
auto2.stoveti()
auto2.pildyti_degalu()
auto2.vaziuoti_autonomiskai()