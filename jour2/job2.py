class Livre :
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
    
    # Setters
    def changer_titre(self, titre) :
        self.__titre = titre
    
    def changer_auteur(self, auteur) :
        self.__auteur = auteur
    
    def changer_nombre_pages(self, nombre_pages) :
        if nombre_pages > 0 :
            self.__nombre_pages = nombre_pages
        else : # Si nombres de pages inférieur ou égal à 0, ne pas changer
            print("Nombre de pages invalide")
            return
    
    # Getters
    def recuperer_titre(self) :
        return self.__titre

    def recuperer_auteur(self) :
        return self.__auteur

    def recuperer_nombre_pages(self) :
        return self.__nombre_pages

livre = Livre("L'étranger", "Albert Camus", 228)

# Afficher
print(f"Titre : {livre.recuperer_titre()} \nAuteur : {livre.recuperer_auteur()} \nNombre de pages : {livre.recuperer_nombre_pages()}")