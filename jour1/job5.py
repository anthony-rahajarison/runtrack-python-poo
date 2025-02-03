class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    
    def afficherLesPoints(self) :
        """Affiche dans le terminal les coordonnées du point"""
        print((self.x, self.y))
    
    def afficherX(self) :
        print(f"x : {self.x}")
    
    def afficherY(self) :
        print(f"y : {self.y}")
    
    def changerX(self, x) :
        self.x = x
    
    def changerY(self, y) :
        self.y = y

a = Point(2, 0)
a.afficherX()
a.afficherY()
a.afficherLesPoints()

a.changerX(1)
a.changerY(5)
a.afficherLesPoints()