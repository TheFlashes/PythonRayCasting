from ConsoleTweaks import ConsoleTweaks
from Hero import Hero
from Map import Map
from render.Render3D import Render3D
from Getch import _Getch
import time

class Game:
    map = Map("map.txt", 24)
    hero = Hero()
    getch = _Getch()
    render3D = Render3D()

    def __init__(self):
        ConsoleTweaks.clearScreen()
        self.loop()

    def loop(self):
        while True:
            ConsoleTweaks.setCursorPos(0, 0)
            self.render3D.clearBuffer()
            image3D = self.render3D.render(self.hero, self.map)
            print(image3D)
            #while True:
            self.map.clearBuffor()

            #self.map.draw(self.hero.txt, self.hero.x, self.hero.y)

                

            #buffer = self.map.render2D(self.hero)
            
            #print(buffer)
            print("x: {}, y: {}     ".format(self.hero.x, self.hero.y))
            print("angle: {}".format(self.hero.angle))
            key = self.getch()
            if key == 'w':
                self.hero.y -= 0.1
            elif key == 's':
                self.hero.y += 0.1
            elif key == 'a':
                self.hero.x -= 0.1
            elif key == 'd':
                self.hero.x += 0.1
            elif key == 'k':
                self.hero.angle -= 1
            elif key == 'l':
                self.hero.angle += 1
            elif key == 'q':
                exit()

game = Game()

