# -*- coding: utf-8 -*-

from math import *
from fonctions import *
from Fleur import *

import time
import os

f = Fleur()

# Quand sa vitalité atteint 0 elle est meurt.
while f.vitalite > 0:
    print(f.croissance, f.hydratation, f.vitalite)

    # La plante se desseche
    f.eau(-2)

    # La plante regenere lentement
    f.vie(1)

    # La plante grandit
    f.dvp(1)

    # Une hydratation trop ou pas assez elevée baisse la vitalité
    if f.hydratation < 50 or f.hydratation > 120:
        f.vie(-3)

    # Atteindre 100 de croissance fait baisser la vitalité
    if f.croissance == 100:
        f.vie(-2)

    # Arrosage aléatoire par la pluie
    if alea(10):
        f.eau(20)

    time.sleep(1/3)

print("Flowey est morte !")
os.system("pause")
