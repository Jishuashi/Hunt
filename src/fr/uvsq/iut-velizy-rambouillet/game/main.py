#coding: utf-8
from librairies.tkiteasy import *


# ouverture de fenêtre
g = ouvrirFenetre(800,600)

# afficher image
pacman = g.afficherImage(400,300,"./assets/pacman.png")

# fermeture fenêtre
input("fermer-fenetre - attendreClic Bloquant")
g.attendreClic()
g.fermerFenetre()
