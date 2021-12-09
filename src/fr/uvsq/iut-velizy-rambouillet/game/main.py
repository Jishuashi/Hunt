#coding: utf-8
#Authors - CHARTIER Hugo 
#        - CHARTON SAMUEL
from librairies.tkiteasy import *
from librairies.Point import *
from random import *

RAYON = 10
SPAWN_INIT_PREY = 20
SPAWN_INIT_PRED = 2
D_PREY = 40
D_PRED = 0
CELLSIZE = 30
TIME_CYCLE = 20

aroundCaseOnGrid = [Point(30,-30), Point(-30,30), Point(30,0), Point(0,30), Point(-30,0), Point(0,-30), Point(30,30), Point(-30,-30)]
stageHeight = 900
stageWidth = 900
grid = [ ]
preyList = [ ]
predList = [ ]
cycleTime = 0

def coordinateToRawCol(x, y):
    lPosGrid = Point((x - 15)/30, (y - 15)/30)

    if(lPosGrid.x >= 30):
        lPosGrid.set_x = 29
    if(lPosGrid.y >= 30):
        lPosGrid.set_y = 29
    if(lPosGrid.x < 0):
        lPosGrid.set_x = 0
    if(lPosGrid.y < 0):
        lPosGrid.set_y = 0

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
            grid[lPosGrid.x][(lPosGrid.y)][1] = "Prey"
            preyList.append([None, D_PREY, "Prey", True])
            preyList[i][0] = g.dessinerDisque(lSpawnX, lSpawnY, RAYON, "lime")
            i += 1

            g.update()

def spawnPred(pIndex):
    i = 0
    
    while i != pIndex:
        lSpawnX = randrange(15, stageHeight, CELLSIZE)
        lSpawnY = randrange(15, stageHeight, CELLSIZE)
        

        lPosGrid = coordinateToRawCol(lSpawnX, lSpawnY)
        
        if(grid[lPosGrid.x][(lPosGrid.y)][0] == False):
            grid[lPosGrid.x][(lPosGrid.y)][0] =  True
            grid[lPosGrid.x][(lPosGrid.y)][1] = 'Pred'
            predList.append([None, D_PRED, "Pred"])
            predList[i][0] = g.dessinerDisque(lSpawnX, lSpawnY, RAYON, "orange")
            i += 1

            g.update()



def drawGrid(pObjGraph, pCellSize, pEndY, pEndX):
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

def testCaseMove(pName, pIndexObj, pNextPos):

    if (pName == "Prey"):
        lPosOnGrid = coordinateToRawCol(pNextPos.x , pNextPos.y)

        if(grid[lPosOnGrid.x][lPosOnGrid.y][0]):
            return False
        else :
            return True
        
    
    if (pName == 'Pred'):
        return True

def testCaseSpawn(pCoord):
    lPosOnGrid = coordinateToRawCol(pCoord.x , pCoord.y)

    if(grid[lPosOnGrid.x][lPosOnGrid.y][0]):
        return False
    else :
        return True
    

def updatePosGrid (pLastPos, pNextPos):
    lPosOnGrid = coordinateToRawCol(pLastPos.x , pLastPos.y)
    lNextPosOnGrid = coordinateToRawCol(pNextPos.x , pNextPos.y)

    grid[lNextPosOnGrid.x][lNextPosOnGrid.y] = grid[lPosOnGrid.x][lPosOnGrid.y]
    grid[lPosOnGrid.x][lPosOnGrid.y] = [False, None]

def updateDeathGrid(pPos):
    lPosOnGrid = coordinateToRawCol(pPos.x , pPos.y)
    grid[lPosOnGrid.x][lPosOnGrid.y] = [False, None]

def death(pList):
    sleep(0.25)
    lIndex = len(pList) - 1

    #print(lIndex)

    if(len(pList) != 0 and len(pList) > 0):

        while lIndex >= 0:
            if(len(pList) != 0 and len(pList) > 0):

                if (pList[lIndex][1] <= 0):
                    updateDeathGrid(Point(pList[lIndex][0].x, pList[lIndex][0].y))
                    g.supprimer(pList[lIndex][0])
                    pList.remove(pList[lIndex])
                else :
                    pList[lIndex][1] -= 1
                
                lIndex -= 1  
                #print(lIndex)


