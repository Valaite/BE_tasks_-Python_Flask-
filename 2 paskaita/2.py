#Parašyti programą, kuri:
# Leistų vartotojui įvesti skaičių.
# Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, break

skaicius1 = int(input("Įveskite skaičių: "))
i = 0

if skaicius1 < 0:
    a = skaicius1
    print("neįvestas nė vienas teigiamas skaičius")

while skaicius1 > 0:
    skaicius2 = int(input("Įveskite dar vieną skaičių: "))
    if skaicius2 < 0:
        break
    i += skaicius2
    a = i + skaicius1

print(a)