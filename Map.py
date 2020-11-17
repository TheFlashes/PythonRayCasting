class Map:
    _map = []
    mapWidth = -1
    mapHeight = -1

    def __init__(self, mappath):
        mapFile = open(mappath, "r")
        
        fileWidth = len(mapFile.readline())
        for x in range(fileWidth - 1):
            mapFile.seek(0)
            mapColumn = []
            for y in mapFile:
                mapColumn.append(y[x])
            self._map.append(mapColumn)
        
        self.mapWidth = len(self._map)
        self.mapHeight = len(self._map[0])
        mapFile.close()

    def render(self):
        buffer = ""
        for y in range (self.mapHeight):
            for x in range (self.mapWidth):
                buffer += self._map[x][y]
            buffer += "\n"
        return buffer