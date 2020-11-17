from os import system, name 

class ConsoleTweaks:
    @staticmethod
    def setCursorPos(x, y):
        print("\033[%d;%dH" % (y, x))

    @staticmethod
    def clearScreen(): 
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear')