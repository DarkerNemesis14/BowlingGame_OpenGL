from OpenGL.GL import *

import numpy as np
from math import sin, cos, radians

class Algorithms:
    def __init__(self, display) -> None:
        self.display = display

    def __addPixel(self, cors: tuple) -> None:
        glVertex2f(cors[0] / (self.display[0]/2), cors[1] / (self.display[1]/2))

    def __drawPoint(self, centre: tuple, coOrds: tuple):
        self.__addPixel((centre[0] + coOrds[0], centre[1] + coOrds[1]))

    def __convert(self, x: int, y: int, zone:int, reverse = False):
        dct = {0:(x,y),1:(y,x),2:(y,-x),3:(-x,y),4:(-x,-y),5:(-y,-x),6:(-y,x),7:(x,-y)}
        dctRev = {0:[x,y],1:[y,x],2:[-y,x],3:[-x,y],4:[-x,-y],5:[-y,-x],6:[y,-x],7:[x,-y]}
        if reverse:
            return dctRev[zone]
        return dct[zone]
    
    def __findZone(self, x1: int, y1: int, x2: int, y2: int) -> int:
        dx, dy = x2 - x1, y2 - y1
        if abs(dx) >= abs(dy):
            if dx > 0:
                if dy > 0:
                    return 0
                return 7
            else:
                if dy > 0:
                    return 3
                return 4
        else:
            if dx > 0:
                if dy > 0:
                    return 1
                return 6
            else:
                if dy > 0:
                    return 2
                return 6

    def __drawPoints(self, centre: tuple, x: int, y: int) -> None:
        self.__drawPoint(centre, (x, y))
        self.__drawPoint(centre, self.__convert(x, y, 1))
        self.__drawPoint(centre, self.__convert(x, y, 2))
        self.__drawPoint(centre, self.__convert(x, y, 3))
        self.__drawPoint(centre, self.__convert(x, y, 4))
        self.__drawPoint(centre, self.__convert(x, y, 5))
        self.__drawPoint(centre, self.__convert(x, y, 6))
        self.__drawPoint(centre, self.__convert(x, y, 7))

    def __drawZero(self, init: tuple, trFac = (0,0)):
        self.__line1(init, trFac)
        self.__line2(init, trFac)
        self.__line3(init, trFac)
        self.__line5(init, trFac)
        self.__line6(init, trFac)
        self.__line7(init, trFac)

    def __drawOne(self, init: tuple, trFac = (0,0)):
        self.__line6(init, trFac)
        self.__line7(init, trFac)
    
    def __drawTwo(self, init: tuple, trFac = (0,0)):
        self.__line2(init, trFac)
        self.__line3(init, trFac)
        self.__line4(init, trFac)
        self.__line5(init, trFac)
        self.__line6(init, trFac)

    def __drawThree(self, init: tuple, trFac = (0,0)):
        self.__line3(init, trFac)
        self.__line4(init, trFac)
        self.__line5(init, trFac)
        self.__line6(init, trFac)
        self.__line7(init, trFac)

    def __drawFour(self, init: tuple, trFac = (0,0)):
        self.__line1(init, trFac)
        self.__line4(init, trFac)
        self.__line6(init, trFac)
        self.__line7(init, trFac)
    
    def __drawFive(self, init: tuple, trFac = (0,0)):
        self.__line1(init, trFac)
        self.__line3(init, trFac)
        self.__line4(init, trFac)
        self.__line5(init, trFac)
        self.__line7(init, trFac)
    
    def __drawSix(self, init: tuple, trFac = (0,0)):
        self.__line1(init, trFac)
        self.__line2(init, trFac)
        self.__line3(init, trFac)
        self.__line4(init, trFac)
        self.__line5(init, trFac)
        self.__line7(init, trFac)

    def __drawSeven(self, init: tuple, trFac = (0,0)):
        self.__line3(init, trFac)
        self.__line6(init, trFac)
        self.__line7(init, trFac)

    def __drawEight(self, init: tuple, trFac = (0,0)):
        self.__line1(init, trFac)
        self.__line2(init, trFac)
        self.__line3(init, trFac)
        self.__line4(init, trFac)
        self.__line5(init, trFac)
        self.__line6(init, trFac)
        self.__line7(init, trFac)

    def __drawNine(self, init: tuple, trFac = (0,0)):
        self.__line1(init, trFac)
        self.__line3(init, trFac)
        self.__line4(init, trFac)
        self.__line5(init, trFac)
        self.__line6(init, trFac)
        self.__line7(init, trFac)

    def __line1(self, init: tuple, trFac = (0, 0)):
        self.MPLine((init[0] - 20, init[1]), (init[0] - 20, init[1] + 50), trFac)

    def __line2(self, init: tuple, trFac = (0, 0)):
        self.MPLine((init[0] - 20, init[1]), (init[0] - 20, init[1] - 50), trFac)

    def __line3(self, init: tuple, trFac = (0, 0)):
        self.MPLine((init[0] - 20, init[1] + 50), (init[0] + 20, init[1] + 50), trFac)

    def __line4(self, init: tuple, trFac = (0, 0)):
        self.MPLine((init[0] - 20, init[1]), (init[0] + 20, init[1]), trFac)
    
    def __line5(self, init: tuple, trFac = (0, 0)):
        self.MPLine((init[0] - 20, init[1] - 50), (init[0] + 20, init[1] - 50), trFac)

    def __line6(self, init: tuple, trFac = (0, 0)):
        self.MPLine((init[0] + 20, init[1]), (init[0] + 20, init[1] + 50), trFac)

    def __line7(self, init: tuple, trFac = (0, 0)):
        self.MPLine((init[0] + 20, init[1]), (init[0] + 20, init[1] - 50), trFac)

    def digit(self, digit: str, init: tuple, trFac = (0,0)):
        dct = {'0': self.__drawZero, '1': self.__drawOne, '2': self.__drawTwo, '3': self.__drawThree, '4': self.__drawFour, '5': self.__drawFive, '6': self.__drawSix, '7': self.__drawSeven, '8': self.__drawEight, '9': self.__drawNine}
        dct[digit](init, trFac)
        
    def __translate(self, tsMat: np.array, points: tuple) -> None:
        temp = np.matmul(tsMat, np.array([[float(points[0])], [float(points[1])], [1.]]))
        return (temp[0], temp[1])

    def __rotate(self, rtMat: np.array, points: tuple) -> None:
        temp = np.matmul(rtMat, np.array([[float(points[0])],[float(points[1])],[1.]]))
        return (temp[0], temp[1])

    def MPLine(self, p1: tuple, p2: tuple, trFac = (0, 0), degree = 0) -> None:
        trnMatLine = np.array([[1, 0, trFac[0]],[0, 1, trFac[1]],[0, 0, 1]])
        rotMatLine = np.array([[cos(radians(degree)), -sin(radians(degree)), 0],[sin(radians(degree)), cos(radians(degree)), 0],[0, 0, 1]])

        x1, y1 = map(int, self.__translate(trnMatLine, self.__rotate(rotMatLine, p1)))
        x2, y2 = map(int, self.__translate(trnMatLine, self.__rotate(rotMatLine, p2)))

        zone = self.__findZone(x1, y1, x2, y2)
        x1, y1 = self.__convert(x1, y1, zone)
        x2, y2 = self.__convert(x2, y2, zone)

        dx, dy, y = x2 - x1, y2 - y1, y1
        d = 2*dy - dx

        for x in range(x1, x2 + 1):
            wx, wy = self.__convert(x, y, zone, reverse = True)
            self.__addPixel((wx, wy))
            if d > 0:
                d += 2*(dy - dx)
                y += 1
            else:
                d += 2*dy

    def MPCircle(self, centre: tuple, r: int, trFac = (0, 0), scFac = 1) -> None:
        trnMatCir = np.array([[1, 0, trFac[0]],[0, 1, trFac[1]],[0, 0, 1]])
        centre = self.__translate(trnMatCir, centre)
        r *= scFac
        d, x, y = 1 - r, r, 0

        while x > y:
            self.__drawPoints(centre, x, y)

            y += 1
            if d < 0:
                d += 2*y + 1
            else:
                x -= 1
                d += 2*y - 2*x + 1