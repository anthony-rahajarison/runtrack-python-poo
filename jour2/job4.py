class Student :
    def __init__(self, name, first_name, id):
        self.__name = name
        self.__first_name = first_name
        self.__id = id
        self.__credits = 0
        self.__level = self.__student_eval()
    
    def add_credits(self, credits) :
        if credits > 0 :
            self.__credits += credits
            # Actualise le niveau de l'étudiant
            self.__level = self.__student_eval()
        else :
            print("Nombre de crédits invalide")
    
    # Getters
    def get_name(self) :
        return self.__name

    def get_first_name(self) :
        return self.__first_name

    def get_id(self) :
        return self.__id
    
    def get_credits(self) :
        return self.__credits

    def get_level(self) :
        return self.__level

    def student_info(self) :
        print(f"Nom = {self.get_name()} \nPrénom = {self.get_first_name()} \nid = {self.get_id()} \nNiveau = {self.get_level()}")

    # Donne le niveau de l'élève
    def __student_eval(self) :
        if self.get_credits() >= 90 :
            return "Excellent"
        elif self.get_credits() >= 80 :
            return "Très Bien"
        elif self.get_credits() >= 70 :
            return "Bien"
        elif self.get_credits() >= 60 :
            return "Passable"
        elif self.get_credits() < 60 :
            return "Insuffisant"
    



# Crée l'objet
eleve1 = Student("Doe", "John", 145)

# Ajouter les crédits
eleve1.add_credits(10)
eleve1.add_credits(15)
eleve1.add_credits(50)

# Affiche le nombre de crédit
print(f"Le nombre de credits de {eleve1.get_first_name()} {eleve1.get_name()} est de {eleve1.get_credits()} points")

# Affiche les infos
eleve1.student_info()