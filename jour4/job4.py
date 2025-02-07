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

# On teste de la classe Rectangle
rectangle = Rectangle(5, 3)
print(f"Aire du rectangle : {rectangle.aire()}")