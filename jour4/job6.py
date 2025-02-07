class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"\nMarque = {self.marque} \nModèle = {self.modele} \nAnnée = {self.annee} \nPrix = {self.prix}€")
    
    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.portes}")
    
    def demarrer(self):
        print("La voiture démarre")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues = {self.roues}")
    
    def demarrer(self):
        print("La moto démarre")

# On crée les objets
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)

# On affiche les infos de la voiture et on la démarre
voiture.informationsVehicule()
voiture.demarrer()

# On affiche les infos de la moto et on la démarre
moto.informationsVehicule()
moto.demarrer()