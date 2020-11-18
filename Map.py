class Map:
    __map = []
    __buffer = []
    mapWidth = -1
    mapHeight = -1

    __rW = 0
    __rH = 0

    def __init__(self, mapPath, renderDistance):
        self.__rW = renderDistance
        self.__rH = int(renderDistance / 2.5)

        mapFile = open(mapPath, "r")
        
        fileWidth = len(mapFile.readline())
        for x in range(fileWidth - 1):
            mapFile.seek(0)
            mapColumn = []
            bufferColumn = []
            for y in mapFile:
                mapColumn.append(y[x])
                bufferColumn.append(" ")
            self.__map.append(mapColumn)
            self.__buffer.append(bufferColumn)
        
        self.mapWidth = len(self.__map)
        self.mapHeight = len(self.__map[0])

        mapFile.close()

    def render2D(self, hero):
        buffer = "╔"
        for x in range(self.__rW * 2):
            buffer += "═"
        buffer += "╗\n"

        for y in range (hero.y - self.__rH, hero.y + self.__rH):
            buffer += "║"
            for x in range (hero.x - self.__rW, hero.x + self.__rW):
                if x < 0 or y < 0 or x > self.mapWidth - 1 or y > self.mapHeight - 1:
                    buffer += " "
                elif self.__buffer[x][y] != " ":
                    buffer += self.__buffer[x][y]
                else:
                    buffer += self.__map[x][y]
            buffer += "║\n"

        buffer += "╚"
        for x in range(self.__rW * 2):
            buffer += "═"
        buffer += "╝"
        return buffer

    def freeAt(self, xF, yF):
        x = int(xF)
        y = int(yF)
        if x < 0 or y < 0 or x >= self.mapWidth or y >= self.mapHeight:
            return False
        elif self.__map[x][y] == " ":
            return True
        else:
            return False

    def draw(self, str, x, y):
        for ch in str:
            if x < 0 or y < 0:
                continue
            if x >= self.mapWidth or y >= self.mapHeight:
                break
            self.__buffer[x][y] = ch

    def clearBuffor(self):
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.__buffer[x][y] = " "
                