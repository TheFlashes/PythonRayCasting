from ConsoleTweaks import ConsoleTweaks
from Map import Map

class Game:
    map = Map("map.txt")

    def __init__(self):
        self.loop()

    def loop(self):
        buffer = self.map.render()
        ConsoleTweaks.clearScreen()
        print(buffer)

game = Game()

