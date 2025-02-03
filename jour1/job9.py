class Produit :
    def __init__(self, nom, prixHT, TVA) :
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self) :
        """Calcule le prix avec la TVA"""
        return round(self.prixHT*(1 + self.TVA), 2)

    def changerNom(self, nom) :
        self.nom = nom
    
    def changerPrixHT(self, prixHT) :
        self.prixHT = prixHT
    
    def afficher(self) :
        """Renvoie de manière formatée une string avec les infos"""
        return f"{self.nom} : Le prix HT est de {self.prixHT} €, le prix TTC avec une TVA de {self.TVA} est de {self.CalculerPrixTTC()} €"

produit1 = Produit("Pommes", 1, 0.2)
produit2 = Produit("Fraises", 5, 0.2)
produit3 = Produit("Bananes", 4, 0.2)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# On change les prix et noms des produits
produit1.changerPrixHT(2)
produit1.changerNom("Poires")

produit2.changerPrixHT(6)
produit2.changerNom("Framboises")

produit3.changerPrixHT(3)
produit3.changerNom("Mangues")

print(f"\n{produit1.afficher()}")
print(produit2.afficher())
print(produit3.afficher())