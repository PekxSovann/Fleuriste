# -*- coding: utf-8 -*-

from math import *
from fonctions import *
from Fleur import *

import time
import os
parametres = charger_parametres()

fleurs = list()
nb = int(input("Nombre de fleurs : "))

for i in range(nb):
    fleurs.append(Fleur())

continuer = True

while continuer:

    en_vie = 0
    print("-----------------------")
    for fleur in fleurs:
        if fleur.tic():
            en_vie += 1

    if en_vie == 0:
        continuer = False

    time.sleep(eval(parametres["VitesseTic"]))

print("-----------------------\n")
os.system("pause")
