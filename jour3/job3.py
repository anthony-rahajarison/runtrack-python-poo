class Tache :
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"

class ListeDeTaches :
    def __init__(self, liste) :
        self.liste = liste
    
    def ajouterTache(self, tache) :
        self.liste.append(tache)
    
    def supprimerTache(self, titre) :
        i = 0
        for tache in self.liste :
            if tache.titre == titre:
                self.liste.pop(i)
            i += 1
    
    def marquerCommeFinie(self, titre) :
        for tache in self.liste :
            if tache.titre == titre:
                tache.statut = "terminée"
    
    def afficherListe(self) :
        """Affiche la liste entière"""
        print(f"\nVoici la liste de taches :")
        for tache in self.liste :
            print(f"{tache.titre} : {tache.description} ({tache.statut})")
    
    def filtrerListe(self, statut) :
        liste_filtrée = []
        for tache in self.liste :
            if tache.statut == statut :
                liste_filtrée.append(tache)
        return liste_filtrée

# On crée 4 taches à faire
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Réviser Python", "Pratiquer les classes et objets")
tache3 = Tache("Faire du sport", "Courir 5km")
tache4 = Tache("Lire un livre", "Lire au moins 20 pages d'un roman")

# On crée la liste de tache et on ajoute les taches
liste_taches = ListeDeTaches([])
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)
liste_taches.ajouterTache(tache4)

liste_taches.afficherListe()

# On modifie la liste
liste_taches.supprimerTache("Faire les courses")
liste_taches.marquerCommeFinie("Faire du sport")

liste_taches.afficherListe()

# On filtre les taches pour avoir la liste des taches "à faire"
# On stocke la nouvelle liste dans "liste_a_faire"
liste_a_faire = ListeDeTaches(liste_taches.filtrerListe("à faire"))
liste_a_faire.afficherListe()