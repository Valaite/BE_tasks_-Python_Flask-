# Parašyti programą, kuri:
# Leistų vartotojui įvesti sveiką skaičių.
# Atspausdinti True, jei skaičius teigiamas
# Atspausdinti False, jei skaičius neigiamas ar lygus 0
# True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį ar_skaicius_teigiamas
# Patarimas: naudoti input, boolean, if/else


try:
    skaicius = int(input("Įveskite skaičių: "))
    print(skaicius > 0)
except:
    print("Įvestas klaidingas skaičius")
    
    # ats
while True:
    try:
        print(int(input("Įveskite skaičių: ")) > 0)
        break
    except ValueError:
        print("Įvestas neteisingas skaičius (turi būti sveikasis)")