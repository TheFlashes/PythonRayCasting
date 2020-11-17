from ConsoleTweaks import ConsoleTweaks
from Hero import Hero
from Map import Map
from Getch import _Getch

class Game:
    map = Map("map.txt", 24)
    hero = Hero()
    getch = _Getch()

    def __init__(self):
        ConsoleTweaks.clearScreen()
        self.loop()

    def loop(self):
        while True:
            self.map.clearBuffor()

            self.map.draw(self.hero.txt, self.hero.x, self.hero.y)

            buffer = self.map.render2D(self.hero)
            ConsoleTweaks.setCursorPos(0, 0)
            print(buffer)

            key = self.getch()
            if key == b'w':
                self.hero.y -= 1
            elif key == b's':
                self.hero.y += 1
            elif key == b'a':
                self.hero.x -= 1
            elif key == b'd':
                self.hero.x += 1
            elif key == b'q':
                exit()

game = Game()

