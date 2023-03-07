from app import db, Signature

db.create_all()  # sukurs mūsų lentelę DB

# Iš karto inicijuosime testams keletą įrašų:
jonas = Signature('Jonas', 'Bailys', 'Kažkoks labai rimtas atsiliepimas.')
antanas = Signature('Antanas', 'Kairys', 'Antano nuomonė labai svarbi.')
juozas = Signature('Juozas', 'Gaidys', 'Aš labai piktas, nes blogai.')
bronius = Signature('Bronius', 'Baublys', 'Aš tai linksmas esu, man patinka.')

# Pridėsime šiuos veikėjus į mūsų DB
db.session.add_all([jonas, antanas, juozas, bronius])
# .commit išsaugo pakeitimus
db.session.commit()

print(jonas.id)
print(antanas.id)
print(bronius.id)
print(juozas.id)

# 1
# 2
# 4
# 3