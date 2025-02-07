import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    # Getters
    def get_largeur(self):
        return self.__largeur
    
    def get_hauteur(self):
        return self.__hauteur
    
    # Setters
    def set_largeur(self, largeur):
        self.__largeur = largeur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    # Calcul aire
    def aire(self):
        return self.__largeur * self.__hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius
    
    # Getter
    def get_radius(self):
        return self.__radius
    
    # Setter
    def set_radius(self, radius):
        self.__radius = radius
    
    # Calcul aire
    def aire(self):
        return math.pi * self.__radius ** 2

# On crée les objets
rectangle = Rectangle(5, 3)
cercle = Cercle(4)

# On teste les méthodes
print(f"Aire du rectangle : {rectangle.aire()}")
print(f"Aire du cercle : {cercle.aire()}")