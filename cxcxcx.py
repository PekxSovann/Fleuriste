# -*- coding: utf-8 -*-

"""
Présentation...
"""


from tkinter import ttk
import tkinter as tk


class MonApplication(object):

    def __init__(self, master):

        # Labels sur la première ligne
        ttk.Label(master, text="Votre nom ?", background='blue').grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Label(master, text="Votre année de naissance ?").grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self.reponse = ttk.Label(master, text="")
        self.reponse.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        # Deuxième ligne
        # Champ de texte
        self.nom_var = tk.StringVar
        self.nom = ttk.Entry(master, width=17, textvariable=self.nom_var)
        self.nom.grid(row=1, column=0, sticky=tk.W)
        self.nom.focus()

        # Boite déroulante
        self.annee_var = tk.StringVar
        self.annee = ttk.Combobox(master, width=17, textvariable=self.annee_var, state='readonly')
        self.annee['values'] = tuple(x for x in range(1970, 2001))
        self.annee.current(0)
        self.annee.grid(row=1, column=1, sticky=tk.W)

        # Boutton à cliquer
        self.bouton_affichage = ttk.Button(master, text="Validez", command=self.clicked)
        self.bouton_affichage.grid(row=1, column=2)

    def clicked(self):
        print(self.reponse)
        age = 2016 - int(self.annee.get())

        if len(self.nom.get()) == 0:
            chaine_reponse = "Entrée non valide !"
        else:
            chaine_reponse = self.nom.get() + " : " + str(age) + " ans"
            self.bouton_affichage.config(state='disabled')

        self.reponse.configure(text=chaine_reponse)
        self.reponse.configure(foreground='red')



def main():
    appli = tk.Tk()
    MonApplication(appli)
    appli.mainloop()


if __name__ == "__main__":
    main()
