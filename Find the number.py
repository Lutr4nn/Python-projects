#Make by Lutr4nn
# -*- coding: utf-8 -*-

import random
from tkinter import *

class JeuNombreAleatoire:
    def __init__(self, mainapp):
        self.mainapp = mainapp
        self.nombre_a_trouver = random.randint(1, 100)
        self.essaie = 0
        self.essaie_max = 10
        self.essaie_restant = self.essaie_max
        
        self.setup_ui()

    def setup_ui(self):
        self.mainapp.config(bg="light blue")
        self.mainapp.title("Lutr4nn - Find the number")
        
        screen_x = int(self.mainapp.winfo_screenwidth())
        screen_y = int(self.mainapp.winfo_screenheight())
        window_x, window_y = 1200, 600
        posX = (screen_x // 2) - (window_x // 2)
        posY = (screen_y // 2) - (window_y // 2)
        self.mainapp.geometry(f"{window_x}x{window_y}+{posX}+{posY}")
        
        self.label_regle = Label(self.mainapp, text="Bienvenue dans ce jeu, \n vous disposez de 10 essais pour trouver un nombre choisi aléatoirement entre 1 et 100", font=("arial", 14), bg="light blue")
        self.label_regle.pack()
        
        self.label_renvoie = Label(self.mainapp, text="Entrez un nombre entre 0 et 100", bg="light blue")
        self.label_renvoie.pack()
        
        self.entree_nombre = Entry(self.mainapp, exportselection=0)
        self.entree_nombre.pack()

        self.bouton_envoyer = Button(self.mainapp, text="Envoyer ce nombre", command=self.verifier_nombre, bg="light blue")
        self.bouton_envoyer.pack()

        self.bouton_recommencer = Button(self.mainapp, text="Nouvelle partie", command=self.nouvelle_partie)

        self.label_nombre_essais = Label(self.mainapp, text=f"Essais restants : {self.essaie_restant}")
        self.label_nombre_essais.pack()

        self.bouton_quitter = Button(self.mainapp, text="Quitter le jeu", command=self.mainapp.quit, bg="red")
        self.bouton_quitter.place(relx=1.0, rely=0.0, anchor='ne')

        self.mainapp.bind('<Return>', lambda event: self.verifier_nombre())
    
    def verifier_nombre(self):
        try:
            nombre_utilisateur = int(self.entree_nombre.get())
            if nombre_utilisateur < 1 or nombre_utilisateur > 100:
                self.label_renvoie.config(text="Le nombre doit être entre 1 et 100")
                self.entree_nombre.delete(0, END)
                return
        except ValueError:
            self.label_renvoie.config(text="Veuillez entrer un nombre valide")
            self.entree_nombre.delete(0, END)
            return
        
        if self.essaie < self.essaie_max:
            self.essaie += 1
            self.essaie_restant -= 1
            self.label_nombre_essais.config(text=f"Essais restants : {self.essaie_restant}")
            self.entree_nombre.delete(0, END)
            
            if nombre_utilisateur == self.nombre_a_trouver:
                self.label_renvoie.config(text="Bien joué ! Vous avez trouvé le bon nombre")
                self.bouton_envoyer.pack_forget()
                self.bouton_recommencer.pack()
            elif nombre_utilisateur < self.nombre_a_trouver:
                self.label_renvoie.config(text="Le nombre à trouver est plus grand")
            else:
                self.label_renvoie.config(text="Le nombre à trouver est plus petit")
            
            if self.essaie == self.essaie_max and nombre_utilisateur != self.nombre_a_trouver:
                self.label_renvoie.config(text=f"Vous avez perdu ! Le nombre à trouver était : {self.nombre_a_trouver}")
                self.bouton_envoyer.pack_forget()
                self.bouton_recommencer.pack()
        else:
            self.label_renvoie.config(text="Une nouvelle partie ?")

    def nouvelle_partie(self):
        self.nombre_a_trouver = random.randint(1, 100)
        self.essaie = 0
        self.essaie_restant = self.essaie_max
        self.entree_nombre.delete(0, END)
        self.bouton_envoyer.pack()
        self.label_renvoie.config(text="Entrez un nombre entre 0 et 100")
        self.bouton_recommencer.pack_forget()

if __name__ == "__main__":
    mainapp = Tk()
    JeuNombreAleatoire(mainapp)
    mainapp.mainloop()
