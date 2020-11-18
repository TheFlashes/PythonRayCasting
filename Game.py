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
            self.map.clearBuffor()

            self.map.draw(self.hero.txt, self.hero.x, self.hero.y)

            self.render3D.render(self.hero, self.map)

            buffer = self.map.render2D(self.hero)
            ConsoleTweaks.setCursorPos(0, 0)
            print(buffer)
            print("x: {}, y: {}     ".format(self.hero.x, self.hero.y))
            """
            key = self.getch()
            if key == 'w':
                self.hero.y -= 1
            elif key == 's':
                self.hero.y += 1
            elif key == 'a':
                self.hero.x -= 1
            elif key == 'd':
                self.hero.x += 1
            elif key == 'q':
                exit()
            """
            time.sleep(0.075)

game = Game()

