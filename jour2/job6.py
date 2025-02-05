class Commande :
    def __init__(self, numero):
        self.__numero = int(numero)
        self.__liste_plat = {}
        self.__status = "En cours"
        self.__prix_total_HT = 0
    
    # Getters
    def get_numero(self) :
        return self.__numero
    
    def get_liste_plat(self) :
        return self.__liste_plat
    
    def get_status(self) :
        return self.__status

    def add_plat(self, nom, prix) :
        if self.__status == "En cours" :
            self.__liste_plat[nom] = float(prix)
        else :
            print("La commande n'est pas en cours")

        self.__prix_total_HT = self.calculer_prix_total()

    def terminer(self) :
        self.__status = "Terminé"

    def annuler(self) :
        self.__status = "Annulé"
    
    def ajouter_TVA(self) :
        """Ajouter les 20% de TVA au prix Hors Taxes"""
        return round(self.__prix_total_HT * 1.2, 2)
    
    def calculer_prix_total(self) :
        return sum(self.__liste_plat.values())

    def afficher_commande(self) :
        """Affiche dans le terminal toutes les informations de la commande"""
        prixTTC = self.ajouter_TVA()
        print(f"\nNuméro de commande : {self.__numero} \nStatus : {self.__status}")
        print("Liste des Plats : ")
        i = 1
        for plat, prix in self.__liste_plat.items() :
            print(f"{i}. {plat}: {prix}€")
            i += 1
        print(f"Total HT : {self.__prix_total_HT}       Total TTC : {prixTTC}")

# Création des commandes
commande1 = Commande(1)
commande1.add_plat("Pizza", 12)
commande1.add_plat("Spaghetti", 8)

commande2 = Commande(2)
commande2.add_plat("Spaghetti", 8)
commande2.annuler()

commande3 = Commande(3)
commande3.add_plat("Viande", 10)
commande3.add_plat("Boisson", 1.5)
commande3.terminer()

# Affichage des commandes
commande1.afficher_commande()
commande2.afficher_commande()
commande3.afficher_commande()