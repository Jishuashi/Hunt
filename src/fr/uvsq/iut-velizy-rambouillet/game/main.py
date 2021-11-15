#coding: utf-8
from librairies.tkiteasy import *
from librairies.Point import *


cellSize = 30
stageHeight = 900
stageWidth = 930

def drawGrid(pObjGraph, pCellSize, pOriginX, pOriginY, pEndY, pEndX):
    lOriginX = pOriginX
    lOriginY = pOriginY

    lStartLigneCol = 0
    lStartLigneRaw = 0

    lNcellCol = int(stageWidth / pCellSize)
    lNCellRaw = int(stageHeight / pCellSize)

    for i in range(lNCellRaw):
        
        lRaw = pObjGraph.dessinerLigne(0, lStartLigneRaw, pEndX, lStartLigneRaw, "white")
        pObjGraph.update()
        lStartLigneRaw += pCellSize
    
    for j in range(lNcellCol):

        lCol = pObjGraph.dessinerLigne(lStartLigneCol, 0, lStartLigneCol , pEndY, "white")
        pObjGraph.update()
        
        lStartLigneCol += pCellSize
        

# ouverture de fenêtre
g = ouvrirFenetre(stageWidth, stageHeight)

# afficher image
drawGrid(g, cellSize, 0 , 0, stageHeight , stageWidth)

while(True):

    test = g.recupererClic()
    g.update()

    if(test):
        g.fermerFenetre()
