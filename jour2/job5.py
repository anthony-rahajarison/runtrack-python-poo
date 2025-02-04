class Voiture :
    def __init__(self, marque, modèle, année, kilométrage):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self.__reservoir = 50
    
    # Setters
    def set_marque(self, marque) :
        self.__marque = marque
    
    def set_modèle(self, modèle) :
        self.__modèle = modèle

    def set_année(self, année) :
        self.__année = année

    def set_kilométrage(self, kilométrage) :
        self.__kilométrage = kilométrage
    
    def demarrer(self) :
        if self.verifier_plein() > 5 : # Peut démarrer si reservoir > 5
            self.__en_marche = True
    
    def arreter(self) :
        self.__en_marche = False

    # Getters
    def get_marque(self) :
        return self.__marque
    
    def get_modèle(self) :
        return self.__modèle

    def get_année(self) :
        return self.__année

    def get_kilométrage(self) :
        return self.__kilométrage
    
    def verifier_plein(self) :
        """Vérifie le reservoir"""
        return self.__reservoir


voiture1 = Voiture("Audi", "A1", 2010, 0)
print(f"{voiture1.get_marque()} {voiture1.get_modèle()} ({voiture1.get_année()}) \nRéservoir : {voiture1.verifier_plein()}")