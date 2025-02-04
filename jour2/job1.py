class Rectangle :
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    # Setters
    def changer_dimensions(self, longueur, largeur) :
        self.__longueur = longueur
        self.__largeur = largeur
    
    # Getters
    def recuperer_dimensions(self) :
        return (self.__longueur, self.__largeur)

forme = Rectangle(10, 5)
print(forme.recuperer_dimensions())

# Changer dimensions de "forme"
forme.changer_dimensions(20, 10)
print(forme.recuperer_dimensions())