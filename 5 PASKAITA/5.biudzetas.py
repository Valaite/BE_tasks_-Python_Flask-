# Padaryti minibiudžeto programą, kuri:
# Leistų vartotojui įvesti pajamas
# Leistų vartotojui įvesti išlaidas
# Programa turi turėti klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) 
# ir suma. Galima prirašyti str metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas 
# objektas.
class Įrašas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f"{self.tipas}: {self.suma}"
    
# Leistų vartotojui parodyti pajamų/išlaidų balansą
# Programa turi turėti klasę Biudzetas, kurioje būtų:
# Metodas init, kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai
# Metodas prideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
# Metodas prideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
# Metodas gauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą.
# Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
# Metodas parodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).

class Balansas:
    def __init__(self):
        self.sarasas = []
        
    def prideti_pajamu_irasa(self, suma):
        pajamos = Įrašas("Pajamos", suma)
        self.sarasas.append(pajamos)
        
    def prideti_islaidu_irasa(self, suma):
        islaidos = Įrašas("Išlaidos", suma)
        self.sarasas.append(islaidos)
        
    def gauti_balansa(self):
        suma = 0
        for irasas in self.sarasas:
            if irasas.tipas == "Pajamos":
                suma += irasas.suma
            if irasas.tipas == "Islaidos":
                suma -= irasas.suma
        print(suma)
        
    def parodyti_ataskaita(self):
        for irasas in self.sarasas:
            print(f"{irasas.tipas}: {irasas.suma}")

balansas = Balansas()

# Leistų vartotojui išeiti iš programos

while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        balansas.prideti_pajamu_irasa(suma)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        balansas.prideti_islaidu_irasa(suma)
    if pasirinkimas == 3:
        balansas.gauti_balansa()
    if pasirinkimas == 4:
        balansas.parodyti_ataskaita()
    if pasirinkimas == 9:
        print("Viso gero")
        break


