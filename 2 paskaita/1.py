sarasas = [5, 2, 6]
amzius = {"Rokas": 20, "Andrius": 34, "Laura": 25}

#Atspausdinti vieną norimą įrašą
print(sarasas[1])
print(amzius["Andrius"])
#Pridėti įrašą
amzius["Aiste"] = 35
sarasas.append(11)
print(sarasas)
print(amzius)
#Ištrinti įrašą
sarasas.pop(0)
print(sarasas)

del amzius["Rokas"]
print(amzius)

#pakeisti įrašą
amzius["Laura"] = 24
print(amzius)

sarasas[1]=3
print(sarasas)

#Išbandyti kitas sąrašų ir žodynų funkcijas: 

# index()
x = sarasas.index(11)
print(x)

# insert()
sarasas.insert(0, 25)
print(sarasas)

# remove
sarasas.remove(2)
print(sarasas)
#clear()
sarasas.clear()
print(sarasas)