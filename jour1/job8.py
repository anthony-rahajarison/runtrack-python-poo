import math

class Cercle :
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, rayon):
        self.rayon = rayon
    
    def circonférence(self):
        """Calcule et renvoie la circonférence du cercle (2R*Pi)"""
        return 2*self.rayon*math.pi
    
    def aire(self) :
        """Calcule et renvoie l'aire du cercle (Pi*R²)"""
        return self.rayon**2*math.pi
    
    def diametre(self) :
        """Calcule et renvoie le diametre du cercle (2R)"""
        return self.rayon*2
    
    def afficherInfos(self) :
        """Affiche dans le terminal les infos de manières formatées"""
        print(f"Le rayon du cercle est de {self.rayon}\nSa circonférence est de {self.circonférence()}\nSon aire est de {self.aire()}\nSon diametre est de {self.diametre()}")
    
cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
print("")
cercle2.afficherInfos()