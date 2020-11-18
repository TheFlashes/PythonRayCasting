import math 

class Render3D:
    __rayLength = 20
    __rayAngle = 45
    __rayIncreaseStep = 1

    def render(self, hero, map):
        # Ray starting position
        rayStartX = hero.x
        rayStartY = hero.y

        # Ray end position
        rayAngleRad = math.radians(self.__rayAngle)
        rayEndX = int(rayStartX + (self.__rayLength * math.cos(rayAngleRad)))
        rayEndY = int(rayStartY + (self.__rayLength * math.sin(rayAngleRad)))
        
        a = self.safeDiv(rayEndY - rayStartY, rayEndX - rayStartX)
        b = rayStartY - a * rayStartX

        # Ray line formula: y = ax + b for angle 315-45 and 135-225
        if self.__rayAngle > 315 or self.__rayAngle < 45 or (self.__rayAngle > 135 and self.__rayAngle < 225):
            rayStep = self.__rayIncreaseStep if rayEndX > rayStartX else -self.__rayIncreaseStep
            for xU in range(rayStartX * 10, rayEndX * 10, rayStep):
                x = xU / 10.0
                y = a * x + b
                if map.freeAt(x, y) == False:
                    break
                map.draw("o", int(x), int(y))
        # Ray line formula: x = y/a - b/a for rest
        else:
            rayStep = self.__rayIncreaseStep if rayEndY > rayStartY else -self.__rayIncreaseStep
            for yU in range(rayStartY * 10, rayEndY * 10, rayStep):
                y = yU / 10.0
                xPos = self.safeDiv(y, a) - self.safeDiv(b, a)
                x = xPos if xPos != 0 else rayEndX
                if map.freeAt(x, y) == False:
                    break
                map.draw("*", int(x), int(y))

        self.rayAngleIncrease()

    def rayAngleIncrease(self):
        self.__rayAngle += 1
        if self.__rayAngle > 360:
            self.__rayAngle = 0

    def safeDiv(self, num1, num2):
        if num1 == 0 or num2 == 0:
            return 0
        else:
            return num1 / num2