class Commande :
    def __init__(self, numero, liste_plat, status):
        self.__numero = numero
        self.__liste_plat = liste_plat
        self.__status = status
    
    # Getters
    def get_numero(self) :
        return self.__numero
    
    def get_liste_plat(self) :
        return self.__liste_plat
    


    class Plat :
        def __init__(self, nom, prix) :
            self.__nom = nom
            self.__prix = prix
        