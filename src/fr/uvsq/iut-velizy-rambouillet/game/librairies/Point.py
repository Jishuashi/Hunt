#Author : Chartier Hugo
from math import *

class Point:
    """ Crée un point de Coordonnée X Y
        X -> int
        Y -> int """
    
    def __init__(self, x , y):
        #constructeur de Point attrbut à x et y les valeur d'appel
        self._x = int(x)
        self._y = int(y)

    @property
    def x(self):
        #retourne  la coord x
        return self._x

    @property
    def y(self):
        #retourne  la coord y
       return self._y

    @x.setter
    def set_x(self, pX):
        #Defini la coord x selon pX
        self._x = pX

    @y.setter
    def set_y(self, pY):
        #Defini la coord y selon pY
        self._y = pY
    

    @property
    def get(self):
        #Retourne le Point -> (x, y)

        return (self.x, self.y)


    @staticmethod
    def vectorBetweenPoint(pA, pB) -> tuple:
        """Calcul Le vecteur entre deux points
            pA -> Point
            pB -> Point """

        lVector = Point((pB.x - pA.y), (pB.y - pA.y))
        return lVector.get

    @staticmethod
    def getDistanceBetweenPoint(pA , pB) -> float:
        """Calcul la distance entre deux points
            pA -> Point
            pB -> Point """

        lDistance = 0

        lDistance = sqrt(((pA.x - pB.x) * (pA.x - pB.x)) + ((pA.y - pB.y) * (pA.y - pB.y)))
        return lDistance

    @staticmethod
    def cartesianToPolar(pA) -> tuple:
        """Transforme des coordonées Cartésienne en coordonées Polaire"""
        RADTODEG = 180/pi

        lR = 0
        lAngle = 0


        lR = floor(sqrt((pA.x * pA.x)+ (pA.y * pA.y)))
        lAngle = tanh((pA.y/pA.x))

        lAngle *= RADTODEG

        return (lR, ceil(lAngle))


    @staticmethod
    def polarToCartesian(pA) -> tuple:
        """Transforme des coordonées Polaire en coordonées Cartésienne"""
        lX = 0
        lY = 0

        DEGTORAD = pi/180

        lAngle = pA.y * DEGTORAD

        lX = ceil(pA.x * cos(lAngle))
        lY = ceil(pA.x * sin(lAngle))

        return (lX, lY)

    @staticmethod
    def normalize(pA) -> tuple:
        """Normalise le vecteur """
        lNorme = sqrt((pA.x * pA.x) + (pA.y * pA.y))

        lNormalizedVector = (pA.x / lNorme, pA.y / lNorme)

        return lNormalizedVector