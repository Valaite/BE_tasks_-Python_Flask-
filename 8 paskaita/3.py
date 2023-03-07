# Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# Sukurti programą, kuri:
# Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą

sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

skaiciai = sum(filter(lambda s: type(s) is int or type(s) is float, sarasas))

print(skaiciai)

# Sudėtų ir atspausdintų visus sąrašo žodžius

zodziai = filter(lambda s: type(s) is str, sarasas)
sakinys = " ".join(zodziai)
print(sakinys)

# Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme

boolean = filter(lambda s: type(s) is bool, sarasas)

print(sum(boolean))

