#Sukurti programą, kuri:
# Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break

import random

i=0
skaiciai = []

for i in range(3):
   skaiciai.append(random.randint(1, 6))

for x in skaiciai:
    print(x)
    if x == 5:
        print("Pralaimėjai")
        break
else:
    print("Laimėjai")
    