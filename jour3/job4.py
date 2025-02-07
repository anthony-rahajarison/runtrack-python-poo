class Joueur:
    def __init__(self, nom, numero, position, nombre_but, nombre_passes_d, carton_jaune, carton_rouge):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nombre_but = nombre_but
        self.nombre_passes_d = nombre_passes_d
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge
    
    def marquerUnBut(self) :
        self.nombre_but += 1
    
    def effectuerUnePasseDecisive(self) :
        self.nombre_passes_d += 1

    def recevoirUnCartonJaune(self) :
        self.carton_jaune += 1

    def recevoirUnCartonRouge(self) :
        self.carton_rouge += 1

    def afficherStatistiques(self) :
        print(f"\nStatistiques de {self.nom} ({self.numero})")
        print(f"POS : {self.position}")
        print(f"BUT : {self.nombre_but}")
        print(f"PDE : {self.nombre_passes_d}")
        print(f"JAU : {self.carton_jaune}")
        print(f"ROU : {self.carton_rouge}")

class Equipe :
    def __init__(self, nom_equipe) :
        self.nom_equipe = nom_equipe
        self.liste_joueurs = []
    
    def ajouterJoueur(self, joueur) :
        self.liste_joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self) :
        for joueur in self.liste_joueurs :
            joueur.afficherStatistiques()

# On crée 10 joueurs avec des statistiques à 0
joueur1 = Joueur("Lionel Messi", 10, "ATT", 0, 0, 0, 0)
joueur2 = Joueur("Cristiano Ronaldo", 7, "ATT", 0, 0, 0, 0)
joueur3 = Joueur("Kevin De Bruyne", 17, "MIL", 0, 0, 0, 0)
joueur4 = Joueur("Virgil van Dijk", 4, "DEF", 0, 0, 0, 0)
joueur5 = Joueur("Neymar Jr", 11, "ATT", 0, 0, 0, 0)
joueur6 = Joueur("Kylian Mbappé", 7, "ATT", 0, 0, 0, 0)
joueur7 = Joueur("Luka Modric", 10, "MIL", 0, 0, 0, 0)
joueur8 = Joueur("Sergio Ramos", 4, "DEF", 0, 0, 0, 0)
joueur9 = Joueur("Robert Lewandowski", 9, "ATT", 0, 0, 0, 0)
joueur10 = Joueur("Manuel Neuer", 1, "GAR", 0, 0, 0, 0)

# On crée 2 équipes et on ajoute les joueurs a ces équipes
equipe1 = Equipe("FC Barcelone")
equipe2 = Equipe("Real Madrid")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)
equipe1.ajouterJoueur(joueur5)

equipe2.ajouterJoueur(joueur6)
equipe2.ajouterJoueur(joueur7)
equipe2.ajouterJoueur(joueur8)
equipe2.ajouterJoueur(joueur9)
equipe2.ajouterJoueur(joueur10)

# On affiche les joueurs
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

print("\nDébut du match")
# Evènements du match
joueur2.marquerUnBut()
joueur3.effectuerUnePasseDecisive()
joueur8.recevoirUnCartonJaune()
joueur1.recevoirUnCartonRouge()
joueur4.marquerUnBut()
joueur3.effectuerUnePasseDecisive()

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()