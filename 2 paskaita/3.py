#Sukurti programą, kuri:
# Leistų vartotojui po vieną įvesti 5 žodžius
# Pridėtų įvestus žodžius į sąrašą
# Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
# Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
# Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index

zodziai = []

for i in range(5):
    zodziai.append(input("Įveskite žodį: "))

for zodis in zodziai:
    print(zodis, len(zodis), zodziai.index(zodis))