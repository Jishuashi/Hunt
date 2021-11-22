#coding: utf-8
#Authors - CHARTIER Hugo
#        _ CHARTON SAMUEL
from librairies.tkiteasy import *
from librairies.Point import *
from random import *

RAYON = 10
SPAWN_INIT_PREY = 10
SPAWN_INIT_PRED = 2
D_PREY = 40
CELLSIZE = 30

stageHeight = 900
stageWidth = 900
grid = [ ]
preyList = [ ]
predList = [ ]

def coordinateToRawCol(x, y):
    lPosGrid = Point((x - 15)/30, (y - 15)/30)
    return lPosGrid

def coordinateToCol(x):
    Col = (x - 15)/30
    return Col
def coordinateToRaw(y):
    Raw = (y - 15)/30
    return Raw
def spawnPrey(pIndex):
    i = 0
    
    while i != pIndex:
        lSpawnX = randrange(15, stageHeight, CELLSIZE)
        lSpawnY = randrange(15, stageHeight, CELLSIZE)
        

        lPosGrid = coordinateToRawCol(lSpawnX, lSpawnY)
        
        if(grid[lPosGrid.x][(lPosGrid.y)][0] == False):
            grid[lPosGrid.x][(lPosGrid.y)][0] =  True
            grid[lPosGrid.x][(lPosGrid.y)][1] = 'Prey'
            preyList.append([None, D_PREY, "Prey"])
            preyList[i][0] = g.dessinerDisque(lSpawnX, lSpawnY, RAYON, "green")
            i += 1

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
            grid[i][m] = [False , None]

def testCase(pName, pIndexObj):
    
    print("in function")

    if (pName == "Prey"):
        lPosOnGrid = coordinateToRawCol(preyList[pIndexObj][0].x , preyList[pIndexObj][0].y)
        print(lPosOnGrid.get)
    
    if (pName == 'Pred'):
        print('Pred')



def move(pList):
    lNcellCol = int(stageWidth / CELLSIZE)
    lNCellRaw = int(stageHeight / CELLSIZE)
    
    sleep(0.5)
    
    for i in range(len(pList)):
        posNeg = [1 , -1]

        ranX = CELLSIZE * randrange(0, 2) * posNeg[randrange(0, 2)]
        ranY = CELLSIZE * randrange(0, 2) * posNeg[randrange(0, 2)]
        
        if (coordinateToCol(pList[i][0].x) == 0):
            if (ranX < 0):
                ranX *= -1
        elif (coordinateToCol(pList[i][0].x) == (lNcellCol - 1)):
            if (ranX > 0):
                ranX *= -1
        elif (coordinateToCol(pList[i][0].y) == 0):
            if (ranY < 0):
                ranY *= -1
        elif (coordinateToCol(pList[i][0].y) == (lNCellRaw - 1)):
            if (ranY > 0):
                ranY *= -1
        
        g.deplacer(pList[i][0] , ranX, ranY)

        print(ranX , ranY)       

    

# ouverture de fenêtre
g = ouvrirFenetre(stageWidth, stageHeight)

# afficher image
drawGrid(g, CELLSIZE, 0 , 0, stageHeight , stageWidth)




spawnPrey(SPAWN_INIT_PREY)


#print(grid)
#print(preyList)

while(True):
    g.update()
    move(preyList)


    test = g.recupererClic()

    if(test):
        g.fermerFenetre()
        break
