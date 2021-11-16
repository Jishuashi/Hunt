#coding: utf-8
#Authors - CHARTIER Hugo
#        _ CHARTON SAMUEL

from librairies.tkiteasy import *
from librairies.Point import *
from random import *


cellSize = 30
stageHeight = 900
stageWidth = 900
grid = [ ]
RAYON = 10
SPAWN_INIT_PREY = 10
SPAWN_INIT_PRED = 2 
D_PREY = 40



def coordinateToRawCol(x, y):
    lPosGrid = Point((x - 15)/30, (y - 15)/30)
    return lPosGrid


def spawnPrey():
    while True:
        lSpawnX = randrange(15, stageHeight, cellSize)
        lSpawnY = randrange(15, stageHeight, cellSize)

        lPosGrid = coordinateToRawCol(lSpawnX, lSpawnY)
        
        if(grid[lPosGrid.x][(lPosGrid.y)][0] == False):
            grid[lPosGrid.x][(lPosGrid.y)][0] =  True
            grid[lPosGrid.x][(lPosGrid.y)][1] = 'Prey'
            g.dessinerDisque(lSpawnX, lSpawnY, RAYON, "green")
            g.update()
            break

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
            grid[i][m] = [False , None]
    
    
        

# ouverture de fenêtre
g = ouvrirFenetre(stageWidth, stageHeight)

# afficher image
drawGrid(g, cellSize, 0 , 0, stageHeight , stageWidth)



for i in range(SPAWN_INIT_PREY):
    spawnPrey()

print(grid)
g.afficherTexte(SPAWN_INIT_PREY, 450, 10)
while(True):

    test = g.recupererClic()
    g.update()

    if(test):
        g.fermerFenetre()
