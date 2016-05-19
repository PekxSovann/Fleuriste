# -*- coding: utf-8 -*-

from math import *
from fonctions import *
from Fleur import *

import time
import os

fleurs = list()
nb = int(input("Nombre de fleurs : "))

for i in range(nb):
    fleurs.append(Fleur())

continuer = True

# Quand sa vitalité atteint 0 elle est meurt.
while continuer:

    en_vie = 0
    print("-----------------------")
    for fleur in fleurs:
        if fleur.tic():
            en_vie += 1

    if en_vie == 0:
        continuer = False

    time.sleep(1/3)

print("-----------------------\n")
os.system("pause")
