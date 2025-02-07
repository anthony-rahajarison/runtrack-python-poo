class CompteBancaire :
    def __init__(self, numero, nom, prenom, solde, decouvert):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self) :
        print(f"\nNumero de compte : {self.__numero} \n{self.__nom} {self.__prenom}")
        self.afficherSolde()
    
    def afficherSolde(self) :
        print(f"Solde du compte {self.__numero}: {self.__solde}")
    
    def versement(self, montant) :
        self.__solde += montant
    
    def retrait(self, montant) :
        if (montant <= self.__solde) or (self.__decouvert == True) :
            self.__solde -= montant
            self.afficherSolde()
        else :
            print("Solde insuffisant")
    
    def agios(self) :
        if self.__solde < 0 :
            self.retrait(100)
    
    def virement(self, bénéficiaire, montant) :
        if (self.__solde >= montant) or (self.__decouvert == True) :
            self.retrait(montant)
            bénéficiaire.versement(montant)
            print("\nVirement validé")
        else :
            print("Solde Insuffisant")

compte1 = CompteBancaire(1, "Doe", "John", 2000, False)
compte1.afficher()
compte1.retrait(2500)

compte2 = CompteBancaire(2, "Brook", "Eric", 3000, False)
compte2.versement(150)
compte2.afficher()

compte3 = CompteBancaire(3, "Graham", "Aubrey", -2000, True)
compte3.agios()
compte3.afficher()

# Compte 2 fait un virement à Compte 3
compte2.virement(compte3, 2100)
compte2.afficher()
compte3.afficher()