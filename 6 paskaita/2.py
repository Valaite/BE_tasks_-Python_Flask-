# Sukurti programą, kuri:
# Turėtų klasę Darbuotojas
# Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo

# Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos 
# dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)

# Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, 
# paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)

import datetime

class Darbuotojas():
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo
        
    def nudirbo_dienu(self):
        nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y, %m, %d, %H, %M, %S")
        dabar = datetime.datetime.today()
        skirtumas = dabar - nuo_kada_dirba
        return skirtumas.days
    
    def sk_atlyginimas(self):
        atlyginimas = round(self.valandos_ikainis * self.nudirbo_dienu() * 8)
        print(self.vardas + " uždirbo " + str(atlyginimas) + " Eur")


# Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų 
# atlyginimą, dirbant darbuotojui 5 dienas per savaitę

class Normalus_darbuotojas(Darbuotojas):
    def nudirbo_dienu(self):
        nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y, %m, %d, %H, %M, %S")
        dabar = datetime.datetime.today()
        skirtumas = dabar - nuo_kada_dirba
        dirbo_dienu = skirtumas.days / 7 * 5
        return dirbo_dienu

# Sukurti norimą Darbuotojo objektą
darbuotojas1 = Darbuotojas("Saulius", 15, "2020, 03, 12, 12, 00, 00")
darbuotojas1.nudirbo_dienu()

# Sukurti norimą NormalusDarbuotojas objektą
darbuotojas2 = Normalus_darbuotojas("Paulius", 15, "2020, 03, 12, 12, 00, 00")
darbuotojas2.nudirbo_dienu()

# Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima
darbuotojas1.sk_atlyginimas()
darbuotojas2.sk_atlyginimas()