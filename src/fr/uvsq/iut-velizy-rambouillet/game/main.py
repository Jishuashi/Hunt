#coding: utf-8
from librairies.tkiteasy import *


# ouverture de fenêtre
g = ouvrirFenetre(800,600)

# afficher image
pacman = g.dessinerCercle(250, 250, 150, "white")

while(True):
    test = g.recupererClic()
    g.update()

    if(test):
        g.fermerFenetre()



