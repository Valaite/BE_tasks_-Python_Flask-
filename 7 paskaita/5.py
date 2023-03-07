# Sukurti programą, kuri:
# Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
# Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
# Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
# Patarimai:
# Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime

import os
from datetime import datetime

location = "c:/Users/Dell/Downloads/Monika_kursai/BE/ND/7 paskaita"
folder_name = "5_uzd"

print(os.getcwd())

try:
    os.chdir(location)
    os.mkdir(folder_name)
except:
    print("Folder found")
    
os.chdir(location + "/" + folder_name)

with open(folder_name + ".txt", "w") as f:
    f.write(str(datetime.today()))

print(os.stat(folder_name + ".txt").st_size)
