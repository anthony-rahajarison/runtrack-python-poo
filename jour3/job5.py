import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        """Inflige des dégats aléatoire entre 5 et 15 à adversaire"""
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts.")
        if adversaire.vie < 0:
            adversaire.vie = 0
        print(f"Il reste {adversaire.vie} points de vie à {adversaire.nom}.\n")

    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = 100
    
    def choisir_niveau(self):
        print("Choisissez un niveau de difficulté :")
        print("1 - Facile (100 PV chacun)")
        print("2 - Moyen (75 PV chacun)")
        print("3 - Difficile (50 PV chacun)")
        choix = input("Entrez 1, 2 ou 3 : ")
        if choix == "1":
            self.niveau = 100
        elif choix == "2":
            self.niveau = 75
        elif choix == "3":
            self.niveau = 50
        else:
            print("Choix invalide, niveau par défaut : Facile (100 PV).")
            self.niveau = 100
    
    def lancerJeu(self):
        self.choisir_niveau()
        joueur = Personnage("Joueur", self.niveau)
        ennemi = Personnage("Ennemi", self.niveau)
        
        print("\nDébut du combat !\n")
        while joueur.est_vivant() and ennemi.est_vivant():
            input("Appuyez sur Entrée pour attaquer...")
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)
        
        self.afficherGagnant(joueur, ennemi)
    
    def afficherGagnant(self, joueur, ennemi):
        if joueur.est_vivant():
            print("Victoire ! Joueur a vaincu l'ennemi !")
        else:
            print("Défaite... L'ennemi vous a vaincu.")
        
# Lancement du jeu
jeu1 = Jeu()
jeu.lancerJeu()