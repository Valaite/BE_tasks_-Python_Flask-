

eilute = "Zen of Python"

#Atspausdintų paskutinį antro žodžio simbolį
print(eilute[5])
print(eilute[-8])
#Atspausdintų pirmą trečio žodžio simbolį
print(eilute[7])
print(eilute[-6])
#Atspausdintų tik pirmą žodį
print(eilute[:3])
#Atspausdintų tik paskutinį žodį
print(eilute[7:])
#Atspausdintų visą frazę atbulai
print(eilute[::-1])
#Atskirtų žodžius ir juos atspausdintų
print(eilute.split())
#Žodį "Python" pakeistų į "Programming" ir atspausdintų naują sakinį
print(eilute.replace('Python', 'Programming'))

print(eilute.upper())
print(eilute.casefold())
print(eilute.capitalize())
print(eilute.count('o'))
print(eilute.find('Zen'))
