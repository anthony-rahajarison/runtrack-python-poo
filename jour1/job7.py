class Personnage :
    def __init__(self) :
        # Position intialisée en (0, 0)
        self.x = 0
        self.y = 0

    def gauche(self) :
        self.x -= 1
    
    def droite(self) :
        self.x += 1
    
    def bas(self) :
        self.y -= 1
    
    def haut(self) :
        self.y += 1
    
    def position(self) :
        return (self.x, self.y)

a = Personnage()

a.gauche()
a.gauche()
a.bas()
print(a.position())