# Sukurkite ir išsibandykite funkcijas, kurios:
# 1. Gražintų trijų paduotų skaičių sumą.
def skaiciu_suma(num1, num2, num3):
    suma = (num1 + num2 + num3)
    return suma
print(skaiciu_suma(2,9,8))

# 2. Gražintų paduoto sąrašo iš skaičių, sumą.
def saraso_suma(sarasas):
    skaiciu_suma = 0 
    for skaicius in sarasas:
        skaiciu_suma += skaicius
    return skaiciu_suma
sarasas = [1, 9, 8, 9, 92, 4]
print(saraso_suma(sarasas))

# 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
def did_sk(*args):
    max = args[0]
    for skaicius in args:
        if skaicius > max:
            max = skaicius
    return max

print(did_sk(2,6,9,8,11))

# 4. Gražintų paduotą stringą atbulai.
def atbulai(stringas):
    return (stringas[::-1])

print(atbulai("katinas"))

# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
def info(stringas):
    lower=0
    upper=0
    number=0
    words = (len(stringas.split()))
    for i in stringas:
      if i.islower():
            lower+=1
      if i.isupper():
            upper+=1
      if i.isnumeric():
            number+=1
    print (f"Upper: {upper}, lower: {lower}, numbers: {number} words: {words} ")

info ("Mano batai buvo 2")

# 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
def unikalus(*args):
 # initialize a null list
    unique_list = []
    for x in args:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list
        
print(unikalus(1,1,66,5,6,4,4,2,8,2,3))

# 7. Gražintų, ar paduotas skaičius yra pirminis.

def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True;
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True


print(test_prime(5))

# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

def nuo_galo(stringas):
    atskirti_zodziai = stringas.split()[::-1]
    return " # ".join(atskirti_zodziai)

print(nuo_galo("Mano batai buvo keturi"))
    
# 9. Gražina, ar paduoti metai yra keliamieji, ar ne.

def keliamieji_metai(metai):
    if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
        print("keliamieji metai")
    else:
        print("Nekeliamieji metai")

keliamieji_metai (1991)

#10. Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.
import datetime
def kiek_praejo(date):
    data = datetime.datetime.strptime(date, "%Y-%m-%d %X")
    skirtumas = (datetime.datetime.now() - data)
    print(round(skirtumas.days/365))
    print(round(skirtumas.days/365*12))
    print(skirtumas.days)
    print(round(skirtumas.total_seconds()/3600))
    print(round(skirtumas.total_seconds()/60))
    print(skirtumas.total_seconds())

kiek_praejo("1984-06-11 00:00:00")
