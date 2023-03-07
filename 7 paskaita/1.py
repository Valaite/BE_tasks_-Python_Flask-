# Python faile padaryti šiuos veiksmus (atskirai, ne iškart):
# Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu, 
import datetime
print(datetime.datetime.today())
# tik datą (date.today()) 
print(datetime.date.today())
# bei tik laiką (.now().time()).
print(datetime.datetime.now().time())
# Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą.

from datetime import date

print(date.today())

# Iš paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.

from datetime import date as data

print(data.today())



try:
    print(12/0)
except:
    print("Dalyba")
    
print("vykdoma")


sk = 12
if sk % 2 == 0:
    print("lyg")
if sk % 2 != 0:
    print("nelyg")
if sk % 3 == 0:
    print("3")