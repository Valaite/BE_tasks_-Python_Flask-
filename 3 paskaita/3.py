# Parašyti programą, kuri:
# Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
import datetime
while True:
    try:
        ivesta_data = input("Įveskite gimimo datą: pvz. (YYYY-MM-DD HH:MM:SS) ")
        data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %X")
        break
    except:
        print("Įvestas netinkamas datos skaičius")

# Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
skirtumas = (datetime.datetime.now() - data)
# # Metų
print(round(skirtumas.days/365))
# Mėnesių
print(round(skirtumas.days/365*12))
# Savaičių 
print(round(skirtumas.days/7))
# # Dienų
print(skirtumas.days)
# # Valandų
print(round(skirtumas.total_seconds()/3600))
# # Minučių
print(round(skirtumas.total_seconds()/60))
# # Sekundžių
print(skirtumas.total_seconds())
# Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
# Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):
# skaicius = 4.66
# print(round(skaicius))