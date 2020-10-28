import random
from tkinter import Frame, Label, CENTER

import logique
import constantes as c


class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title(c.TITRE)
        self.master.bind("<Key>", self.key_down)

        self.commands = {c.TOUCHE_HAUT: logique.bouger_matrice_en_haut, c.TOUCHE_BAS: logique.bouger_la_matrice_en_bas,
                         c.TOUCHE_GAUCHE: logique.bouger_matrice_a_gauche, c.TOUCHE_DROIT: logique.bouger_matrice_a_droite}
        
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.COULEUR_BACKGROUND_JEU,
                           width=c.TAILLE_GRILLE_EN_PX, height=c.TAILLE_GRILLE_EN_PX)
        background.grid()

        self.grid_cells = []
        for i in range(c.NB_CHIFFRE_DANS_GRILLE):
            grid_row = []
            for j in range(c.NB_CHIFFRE_DANS_GRILLE):
                cell = Frame(background, bg=c.COULEUR_BACKGROUND_TUILE_VIDE,
                             width=c.TAILLE_GRILLE_EN_PX / c.NB_CHIFFRE_DANS_GRILLE,
                             height=c.TAILLE_GRILLE_EN_PX / c.NB_CHIFFRE_DANS_GRILLE)
                cell.grid(row=i, column=j, padx=c.PADDING_GRILLE_EN_PX,
                          pady=c.PADDING_GRILLE_EN_PX)
                t = Label(master=cell, text="",
                          bg=c.COULEUR_BACKGROUND_TUILE_VIDE,
                          justify=CENTER, font=c.POLICE_DE_CARACTERE, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = logique.demarrer_jeu()

    def update_grid_cells(self):
        for i in range(c.NB_CHIFFRE_DANS_GRILLE):
            for j in range(c.NB_CHIFFRE_DANS_GRILLE):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.COULEUR_BACKGROUND_TUILES[new_number],
                        fg=c.COULEUR_TUILES[new_number])
        self.update_idletasks()

    def key_down(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = logique.ajouter_nouveau_2_ou_4(self.matrix)
                self.update_grid_cells()
                done = False

                status = logique.get_etat_jeu_courant(self.matrix)
                if status == 'WON': 
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)
                if status == 'LOST':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=c.COULEUR_BACKGROUND_TUILE_VIDE)

gamegrid = GameGrid()
