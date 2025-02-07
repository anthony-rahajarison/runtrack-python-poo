class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    # Getters
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    # Setters
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    #Calculs
    def perimetre(self):
        """On renvoie le perimetre du rectangle"""
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        """On renvoie la surface du rectangle"""
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    # Getter
    def get_hauteur(self):
        return self.__hauteur
    
    # Setter
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    # Calcul
    def volume(self):
        """On renvoie le volume du solide"""
        return self.surface() * self.__hauteur

# On teste de la classe Rectangle
rectangle = Rectangle(5, 3)
print(f"Périmètre du rectangle : {rectangle.perimetre()}")
print(f"Surface du rectangle : {rectangle.surface()}")

# On teste de la classe Parallelepipede
parallelepipede = Parallelepipede(5, 3, 4)
print(f"Volume du parallélépipède : {parallelepipede.volume()}")