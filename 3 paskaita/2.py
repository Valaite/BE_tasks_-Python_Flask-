# Parašyti programą, kuri:
# Atspausdintų dabartinę datą ir laiką
import datetime

now = datetime.datetime.today()
print(now)
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
print(now - datetime.timedelta(days=5))
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
print(now + datetime.timedelta(hours=8))
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
print(now.strftime("%Y %m %d, %H:%M:%S"))

# https://www.w3schools.com/python/python_datetime.asp 



