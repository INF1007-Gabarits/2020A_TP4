import random
from tkinter import Frame, Label, CENTER

import logique_corrige as logique
import constantes as c


class GrilleDeJeu(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title(c.TITRE)
        self.master.bind("<Key>", self.touche_appuyee)

        self.commands = {c.TOUCHE_HAUT: logique.faire_translation_haut, c.TOUCHE_BAS: logique.faire_translation_bas,
                         c.TOUCHE_GAUCHE: logique.faire_translation_gauche, c.TOUCHE_DROIT: logique.faire_translation_droite}
        
        self.initialiser_grille()
        self.initialiser_matrice()
        self.mettre_a_jour_cellules_grille()

        self.mainloop()

    def initialiser_grille(self):
        background = Frame(self, bg=c.COULEUR_BACKGROUND_JEU,
                           width=c.TAILLE_GRILLE_EN_PX, height=c.TAILLE_GRILLE_EN_PX)
        background.grid()

        self.cellules_grille = []
        for i in range(c.TAILLE_GRILLE):
            rangee_grille = []
            for j in range(c.TAILLE_GRILLE):
                cell = Frame(background, bg=c.COULEUR_BACKGROUND_TUILE_VIDE,
                             width=c.TAILLE_GRILLE_EN_PX / c.TAILLE_GRILLE,
                             height=c.TAILLE_GRILLE_EN_PX / c.TAILLE_GRILLE)
                cell.grid(row=i, column=j, padx=c.PADDING_GRILLE_EN_PX,
                          pady=c.PADDING_GRILLE_EN_PX)
                t = Label(master=cell, text="",
                          bg=c.COULEUR_BACKGROUND_TUILE_VIDE,
                          justify=CENTER, font=c.POLICE_DE_CARACTERE, width=5, height=2)
                t.grid()
                rangee_grille.append(t)

            self.cellules_grille.append(rangee_grille)

    def initialiser_matrice(self):
        self.matrice = logique.demarrer_jeu()

    def mettre_a_jour_cellules_grille(self):
        for i in range(c.TAILLE_GRILLE):
            for j in range(c.TAILLE_GRILLE):
                nouveau_nombre = self.matrice[i][j]
                if nouveau_nombre == 0:
                    self.cellules_grille[i][j].configure(
                        text="", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)
                else:
                    self.cellules_grille[i][j].configure(text=str(
                        nouveau_nombre), bg=c.COULEUR_BACKGROUND_TUILES[nouveau_nombre],
                        fg=c.COULEUR_TUILES[nouveau_nombre])
        self.update_idletasks()

    def touche_appuyee(self, event):
        touche = repr(event.char)
        if touche in self.commands:
            self.matrice, fini = self.commands[repr(event.char)](self.matrice)
            if fini:
                self.matrice = logique.ajouter_nouveau_2_ou_4(self.matrice)
                self.mettre_a_jour_cellules_grille()
                fini = False

                status = logique.get_etat_jeu_courant(self.matrice)
                if status == c.ETAT_VICTOIRE: 
                    self.cellules_grille[1][1].configure(
                        text="Tu as", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)
                    self.cellules_grille[1][2].configure(
                        text="Gagné!", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)
                if status == c.ETAT_DEFAITE:
                    self.cellules_grille[1][1].configure(
                        text="Tu as", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)
                    self.cellules_grille[1][2].configure(
                        text="Perdu!", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)

grille_de_jeu = GrilleDeJeu()
