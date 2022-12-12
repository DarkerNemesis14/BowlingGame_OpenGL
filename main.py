import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from utils import Algorithms

class Bowling:
    def __init__(self, display = (900, 900)) -> None:
        self.algorithms = Algorithms(display)
        self.display = display
        self.ballCentre = (0, -(self.display[1]+500))
        self.ballTrans = (0, 0)
        self.ballFactor = 1
        self.pinLoc = [-700, -800, -900, -1000, -1100]
        self.score = 0
        self.rate = pg.time.Clock()
        glClear(GL_COLOR_BUFFER_BIT)

    def __drawRamp(self):
        self.algorithms.MPLine((-(self.display[1]+700), self.display[1]-200), (self.display[1]+700, self.display[1]-200))
        self.algorithms.MPLine((0, -(self.display[1]+500)), (0, self.display[1]-200), (90, 0), 3)
        self.algorithms.MPLine((0, -(self.display[1]+500)), (0, self.display[1]-200), (-90, 0), -3)
        self.algorithms.MPLine((0, -(self.display[1]+500)), (0, self.display[1]-200), (240, 0), 7)
        self.algorithms.MPLine((0, -(self.display[1]+500)), (0, self.display[1]-200), (-240, 0), -7)
        self.algorithms.MPLine((0, -(self.display[1]+500)), (0, self.display[1]-200), (390, 0), 12)
        self.algorithms.MPLine((0, -(self.display[1]+500)), (0, self.display[1]-200), (-390, 0), -12)

    def __drawBall(self):
        self.algorithms.MPCircle(self.ballCentre, 100, self.ballTrans, self.ballFactor)

    def __drawPin(self, centre: tuple):
        self.algorithms.MPCircle(centre, 20)
        self.algorithms.MPLine(centre, (centre[0], centre[1]-100))
        self.algorithms.MPLine(centre, (centre[0]+30, centre[1]-100))

    def __drawPins(self, range: list):
        for loc in range:
            self.__drawPin((-(self.display[1]+loc), self.display[1] - 150))
    
    def __drawScore(self):
        trFac = [self.display[1]+400, self.display[1]+200]
        for dig in str(self.score)[::-1]:
            self.algorithms.digit(dig, (trFac[0], trFac[1]))
            trFac[0] -= 70


    def run(self):
        zone = 0
        opFlag = True
        shoot = False

        pg.init()
        pg.display.set_mode(self.display, DOUBLEBUF|OPENGL)
        pg.display.set_caption("Bowling")

        gluPerspective(40, self.display[0]/ self.display[1], 1, 10)
        glTranslate(0.0, 0.0, -10)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if self.ballTrans[0] > -600:
                            self.ballTrans = (self.ballTrans[0] - 200, self.ballTrans[1])
                            zone -= 1
                    if event.key == K_RIGHT:
                        if self.ballTrans[0] < 600:
                            self.ballTrans = (self.ballTrans[0] + 200, self.ballTrans[1])
                            zone += 1
                    
                    if event.key == K_SPACE:
                        shoot = True
                    if event.key == K_ESCAPE:
                        shoot = False
                        zone = 0
                        self.pinLoc = [-700, -800, -900, -1000, -1100]
                        self.ballTrans = (0, 0)
                        self.ballFactor = 1
                        opFlag = True


            glBegin(GL_POINTS)
            self.__drawRamp()
            if self.ballTrans[1] < 2100:
                self.__drawBall()
            self.__drawPins(self.pinLoc)
            self.__drawScore()
            glEnd()


            if shoot:
                if zone == 0:
                    self.ballTrans = (self.ballTrans[0], self.ballTrans[1] + 50)
                    self.ballFactor -= .01
                elif zone < 0:
                    self.ballTrans = (self.ballTrans[0] + 4, self.ballTrans[1] + 50)
                    self.ballFactor -= .01
                elif zone > 0:
                    self.ballTrans = (self.ballTrans[0] - 4, self.ballTrans[1] + 50)
                    self.ballFactor -= .01

            if self.ballTrans[1] > 2100 and opFlag:
                if zone == 0:
                    self.pinLoc = []
                    self.score += 5
                elif zone == -2:
                    self.pinLoc = [-800, -900, -1000, -1100]
                    self.score += 1
                elif zone == -1:
                    self.pinLoc = [-700, -1000, -1100]
                    self.score += 2
                elif zone == 1:
                    self.pinLoc = [-700, -800, -1100]
                    self.score += 2
                elif zone == 2:
                    self.pinLoc = [-700, -800, -900, -1000]
                    self.score += 1
                opFlag = False


            pg.display.flip()
            glClear(GL_COLOR_BUFFER_BIT)
            self.rate.tick(40)


if __name__ == '__main__':
    obj = Bowling()
    obj.run()