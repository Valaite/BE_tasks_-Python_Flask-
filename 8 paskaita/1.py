# Sukurti programą, kuri:
# Prie kiekvieno sakinio „The Zen of Python tekstu“ žodžio pridėtų šauktuką ir atspausdintų naują sakinį.
sakinys = "The Zen of Python"
zodziu_sarasas = ("! ".join(sakinys.split(" ")))
print(zodziu_sarasas)
# Patarimai:
# Naudoti map (su lambda) arba comprehension, " ".join()

sakinys = "The Zen of Python"

naujas = map(lambda x: x + "!", sakinys.split())
print(" ".join(naujas))

# arba:

naujas = [x + "!" for x in sakinys.split()]
print(" ".join(naujas))