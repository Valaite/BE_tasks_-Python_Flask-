# Sukurti programą, kuri:
# Sukurtų sąrašą iš skaičių nuo 0 iki 50
# for skaicius in range (0, 50):
#     suma = skaicius * 10
#     print(suma)
# Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
skaiciai = list(range(51))
dalijas_is_7 = filter(lambda x: x % 7 == 0, skaiciai)
print(list(dalijas_is_7))
# Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
kvadratu = list(map(lambda x: x**2, skaiciai))
print(list(kvadratu))
# Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir
# didžiausią skaičių, vidurkį, medianą
from statistics import mean, median
print(sum(kvadratu))
print(min(kvadratu))
print(max(kvadratu))
print(mean(kvadratu))
print(median(kvadratu))
# Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
atbulai = sorted(kvadratu, reverse=True)
print(atbulai)

