class Ville :
    def __init__(self, nom, habitants) :
        self.__nom = nom
        self.__habitants = habitants
    
    def get_nom(self) :
        return self.__nom

    def get_habitants(self) :
        return self.__habitants
    
    def ajouterHabitant(self) :
        """Augmente de 1 le nombre d'habitant dans la ville"""
        self.__habitants += 1
    

class Personne :
    def __init__(self, nom, age, ville) :
        self.__nom = nom
        self.__age = int(age)
        self.__ville = ville
        # On ajoute 1 à la population de la ville lorsqu'on créé un habitant
        self.ajouterPopulation()
    
    def ajouterPopulation(self) :
        self.__ville.ajouterHabitant()

# Objets Ville créés
ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)

print(f"Population de la ville de {ville1.get_nom()}: {ville1.get_habitants()} habitants")
print(f"Population de la ville de {ville2.get_nom()}: {ville2.get_habitants()} habitants")

# Objets Personne créés
personne1 = Personne("John", 45, ville1)
personne2 = Personne("Myrtille", 4, ville1)
personne3 = Personne("Chloé", 45, ville2)

print(f"Mise à jour de la population de la ville de {ville1.get_nom()}: {ville1.get_habitants()} habitants")
print(f"Mise à jour de la population de la ville de {ville2.get_nom()}: {ville2.get_habitants()} habitants")