def testCaseArroud(pList):
    lIndex = len(pList) - 1
    while lIndex !=0 :
        
        lPosOfObj = Point(pList[lIndex][0].x, pList[lIndex][0].y)

        for i in range(len(aroundCaseOnGrid)):
            lTestPos = Point((aroundCaseOnGrid[i].x + lPosOfObj.x),  (aroundCaseOnGrid[i].y + lPosOfObj.y))
            lTestCase = coordinateToRawCol(lTestPos.x, lTestPos.y)
            if(pList[lIndex][3]):
                pList[lIndex][3] = False
                if (grid[lTestCase.x][lTestCase.y][0] == True):
                    if (grid[lTestCase.x][lTestCase.y][1] == "Prey"):
                        birthPrey(True, lPosOfObj, lTestPos, pList)
                        break
        lIndex -= 1                    


def move(pList):
    lNcellCol = int(stageWidth / CELLSIZE)
    lNCellRaw = int(stageHeight / CELLSIZE)
    
    sleep(0.25)
    
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
        
        lNextPos = Point((ranX + pList[i][0].x), (ranY + pList[i][0].y))

        if (testCaseMove(pList[i][2], i, lNextPos)):
            lPrevPos = Point(pList[i][0].x , pList[i][0].y)
            updatePosGrid(lPrevPos, lNextPos)
            g.deplacer(pList[i][0] , ranX, ranY)
            testCaseArroud(pList)
            
def birthPrey(pBirth = False, pCoord1 = None,  pCoord2 = None, Plist = None):
    
    if (pBirth == False):
        while True:
            lSpawnX = randrange(15, stageHeight, CELLSIZE)
            lSpawnY = randrange(15, stageHeight, CELLSIZE)
        

            lPosGrid = coordinateToRawCol(lSpawnX, lSpawnY)
        
            if(grid[lPosGrid.x][(lPosGrid.y)][0] == False):
                grid[lPosGrid.x][(lPosGrid.y)][0] =  True
                grid[lPosGrid.x][(lPosGrid.y)][1] = 'Prey'
                preyList.append([None, D_PREY, "Prey", True])
                preyList[(len(preyList) - 1)][0] = g.dessinerDisque(lSpawnX, lSpawnY, RAYON, "blue")

                g.update()
                break
    else :
        lListOfCoord = [pCoord1, pCoord2]
        lListCoordPoss = [ ]

        for m in range(len(lListOfCoord)):
            for i in range(len(aroundCaseOnGrid)):
                
                lNextPos = Point(aroundCaseOnGrid[i].x + lListOfCoord[m].x, aroundCaseOnGrid[i].y + lListOfCoord[m].y)

                if (testCaseSpawn(lNextPos)):
                    print("yo")
                else : 
                    lListCoordPoss.append([lNextPos, m])

        lRandomIndex = randint(0, len(lListCoordPoss) - 1)


        lRandPos = Point(lListCoordPoss[lRandomIndex][0].x + lListOfCoord[lListCoordPoss[lRandomIndex][1]].x , lListCoordPoss[lRandomIndex][0].y + lListOfCoord[lListCoordPoss[lRandomIndex][1]].y)

        lPosGrid = coordinateToRawCol(lRandPos.x , lRandPos.y)

        grid[lPosGrid.x][lPosGrid.y][0] =  True
        grid[lPosGrid.x][lPosGrid.y][1] = 'Prey'
        preyList.append([None, D_PREY, "Prey", True])
        preyList[(len(preyList) - 1)][0] = g.dessinerDisque(lRandPos.x + 15 , lRandPos.y + 15 , RAYON, "red")
        return
        

        

        


#ouverture de fenêtre
g = ouvrirFenetre(stageWidth, stageHeight)

#afficher image
drawGrid(g, CELLSIZE, stageHeight , stageWidth)




spawnPrey(SPAWN_INIT_PREY)
#spawnPred(SPAWN_INIT_PRED)

while(True):
    g.update()
    move(preyList)
    cycleTime +=1

    if (cycleTime >= TIME_CYCLE):
        cycleTime = 0
        birthPrey() 
    
    
    #move(predList)

    death(preyList)


    test = g.recupererClic()

    if(test):
        g.fermerFenetre()
        break
