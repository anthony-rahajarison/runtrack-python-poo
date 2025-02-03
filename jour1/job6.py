class Animal :
    def __init__(self):
        self.age = 0
        self.nom = ""
    
    def viellir(self):
        """Augmente l'age de l'animal de 1 an"""
        self.age += 1
    
    def nommer(self, nom) :
        self.nom = nom
        print(f"L'animal se nomme {self.nom}")

animal1 = Animal()

print(f"L'age de l'animal {animal1.age} ans")
animal1.viellir()
print(f"L'age de l'animal {animal1.age} ans")

animal1.nommer("Luna")