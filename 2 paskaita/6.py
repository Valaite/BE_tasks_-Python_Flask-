#Perdaryti 5 užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.


for metai in range(1900, 2100):
    if metai % 400 == 0:
        print(metai)
    elif metai % 100 == 0:
        continue
    elif metai % 4 == 0:
        print(metai)
    else:
        continue
