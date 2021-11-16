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
SPAWN_RATE_PREY = 10
SPAWN_RATE_PRED = 2 

def coordinateToRawCol(x, y):
    posGrid = Point((x - 15)/30, (y - 15)/30)
    return posGrid

def drawProie():
    while True:
        spawnX = randrange(15, stageHeight, cellSize)
        spawnY = randrange(15, stageHeight, cellSize)
        
        if(grid[coordinateToRawCol(spawnX, spawnY).x][(coordinateToRawCol(spawnX, spawnY).y)][0] == False):
            grid[coordinateToRawCol(spawnX, spawnY).x][(coordinateToRawCol(spawnX, spawnY).y)][0] =  True
            grid[coordinateToRawCol(spawnX, spawnY).x][(coordinateToRawCol(spawnX, spawnY).y)][1] = 'Prey'
            g.dessinerDisque(spawnX, spawnY, RAYON, "green")
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
    
    
        
for i in range(SPAWN_RATE_PREY):
    spawnProie()


print(grid)

while(True):

    test = g.recupererClic()
    g.update()

    if(test):
        g.fermerFenetre()
