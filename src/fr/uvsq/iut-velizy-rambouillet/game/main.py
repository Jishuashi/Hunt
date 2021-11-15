#coding: utf-8
from librairies.tkiteasy import *
from librairies.Point import *
from random import *


cellSize = 30
stageHeight = 900
stageWidth = 900
grid = [ ]
RAYON = 10

def drawProie():
    spawnX = randrange(15, stageHeight, cellSize)
    spawnY = randrange(15, stageHeight, cellSize)
    Ligne = (spawnX - 15)/30
    Col = (spawnY - 15)/30
    g.dessinerDisque(spawnX, spawnY, RAYON, "green")
    g.update()

def drawGrid(pObjGraph, pCellSize, pOriginX, pOriginY, pEndY, pEndX):
    lOriginX = pOriginX
    lOriginY = pOriginY

    lStartLigneCol = 0
    lStartLigneRaw = 0

    lNcellCol = int(stageWidth / pCellSize)
    lNCellRaw = int(stageHeight / pCellSize)
    for j in range(lNcellCol):

        lCol = pObjGraph.dessinerLigne(lStartLigneCol, 0, lStartLigneCol , pEndY, "white")
        pObjGraph.update()
        
        lStartLigneCol += pCellSize
        grid.append({})
        


    for i in range(lNCellRaw):
        
        lRaw = pObjGraph.dessinerLigne(0, lStartLigneRaw, pEndX, lStartLigneRaw, "white")
        pObjGraph.update()
        lStartLigneRaw += pCellSize
        
        for m in range(lNCellRaw):
            grid[i][str(m)] = [False , None]
    
    
        

# ouverture de fenêtre
g = ouvrirFenetre(stageWidth, stageHeight)

# afficher image
drawGrid(g, cellSize, 0 , 0, stageHeight , stageWidth)

print(grid)
drawProie()

while(True):

    test = g.recupererClic()
    g.update()

    if(test):
        g.fermerFenetre()
