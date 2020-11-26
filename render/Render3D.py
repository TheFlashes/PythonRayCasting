import math 

class Render3D:
    __rayLength = 30
    __rayIncreaseStep = 1
    __fov = 80
    __bufferWidth = 115
    __bufferHeigth = 56
    __buffer = []
    __wallHeight = 100

    def __init__(self):
        for _ in range(self.__bufferWidth):
            bufferColumn = []
            for _ in range(self.__bufferHeigth):
                bufferColumn.append(" ")
            self.__buffer.append(bufferColumn)

    def clearBuffer(self):
        for y in range(self.__bufferHeigth):
            for x in range(self.__bufferWidth):
                self.__buffer[x][y] = " "


    def render(self, hero, map):
        rayAngleStart = hero.angle - self.__fov / 2
        rayAngleEnd = hero.angle + self.__fov / 2
        rayAngle = 0

        # Ray starting position
        rayStartX = hero.x
        rayStartY = hero.y

        bufferColumn = 0

        rayAngleIncreaseStep = self.__fov / self.__bufferWidth
        print(rayAngleIncreaseStep)

        for bufferColumn in range(self.__bufferWidth):
            # Ray end position
            rayAngleRad = math.radians(rayAngleStart)
            rayEndX = int(rayStartX + (self.__rayLength * math.cos(rayAngleRad)))
            rayEndY = int(rayStartY + (self.__rayLength * math.sin(rayAngleRad)))
            
            a = self.safeDiv(rayEndY - rayStartY, rayEndX - rayStartX)
            b = rayStartY - a * rayStartX


            rayXPos = 0
            rayYPos = 0
            hitWall = False

            # Ray line formula: y = ax + b for angle 315-45 and 135-225
            if rayAngleStart > 315 or rayAngleStart <= 45 or (rayAngleStart > 135 and rayAngleStart < 225):
                rayStep = self.__rayIncreaseStep if rayEndX > rayStartX else -self.__rayIncreaseStep
                for xU in range(int(rayStartX * 10), int(rayEndX * 10), rayStep):
                    rayXPos = xU / 10.0
                    rayYPos = a * rayXPos + b
                    if not map.freeAt(rayXPos, rayYPos):
                        hitWall = True
                        break
            # Ray line formula: x = y/a - b/a for rest
            else:
                rayStep = self.__rayIncreaseStep if rayEndY > rayStartY else -self.__rayIncreaseStep
                for yU in range(int(rayStartY * 10), int(rayEndY * 10), rayStep):
                    rayYPos = yU / 10.0
                    xPos = self.safeDiv(rayYPos, a) - self.safeDiv(b, a)
                    rayXPos = xPos if xPos != 0 else rayEndX
                    if not map.freeAt(rayXPos, rayYPos):
                        hitWall = True
                        break
            
            # The distance between the start of the ray (player) and the end of the ray, e.g. hitting a wall 122-131
            # distance = √((Xa - Xb)² + (Ya - Yb)²)
            rayLength = ((rayStartX - rayXPos)**2 + (rayStartY - rayYPos)**2)**(1/2)
            #print("bc: {}  -  rl: {} = √(({}a - {}b)² + ({}a - {}b)²)".format(bufferColumn, str(rayLength)[0:10], str(rayStartX)[0:10], str(rayXPos)[0:10], str(rayStartY)[0:10], str(rayYPos)[0:10]))
            
            correction = math.cos(math.radians(self.__fov / 2.0 - rayAngle))
            rayLength = rayLength * correction
            wallHeight = self.__wallHeight / rayLength

            #print("bc: {}  -  a: {}  -  rl: {}  -  ang: {}".format(bufferColumn, str(a)[0:10], str(rayLength)[0:10], rayAngleStart))

            drawStartHeigth = int(self.__bufferHeigth / 2 - wallHeight / 2)
            for y in range(drawStartHeigth, drawStartHeigth + int(wallHeight)):
                if y > self.__bufferHeigth - 1: continue
                elif y < 0: continue
                else:
                    walTexture = "█"
                    if wallHeight < 6: walTexture = "░"
                    elif wallHeight < 12: walTexture = "▒"
                    elif wallHeight < 19: walTexture = "▓"
                    self.__buffer[bufferColumn][y] = walTexture if hitWall else " "

            rayAngleStart += rayAngleIncreaseStep
            rayAngle += rayAngleIncreaseStep
        
        output = "╔"
        for x in range(self.__bufferWidth):
            output += "═"
        output += "╗\n"
        for y in range(self.__bufferHeigth):
            output += "║"
            for x in range(self.__bufferWidth):
                output += self.__buffer[x][y]
            output += "║\n"
        output += "╚"
        for x in range(self.__bufferWidth):
            output += "═"
        output += "╝"
        return output
        

    def safeDiv(self, num1, num2):
        if num1 == 0 or num2 == 0:
            return 0
        else:
            return num1 / num2
