# -*- coding: utf-8 -*-


class Fleur:
    """
    Classe représentant la fleur, elle possède comme caractéristiques:
    - Croissance : int en %
    - Hydratation : int en % ( peut depasser 100 )
    - Vitalité : int en %
    - Resistances : dictionnaire :
        - Clé : string "NomResistance"
        - Valeur : int en %

    - Maladie : dictionnaire :
        -
        - pass

    Une hydratation trop ou pas assez elevée baisse la vitalité
    La resistance est la chance de ne pas subir l'influance d'un evenement
    Atteindre 100 de croissance fait baisser la vitalité
    Quand sa vitalité atteint 0 elle est meurt.
    """
    # Espace pour les paramètres de classe

    def __init__(self):

        self.croissance = 0
        self.hydratation = 100
        self.vitalite = 100
        self.resistances = dict()
        # self.maladies = dict()

    def eau(self, quantite):

        if self.hydratation + quantite <= 0:
            self.hydratation = 0
        else:
            self.hydratation += quantite

    def dvp(self, quantite):

        if quantite < 0:
            raise ValueError("La croissance ne peut être que positive")

        if self.croissance + quantite > 100:
            self.croissance = 100
        else:
            self.croissance += quantite

    def vie(self, quantite):

        if self.vitalite + quantite > 100:
            self.vitalite = 100
        elif self.vitalite + quantite < 0:
            self.vitalite = 0
        else:
            self.vitalite += quantite
