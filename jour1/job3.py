class Operation :
    nombre1 = 0
    nombre2 = 0
    def __init__(self, nombre1, nombre2): # Constructeur
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self) :
        print(f"Le résultat est {self.nombre1 + self.nombre2}")

    def str(self) : # Renvoie l'objet en string formaté
        return (f"Le nombre1 est {self.nombre1} \nLe nombre2 est {self.nombre2}")

a = Operation(10, 5)

a.addition()