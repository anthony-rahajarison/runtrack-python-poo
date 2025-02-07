class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J’ai {self.age} ans")


class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# On crée les objets
personne = Personne()
eleve = Eleve()

# On affiche l'age en console
eleve.afficherAge()