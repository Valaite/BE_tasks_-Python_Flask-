# Sukurti programą, kuri:
# Leistų vartotojui įvesti norimą eilučių kiekį
# Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą

# Patarimai:
# Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)

tekstas = ""

while True:
    ivestas_tekstas = input("Iveskite tekstą: ")
    if ivestas_tekstas != "":
        tekstas += ivestas_tekstas + "\n"
    else:
        break

failo_pav = input("Failo pavadinimas: ")
with open(failo_pav + ".txt", "w", encoding="UTF-8") as f:
    f.write(tekstas)