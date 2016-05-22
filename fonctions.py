# -*- coding: utf-8 -*-

from random import *


def alea(x):
    """Renvoie True avec une probabilité de x%"""
    if random() * 100 < x:
        return True
    else:
        return False


def sauvegarder_partie():
    """Sauvegarde les paramètres et la progression dans le jeu dans un pickler
    ( dossier en binaire )"""
    pass


def charger_partie():
    """"""
    pass


def charger_parametres():
    """Extrait les paramètres d'un fichier texte dedié"""
    with open('parametres.txt', 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.split()
        parametres = dict()
        for ligne in lignes:
            parametre = ligne.split("=")
            parametres[parametre[0]] = parametre[1]
        return parametres