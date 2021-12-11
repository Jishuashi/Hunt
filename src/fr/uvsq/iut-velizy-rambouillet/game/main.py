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
TIME_CYCLE = 10
TIME_CYCLE2 = 10

aroundCaseOnGrid = [Point(30,-30), Point(-30,30), Point(30,0), Point(0,30), Point(-30,0), Point(0,-30), Point(30,30), Point(-30,-30)]
stageHeight = 900
stageWidth = 900
grid = [ ]
preyList = [ ]
predList = [ ]
cycleTime = 0
cycleTime2 = 0

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
            grid[lPosGrid.x][(lPosGrid.y)][2] = i
            preyList.append([None, D_PREY, "Prey", True, [ ]])
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
            grid[lPosGrid.x][(lPosGrid.y)][2] = i
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
            grid[i][m] = [False , None, -1]

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
    grid[lPosOnGrid.x][lPosOnGrid.y] = [False, None, -1]

def updateDeathGrid(pPos, pList):
    lPosOnGrid = coordinateToRawCol(pPos.x , pPos.y)
    grid[lPosOnGrid.x][lPosOnGrid.y] = [False, None, -1]

    for i in range(len(pList)):
        
        lPosOnGridObj = coordinateToRawCol(pList[i][0].x , pList[i][0].y)

        grid[lPosOnGridObj.x][lPosOnGridObj.y] = [grid[lPosOnGridObj.x][lPosOnGridObj.y][0], grid[lPosOnGridObj.x][lPosOnGridObj.y][0], i]
        

def death(pList):
    sleep(0.25)
    lIndex = len(pList) - 1

    #print(lIndex)

    if(len(pList) != 0 and len(pList) > 0):

        while lIndex >= 0:
            if(len(pList) != 0 and len(pList) > 0):

                if (pList[lIndex][1] <= 0):
                    updateDeathGrid(Point(pList[lIndex][0].x, pList[lIndex][0].y), pList)
                    g.supprimer(pList[lIndex][0])
                    pList.remove(pList[lIndex])
                else :
                    pList[lIndex][1] -= 1
                
                lIndex -= 1  
                #print(lIndex)
    
def testCaseBirth(pList, pListCord):
    for i in range(len(pList)):
        if(pList[i][3]):
            lPosObj = Point(pList[i][0].x, pList[i][0].y)

            for m in range(len(pListCord)):

                lArroundCaseTest = coordinateToRawCol(lPosObj.x + pListCord[m].x, lPosObj.y + pListCord[m].y)

                if(grid[lArroundCaseTest.x][lArroundCaseTest.y][0]):
                    if(grid[lArroundCaseTest.x][lArroundCaseTest.y][1] == "Prey"):
                        
                        lObj = pList[i][0]
                        lIndexObj2 = grid[lArroundCaseTest.x][lArroundCaseTest.y][2]
                        lObj2 = pList[lIndexObj2][0]

                        for j in range(len(pList[i][4])):
                            if (pList[i][4][j] == lIndexObj2):
                                print("YUUUUUUUUUUUUUUUUUUu")
                                return
                        
                        pList[i][3] = False
                        pList[grid[lArroundCaseTest.x][lArroundCaseTest.y][2]][3] = False
                        
                        birthPrey(True, lObj, lObj2)
                         
                    elif(grid[lArroundCaseTest.x][lArroundCaseTest.y][1] == "Pred"):
                        pass
            
            
            
            
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
            testCaseBirth(pList, aroundCaseOnGrid)
            
            
def birthPrey(pBirth = False, pObj1 = None,  pObj2 = None):
    
    if (pBirth == False):
        while True:
            lSpawnX = randrange(15, stageHeight, CELLSIZE)
            lSpawnY = randrange(15, stageHeight, CELLSIZE)
        

            lPosGrid = coordinateToRawCol(lSpawnX, lSpawnY)
        
            if(grid[lPosGrid.x][(lPosGrid.y)][0] == False):
                grid[lPosGrid.x][(lPosGrid.y)][0] =  True
                grid[lPosGrid.x][(lPosGrid.y)][1] = 'Prey'
                
                
                preyList.append([None, D_PREY, "Prey", True, [ ]])
                preyList[(len(preyList) - 1)][0] = g.dessinerDisque(lSpawnX, lSpawnY, RAYON, "blue")

                g.update()
                break
    else :
        
        lObj = pObj1
        lObj2 = pObj2

        lPosCoord = [ ]
       
        for i in range(len(aroundCaseOnGrid)):
            lPos1 = Point(lObj.x + aroundCaseOnGrid[i].x, lObj.y + aroundCaseOnGrid[i].y)
            lPos2 = Point(lObj2.x + aroundCaseOnGrid[i].x, lObj2.y + aroundCaseOnGrid[i].y)
           

            if(lPos2.get != (lObj.x, lObj.y) or lPos1.get != (lObj2.x, lObj2.y)):
                lPosCoord.append(Point(lObj.x + aroundCaseOnGrid[i].x, lObj.y + aroundCaseOnGrid[i].y))
                lPosCoord.append(Point(lObj2.x + aroundCaseOnGrid[i].x, lObj2.y + aroundCaseOnGrid[i].y))
        
        lGridCoord1 = coordinateToRawCol(lPos1.x , lPos1.y)
        lGridCoord2 = coordinateToRawCol(lPos2.x , lPos2.y)

        lIndexObj1 = grid[lGridCoord1.x][lGridCoord1.y][2]
        lIndexObj2 = grid[lGridCoord2.x][lGridCoord2.y][2]

        preyList[lIndexObj1][4].append(len(preyList))
        preyList[lIndexObj2][4].append(len(preyList))


        lRandIndex = randrange(0, len(lPosCoord))
        lRandPos = lPosCoord[lRandIndex]
        
        lRandCoordGrid = coordinateToRawCol(lRandPos.x, lRandPos.y)

        grid[lRandCoordGrid.x][(lRandCoordGrid.y)][0] =  True
        grid[lRandCoordGrid.x][(lRandCoordGrid.y)][1] = "Prey"
        preyList.append([None, D_PREY, "Prey", False, [ ]])
        grid[lRandCoordGrid.x][(lRandCoordGrid.y)][1] = (len(preyList) - 1)
        preyList[(len(preyList) - 1)][0] = g.dessinerDisque(lRandPos.x, lRandPos.y, RAYON, "Red")



        

        

        


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
    cycleTime2 +=1

    if (cycleTime >= TIME_CYCLE):
        cycleTime = 0
        birthPrey()

    if (cycleTime2 >= TIME_CYCLE2):
        for i in range(len(preyList)):
            preyList[i][3] = True

        cycleTime2
        
    
    #print(preyList)
    #move(predList)
    death(preyList)


    test = g.recupererClic()
    

    if(test):
        g.fermerFenetre()
        break
